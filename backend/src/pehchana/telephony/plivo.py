"""Plivo answer-URL XML and request verification.  Owner: WS1 (Calls).

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
measured by the same pipeline. Use the SDK's ``plivo.plivoxml`` builders (already a
dependency) rather than hand-written XML.
"""

from __future__ import annotations

from collections.abc import Sequence


def answer_xml(
    *,
    dial_numbers: Sequence[str],
    caller_id: str | None,
    base_url: str,
    call_id: str,
    consent_audio_url: str | None,
) -> str:
    """XML for an answered game: consent, then record + dial. TODO(WS1)"""
    raise NotImplementedError


def busy_xml() -> str:
    """XML when no arm is available: short apology, then hang up. TODO(WS1)"""
    raise NotImplementedError


def verify_signature(
    *,
    method: str,
    url: str,
    nonce: str | None,
    signature: str | None,
    auth_token: str,
    params: dict[str, str] | None,
) -> bool:
    """Validate ``X-Plivo-Signature-V3``. Must fail closed.

    TODO(WS1): wrap ``plivo.utils.validate_v3_signature``.
    """
    raise NotImplementedError
