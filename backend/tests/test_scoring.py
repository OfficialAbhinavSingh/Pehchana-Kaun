"""Turing Clock statistics. Reference values come from lifelines 0.30 (KaplanMeierFitter,
default log-log Greenwood interval) on the same data."""

from datetime import UTC, datetime, timedelta

import pytest

from pehchana.scoring import (
    Observation,
    arm_stats,
    first_calls,
    group_by,
    kaplan_meier,
    survival_at,
)

T = [5, 8, 8, 12, 15, 15, 15, 20, 22, 30, 30, 41, 45, 60, 75]
E = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
SAMPLE = [Observation(float(t), bool(e)) for t, e in zip(T, E, strict=True)]

# t: (survival, ci_low, ci_high) from lifelines
LIFELINES = {
    5: (0.9333333333, 0.6126412438, 0.9903322367),
    8: (0.8666666667, 0.5639120057, 0.9648844959),
    12: (0.7944444444, 0.4879051957, 0.9288700888),
    15: (0.65, 0.3512710898, 0.8374618939),
    20: (0.65, 0.3512710898, 0.8374618939),
    22: (0.5571428571, 0.2603204161, 0.7755169339),
    30: (0.4642857143, 0.1850115582, 0.7054768025),
    41: (0.3482142857, 0.0989853978, 0.6180462676),
    45: (0.3482142857, 0.0989853978, 0.6180462676),
    60: (0.1741071429, 0.0122517806, 0.4994883477),
    75: (0.1741071429, 0.0122517806, 0.4994883477),
}


def test_curve_and_pointwise_ci_match_lifelines():
    curve = kaplan_meier(SAMPLE)
    assert [p.t for p in curve] == sorted(LIFELINES)
    for p in curve:
        s, low, high = LIFELINES[int(p.t)]
        assert (p.survival, p.ci_low, p.ci_high) == pytest.approx((s, low, high), abs=1e-9)


def test_median_and_its_ci_match_lifelines():
    stats = arm_stats("x", SAMPLE)
    assert stats.median_turing_clock_s == 30
    assert (stats.median_ci_low_s, stats.median_ci_high_s) == (12, 60)


def test_summary_numbers():
    stats = arm_stats("kalpa", SAMPLE)
    assert (stats.arm_id, stats.n_calls, stats.n_accused) == ("kalpa", 15, 9)
    assert stats.accusation_rate == pytest.approx(9 / 15)
    assert stats.fooled_at_60s == pytest.approx(0.1741071429)


def test_ties_count_events_before_censoring():
    # At t=8 one accusation and one hang-up: both are at risk at 8, so S = 3/4 * (1 - 1/3).
    curve = kaplan_meier(
        [Observation(4, True), Observation(8, True), Observation(8, False), Observation(9, True)]
    )
    assert [(p.t, p.at_risk, p.events) for p in curve] == [(4, 4, 1), (8, 3, 1), (9, 1, 1)]
    assert curve[1].survival == pytest.approx(0.5)
    assert curve[2].survival == 0.0


def test_censor_only_times_keep_survival_and_mark_no_events():
    curve = kaplan_meier([Observation(10, True), Observation(20, False), Observation(30, True)])
    assert [(p.t, p.events) for p in curve] == [(10, 1), (20, 0), (30, 1)]
    assert curve[1].survival == curve[0].survival


def test_all_censored_means_the_arm_passed():
    stats = arm_stats("human", [Observation(t, False) for t in (30, 45, 90)])
    assert stats.n_accused == 0
    assert stats.accusation_rate == 0.0
    assert stats.median_turing_clock_s is None
    assert (stats.median_ci_low_s, stats.median_ci_high_s) == (None, None)
    assert stats.fooled_at_60s == 1.0
    assert all(p.survival == 1.0 and p.ci_low is None for p in stats.curve)


def test_no_calls():
    stats = arm_stats("sarvam", [])
    assert (stats.n_calls, stats.n_accused, stats.accusation_rate) == (0, 0, 0.0)
    assert stats.median_turing_clock_s is None
    assert stats.fooled_at_60s == 1.0
    assert stats.curve == []


def test_everyone_accused_at_once_drops_to_zero():
    stats = arm_stats("x", [Observation(12, True)] * 3)
    (point,) = stats.curve
    assert (point.survival, point.ci_low, point.ci_high) == (0.0, 0.0, 0.0)
    assert stats.median_turing_clock_s == 12


def test_median_is_the_first_time_at_or_below_half():
    # S lands on exactly 0.5 at t=20 and never goes lower. docs/metrics.md defines the
    # median as the first t with S <= 0.5, so it is 20. (lifelines needs S < 0.5 and
    # would call this arm "passed".)
    obs = [Observation(10, True), Observation(20, True), Observation(30, False)]
    obs += [Observation(40, False)]
    assert survival_at(kaplan_meier(obs), 20) == 0.5
    assert arm_stats("x", obs).median_turing_clock_s == 20


def test_float_noise_at_half_still_counts_as_half():
    # 0.8 * 0.75 * (5/6) is 0.5000000000000001 in floating point.
    obs = [Observation(1, True)] * 2 + [Observation(2, True)] * 2 + [Observation(3, True)]
    obs += [Observation(3, False)] * 3 + [Observation(10, False)] * 2
    assert survival_at(kaplan_meier(obs), 3) > 0.5
    assert arm_stats("x", obs).median_turing_clock_s == 3


def test_survival_at_is_a_right_continuous_step():
    curve = kaplan_meier(SAMPLE)
    assert survival_at(curve, 0) == 1.0
    assert survival_at(curve, 4.99) == 1.0
    assert survival_at(curve, 5) == pytest.approx(0.9333333333)
    assert survival_at(curve, 1000) == pytest.approx(0.1741071429)


@pytest.mark.parametrize("bad", [-1.0, float("nan"), float("inf")])
def test_invalid_times_are_rejected(bad):
    with pytest.raises(ValueError, match="finite"):
        kaplan_meier([Observation(bad, True)])


def test_group_by_keeps_order_within_groups():
    items = [("hi", 1), ("ta", 2), ("hi", 3)]
    assert group_by(items, lambda i: i[0]) == {"hi": [("hi", 1), ("hi", 3)], "ta": [("ta", 2)]}


def test_first_calls_keeps_each_callers_earliest_call_and_all_anonymous_ones():
    t0 = datetime(2026, 10, 27, tzinfo=UTC)
    calls = [
        ("a", t0 + timedelta(minutes=5), "a-second"),
        ("a", t0, "a-first"),
        (None, t0 + timedelta(minutes=1), "web-1"),
        ("b", t0 + timedelta(minutes=2), "b-first"),
        (None, t0 + timedelta(minutes=3), "web-2"),
    ]
    kept = first_calls(calls, caller=lambda c: c[0], started_at=lambda c: c[1])
    assert [c[2] for c in kept] == ["a-first", "web-1", "b-first", "web-2"]
