"""Provider contract + Plivo behaviour. A new provider should pass the contract tests."""

import pytest
from plivo.utils.signature_v3 import construct_post_url, get_signature_v3

from pehchana.config import Settings
from pehchana.telephony.base import (
    CallPlan,
    TelephonyProvider,
    UnknownProvider,
    WebhookRequest,
)
from pehchana.telephony.plivo import PlivoProvider
from pehchana.telephony.registry import get_provider, provider_names

TOKEN = "secret-token"
URL = "https://example.test/telephony/plivo/answer"
NONCE = "12345"
FORM = {"From": "+919999999999", "CallUUID": "abc-123"}
PLAN = CallPlan(
    dial_numbers=["+911111111111", "+912222222222"],
    caller_id="+913333333333",
    consent_audio_url="https://cdn.test/consent.mp3",
    dial_status_url="https://example.test/telephony/plivo/dial-status?call_id=c1",
    recording_url="https://example.test/telephony/plivo/recording?call_id=c1",
)


def _signed(form: dict[str, str], token: str = TOKEN) -> WebhookRequest:
    base = construct_post_url(URL, form)
    sig = get_signature_v3(token.encode(), base.decode(), NONCE.encode()).decode()
    return WebhookRequest(
        "POST",
        URL,
        {"x-plivo-signature-v3": sig, "x-plivo-signature-v3-nonce": NONCE},
        form,
    )


@pytest.fixture
def plivo() -> PlivoProvider:
    return PlivoProvider(auth_token=TOKEN, caller_channel=1)


# --- contract: every provider -------------------------------------------------


def test_plivo_satisfies_protocol(plivo):
    assert isinstance(plivo, TelephonyProvider)


def test_registry_resolves_by_name_and_setting():
    settings = Settings(plivo_auth_token=TOKEN, telephony_provider="plivo")
    assert get_provider(settings=settings).name == "plivo"
    assert get_provider("plivo", settings).name == "plivo"
    assert "plivo" in provider_names()


def test_registry_rejects_unknown_provider():
    with pytest.raises(UnknownProvider):
        get_provider("nope", Settings())


# --- Plivo --------------------------------------------------------------------


def test_verify_accepts_valid_signature(plivo):
    assert plivo.verify(_signed(FORM)) is True


def test_verify_rejects_tampered_form(plivo):
    req = _signed(FORM)
    tampered = WebhookRequest(req.method, req.url, req.headers, {**FORM, "From": "+910000000000"})
    assert plivo.verify(tampered) is False


def test_verify_rejects_wrong_token(plivo):
    assert plivo.verify(_signed(FORM, token="other")) is False


@pytest.mark.parametrize("headers", [{}, {"x-plivo-signature-v3": "x"}])
def test_verify_fails_closed_on_missing_headers(plivo, headers):
    assert plivo.verify(WebhookRequest("POST", URL, headers, FORM)) is False


def test_verify_fails_closed_without_configured_token():
    assert PlivoProvider(auth_token="").verify(_signed(FORM)) is False


def test_parse_incoming(plivo):
    call = plivo.parse_incoming(FORM)
    assert (call.caller, call.provider_call_id) == ("+919999999999", "abc-123")


def test_answer_xml_consent_record_then_dial(plivo):
    r = plivo.answer_response(PLAN)
    xml = r.body
    assert r.media_type == "application/xml"
    assert xml.index("<Play") < xml.index("<Record") < xml.index("<Dial")
    assert 'recordSession="true"' in xml
    assert 'startOnDialAnswer="true"' in xml
    assert 'recordChannelType="stereo"' in xml
    assert "recording?call_id=c1" in xml
    assert "dial-status?call_id=c1" in xml
    # Simultaneous ring = one <Number> per number (first to answer wins).
    assert xml.count("<Number>") == 2
    assert "<Number>+911111111111</Number>" in xml
    assert "<Number>+912222222222</Number>" in xml
    assert "&lt;" not in xml


def test_answer_xml_caps_ring_and_call_length(plivo):
    xml = plivo.answer_response(PLAN).body
    assert 'timeout="30"' in xml  # stop ringing an arm that never picks up
    assert 'timeLimit="600"' in xml  # Plivo's default is 4 hours


def test_answer_xml_falls_back_to_tts_consent(plivo):
    xml = plivo.answer_response(CallPlan(**{**PLAN.__dict__, "consent_audio_url": None})).body
    assert "<Speak" in xml
    # the spoken fallback says what docs/copy.md says, in both languages
    for phrase in ("game hai", "record hogi", "personal details", "phone rakh dijiye"):
        assert phrase in xml
    for phrase in ("a game", "person or an AI", "recorded for research", "hang up now"):
        assert phrase in xml
    assert "<Play" not in xml


def test_busy_xml_hangs_up(plivo):
    xml = plivo.busy_response().body
    assert "<Speak" in xml
    assert xml.index("<Speak") < xml.index("<Hangup")


@pytest.mark.parametrize(
    ("form", "answered", "duration"),
    [
        ({"DialBLegStatus": "hangup", "DialBLegDuration": "42"}, True, 42.0),
        ({"DialBLegStatus": "no-answer"}, False, None),
        ({"DialBLegStatus": "busy"}, False, None),
        ({}, False, None),
    ],
)
def test_parse_dial_status(plivo, form, answered, duration):
    result = plivo.parse_dial_status(form)
    assert (result.answered, result.duration_s) == (answered, duration)


def test_parse_recording_carries_caller_channel(plivo):
    ev = plivo.parse_recording({"RecordUrl": "https://r.test/x.mp3", "RecordingDuration": "61"})
    assert (ev.url, ev.caller_channel, ev.duration_s) == ("https://r.test/x.mp3", 1, 61.0)


def test_parse_recording_without_url_raises(plivo):
    with pytest.raises(ValueError, match="RecordUrl"):
        plivo.parse_recording({})


def test_parse_recording_takes_the_call_id_only_when_the_callback_has_one(plivo):
    url = {"RecordUrl": "https://media.plivo.com/x.mp3"}
    assert plivo.parse_recording(url).provider_call_id is None
    assert plivo.parse_recording({**url, "CallUUID": "abc"}).provider_call_id == "abc"
