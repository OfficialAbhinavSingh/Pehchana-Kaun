"""Plivo implementation of ``TelephonyProvider``.  Owner: WS1 (Calls).

Call flow for one game (full diagram in docs/architecture.md#call-flow):

1. Caller dials our Plivo number. Plivo POSTs to ``/telephony/plivo/answer``.
2. We pick an arm and reply with XML that
   - plays the consent notice (recorded call, may be an AI),
   - starts a **stereo session recording** that begins when the arm answers
     (``<Record recordSession="true" startOnDialAnswer="true" redirect="false"
     recordChannelType="stereo" callbackUrl=...>``),
   - ``<Dial>``s the arm: a Bolna agent's inbound number, or the volunteers' phones.
3. Plivo POSTs the dial result to ``/telephony/plivo/dial-status`` and the finished
   recording to ``/telephony/plivo/recording``.

Every arm, human or AI, is bridged and recorded the same way, so all arms are
measured by the same pipeline. XML comes from the SDK's ``plivo.plivoxml`` builders.

This is the only module that imports ``plivo``. Form field names below follow Plivo's
docs; confirm them against a real call on Day 1 (docs/architecture.md).
"""

from __future__ import annotations

from collections.abc import Mapping

from plivo import plivoxml
from plivo.utils import validate_v3_signature

from pehchana.config import Settings
from pehchana.telephony.base import (
    CallPlan,
    DialResult,
    IncomingCall,
    ProviderResponse,
    RecordingEvent,
    WebhookRequest,
)

XML = "application/xml"
# DialBLegStatus values meaning the arm picked up (and, on the action callback, hung up).
_ANSWERED = frozenset({"answer", "hangup"})
_CONSENT_TEXT = (
    "Yeh ek game hai. Aap kisi insaan ya AI se baat kar sakte hain. "
    "Call research ke liye record hogi. Line par bane rehna matlab aap sahmat hain. "
    "This is a game. You may be speaking to an AI. The call is recorded for research. "
    "Stay on the line to agree."
)


def _float(value: str | None) -> float | None:
    try:
        return float(value) if value else None
    except ValueError:
        return None


class PlivoProvider:
    name = "plivo"

    def __init__(self, *, auth_token: str, caller_channel: int = 0) -> None:
        self._auth_token = auth_token
        self._caller_channel = caller_channel

    @classmethod
    def from_settings(cls, settings: Settings) -> PlivoProvider:
        return cls(auth_token=settings.plivo_auth_token, caller_channel=settings.caller_channel)

    def verify(self, request: WebhookRequest) -> bool:
        signature = request.headers.get("x-plivo-signature-v3")
        nonce = request.headers.get("x-plivo-signature-v3-nonce")
        if not (self._auth_token and signature and nonce):
            return False
        try:
            return bool(
                validate_v3_signature(
                    request.method,
                    request.url,
                    nonce,
                    self._auth_token,
                    signature,
                    dict(request.form) if request.method.upper() == "POST" else None,
                )
            )
        except Exception:
            return False

    def parse_incoming(self, form: Mapping[str, str]) -> IncomingCall:
        return IncomingCall(caller=form.get("From") or None, provider_call_id=form["CallUUID"])

    def answer_response(self, plan: CallPlan) -> ProviderResponse:
        response = plivoxml.ResponseElement()
        if plan.consent_audio_url:
            response.add(plivoxml.PlayElement(plan.consent_audio_url))
        else:
            response.add(plivoxml.SpeakElement(_CONSENT_TEXT))
        response.add(
            plivoxml.RecordElement(
                record_session=True,
                start_on_dial_answer=True,
                redirect=False,
                record_channel_type="stereo",
                callback_url=plan.recording_url,
                callback_method="POST",
            )
        )
        dial = plivoxml.DialElement(
            action=plan.dial_status_url,
            method="POST",
            caller_id=plan.caller_id,
            redirect=False,
            timeout=plan.ring_timeout_s,
            time_limit=plan.time_limit_s,
        )
        # One <Number> per number: Plivo rings them all at once, first to answer wins.
        for number in plan.dial_numbers:
            dial.add(plivoxml.NumberElement(number))
        response.add(dial)
        return ProviderResponse(response.to_string(False), XML)

    def busy_response(self) -> ProviderResponse:
        response = plivoxml.ResponseElement()
        response.add(
            plivoxml.SpeakElement("Abhi sab lines busy hain. Kuch der baad dobara call kijiye.")
        )
        response.add(plivoxml.HangupElement())
        return ProviderResponse(response.to_string(False), XML)

    def parse_dial_status(self, form: Mapping[str, str]) -> DialResult:
        status = (form.get("DialBLegStatus") or form.get("DialStatus") or "").lower()
        duration = _float(form.get("DialBLegDuration"))
        return DialResult(
            answered=status in _ANSWERED or bool(duration),
            duration_s=duration,
            provider_call_id=form.get("CallUUID"),
        )

    def parse_recording(self, form: Mapping[str, str]) -> RecordingEvent:
        url = form.get("RecordUrl")
        if not url:
            raise ValueError("Plivo recording callback has no RecordUrl")
        return RecordingEvent(
            url=url,
            caller_channel=self._caller_channel,
            duration_s=_float(form.get("RecordingDuration")),
        )
