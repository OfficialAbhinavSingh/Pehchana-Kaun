"""/bolna/fn/accuse and /bolna/webhook.

The execution payload below is a real completed execution (Soham's #3 bridge test),
pulled live and redacted -- not hand-guessed -- so a test passing here means the real
shape is handled, not just a plausible one. See the note on PR #52.
"""

from datetime import UTC, datetime, timedelta

import pytest

from pehchana import db
from pehchana.api.deps import get_arms
from pehchana.arms import Arm
from pehchana.config import Settings, get_settings
from pehchana.models import Accusation, AccusationSource, Call, CallStatus, Channel, Source

AGENT_ID = "f5ac42a4-7ddb-4af9-a85b-91329aa0891b"
AI = Arm("kalpa", "ai", "Voice A", "Kalpa", 1.0, bolna_agent_id=AGENT_ID)
SALT = "test-salt"


def hash_of(number: str) -> str:
    from pehchana.telephony.call_flow import hash_caller

    result = hash_caller(number, SALT)
    assert result is not None
    return result


EXECUTION = {
    "id": "be0571d1-2112-4fe5-b60b-ba4e0ad3b92a",
    "agent_id": AGENT_ID,
    "status": "completed",
    "conversation_duration": 37.0,
    "total_cost": 4.68,
    "transcript": "assistant: Haan hello?\nuser: tum bot ho\nassistant: Haan, main AI hoon.",
    "user_number": "+910000000001",
    "agent_number": "+910000000002",
    "created_at": "2026-10-28T18:00:24.716297+00:00",
    "updated_at": "2026-10-28T18:01:22.533263+00:00",
    "processing_status": None,
    "billing_settled": False,
    "termination_reason": "agent_ended_call",
    "telephony_data": {
        "duration": 37.0,
        "to_number": "+910000000002",
        "from_number": "+910000000001",
        "recording_url": "https://api.bolna.ai/recordings/call/REDACTED.mp3",
        "hosted_telephony": True,
        "provider_call_id": "53d87850-dff5-4f6e-8c9c-13f6757ab1e1",
        "call_type": "inbound",
        "provider": "vobiz",
        "hangup_by": "Callee",
        "hangup_reason": "end_call_tool",
        "hangup_provider_code": 4010,
        "ring_duration": None,
        "post_dial_delay": None,
        "to_number_carrier": None,
    },
    "provider": "vobiz",
    "tool_call_logs": [],
}


@pytest.fixture
def bolna(client):
    client.app.dependency_overrides[get_arms] = lambda: [AI]
    client.app.dependency_overrides[get_settings] = lambda: Settings(
        caller_hash_salt=SALT, bolna_shared_secret="shh"
    )
    yield client
    client.app.dependency_overrides.clear()


def make_call(
    *,
    arm_id: str = "kalpa",
    caller: str = "+910000000001",
    started_at: datetime | None = None,
    answered_at: datetime | None = None,
    status: CallStatus = CallStatus.LIVE,
    duration_s: float | None = None,
) -> Call:
    now = datetime.now(UTC)
    call = Call(
        channel=Channel.PHONE,
        source=Source.REAL,
        status=status,
        arm_id=arm_id,
        arm_kind="ai",
        caller_hash=hash_of(caller),
        started_at=started_at or now,
        answered_at=answered_at or now,
        duration_s=duration_s,
    )
    with db.get_sessionmaker()() as s:
        s.add(call)
        s.commit()
        s.refresh(call)
    return call


def get_call(call_id: str) -> Call:
    with db.get_sessionmaker()() as s:
        call = s.get(Call, call_id)
        assert call is not None
        s.expunge(call)
        return call


# --- /bolna/fn/accuse ----------------------------------------------------------------

ACCUSE_BODY = {"caller_phrase": "tum bot ho", "agent_id": AGENT_ID, "from_number": "+910000000001"}


def test_accuse_needs_the_right_bearer_secret(bolna):
    make_call()
    assert bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY).status_code == 401
    bad = {"Authorization": "Bearer wrong"}
    assert bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY, headers=bad).status_code == 401


def test_accuse_logs_a_function_accusation_and_returns_the_reveal(bolna):
    call = make_call()
    r = bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY, headers={"Authorization": "Bearer shh"})
    assert r.status_code == 200
    body = r.json()
    assert body["result"] == "caught" and "AI" in body["say"]
    with db.get_sessionmaker()() as s:
        (acc,) = s.query(Accusation).filter(Accusation.call_id == call.id).all()
        assert acc.source == AccusationSource.FUNCTION
        assert acc.phrase == "tum bot ho"
        assert acc.at_s is not None and acc.at_s >= 0


def test_accuse_never_logs_the_raw_caller_number(bolna, caplog):
    make_call()
    bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY, headers={"Authorization": "Bearer shh"})
    assert "+910000000001" not in caplog.text


def test_accuse_with_unknown_agent_id_still_reveals_but_logs_nothing(bolna):
    body = {**ACCUSE_BODY, "agent_id": "no-such-agent"}
    r = bolna.post("/bolna/fn/accuse", json=body, headers={"Authorization": "Bearer shh"})
    assert r.status_code == 200 and r.json()["result"] == "caught"
    with db.get_sessionmaker()() as s:
        assert s.query(Accusation).count() == 0


def test_accuse_with_no_matching_open_call_still_reveals(bolna):
    # a call for a different caller only
    make_call(caller="+910000000099")
    r = bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY, headers={"Authorization": "Bearer shh"})
    assert r.status_code == 200 and r.json()["result"] == "caught"
    with db.get_sessionmaker()() as s:
        assert s.query(Accusation).count() == 0


def test_accuse_ignores_a_call_too_old_to_be_live(bolna):
    make_call(started_at=datetime.now(UTC) - timedelta(minutes=20))
    bolna.post("/bolna/fn/accuse", json=ACCUSE_BODY, headers={"Authorization": "Bearer shh"})
    with db.get_sessionmaker()() as s:
        assert s.query(Accusation).count() == 0


# --- /bolna/webhook --------------------------------------------------------------------


def test_webhook_needs_the_right_header_secret(bolna):
    assert bolna.post("/bolna/webhook", json=EXECUTION).status_code == 401
    bad = {"x-bolna-webhook-secret": "wrong"}
    assert bolna.post("/bolna/webhook", json=EXECUTION, headers=bad).status_code == 401


def test_webhook_attaches_a_real_terminal_execution_to_its_call(bolna):
    call = make_call(
        started_at=datetime.fromisoformat("2026-10-28T18:00:10+00:00"),
        duration_s=37.0,
    )
    r = bolna.post("/bolna/webhook", json=EXECUTION, headers={"x-bolna-webhook-secret": "shh"})
    assert r.status_code == 200 and r.json() == {"attached": call.id}
    saved = get_call(call.id)
    assert saved.bolna_execution_id == EXECUTION["id"]
    assert saved.bolna_payload is not None and saved.bolna_payload["status"] == "completed"


def test_webhook_is_idempotent_on_repeated_delivery(bolna):
    call = make_call(
        started_at=datetime.fromisoformat("2026-10-28T18:00:10+00:00"), duration_s=37.0
    )
    headers = {"x-bolna-webhook-secret": "shh"}
    first = bolna.post("/bolna/webhook", json=EXECUTION, headers=headers)
    second = bolna.post("/bolna/webhook", json=EXECUTION, headers=headers)
    assert first.status_code == 200 and first.json() == {"attached": call.id}
    assert second.json() == {"ignored": "already attached (idempotent)"}


def test_webhook_ignores_non_terminal_statuses(bolna):
    make_call(started_at=datetime.fromisoformat("2026-10-28T18:00:10+00:00"), duration_s=37.0)
    r = bolna.post(
        "/bolna/webhook",
        json={**EXECUTION, "status": "in-progress"},
        headers={"x-bolna-webhook-secret": "shh"},
    )
    assert r.json() == {"ignored": "non-terminal status"}


def test_webhook_ignores_a_call_nobody_answered(bolna):
    r = bolna.post(
        "/bolna/webhook",
        json={**EXECUTION, "conversation_duration": 0},
        headers={"x-bolna-webhook-secret": "shh"},
    )
    assert r.json() == {"ignored": "nobody talked"}


def test_webhook_falls_back_to_the_single_open_call_when_caller_id_is_suppressed(bolna):
    call = make_call(
        caller="+919999999999",  # different hash than EXECUTION's user_number
        started_at=datetime.fromisoformat("2026-10-28T18:00:10+00:00"),
        duration_s=37.0,
    )
    r = bolna.post("/bolna/webhook", json=EXECUTION, headers={"x-bolna-webhook-secret": "shh"})
    assert r.json() == {"attached": call.id}


# --- IP allowlist (off by default; both routes share the same check) -----------------


@pytest.fixture
def bolna_with_allowlist(client):
    from fastapi.testclient import TestClient

    client.app.dependency_overrides[get_arms] = lambda: [AI]
    client.app.dependency_overrides[get_settings] = lambda: Settings(
        caller_hash_salt=SALT,
        bolna_shared_secret="shh",
        enforce_bolna_ip_allowlist=True,
        bolna_webhook_ips=["13.203.39.153"],
    )
    yield TestClient(client.app, client=("203.0.113.9", 5000))
    client.app.dependency_overrides.clear()


def test_accuse_refuses_an_unlisted_source_ip_when_enforced(bolna_with_allowlist):
    r = bolna_with_allowlist.post(
        "/bolna/fn/accuse", json=ACCUSE_BODY, headers={"Authorization": "Bearer shh"}
    )
    assert r.status_code == 403


def test_webhook_refuses_an_unlisted_source_ip_when_enforced(bolna_with_allowlist):
    r = bolna_with_allowlist.post(
        "/bolna/webhook", json=EXECUTION, headers={"x-bolna-webhook-secret": "shh"}
    )
    assert r.status_code == 403
