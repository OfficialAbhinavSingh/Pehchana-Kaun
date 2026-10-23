"""Executable specs for the stubs. Each is xfail until its owner implements it;
once the stub is real, a wrong answer fails loudly (AssertionError is not xfailed).
Add cases as you learn from real test calls."""

import pytest

todo = pytest.mark.xfail(raises=NotImplementedError, reason="stub not implemented yet")


@todo
def test_ws2_detects_hinglish_accusation():
    from pehchana.detection import Word, detect_accusations

    words = [
        Word("acha", 10.0, 10.3),
        Word("tum", 41.2, 41.4),
        Word("bot", 41.4, 41.7),
        Word("ho!", 41.7, 41.9),
    ]
    hits = detect_accusations(words)
    assert [round(h.at_s, 1) for h in hits] == [41.2]


@todo
def test_ws2_ignores_talk_about_bots():
    from pehchana.detection import Word, detect_accusations

    words = [Word(w, i, i + 0.2) for i, w in enumerate(["kal", "maine", "ek", "bot", "banaya"])]
    assert detect_accusations(words) == []


@todo
def test_ws3_kaplan_meier_with_censoring():
    from pehchana.scoring import Observation, arm_stats

    obs = [
        Observation(10, True),
        Observation(20, False),
        Observation(30, True),
        Observation(40, True),
    ]
    stats = arm_stats("x", obs)
    # S(10)=3/4, S(30)=3/4*(1-1/2)=3/8 -> median at 30s
    assert stats.median_turing_clock_s == 30
    assert stats.n_accused == 3


def test_ws1_human_arm_only_in_live_hours():
    from datetime import UTC, datetime

    from pehchana.arms import Arm, eligible_arms

    human = Arm("human", "human", "Insaan", None, 1.0, dial_numbers=("+910000000000",))
    ai = Arm(
        "kalpa",
        "ai",
        "Voice A",
        "Kalpa Labs",
        1.0,
        dial_numbers=("+910000000001",),
        bolna_agent_id="agent",
    )
    at_3am_ist = datetime(2026, 10, 27, 21, 30, tzinfo=UTC)
    assert eligible_arms([human, ai], channel="phone", now=at_3am_ist) == [ai]
    assert eligible_arms([human, ai], channel="phone", now=at_3am_ist, humans_override=True) == [
        human,
        ai,
    ]
