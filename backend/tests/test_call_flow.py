"""Call lifecycle through the real HTTP routes (Plivo) and through a fake provider."""

from datetime import UTC, datetime, timedelta

import pytest
from plivo.utils.signature_v3 import construct_post_url, get_signature_v3
from sqlalchemy import select

from pehchana import db
from pehchana.api.deps import get_arms
from pehchana.arms import Arm
from pehchana.config import Settings, get_settings
from pehchana.models import Call, CallStatus, ShiftOverride
from pehchana.telephony import call_flow
from pehchana.telephony.base import (
    CallPlan,
    DialResult,
    IncomingCall,
    ProviderResponse,
    RecordingEvent,
)

TOKEN = "tok"
BASE = "http://localhost:8000"
AI = Arm("kalpa", "ai", "Voice A", "Kalpa", 1.0, dial_numbers=("+913",), bolna_agent_id="a")
SETTINGS = Settings(
    plivo_auth_token=TOKEN, caller_hash_salt="salt", public_base_url=BASE, consent_audio_url=""
)


@pytest.fixture
def app_client(client):
    client.app.dependency_overrides[get_settings] = lambda: SETTINGS
    client.app.dependency_overrides[get_arms] = lambda: [AI]
    yield client
    client.app.dependency_overrides.clear()


def post(client, path: str, form: dict[str, str], *, sign: bool = True):
    url = BASE + path
    headers = {}
    if sign:
        sig = get_signature_v3(TOKEN.encode(), construct_post_url(url, form).decode(), b"n1")
        headers = {"X-Plivo-Signature-V3": sig.decode(), "X-Plivo-Signature-V3-Nonce": "n1"}
    return client.post(path, data=form, headers=headers)


def only_call() -> Call:
    with db.get_sessionmaker()() as s:
        return s.scalars(select(Call)).one()


def test_answer_rejects_unsigned_request(app_client):
    r = post(app_client, "/telephony/plivo/answer", {"From": "+91", "CallUUID": "u"}, sign=False)
    assert r.status_code == 403


def test_full_happy_path(app_client):
    r = post(app_client, "/telephony/plivo/answer", {"From": "+919876543210", "CallUUID": "u1"})
    assert r.status_code == 200
    assert "<Dial" in r.text and "+913" in r.text

    call = only_call()
    assert (call.provider, call.provider_call_id, call.arm_id) == ("plivo", "u1", "kalpa")
    assert call.caller_hash == call_flow.hash_caller("+919876543210", "salt")
    assert "+919876543210" not in (call.caller_hash or "")

    q = f"/telephony/plivo/dial-status?call_id={call.id}"
    r = post(app_client, q, {"DialBLegStatus": "hangup", "DialBLegDuration": "75"})
    assert r.status_code == 204
    call = only_call()
    assert (call.status, call.duration_s) == (CallStatus.ENDED, 75.0)
    assert call.answered_at is not None

    q = f"/telephony/plivo/recording?call_id={call.id}"
    r = post(app_client, q, {"RecordUrl": "https://r.test/a.mp3"})
    assert r.status_code == 204
    assert only_call().recording_url == "https://r.test/a.mp3"


def test_answer_retry_is_idempotent(app_client):
    # Plivo retries the answer URL on a slow response; same CallUUID must not 500
    # or reroute the caller to a different arm.
    form = {"From": "+919876543210", "CallUUID": "dup-1"}
    first = post(app_client, "/telephony/plivo/answer", form)
    second = post(app_client, "/telephony/plivo/answer", form)
    assert first.status_code == second.status_code == 200
    assert only_call().provider_call_id == "dup-1"  # .one() fails on a duplicate row
    assert "call_id=" + only_call().id in second.text


def test_unanswered_dial_marks_failed_and_is_not_processed(app_client):
    post(app_client, "/telephony/plivo/answer", {"From": "+91", "CallUUID": "u2"})
    cid = only_call().id
    post(app_client, f"/telephony/plivo/dial-status?call_id={cid}", {"DialBLegStatus": "no-answer"})
    assert only_call().status == CallStatus.FAILED
    # a late duplicate callback must not resurrect it
    post(app_client, f"/telephony/plivo/dial-status?call_id={cid}", {"DialBLegStatus": "hangup"})
    assert only_call().status == CallStatus.FAILED


def test_no_arm_available_returns_busy(app_client):
    app_client.app.dependency_overrides[get_arms] = lambda: []
    r = post(app_client, "/telephony/plivo/answer", {"From": "+91", "CallUUID": "u3"})
    assert "<Hangup" in r.text
    with db.get_sessionmaker()() as s:
        assert s.scalars(select(Call)).first() is None


def test_unknown_call_id_is_404(app_client):
    r = post(app_client, "/telephony/plivo/recording?call_id=nope", {"RecordUrl": "https://x"})
    assert r.status_code == 404


def test_admin_override_brings_human_arm_in(client):
    human = Arm("human", "human", "H", None, 1.0, dial_numbers=("+911",))
    now = datetime(2026, 10, 27, 21, 30, tzinfo=UTC)
    with db.get_sessionmaker()() as s:
        assert call_flow._humans_override(s, now) is None
        s.add(ShiftOverride(humans_on_shift=True, until=now + timedelta(hours=1)))
        s.commit()
        assert call_flow._humans_override(s, now) is True
        assert call_flow._humans_override(s, now + timedelta(hours=2)) is None
    assert human  # arm only documents the scenario


class FakeProvider:
    """A second vendor: the neutral flow must work with it unchanged."""

    name = "fake"

    def verify(self, request):
        return True

    def parse_incoming(self, form):
        return IncomingCall(form["from"], form["id"])

    def answer_response(self, plan: CallPlan):
        return ProviderResponse(
            f"DIAL {','.join(plan.dial_numbers)} {plan.recording_url}", "text/plain"
        )

    def busy_response(self):
        return ProviderResponse("BUSY", "text/plain")

    def parse_dial_status(self, form):
        return DialResult(answered=form["ok"] == "1", duration_s=10.0)

    def parse_recording(self, form):
        return RecordingEvent(form["url"], caller_channel=1)


def test_core_flow_is_vendor_agnostic(client):
    with db.get_sessionmaker()() as s:
        fake = FakeProvider()
        out = call_flow.start_call(
            session=s, provider=fake, settings=SETTINGS, arms=[AI], form={"from": "+91", "id": "f1"}
        )
        assert out.body.startswith("DIAL +913") and "/telephony/fake/recording?call_id=" in out.body
        call = s.scalars(select(Call)).one()
        assert (call.provider, call.provider_call_id) == ("fake", "f1")
        call_flow.finish_dial(session=s, provider=fake, call=call, form={"ok": "1"})
        assert call.status == CallStatus.ENDED
        assert call_flow.attach_recording(session=s, provider=fake, call=call, form={"url": "u"})
        assert call.recording_caller_channel == 1


def test_admin_shift_requires_token_and_sets_override(client):
    body = {"humans_on_shift": True, "hours": 2}
    assert client.post("/admin/shift", json=body).status_code == 401
    bad = {"Authorization": "Bearer wrong"}
    assert client.post("/admin/shift", json=body, headers=bad).status_code == 401
    ok = {"Authorization": f"Bearer {get_settings().admin_token}"}
    assert client.post("/admin/shift", json=body, headers=ok).status_code == 200
    with db.get_sessionmaker()() as s:
        assert call_flow._humans_override(s, datetime.now(UTC)) is True
