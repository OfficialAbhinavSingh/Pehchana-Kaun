"""Public stats.  Owner: WS3 (Leaderboard).

Response shape is the contract with web/: keep it in sync with
web/src/lib/api.ts. Only REAL calls with status=processed count; demo rows only
when INCLUDE_DEMO_DATA=true (and the response must say so). Vendor names only when
REVEAL_VENDORS=true, otherwise public_label from bolna/arms.yaml.
"""

from __future__ import annotations

import logging
import re
import time
from collections import Counter
from collections.abc import Sequence
from datetime import datetime
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import or_, select
from sqlalchemy.orm import Session, selectinload

from pehchana.api.deps import ArmLabelsDep, SessionDep, SettingsDep
from pehchana.arms import ArmLabel
from pehchana.config import Settings
from pehchana.models import Call, CallStatus, Source, utcnow
from pehchana.scoring import ArmStats, Observation, arm_stats, first_calls, group_by

log = logging.getLogger(__name__)

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

TOP_GIVEAWAYS = 5
UNKNOWN_LANGUAGE = "unknown"


class SurvivalPointOut(BaseModel):
    t: float
    survival: float
    at_risk: int
    events: int
    ci_low: float | None
    ci_high: float | None


class GiveawayCount(BaseModel):
    tag: str
    count: int


class ArmStatsOut(BaseModel):
    arm_id: str
    display_name: str
    kind: Literal["human", "ai"]
    ranked: bool
    n_calls: int
    n_accused: int
    accusation_rate: float
    median_turing_clock_s: float | None
    median_ci_low_s: float | None
    median_ci_high_s: float | None
    fooled_at_60s: float | None
    max_observed_s: float | None
    curve: list[SurvivalPointOut]
    top_giveaways: list[GiveawayCount]


class Leaderboard(BaseModel):
    generated_at: datetime
    includes_demo_data: bool
    first_call_only: bool
    min_calls_for_ranking: int
    total_calls: int
    arms: list[ArmStatsOut]
    by_language: dict[str, list[ArmStatsOut]]


def _public_id(label: ArmLabel, reveal: bool) -> str:
    """Arm ids name vendors ("kalpa"), so they stay hidden unless vendors are revealed."""
    if reveal or label.kind == "human":
        return label.id
    return re.sub(r"[^a-z0-9]+", "-", label.public_label.lower()).strip("-")


def _observation(call: Call) -> Observation | None:
    """Accused calls end at the first timed accusation; the rest are censored at their
    length. A call we cannot place on the clock is left out rather than guessed."""
    accused_at = call.first_accusation_s
    if accused_at is not None:
        return Observation(accused_at, True)
    if call.accusations:
        log.warning("call %s has an accusation with no time; left out of the stats", call.id)
        return None
    if call.duration_s is None:
        log.warning("processed call %s has no duration; left out of the stats", call.id)
        return None
    return Observation(call.duration_s, False)


def _arm_out(
    label: ArmLabel, calls: Sequence[Call], settings: Settings
) -> tuple[ArmStatsOut, ArmStats]:
    observations = [o for o in map(_observation, calls) if o is not None]
    stats = arm_stats(label.id, observations)
    tags = Counter(g.tag for c in calls for g in c.giveaways)
    out = ArmStatsOut(
        arm_id=_public_id(label, settings.reveal_vendors),
        display_name=(label.vendor or label.public_label)
        if settings.reveal_vendors
        else label.public_label,
        kind=label.kind,
        ranked=stats.n_calls >= settings.min_calls_for_ranking,
        n_calls=stats.n_calls,
        n_accused=stats.n_accused,
        accusation_rate=stats.accusation_rate,
        median_turing_clock_s=stats.median_turing_clock_s,
        median_ci_low_s=stats.median_ci_low_s,
        median_ci_high_s=stats.median_ci_high_s,
        fooled_at_60s=stats.fooled_at_60s,
        max_observed_s=stats.max_observed_s,
        curve=[SurvivalPointOut(**vars(p)) for p in stats.curve],
        top_giveaways=[GiveawayCount(tag=t, count=n) for t, n in tags.most_common(TOP_GIVEAWAYS)],
    )
    return out, stats


def _order(arms: list[ArmStatsOut]) -> list[ArmStatsOut]:
    """Human baseline first, then ranked AI arms from hardest to catch to easiest, then
    AI arms with too few calls to rank.

    An arm that half the callers never caught has no median; it ranks by the longest
    time it was watched, the most we know about its clock. Five calls dropped at 5 s
    must not outrank an arm that held out for 50 s.
    """

    def key(a: ArmStatsOut) -> tuple[int, float, float]:
        if a.kind == "human":
            return (0, 0.0, 0.0)
        if not a.ranked:
            return (2, 0.0, 0.0)
        clock = a.median_turing_clock_s
        if clock is None:
            clock = a.max_observed_s or 0.0
        fooled = a.fooled_at_60s if a.fooled_at_60s is not None else -1.0
        return (1, -clock, -fooled)

    return sorted(arms, key=key)


def build_leaderboard(
    session: Session,
    settings: Settings,
    labels: Sequence[ArmLabel],
    *,
    first_call_only: bool = False,
) -> Leaderboard:
    sources = [Source.REAL, Source.DEMO] if settings.include_demo_data else [Source.REAL]
    calls: Sequence[Call] = session.scalars(
        select(Call)
        .where(Call.status == CallStatus.PROCESSED, Call.source.in_(sources))
        .options(selectinload(Call.accusations), selectinload(Call.giveaways))
    ).all()
    if first_call_only:
        # A caller's first game is their first call that reached an arm, scored or not
        # (a later call is a repeat even if the earlier one failed in processing).
        played = session.execute(
            select(Call.id, Call.caller_hash, Call.started_at).where(
                Call.source.in_(sources),
                or_(Call.duration_s.is_not(None), Call.status == CallStatus.PROCESSED),
            )
        ).all()
        firsts = {
            row.id
            for row in first_calls(
                played, caller=lambda r: r.caller_hash, started_at=lambda r: r.started_at
            )
        }
        calls = [c for c in calls if c.id in firsts]

    by_id = {label.id: label for label in labels}
    unknown = {c.arm_id for c in calls} - by_id.keys()
    if unknown:
        log.warning("calls for arms not in arms.yaml left out: %s", ", ".join(sorted(unknown)))
    calls = [c for c in calls if c.arm_id in by_id]

    per_arm = group_by(calls, lambda c: c.arm_id)
    arms: list[ArmStatsOut] = []
    total = 0
    for label in labels:  # every configured arm, even one with no calls yet
        out, stats = _arm_out(label, per_arm.get(label.id, []), settings)
        arms.append(out)
        total += stats.n_calls

    by_language: dict[str, list[ArmStatsOut]] = {}
    for language, lang_calls in sorted(
        group_by(calls, lambda c: c.language or UNKNOWN_LANGUAGE).items()
    ):
        lang_arms = group_by(lang_calls, lambda c: c.arm_id)
        by_language[language] = _order(
            [
                _arm_out(label, lang_arms[label.id], settings)[0]
                for label in labels
                if label.id in lang_arms
            ]
        )

    return Leaderboard(
        generated_at=utcnow(),
        includes_demo_data=settings.include_demo_data,
        first_call_only=first_call_only,
        min_calls_for_ranking=settings.min_calls_for_ranking,
        total_calls=total,
        arms=_order(arms),
        by_language=by_language,
    )


# (include_demo_data, reveal_vendors, min_calls_for_ranking, first_call_only) ->
# (monotonic expiry, response). Per process; launch traffic hits this, not the DB.
_cache: dict[tuple[bool, bool, int, bool], tuple[float, Leaderboard]] = {}


def clear_cache() -> None:
    _cache.clear()


@router.get("")
def leaderboard(
    session: SessionDep,
    settings: SettingsDep,
    labels: ArmLabelsDep,
    first_call_only: bool = False,
) -> Leaderboard:
    """Per-arm Turing Clock stats, a per-language breakdown, top giveaways and totals.

    ``first_call_only=true`` keeps each caller's first call only (repeat callers learn
    the voices), as a check on the headline numbers.
    """
    key = (
        settings.include_demo_data,
        settings.reveal_vendors,
        settings.min_calls_for_ranking,
        first_call_only,
    )
    now = time.monotonic()
    hit = _cache.get(key)
    if hit is not None and hit[0] > now:
        return hit[1]
    board = build_leaderboard(session, settings, labels, first_call_only=first_call_only)
    if settings.leaderboard_cache_s > 0:
        _cache[key] = (now + settings.leaderboard_cache_s, board)
    return board
