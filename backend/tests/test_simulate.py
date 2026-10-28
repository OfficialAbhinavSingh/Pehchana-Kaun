import pytest
from sqlalchemy import select
from typer.testing import CliRunner

from pehchana import db
from pehchana.api.deps import get_arms
from pehchana.arms import Arm
from pehchana.cli import app
from pehchana.config import Settings, get_settings
from pehchana.models import Call, CallStatus, Source
from pehchana.simulate import (
    SCENARIOS,
    Answer,
    PlivoDialect,
    Simulator,
    UnknownDialect,
    arm_for_numbers,
    get_dialect,
    verify_db,
)
from pehchana.telephony import call_flow
from pehchana.telephony.base import (
    DialResult,
    IncomingCall,
    ProviderResponse,
    RecordingEvent,
)

TOKEN = "sim-token"
BASE = "https://pk.example"
AI = Arm("kalpa", "ai", "Voice A", "Kalpa", 1.0, dial_numbers=("+913",), bolna_agent_id="a")
OTHER = Arm(
    "cartesia", "ai", "Voice B", "Cartesia", 1.0, dial_numbers=("+914",), bolna_agent_id="b"
)
SETTINGS = Settings(
    plivo_auth_token=TOKEN, caller_hash_salt="salt", public_base_url=BASE, consent_audio_url=""
)


@pytest.fixture
def sim(client):
    client.app.dependency_overrides[get_settings] = lambda: SETTINGS
    client.app.dependency_overrides[get_arms] = lambda: [AI]
    yield Simulator(client, SETTINGS, [AI])
    client.app.dependency_overrides.clear()


def failures(report):
    return [f"{s.name}: {s.detail}" for s in report.steps if not s.ok]


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_every_scenario_passes_against_the_app_and_leaves_the_right_row(sim, scenario):
    report = sim.run(scenario)
    with db.get_sessionmaker()() as s:
        verify_db(s, report)
    assert failures(report) == []
    assert report.steps  # a scenario that checks nothing would pass trivially


def test_happy_path_reports_which_arm_answered(sim):
    assert sim.happy().arm_id == "kalpa"


def test_calls_are_rehearsals_that_stay_out_of_stats_and_balancing(sim):
    sim.happy()
    with db.get_sessionmaker()() as s:
        call = s.scalars(select(Call)).one()
        assert call.source == Source.DEMO
        assert call_flow._recent_counts(s, call.started_at) == {}


def test_wrong_signing_token_fails_instead_of_passing(client):
    client.app.dependency_overrides[get_settings] = lambda: SETTINGS
    client.app.dependency_overrides[get_arms] = lambda: [AI]
    wrong = Settings(plivo_auth_token="other", public_base_url=BASE)
    report = Simulator(client, wrong, [AI]).happy()
    client.app.dependency_overrides.clear()
    assert not report.ok
    assert any("answer returns 200" in f for f in failures(report))


def test_busy_answer_is_reported_as_no_arm_not_as_a_crash(client):
    client.app.dependency_overrides[get_settings] = lambda: SETTINGS
    client.app.dependency_overrides[get_arms] = lambda: []
    report = Simulator(client, SETTINGS, []).happy()
    client.app.dependency_overrides.clear()
    assert not report.ok
    assert any("an arm picked the call" in f for f in failures(report))


def test_verify_db_notices_a_call_that_is_in_the_wrong_state(sim):
    report = sim.happy()
    with db.get_sessionmaker()() as s:
        s.get(Call, report.call_id).status = CallStatus.FAILED
        s.commit()
        verify_db(s, report)
    assert any("status is ended" in f for f in failures(report))


def test_verify_db_accepts_a_call_the_pipeline_already_processed(sim):
    report = sim.happy()
    with db.get_sessionmaker()() as s:
        s.get(Call, report.call_id).status = CallStatus.PROCESSED
        s.commit()
        verify_db(s, report)
    assert failures(report) == []


def test_parse_answer_and_arm_lookup():
    xml = (
        '<Response><Record callbackUrl="x"/><Dial action="https://h/d?call_id=c1">'
        "<Number>+913</Number><Number>+915</Number></Dial></Response>"
    )
    answer = PlivoDialect().parse_answer(xml)
    assert (answer.call_id, answer.dial_numbers, answer.has_record) == (
        "c1",
        ("+913", "+915"),
        True,
    )
    assert arm_for_numbers([AI, OTHER], ("+914",)) == "cartesia"
    assert arm_for_numbers([AI, OTHER], ("+999",)) is None
    assert arm_for_numbers([AI], ()) is None


def test_cli_needs_a_token_and_a_known_scenario(monkeypatch):
    runner = CliRunner()
    monkeypatch.setenv("PLIVO_AUTH_TOKEN", "")
    get_settings.cache_clear()
    assert runner.invoke(app, ["simulate-call"]).exit_code == 2
    monkeypatch.setenv("PLIVO_AUTH_TOKEN", "t")
    get_settings.cache_clear()
    assert runner.invoke(app, ["simulate-call", "--scenario", "nope"]).exit_code == 2
    # nothing listens on the discard port: reported, not a traceback
    dead = runner.invoke(app, ["simulate-call", "--target", "http://127.0.0.1:9"])
    assert dead.exit_code == 2
    get_settings.cache_clear()


def test_bad_recording_scenario_ends_the_call_before_the_recording(sim):
    report = sim.bad_recording()
    with db.get_sessionmaker()() as s:
        verify_db(s, report)
    assert failures(report) == []
    names = [step.name for step in report.steps]
    assert names.index("dial-status gets 204") < names.index("recording gets 400")
    with db.get_sessionmaker()() as s:
        call = s.scalars(select(Call)).one()
        assert (call.status, call.duration_s) == (CallStatus.ENDED, 75.0)


def test_provider_defaults_to_the_configured_one_and_unknown_is_refused():
    assert get_dialect("plivo").name == "plivo"
    with pytest.raises(UnknownDialect, match="no simulator for provider 'twilio'"):
        get_dialect("twilio")
    assert Simulator(None, SETTINGS).dialect.name == SETTINGS.telephony_provider  # type: ignore[arg-type]


def test_cli_refuses_a_provider_it_cannot_imitate(monkeypatch):
    monkeypatch.setenv("PLIVO_AUTH_TOKEN", "t")
    get_settings.cache_clear()
    r = CliRunner().invoke(app, ["simulate-call", "--provider", "twilio"])
    get_settings.cache_clear()
    assert r.exit_code == 2


class FakeProvider:
    """A second vendor with its own field names, plain-text answer and no signature."""

    name = "fake"

    def verify(self, request):
        return True

    def parse_incoming(self, form):
        return IncomingCall(form["from"], form["id"])

    def answer_response(self, plan):
        return ProviderResponse(
            f"DIAL {','.join(plan.dial_numbers)} {plan.dial_status_url}", "text/plain"
        )

    def busy_response(self):
        return ProviderResponse("BUSY", "text/plain")

    def parse_dial_status(self, form):
        return DialResult(answered=form["ok"] == "1", duration_s=float(form["secs"]))

    def parse_recording(self, form):
        return RecordingEvent(form["url"], caller_channel=1)


class FakeDialect:
    name = "fake"

    def token(self, settings):
        return "unused"

    def sign(self, url, form, token):
        return {}

    def answer_form(self, caller, call_uuid):
        return {"from": caller, "id": call_uuid}

    def dial_status_form(self, call_uuid, *, answered, duration_s=None):
        return {"ok": "1" if answered else "0", "secs": str(duration_s or 0)}

    def recording_form(self, url):
        return {"url": url}

    def parse_answer(self, body):
        _head, numbers, action = body.split(" ")
        return Answer(action.split("call_id=")[1], tuple(numbers.split(",")), has_record=True)


@pytest.fixture
def fake_vendor(monkeypatch):
    """Register a second provider before the app (and so its routes) is built."""
    from pehchana.telephony import registry

    monkeypatch.setitem(registry._FACTORIES, "fake", lambda settings: FakeProvider())


@pytest.mark.parametrize("scenario", ["happy", "retries", "no-answer"])
def test_scenarios_are_vendor_neutral(fake_vendor, client, scenario):
    from pehchana.api import telephony

    client.app.include_router(telephony._provider_router("fake"))
    client.app.dependency_overrides[get_settings] = lambda: SETTINGS
    client.app.dependency_overrides[get_arms] = lambda: [AI]
    report = Simulator(client, SETTINGS, [AI], FakeDialect()).run(scenario)
    client.app.dependency_overrides.clear()
    assert report.steps
    assert failures(report) == []
    with db.get_sessionmaker()() as s:
        assert s.scalars(select(Call)).one().provider == "fake"
