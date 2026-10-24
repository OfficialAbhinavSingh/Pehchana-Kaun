import random
from datetime import UTC, datetime
from pathlib import Path

import pytest

from pehchana.arms import Arm, NoArmAvailable, choose_arm, eligible_arms, load_arms

REPO = Path(__file__).resolve().parents[2]
ENV = {
    "HUMAN_ARM_NUMBERS": "+911, +912 ,",
    "BOLNA_AGENT_ID_KALPA": "agent-k",
    "BOLNA_NUMBER_KALPA": "+913",
    "BOLNA_AGENT_ID_SARVAM": "agent-s",  # agent but no number: web only
}
# Tue 2026-10-27 20:00 IST (inside weekday window) and 03:00 IST
EVENING = datetime(2026, 10, 27, 14, 30, tzinfo=UTC)
NIGHT = datetime(2026, 10, 27, 21, 30, tzinfo=UTC)


def test_load_arms_resolves_env_and_skips_unconfigured():
    arms = {a.id: a for a in load_arms(REPO / "bolna" / "arms.yaml", ENV)}
    assert set(arms) == {"human", "kalpa", "sarvam"}  # cartesia has nothing set
    assert arms["human"].dial_numbers == ("+911", "+912")
    assert arms["human"].live_hours is not None
    assert arms["kalpa"].bolna_agent_id == "agent-k"
    assert arms["sarvam"].dial_numbers == ()


def test_load_arms_rejects_duplicate_ids(tmp_path):
    f = tmp_path / "arms.yaml"
    entry = "  - {id: a, kind: ai, public_label: x, weight: 1, dial_numbers_env: N}\n"
    f.write_text("arms:\n" + entry * 2)
    with pytest.raises(ValueError, match="duplicate"):
        load_arms(f, {"N": "+91"})


def test_live_hours_window_edges():
    human = load_arms(REPO / "bolna" / "arms.yaml", ENV)[0]
    assert human.live_hours is not None
    assert human.live_hours.is_open(EVENING)
    assert not human.live_hours.is_open(NIGHT)


def test_eligibility_per_channel_and_override():
    human = Arm("h", "human", "H", None, 1.0, dial_numbers=("+91",))
    web_only = Arm("w", "ai", "W", "v", 1.0, bolna_agent_id="a")
    phone_ai = Arm("p", "ai", "P", "v", 1.0, dial_numbers=("+92",), bolna_agent_id="a")
    arms = [human, web_only, phone_ai]
    assert eligible_arms(arms, channel="phone", now=NIGHT) == [phone_ai]  # no hours: closed
    assert eligible_arms(arms, channel="phone", now=NIGHT, humans_override=True) == [
        human,
        phone_ai,
    ]
    assert eligible_arms(arms, channel="phone", now=NIGHT, humans_override=False) == [phone_ai]
    assert eligible_arms(arms, channel="web", now=NIGHT, humans_override=True) == [
        web_only,
        phone_ai,
    ]


def test_choose_arm_rejects_empty():
    with pytest.raises(NoArmAvailable):
        choose_arm([], {})


def test_choose_arm_balances_toward_undersampled():
    a = Arm("a", "ai", "A", None, 1.0)
    b = Arm("b", "ai", "B", None, 1.0)
    rng = random.Random(0)
    picks = [choose_arm([a, b], {"a": 99, "b": 0}, rng).id for _ in range(1000)]
    assert picks.count("b") > 900
    assert picks.count("a") > 0  # still possible: not predictable
