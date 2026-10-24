"""GET /leaderboard and the demo seed."""

import random
import re
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest
from sqlalchemy import func, select
from typer.testing import CliRunner

from pehchana import db
from pehchana.api import leaderboard
from pehchana.api.deps import get_arm_labels
from pehchana.arms import ArmLabel, load_arm_labels
from pehchana.cli import app as cli
from pehchana.config import Settings, get_settings
from pehchana.demo import clear_demo_calls, seed_demo_calls
from pehchana.models import (
    Accusation,
    AccusationSource,
    Call,
    CallStatus,
    Giveaway,
    Source,
)

API_TS = Path(__file__).resolve().parents[2] / "web" / "src" / "lib" / "api.ts"
LABELS = [
    ArmLabel("human", "human", "Insaan (control)", None),
    ArmLabel("kalpa", "ai", "Voice A", "Kalpa Labs"),
    ArmLabel("cartesia", "ai", "Voice B", "Cartesia"),
]
T0 = datetime(2026, 10, 27, 12, tzinfo=UTC)


@pytest.fixture
def board(client):
    """Returns get(settings_overrides) -> JSON body of /leaderboard."""
    leaderboard.clear_cache()

    def get(query: str = "", **overrides):
        settings = Settings(**{"min_calls_for_ranking": 2, "leaderboard_cache_s": 0, **overrides})
        client.app.dependency_overrides[get_settings] = lambda: settings
        client.app.dependency_overrides[get_arm_labels] = lambda: LABELS
        r = client.get("/leaderboard" + query)
        assert r.status_code == 200
        return r.json()

    yield get
    client.app.dependency_overrides.clear()
    leaderboard.clear_cache()


def add_call(
    arm: str,
    *,
    duration: float | None = 60.0,
    accused: float | None = None,
    status: CallStatus = CallStatus.PROCESSED,
    source: Source = Source.REAL,
    language: str | None = "hi",
    caller: str | None = None,
    minutes: int = 0,
    tags: tuple[str, ...] = (),
) -> None:
    call = Call(
        arm_id=arm,
        arm_kind="human" if arm == "human" else "ai",
        status=status,
        source=source,
        language=language,
        caller_hash=caller,
        started_at=T0 + timedelta(minutes=minutes),
        duration_s=duration,
    )
    if accused is not None:
        call.accusations.append(Accusation(source=AccusationSource.TRANSCRIPT, at_s=accused))
    for tag in tags:
        call.giveaways.append(Giveaway(tag=tag, method="heuristic"))
    with db.get_sessionmaker()() as s:
        s.add(call)
        s.commit()


def arm(body, arm_id: str) -> dict:
    return next(a for a in body["arms"] if a["arm_id"] == arm_id)


def _ts_fields(type_name: str) -> set[str]:
    block = re.search(rf"export type {type_name} = \{{(.*?)\n\}};", API_TS.read_text(), re.S)
    assert block, f"{type_name} not found in api.ts"
    return set(re.findall(r"^\s+(\w+)\??:", block.group(1), re.M))


def test_response_matches_the_web_contract(board):
    add_call("kalpa", accused=10, tags=("slow_reply",))
    body = board()
    assert set(body) == _ts_fields("Leaderboard")
    assert set(body["arms"][0]) == _ts_fields("ArmStats")
    assert set(arm(body, "voice-a")["curve"][0]) == _ts_fields("SurvivalPoint")


def test_every_configured_arm_is_listed_even_without_calls(board):
    body = board()
    assert [a["arm_id"] for a in body["arms"]] == ["human", "voice-a", "voice-b"]
    assert all(a["n_calls"] == 0 and not a["ranked"] for a in body["arms"])
    assert body["total_calls"] == 0
    assert body["by_language"] == {}


def test_only_processed_real_calls_count(board):
    add_call("kalpa", accused=10)
    add_call("kalpa", status=CallStatus.FAILED)
    add_call("kalpa", status=CallStatus.ENDED)
    add_call("kalpa", status=CallStatus.ROUTED, duration=None)
    add_call("kalpa", source=Source.DEMO, accused=5)
    body = board()
    assert body["includes_demo_data"] is False
    assert body["total_calls"] == 1
    assert arm(body, "voice-a")["n_calls"] == 1


def test_demo_calls_only_with_the_flag_and_then_flagged(board):
    add_call("kalpa", accused=10)
    add_call("kalpa", source=Source.DEMO, accused=5)
    body = board(include_demo_data=True)
    assert body["includes_demo_data"] is True
    assert body["total_calls"] == 2


def test_accused_calls_end_at_the_first_accusation_others_are_censored(board):
    add_call("kalpa", duration=90, accused=30)
    add_call("kalpa", duration=40)  # hung up, never accused
    add_call("kalpa", duration=120, accused=50)
    a = arm(board(), "voice-a")
    assert (a["n_calls"], a["n_accused"]) == (3, 2)
    assert [(p["t"], p["events"]) for p in a["curve"]] == [(30, 1), (40, 0), (50, 1)]
    assert a["median_turing_clock_s"] == 50
    assert a["fooled_at_60s"] == 0.0


def test_calls_that_cannot_be_placed_on_the_clock_are_left_out(board, caplog):
    add_call("kalpa", duration=None)
    with db.get_sessionmaker()() as s:  # accused, but the time is unknown
        call = Call(arm_id="kalpa", arm_kind="ai", status=CallStatus.PROCESSED, duration_s=80)
        call.accusations.append(Accusation(source=AccusationSource.FUNCTION, at_s=None))
        s.add(call)
        s.commit()
    assert arm(board(), "voice-a")["n_calls"] == 0
    assert "no duration" in caplog.text and "no time" in caplog.text


def test_vendors_are_hidden_unless_revealed(board):
    add_call("kalpa", accused=10)
    hidden = board()
    assert "kalpa" not in str(hidden).lower()
    assert arm(hidden, "voice-a")["display_name"] == "Voice A"
    revealed = board(reveal_vendors=True)
    assert arm(revealed, "kalpa")["display_name"] == "Kalpa Labs"
    assert arm(revealed, "human")["display_name"] == "Insaan (control)"


def test_arms_below_the_minimum_are_not_ranked(board):
    add_call("kalpa", accused=10)
    add_call("kalpa", accused=20)
    add_call("cartesia", accused=10)
    body = board()
    assert arm(body, "voice-a")["ranked"] is True
    assert arm(body, "voice-b")["ranked"] is False
    assert body["min_calls_for_ranking"] == 2


def test_order_is_human_then_hardest_to_catch_then_unranked(board):
    for t in (10, 20):
        add_call("kalpa", accused=t)
    for t in (80, 90):
        add_call("cartesia", accused=t)
    assert [a["arm_id"] for a in board()["arms"]] == ["human", "voice-b", "voice-a"]
    add_call("human", duration=100)
    add_call("human", duration=100)
    leaderboard.clear_cache()
    body = board(min_calls_for_ranking=3)
    assert [a["arm_id"] for a in body["arms"]] == ["human", "voice-a", "voice-b"]  # file order


def test_human_accusation_rate_is_the_false_accusation_rate(board):
    add_call("human", duration=100)
    add_call("human", duration=100, accused=40)
    assert arm(board(), "human")["accusation_rate"] == 0.5


def test_by_language_splits_each_arm(board):
    add_call("kalpa", accused=10, language="ta")
    add_call("kalpa", duration=200, language="hi")
    add_call("cartesia", accused=30, language="hi")
    add_call("cartesia", duration=50, language=None)
    by_lang = board()["by_language"]
    assert sorted(by_lang) == ["hi", "ta", "unknown"]
    assert [(a["arm_id"], a["n_calls"]) for a in by_lang["ta"]] == [("voice-a", 1)]
    assert {a["arm_id"] for a in by_lang["hi"]} == {"voice-a", "voice-b"}


def test_top_giveaways_are_counted_per_arm(board):
    add_call("kalpa", accused=10, tags=("slow_reply", "too_perfect"))
    add_call("kalpa", accused=20, tags=("slow_reply",))
    assert arm(board(), "voice-a")["top_giveaways"] == [
        {"tag": "slow_reply", "count": 2},
        {"tag": "too_perfect", "count": 1},
    ]


def test_first_call_only_keeps_each_callers_first_game(board):
    add_call("kalpa", accused=60, caller="a", minutes=0)
    add_call("kalpa", accused=5, caller="a", minutes=10)  # learned the voice
    add_call("kalpa", accused=50, caller=None, minutes=20)
    body = board("?first_call_only=true")
    assert body["first_call_only"] is True
    assert arm(body, "voice-a")["n_calls"] == 2
    assert arm(board(), "voice-a")["n_calls"] == 3


def test_calls_for_arms_missing_from_the_config_are_left_out(board, caplog):
    add_call("retired", accused=10)
    assert board()["total_calls"] == 0
    assert "retired" in caplog.text


def test_responses_are_cached_for_the_configured_time(board):
    add_call("kalpa", accused=10)
    first = board(leaderboard_cache_s=30)
    add_call("kalpa", accused=20)
    assert board(leaderboard_cache_s=30) == first
    assert board(leaderboard_cache_s=30, include_demo_data=True)["total_calls"] == 2  # new key
    leaderboard.clear_cache()
    assert board(leaderboard_cache_s=30)["total_calls"] == 2


# --- demo seed -------------------------------------------------------------------


def _count(source: Source) -> int:
    with db.get_sessionmaker()() as s:
        return s.scalar(select(func.count()).select_from(Call).where(Call.source == source)) or 0


def test_seed_demo_makes_plausible_processed_demo_calls(client):
    with db.get_sessionmaker()() as s:
        assert seed_demo_calls(s, LABELS, 120, random.Random(1)) == 120
        calls = s.scalars(select(Call)).all()
        assert {c.source for c in calls} == {Source.DEMO}
        assert {c.status for c in calls} == {CallStatus.PROCESSED}
        assert {c.arm_id for c in calls} == {"human", "kalpa", "cartesia"}
        for c in calls:
            assert c.duration_s is not None and c.duration_s > 0
            if c.first_accusation_s is not None:
                assert c.first_accusation_s <= c.duration_s
                assert c.giveaways
            assert c.caller_hash is not None and len(c.caller_hash) == 64


def test_seed_demo_is_reproducible_and_clear_keeps_real_calls(client):
    add_call("kalpa", accused=10)
    with db.get_sessionmaker()() as s:
        seed_demo_calls(s, LABELS, 30, random.Random(5))
        first = sorted((c.arm_id, c.duration_s) for c in s.scalars(select(Call)).all())
        assert clear_demo_calls(s) == 30
        seed_demo_calls(s, LABELS, 30, random.Random(5))
        again = sorted((c.arm_id, c.duration_s) for c in s.scalars(select(Call)).all())
    assert [x[0] for x in first] == [x[0] for x in again]
    assert _count(Source.REAL) == 1


def test_seeded_data_shows_up_only_with_the_demo_flag(board):
    with db.get_sessionmaker()() as s:
        seed_demo_calls(s, LABELS, 60, random.Random(2))
    assert board()["total_calls"] == 0
    assert board(include_demo_data=True)["total_calls"] == 60


def test_seed_demo_cli_replaces_demo_rows_and_refuses_prod(client, monkeypatch):
    runner = CliRunner()
    result = runner.invoke(cli, ["seed-demo", "--n", "10"])
    assert result.exit_code == 0, result.output
    assert runner.invoke(cli, ["seed-demo", "--n", "10"]).exit_code == 0
    assert _count(Source.DEMO) == 10  # replaced, not added
    assert runner.invoke(cli, ["seed-demo", "--n", "5", "--keep"]).exit_code == 0
    assert _count(Source.DEMO) == 15

    monkeypatch.setenv("ENV", "prod")
    get_settings.cache_clear()
    result = runner.invoke(cli, ["seed-demo"])
    assert result.exit_code == 1
    assert "refusing" in result.output
    get_settings.cache_clear()


def test_the_real_arms_file_has_labels_for_every_arm():
    labels = load_arm_labels(Settings().arms_file)
    assert [x.id for x in labels] == ["human", "kalpa", "cartesia", "sarvam"]
    assert all(x.public_label for x in labels)
