"""Vendor-neutral telephony contract.  Owner: WS1 (Calls).

Everything outside ``telephony/`` talks to a ``TelephonyProvider`` and the plain
dataclasses below, never to a vendor SDK. Adding a vendor means one new module that
implements the protocol plus one line in ``telephony/registry.py``; routing, models,
the pipeline and the HTTP routes stay untouched (open for extension, closed for
modification).

Every provider must deliver what the Turing Clock needs (docs/metrics.md): a two-channel
recording that starts the moment the arm answers, with the caller on a known channel.
A provider that cannot must say so by raising in ``parse_recording`` rather than
returning a recording that would skew timings.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass(frozen=True)
class WebhookRequest:
    """What a provider needs to authenticate an inbound webhook."""

    method: str
    url: str  # full public URL the vendor called, including the query string
    headers: Mapping[str, str]  # keys lower-cased
    form: Mapping[str, str]


@dataclass(frozen=True)
class IncomingCall:
    caller: str | None  # raw number; hash it immediately, never store or log it
    provider_call_id: str


@dataclass(frozen=True)
class CallPlan:
    """What we want the provider to do with an answered game."""

    dial_numbers: Sequence[str]
    caller_id: str | None
    consent_audio_url: str | None
    dial_status_url: str  # provider POSTs the dial result here
    recording_url: str  # provider POSTs the finished recording here
    ring_timeout_s: int = 30  # give up on an arm that doesn't pick up
    time_limit_s: int = 600  # hard cap per game (Plivo's own default is 4 hours)


@dataclass(frozen=True)
class ProviderResponse:
    body: str
    media_type: str


@dataclass(frozen=True)
class DialResult:
    answered: bool
    duration_s: float | None
    provider_call_id: str | None = None


@dataclass(frozen=True)
class RecordingEvent:
    url: str
    caller_channel: int  # 0-based channel of the caller in the recording
    duration_s: float | None = None
    # Extra headers the pipeline must send to download ``url`` (empty if public).
    download_headers: Mapping[str, str] = field(default_factory=dict)


@runtime_checkable
class TelephonyProvider(Protocol):
    name: str

    def verify(self, request: WebhookRequest) -> bool:
        """Authenticate a webhook. Must fail closed: any doubt returns False."""
        ...

    def parse_incoming(self, form: Mapping[str, str]) -> IncomingCall: ...

    def answer_response(self, plan: CallPlan) -> ProviderResponse:
        """Consent notice, then record from answer, then dial the arm."""
        ...

    def busy_response(self) -> ProviderResponse:
        """No arm available: short apology, then hang up."""
        ...

    def parse_dial_status(self, form: Mapping[str, str]) -> DialResult: ...

    def parse_recording(self, form: Mapping[str, str]) -> RecordingEvent: ...


class UnknownProvider(LookupError):
    """``TELEPHONY_PROVIDER`` or the route names a provider that isn't registered."""
