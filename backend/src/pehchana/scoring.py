"""Turing Clock statistics.  Owner: WS3 (Leaderboard).

Each call is a survival observation: the arm "survives" until the caller first says
"tum bot ho". Calls that end with no accusation are right-censored at their length.
Estimate the survival curve per arm with Kaplan-Meier; its median is the arm's
Turing Clock. For the human control arm, the accusation rate is the false-accusation
rate. Full definitions: docs/metrics.md.

Credit: "Turing Clock" is Kalpa Labs' proposed metric
(https://kalpalabs.ai/blog/towards-generalist-audio-models).
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    duration_s: float  # accusation time, or call length if censored
    accused: bool  # True = event observed, False = censored


@dataclass(frozen=True)
class SurvivalPoint:
    t: float
    survival: float
    at_risk: int
    events: int


@dataclass(frozen=True)
class ArmStats:
    arm_id: str
    n_calls: int
    n_accused: int
    accusation_rate: float
    median_turing_clock_s: float | None  # None = curve never fell to 0.5 (arm "passed")
    fooled_at_60s: float  # P(not yet accused at 60 s)
    curve: list[SurvivalPoint]


def kaplan_meier(observations: Iterable[Observation]) -> list[SurvivalPoint]:
    """Kaplan-Meier estimate. Handle ties and censoring correctly. TODO(WS3)"""
    raise NotImplementedError


def arm_stats(arm_id: str, observations: Sequence[Observation]) -> ArmStats:
    """Summary numbers for one arm (and, called per language, one arm x language).
    TODO(WS3)"""
    raise NotImplementedError
