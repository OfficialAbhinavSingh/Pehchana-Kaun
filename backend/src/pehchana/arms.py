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
from datetime import datetime
from pathlib import Path
from typing import Literal

ArmKind = Literal["human", "ai"]
CallChannel = Literal["phone", "web"]


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

    @property
    def is_human(self) -> bool:
        return self.kind == "human"


class NoArmAvailable(RuntimeError):
    """Raised when nobody can take the call (the caller hears a 'try again' message)."""


def load_arms(path: Path, env: Mapping[str, str] | None = None) -> list[Arm]:
    """Parse ``bolna/arms.yaml`` and resolve the env vars it names.

    TODO(WS1): parse live_hours too, reject duplicate ids, skip arms with no numbers.
    """
    raise NotImplementedError


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
    - human arm: only inside its live hours, unless the admin override says otherwise.

    TODO(WS1)
    """
    raise NotImplementedError


def choose_arm(
    candidates: Sequence[Arm],
    recent_counts: Mapping[str, int],
    rng: random.Random | None = None,
) -> Arm:
    """Random pick that keeps sample sizes balanced across arms.

    Plain uniform randomization drifts at small n (a launch weekend may be ~100
    calls). Suggested: weight / (1 + recent count). Must stay unpredictable to callers.

    TODO(WS1)
    """
    raise NotImplementedError
