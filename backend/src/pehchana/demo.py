"""Synthetic demo calls for UI work and screenshots.  Owner: WS3 (Leaderboard).

Every row is ``source=DEMO``: the leaderboard ignores them unless INCLUDE_DEMO_DATA=true,
and then says so. The numbers are made up to look plausible (a human arm that is rarely
called out, AI arms caught at different speeds, a language gap); they are not results.
"""

from __future__ import annotations

import random
from collections.abc import Sequence
from datetime import timedelta

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from pehchana.arms import ArmLabel
from pehchana.models import (
    Accusation,
    AccusationSource,
    Call,
    CallStatus,
    Channel,
    Giveaway,
    Source,
    utcnow,
)
from pehchana.tagging import GiveawayTag

# Share of calls per language, and how much faster AI arms are caught in it.
LANGUAGES = {"hi": (0.45, 1.0), "en": (0.25, 1.2), "ta": (0.15, 0.55), "mr": (0.15, 0.75)}
# Median seconds before an AI arm is called out, by its position among AI arms.
AI_MEDIANS_S = (95.0, 60.0, 35.0, 50.0)
HUMAN_FALSE_ACCUSATION = 0.15
TAG_WEIGHTS = {
    GiveawayTag.SLOW_REPLY: 5,
    GiveawayTag.TOO_PERFECT: 4,
    GiveawayTag.FLAT_EMOTION: 3,
    GiveawayTag.PRONUNCIATION: 3,
    GiveawayTag.WRONG_LANGUAGE: 2,
    GiveawayTag.NUMBER_READING: 2,
    GiveawayTag.TALKED_OVER: 2,
    GiveawayTag.CONTENT: 1,
}


def clear_demo_calls(session: Session) -> int:
    """Delete every DEMO call (and its accusations and giveaways). Real calls are kept."""
    ids = session.scalars(select(Call.id).where(Call.source == Source.DEMO)).all()
    if ids:
        session.execute(delete(Accusation).where(Accusation.call_id.in_(ids)))
        session.execute(delete(Giveaway).where(Giveaway.call_id.in_(ids)))
        session.execute(delete(Call).where(Call.id.in_(ids)))
    session.commit()
    return len(ids)


def seed_demo_calls(
    session: Session, labels: Sequence[ArmLabel], n: int, rng: random.Random
) -> int:
    """Insert ``n`` processed DEMO calls spread over the last three days."""
    if not labels:
        raise ValueError("no arms to seed calls for")
    ai_rank = {label.id: i for i, label in enumerate(x for x in labels if x.kind == "ai")}
    callers = [f"{rng.getrandbits(256):064x}" for _ in range(max(1, int(n * 0.8)))]
    langs, lang_weights = list(LANGUAGES), [w for w, _ in LANGUAGES.values()]
    now = utcnow()
    for _ in range(n):
        label = rng.choice(labels)
        language = rng.choices(langs, lang_weights)[0]
        started = now - timedelta(seconds=rng.uniform(0, 3 * 24 * 3600))
        duration = min(600.0, max(15.0, rng.lognormvariate(4.5, 0.6)))  # median ~90 s

        accused_at: float | None
        if label.kind == "human":
            accused_at = (
                rng.uniform(20, duration) if rng.random() < HUMAN_FALSE_ACCUSATION else None
            )
        else:
            median = AI_MEDIANS_S[ai_rank[label.id] % len(AI_MEDIANS_S)] * LANGUAGES[language][1]
            t = rng.expovariate(0.693147 / median)  # exponential with that median
            accused_at = t if t < duration else None

        length = accused_at if accused_at is not None else duration  # hang up once caught
        call = Call(
            channel=Channel.PHONE,
            source=Source.DEMO,
            status=CallStatus.PROCESSED,
            arm_id=label.id,
            arm_kind=label.kind,
            caller_hash=rng.choice(callers),
            started_at=started,
            answered_at=started,
            ended_at=started + timedelta(seconds=length),
            duration_s=round(length, 1),
            language=language,
        )
        if accused_at is not None:
            call.accusations.append(
                Accusation(
                    source=AccusationSource.TRANSCRIPT,
                    at_s=round(accused_at, 1),
                    phrase="tum bot ho",
                )
            )
            tags = rng.choices(list(TAG_WEIGHTS), list(TAG_WEIGHTS.values()), k=rng.randint(1, 2))
            for tag in dict.fromkeys(tags):
                call.giveaways.append(Giveaway(tag=tag.value, method="demo", confidence=1.0))
        session.add(call)
    session.commit()
    return n
