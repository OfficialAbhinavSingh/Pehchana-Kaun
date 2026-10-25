"""Data freeze: snapshot export/load and the pitch numbers sheet (#28)."""

import json
import random
from datetime import UTC, datetime, timedelta

import pytest
from typer.testing import CliRunner

from pehchana import db
from pehchana.api.leaderboard import build_leaderboard
from pehchana.arms import ArmLabel
from pehchana.cli import app as cli
from pehchana.config import REPO_ROOT, Settings
from pehchana.demo import seed_demo_calls
from pehchana.models import (
    Accusation,
    AccusationSource,
    Call,
    CallStatus,
    Channel,
    Giveaway,
    Source,
)
from pehchana.numbers import numbers_sheet
from pehchana.snapshot import CALL_FIELDS, export_snapshot, load_snapshot

LABELS = [
    ArmLabel("human", "human", "Insaan (control)", None),
    ArmLabel("kalpa", "ai", "Voice A", "Kalpa Labs"),
    ArmLabel("cartesia", "ai", "Voice B", "Cartesia"),
]
T0 = datetime(2026, 10, 27, 6, tzinfo=UTC)  # 11:30 IST
SETTINGS = Settings(min_calls_for_ranking=2)


def add(arm, *, duration=60.0, accused=None, caller=None, minutes=0, **extra):
    call = Call(
        arm_id=arm,
        arm_kind="human" if arm == "human" else "ai",
        status=extra.pop("status", CallStatus.PROCESSED),
        source=extra.pop("source", Source.REAL),
        channel=extra.pop("channel", Channel.PHONE),
        language=extra.pop("language", "hi"),
        caller_hash=caller,
        started_at=T0 + timedelta(minutes=minutes),
        duration_s=duration,
        **extra,
    )
    if accused is not None:
        source = (
            AccusationSource.FUNCTION
            if call.channel == Channel.WEB
            else AccusationSource.TRANSCRIPT
        )
        call.accusations.append(Accusation(source=source, at_s=accused, phrase="tum bot ho"))
    with db.get_sessionmaker()() as s:
        s.add(call)
        s.commit()


def snapshot() -> dict:
    with db.get_sessionmaker()() as s:
        return export_snapshot(s)


def test_export_keeps_no_secrets_or_speech(client):
    add(
        "kalpa",
        accused=12,
        caller="c" * 64,
        recording_url="https://media.plivo.com/secret-recording.mp3",
        transcript=[{"word": "namaste"}],
        bolna_payload={"secret": "payload"},
        provider="plivo",
        provider_call_id="plivo-uuid-1",
        processing_error="boom",
    )
    data = snapshot()
    (row,) = data["calls"]
    assert set(row) == {*CALL_FIELDS, "accusations", "giveaways"}
    assert row["accusations"] == [{"source": "transcript", "at_s": 12.0}]
    text = json.dumps(data)
    for secret in ("secret-recording", "namaste", "payload", "plivo-uuid-1", "tum bot", "boom"):
        assert secret not in text
    assert row["caller_hash"] == "c" * 64  # needed to count repeat callers


def test_loaded_snapshot_gives_the_same_leaderboard(client):
    with db.get_sessionmaker()() as s:
        seed_demo_calls(s, LABELS, 150, random.Random(3))
    add("kalpa", accused=20, caller="a" * 64)
    add("kalpa", duration=40, caller="a" * 64, minutes=5)
    settings = Settings(include_demo_data=True, min_calls_for_ranking=2)

    def boards(session):
        return [
            build_leaderboard(session, settings, LABELS, first_call_only=f).model_dump(
                exclude={"generated_at"}
            )
            for f in (False, True)
        ]

    with db.get_sessionmaker()() as s:
        live = boards(s)
    data = json.loads(json.dumps(snapshot()))  # through real JSON, like the file
    assert boards(load_snapshot(data)) == live
    assert live[0]["total_calls"] == 152


def test_unknown_snapshot_version_is_refused():
    with pytest.raises(ValueError, match="version"):
        load_snapshot({"version": 99, "calls": []})


def test_numbers_sheet(client):
    # human: 4 calls, 1 wrongly accused; Voice A caught fast; Voice B not caught
    for i, accused in enumerate([None, None, 30, None]):
        add("human", duration=90, accused=accused, caller=f"h{i}".ljust(64, "0"), minutes=i)
    add("kalpa", accused=10, caller="r".ljust(64, "0"), minutes=10)
    add("kalpa", accused=20, caller="r".ljust(64, "0"), minutes=20)  # repeat caller
    add("kalpa", accused=30, minutes=30)  # no caller id
    add("cartesia", duration=95, minutes=40, language="ta")
    add("cartesia", duration=4, minutes=50, language="ta")  # short and silent
    add("kalpa", duration=50, status=CallStatus.FAILED, minutes=60)
    add("kalpa", accused=8, channel=Channel.WEB, minutes=70)
    add("kalpa", accused=1, source=Source.DEMO, minutes=80)
    with db.get_sessionmaker()() as s:
        call = Call(
            arm_id="kalpa", arm_kind="ai", status=CallStatus.PROCESSED, duration_s=9, started_at=T0
        )
        call.giveaways = [Giveaway(tag="slow_reply", method="heuristic")]
        s.add(call)
        s.commit()

    data = snapshot()
    # INCLUDE_DEMO_DATA must not leak into pitch numbers
    sheet = numbers_sheet(data, LABELS, SETTINGS.model_copy(update={"include_demo_data": True}))

    assert "Calls counted (real, phone, processed): **10**" in sheet
    assert "Unique callers: **5**, plus 4 calls with no caller id" in sheet
    assert "Human called a bot by mistake: **25% of 4 calls**" in sheet
    # Voice A: censored at 9 s, caught at 10, 20, 30 s: S hits 0.5 at 20 s, then 0
    assert "| Voice A | 4 | 75% | 0:20 (0:10 to 0:30) | 0% | yes |" in sheet
    # first call only drops the repeat caller's 20 s call: S = 0.5 already at 10 s
    assert "| Voice A | 3 | 67% | 0:10 (0:10 to 0:30) | 0% | yes |" in sheet
    assert "| Voice B | 2 | 0% | > 1:35 (not reached) | 100% | yes |" in sheet
    assert "2 such calls dropped" in sheet  # Voice B at 4 s and the 9 s call
    assert "- slow_reply: 1" in sheet
    assert "1 call: 4 callers, 2 calls: 1, 3 or more: 0" in sheet
    assert "- 2026-10-27: 10" in sheet
    assert "Processed: 1; ended with a live `accuse_bot` call: 1" in sheet
    assert "demo rows ignored (1 in the file)" in sheet
    assert "### ta" in sheet
    # same snapshot, same sheet
    assert numbers_sheet(data, LABELS, SETTINGS) == numbers_sheet(data, LABELS, SETTINGS)


def test_export_cli_refuses_the_repo_and_numbers_cli_reads_the_file(client, tmp_path):
    add("kalpa", accused=10)
    runner = CliRunner()
    inside = REPO_ROOT / "snapshot.json"
    result = runner.invoke(cli, ["export-snapshot", str(inside)])
    assert result.exit_code == 1 and "refusing" in result.output
    assert not inside.exists()

    out = tmp_path / "freeze.json"
    result = runner.invoke(cli, ["export-snapshot", str(out)])
    assert result.exit_code == 0, result.output
    assert "1 calls" in result.output and "sha256" in result.output
    result = runner.invoke(cli, ["numbers", str(out)])
    assert result.exit_code == 0, result.output
    assert "# Pehchana Kaun? numbers sheet" in result.output
