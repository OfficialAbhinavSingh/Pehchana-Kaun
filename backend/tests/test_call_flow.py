"""Call lifecycle through the real HTTP routes (Plivo) and through a fake provider."""

from datetime import UTC, datetime, timedelta

import pytest
from plivo.utils.signature_v3 import construct_post_url, get_signature_v3
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

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
    assert second.text == first.text  # same arm, same dial numbers, same callbacks


def test_answer_race_replays_the_winning_row(client, monkeypatch):
    # Two copies of one webhook both miss the lookup; the loser's insert hits the unique
    # constraint. It must answer from the winner's row, not 500 or pick another arm.
    form = {"from": "+91", "id": "race-1"}
    fake = FakeProvider()
    with db.get_sessionmaker()() as s:
        winner = call_flow.start_call(
            session=s, provider=fake, settings=SETTINGS, arms=[AI], form=form
        )
    real_find = call_flow._find_call
    lookups = []

    def blind_first_lookup(*args):
        lookups.append(1)
        return None if len(lookups) == 1 else real_find(*args)

    monkeypatch.setattr(call_flow, "_find_call", blind_first_lookup)
    with db.get_sessionmaker()() as s:
        loser = call_flow.start_call(
            session=s, provider=fake, settings=SETTINGS, arms=[AI], form=form
        )
    assert len(lookups) == 2  # the race path ran
    assert loser.body == winner.body
    assert only_call().provider_call_id == "race-1"


def test_integrity_error_that_is_not_a_retry_is_not_swallowed(client, monkeypatch):
    # Same unique-constraint failure, but no row with this call id exists afterwards.
    def always_miss(*args):
        return None

    with db.get_sessionmaker()() as s:
        call_flow.start_call(
            session=s,
            provider=FakeProvider(),
            settings=SETTINGS,
            arms=[AI],
            form={"from": "x", "id": "k"},
        )
        monkeypatch.setattr(call_flow, "_find_call", always_miss)
        with pytest.raises(IntegrityError):
            call_flow.start_call(
                session=s,
                provider=FakeProvider(),
                settings=SETTINGS,
                arms=[AI],
                form={"from": "x", "id": "k"},
            )


def test_retry_after_the_call_ended_gets_busy_and_a_log_line(app_client, caplog):
    form = {"From": "+919876543210", "CallUUID": "late-1"}
    post(app_client, "/telephony/plivo/answer", form)
    cid = only_call().id
    post(app_client, f"/telephony/plivo/dial-status?call_id={cid}", {"DialBLegStatus": "hangup"})
    with caplog.at_level("WARNING", logger="pehchana.telephony.call_flow"):
        r = post(app_client, "/telephony/plivo/answer", form)
    assert "<Hangup" in r.text
    assert f"answer retry for call {cid} not replayed" in caplog.text
    assert "+919876543210" not in caplog.text


@pytest.fixture
def queued(monkeypatch):
    """Call ids the pipeline was asked to process."""
    ids: list[str] = []
    monkeypatch.setattr("pehchana.pipeline.process_call", ids.append)
    return ids


def _answered_call(app_client, uuid: str) -> str:
    post(app_client, "/telephony/plivo/answer", {"From": "+91", "CallUUID": uuid})
    cid = only_call().id
    post(app_client, f"/telephony/plivo/dial-status?call_id={cid}", {"DialBLegStatus": "hangup"})
    return cid


def test_recording_retry_queues_the_pipeline_once(app_client, queued):
    cid = _answered_call(app_client, "rec-1")
    q = f"/telephony/plivo/recording?call_id={cid}"
    for _ in range(3):
        assert post(app_client, q, {"RecordUrl": "https://r.test/a.mp3"}).status_code == 204
    assert queued == [cid]
    assert only_call().recording_url == "https://r.test/a.mp3"


def test_a_different_second_recording_is_ignored(app_client, queued, caplog):
    cid = _answered_call(app_client, "rec-2")
    q = f"/telephony/plivo/recording?call_id={cid}"
    post(app_client, q, {"RecordUrl": "https://r.test/first.mp3"})
    with caplog.at_level("WARNING", logger="pehchana.telephony.call_flow"):
        post(app_client, q, {"RecordUrl": "https://r.test/second.mp3"})
    assert only_call().recording_url == "https://r.test/first.mp3"
    assert queued == [cid]
    assert "ignoring a different one" in caplog.text
    assert "second.mp3" not in caplog.text  # recording URLs are bearer secrets: never log them


def test_concurrent_recording_callbacks_have_one_winner(client):
    # Both workers loaded the call before either wrote: the second UPDATE must lose.
    fake = FakeProvider()
    with db.get_sessionmaker()() as s:
        call_flow.start_call(session=s, provider=fake, settings=SETTINGS, arms=[AI], form=FAKE_IN)
    with db.get_sessionmaker()() as a, db.get_sessionmaker()() as b:
        call_a, call_b = a.scalars(select(Call)).one(), b.scalars(select(Call)).one()
        assert call_flow.attach_recording(session=a, provider=fake, call=call_a, form={"url": "u1"})
        assert not call_flow.attach_recording(
            session=b, provider=fake, call=call_b, form={"url": "u2"}
        )
        assert call_b.recording_url == "u1"  # refreshed to what the winner stored


def test_recording_for_a_failed_call_is_stored_but_not_processed(app_client, queued):
    post(app_client, "/telephony/plivo/answer", {"From": "+91", "CallUUID": "rec-3"})
    cid = only_call().id
    post(app_client, f"/telephony/plivo/dial-status?call_id={cid}", {"DialBLegStatus": "no-answer"})
    post(app_client, f"/telephony/plivo/recording?call_id={cid}", {"RecordUrl": "https://r.test/x"})
    assert only_call().recording_url == "https://r.test/x"
    assert queued == []


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


FAKE_IN = {"from": "+91", "id": "f9"}


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
