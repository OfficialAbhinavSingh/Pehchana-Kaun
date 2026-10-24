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

import math
from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable, Sequence
from dataclasses import dataclass
from datetime import datetime

# Two-sided 95% normal quantile, for the Greenwood intervals.
Z_95 = 1.959963984540054


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
    # 95% pointwise CI for survival (Greenwood, log-log). None while survival is 1.0,
    # where the interval is undefined.
    ci_low: float | None = None
    ci_high: float | None = None


@dataclass(frozen=True)
class ArmStats:
    arm_id: str
    n_calls: int
    n_accused: int
    accusation_rate: float
    median_turing_clock_s: float | None  # None = curve never fell to 0.5 (arm "passed")
    fooled_at_60s: float  # P(not yet accused at 60 s)
    curve: list[SurvivalPoint]
    # 95% CI for the median; None at either end = that bound is not reached yet.
    median_ci_low_s: float | None = None
    median_ci_high_s: float | None = None


def kaplan_meier(observations: Iterable[Observation], z: float = Z_95) -> list[SurvivalPoint]:
    """Kaplan-Meier estimate, one point per distinct observed time, in time order.

    At each time t with d accusations among n callers still at risk, S *= (1 - d/n).
    Calls censored at t are still at risk at t (events happen before censoring at the
    same time) and leave the risk set after it. Points at censor-only times keep the
    previous survival and have ``events == 0``; the UI can draw them as censor ticks.
    """
    events: defaultdict[float, int] = defaultdict(int)
    censored: defaultdict[float, int] = defaultdict(int)
    for o in observations:
        if not math.isfinite(o.duration_s) or o.duration_s < 0:
            raise ValueError(f"observation time must be finite and >= 0, got {o.duration_s}")
        (events if o.accused else censored)[o.duration_s] += 1

    at_risk = sum(events.values()) + sum(censored.values())
    survival = 1.0
    greenwood = 0.0  # running sum of d / (n * (n - d))
    curve: list[SurvivalPoint] = []
    for t in sorted(events.keys() | censored.keys()):
        d = events[t]
        if d:
            survival *= 1 - d / at_risk
            greenwood = math.inf if d == at_risk else greenwood + d / (at_risk * (at_risk - d))
        low, high = _log_log_ci(survival, greenwood, z)
        curve.append(SurvivalPoint(t, survival, at_risk, d, low, high))
        at_risk -= d + censored[t]
    return curve


def _log_log_ci(survival: float, greenwood: float, z: float) -> tuple[float | None, float | None]:
    """Pointwise CI for S(t) on the log(-log S) scale, so it stays inside [0, 1]."""
    if survival >= 1.0:
        return None, None
    if survival <= 0.0 or math.isinf(greenwood):
        return 0.0, 0.0
    se = math.sqrt(greenwood) / abs(math.log(survival))
    return survival ** math.exp(z * se), survival ** math.exp(-z * se)


def survival_at(curve: Sequence[SurvivalPoint], t: float) -> float:
    """S(t) read off a KM curve (right-continuous step). Past the last observed time the
    last value is carried forward."""
    survival = 1.0
    for p in curve:
        if p.t > t:
            break
        survival = p.survival
    return survival


def _first_time_at_or_below_half(
    curve: Sequence[SurvivalPoint], values: Sequence[float | None]
) -> float | None:
    # Products like 0.8 * 0.75 * (5/6) land on 0.5000000000000001; that is still 0.5.
    for p, v in zip(curve, values, strict=True):
        if v is not None and v <= 0.5 + 1e-9:
            return p.t
    return None


def arm_stats(arm_id: str, observations: Sequence[Observation]) -> ArmStats:
    """Summary numbers for one arm (and, called per language, one arm x language).

    The median is the first time the curve is at or below 0.5. Its CI comes from the
    pointwise band: the lower bound is where the lower band first reaches 0.5, the upper
    bound where the upper band does (the way lifelines reports it). With no
    observations, ``fooled_at_60s`` is 1.0 and ``n_calls`` is 0; show ``n_calls`` next
    to every number.
    """
    curve = kaplan_meier(observations)
    n = len(observations)
    accused = sum(o.accused for o in observations)
    return ArmStats(
        arm_id=arm_id,
        n_calls=n,
        n_accused=accused,
        accusation_rate=accused / n if n else 0.0,
        median_turing_clock_s=_first_time_at_or_below_half(curve, [p.survival for p in curve]),
        fooled_at_60s=survival_at(curve, 60.0),
        curve=curve,
        median_ci_low_s=_first_time_at_or_below_half(curve, [p.ci_low for p in curve]),
        median_ci_high_s=_first_time_at_or_below_half(curve, [p.ci_high for p in curve]),
    )


def group_by[T, K: Hashable](items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Split items by key, keeping input order inside each group (e.g. per language)."""
    groups: dict[K, list[T]] = {}
    for item in items:
        groups.setdefault(key(item), []).append(item)
    return groups


def first_calls[T](
    items: Iterable[T],
    caller: Callable[[T], str | None],
    started_at: Callable[[T], datetime],
) -> list[T]:
    """Keep each caller's first call only (repeat callers learn the voices).

    Items with no caller hash (web calls) cannot be linked to a caller, so each is kept.
    Returned in start order.
    """
    first: dict[str, T] = {}
    anonymous: list[T] = []
    for item in items:
        who = caller(item)
        if who is None:
            anonymous.append(item)
        elif who not in first or started_at(item) < started_at(first[who]):
            first[who] = item
    return sorted([*first.values(), *anonymous], key=started_at)
