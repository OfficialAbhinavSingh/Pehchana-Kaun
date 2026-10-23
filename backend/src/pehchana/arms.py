"""Arm registry and random assignment.  Owner: WS1 (Calls).

An *arm* is whoever picks up a call: the human control group, or one AI voice stack
(one Bolna agent per stack). Arms are declared in ``bolna/arms.yaml``; secrets and
phone numbers come from env vars named there.

See docs/architecture.md#routing for the rules these functions must follow.
"""

from __future__ import annotations

import random
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import datetime, time
from pathlib import Path
from typing import Literal
from zoneinfo import ZoneInfo

import yaml

ArmKind = Literal["human", "ai"]
CallChannel = Literal["phone", "web"]

_DAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


@dataclass(frozen=True)
class LiveWindow:
    days: frozenset[str]
    start: time
    end: time


@dataclass(frozen=True)
class LiveHours:
    timezone: ZoneInfo
    windows: tuple[LiveWindow, ...]

    def is_open(self, now: datetime) -> bool:
        local = now.astimezone(self.timezone)
        day, at = _DAYS[local.weekday()], local.time()
        return any(day in w.days and w.start <= at < w.end for w in self.windows)


@dataclass(frozen=True)
class Arm:
    id: str
    kind: ArmKind
    public_label: str
    vendor: str | None
    weight: float
    dial_numbers: tuple[str, ...] = ()
    bolna_agent_id: str | None = None
    stack: Mapping[str, object] = field(default_factory=dict)
    live_hours: LiveHours | None = None

    @property
    def is_human(self) -> bool:
        return self.kind == "human"


class NoArmAvailable(RuntimeError):
    """Raised when nobody can take the call (the caller hears a 'try again' message)."""


def _parse_live_hours(raw: Mapping[str, object] | None, arm_id: str) -> LiveHours | None:
    if not raw:
        return None
    windows = []
    for w in raw.get("windows", []):  # type: ignore[attr-defined]
        days = frozenset(str(d).lower() for d in w["days"])
        if not days <= set(_DAYS):
            raise ValueError(f"arm {arm_id}: unknown day in {sorted(days)}")
        start, end = time.fromisoformat(w["start"]), time.fromisoformat(w["end"])
        if start >= end:
            raise ValueError(f"arm {arm_id}: live window {start}-{end} must not cross midnight")
        windows.append(LiveWindow(days, start, end))
    return LiveHours(ZoneInfo(str(raw.get("timezone", "UTC"))), tuple(windows))


def load_arms(path: Path, env: Mapping[str, str] | None = None) -> list[Arm]:
    """Parse ``bolna/arms.yaml`` and resolve the env vars it names.

    Rejects duplicate ids. Skips arms that can take no call at all (no dial numbers and
    no Bolna agent id), so an arm whose env vars aren't set yet never gets traffic.
    """
    env = env or {}
    arms: list[Arm] = []
    seen: set[str] = set()
    for raw in yaml.safe_load(path.read_text())["arms"]:
        if raw["id"] in seen:
            raise ValueError(f"duplicate arm id: {raw['id']}")
        seen.add(raw["id"])
        numbers = tuple(
            n.strip() for n in env.get(raw.get("dial_numbers_env", ""), "").split(",") if n.strip()
        )
        agent_id = env.get(raw.get("bolna_agent_id_env", "")) or None
        if not numbers and not agent_id:
            continue
        arms.append(
            Arm(
                id=raw["id"],
                kind=raw["kind"],
                public_label=raw["public_label"],
                vendor=raw.get("vendor"),
                weight=float(raw.get("weight", 1.0)),
                dial_numbers=numbers,
                bolna_agent_id=agent_id,
                stack=raw.get("stack") or {},
                live_hours=_parse_live_hours(raw.get("live_hours"), raw["id"]),
            )
        )
    return arms


def eligible_arms(
    arms: Sequence[Arm],
    *,
    channel: CallChannel,
    now: datetime,
    humans_override: bool | None = None,
) -> list[Arm]:
    """Arms that can take a call right now on this channel.

    Rules (docs/architecture.md#routing):
    - phone: arm needs at least one dial number.
    - web: AI arms only (needs a Bolna agent id). Humans can't take web calls.
    - human arm: only inside its live hours (none declared means never), unless the
      admin override says otherwise.
    """
    out = []
    for arm in arms:
        if channel == "web":
            ok = not arm.is_human and arm.bolna_agent_id is not None
        else:
            ok = bool(arm.dial_numbers)
        if ok and arm.is_human:
            if humans_override is not None:
                ok = humans_override
            else:
                ok = arm.live_hours is not None and arm.live_hours.is_open(now)
        if ok:
            out.append(arm)
    return out


def choose_arm(
    candidates: Sequence[Arm],
    recent_counts: Mapping[str, int],
    rng: random.Random | None = None,
) -> Arm:
    """Random pick that keeps sample sizes balanced across arms.

    Weight divided by (1 + recent count) pulls under-sampled arms up while every arm
    stays possible, so the next arm is not predictable by callers.
    """
    if not candidates:
        raise NoArmAvailable
    rng = rng or random.SystemRandom()
    weights = [a.weight / (1 + recent_counts.get(a.id, 0)) for a in candidates]
    return rng.choices(list(candidates), weights=weights, k=1)[0]
