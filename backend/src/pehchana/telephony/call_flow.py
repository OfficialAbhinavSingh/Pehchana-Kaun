"""Vendor-neutral call lifecycle.  Owner: WS1 (Calls).

All routing and bookkeeping for one game lives here and talks only to the
``TelephonyProvider`` contract, so changing vendor never touches this file.
"""

from __future__ import annotations

import hashlib
import logging
from collections.abc import Mapping, Sequence
from datetime import datetime, timedelta

from sqlalchemy import func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from pehchana.arms import Arm, NoArmAvailable, choose_arm, eligible_arms
from pehchana.config import Settings
from pehchana.models import Call, CallStatus, Channel, ShiftOverride, Source, utcnow
from pehchana.telephony.base import CallPlan, ProviderResponse, TelephonyProvider

log = logging.getLogger(__name__)

# How far back "recent calls" looks when balancing arms.
BALANCE_WINDOW = timedelta(hours=6)
_OPEN = (CallStatus.ROUTED, CallStatus.LIVE)


def hash_caller(number: str | None, salt: str) -> str | None:
    """sha256(salt + number). The raw number is never stored or logged."""
    return hashlib.sha256((salt + number).encode()).hexdigest() if number else None


def _humans_override(session: Session, now: datetime) -> bool | None:
    row = session.scalars(
        select(ShiftOverride)
        .where(ShiftOverride.until > now)
        .order_by(ShiftOverride.created_at.desc(), ShiftOverride.id.desc())
    ).first()
    return row.humans_on_shift if row else None


def _recent_counts(session: Session, now: datetime) -> dict[str, int]:
    rows = session.execute(
        select(Call.arm_id, func.count())
        .where(Call.started_at >= now - BALANCE_WINDOW, Call.source == Source.REAL)
        .group_by(Call.arm_id)
    )
    return {arm_id: n for arm_id, n in rows}


def start_call(
    *,
    session: Session,
    provider: TelephonyProvider,
    settings: Settings,
    arms: Sequence[Arm],
    form: Mapping[str, str],
    now: datetime | None = None,
) -> ProviderResponse:
    """Caller dialled in: pick an arm, record the Call, return the provider's answer."""
    now = now or utcnow()
    incoming = provider.parse_incoming(form)

    # Vendors retry the answer URL on slow responses. Same call id: replay the same arm
    # instead of inserting a duplicate (unique constraint) or rerouting the caller.
    existing = _find_call(session, provider.name, incoming.provider_call_id)
    if existing is not None:
        return _replay(provider, settings, arms, existing)

    candidates = eligible_arms(
        arms, channel="phone", now=now, humans_override=_humans_override(session, now)
    )
    try:
        arm = choose_arm(candidates, _recent_counts(session, now))
    except NoArmAvailable:
        return provider.busy_response()

    call = Call(
        channel=Channel.PHONE,
        arm_id=arm.id,
        arm_kind=arm.kind,
        caller_hash=hash_caller(incoming.caller, settings.caller_hash_salt),
        provider=provider.name,
        provider_call_id=incoming.provider_call_id,
        started_at=now,
    )
    session.add(call)
    try:
        session.commit()
    except IntegrityError:
        # Two copies of the same webhook passed the lookup above together; the other one
        # inserted first. Answer this one from the winner's row so both callers' legs agree.
        session.rollback()
        existing = _find_call(session, provider.name, incoming.provider_call_id)
        if existing is None:
            raise  # some other constraint failed: not a retry, so do not hide it
        return _replay(provider, settings, arms, existing)
    return _answer(provider, settings, call, arm)


def _find_call(session: Session, provider_name: str, provider_call_id: str) -> Call | None:
    return session.scalars(
        select(Call).where(
            Call.provider == provider_name, Call.provider_call_id == provider_call_id
        )
    ).first()


def _replay(
    provider: TelephonyProvider, settings: Settings, arms: Sequence[Arm], call: Call
) -> ProviderResponse:
    """Answer a retried webhook again with the arm already chosen for this call."""
    arm = next((a for a in arms if a.id == call.arm_id), None)
    if arm is None or call.status not in _OPEN:
        # Retry of a call that already finished, or whose arm left the config.
        log.warning(
            "answer retry for call %s not replayed: status=%s arm=%s%s",
            call.id,
            call.status.value,
            call.arm_id,
            "" if arm else " (no longer configured)",
        )
        return provider.busy_response()
    return _answer(provider, settings, call, arm)


def _answer(
    provider: TelephonyProvider, settings: Settings, call: Call, arm: Arm
) -> ProviderResponse:
    base = f"{settings.public_base_url.rstrip('/')}/telephony/{provider.name}"
    return provider.answer_response(
        CallPlan(
            dial_numbers=arm.dial_numbers,
            caller_id=None,  # let the vendor pass the caller's own id through (Day-1 check)
            consent_audio_url=settings.consent_audio_url or None,
            dial_status_url=f"{base}/dial-status?call_id={call.id}",
            recording_url=f"{base}/recording?call_id={call.id}",
        )
    )


def finish_dial(
    *, session: Session, provider: TelephonyProvider, call: Call, form: Mapping[str, str]
) -> None:
    """Dial ended: record timings, or mark FAILED if the arm never picked up."""
    if call.status not in _OPEN:
        return  # late or duplicate callback must not rewrite a finished call
    result = provider.parse_dial_status(form)
    now = utcnow()
    call.ended_at = now
    if not result.answered:
        call.status = CallStatus.FAILED  # never counts in the stats
    else:
        call.status = CallStatus.ENDED
        call.duration_s = result.duration_s
        if result.duration_s is not None:
            call.answered_at = now - timedelta(seconds=result.duration_s)
    session.commit()


def attach_recording(
    *, session: Session, provider: TelephonyProvider, call: Call, form: Mapping[str, str]
) -> bool:
    """Store the recording once. Returns True if the call should now be processed.

    Vendors repeat callbacks until they see a 2xx, and may send two at once. The first
    recording wins: the claim is one conditional UPDATE, so of two concurrent callbacks
    exactly one sees ``True`` and queues the (costly, Deepgram + LLM) pipeline.
    """
    event = provider.parse_recording(form)
    claimed = session.scalars(
        update(Call)
        .where(Call.id == call.id, Call.recording_url.is_(None))
        .values(recording_url=event.url, recording_caller_channel=event.caller_channel)
        .returning(Call.id)
    ).first()
    session.commit()
    session.refresh(call)  # the UPDATE bypassed the ORM object
    if claimed is None:
        if call.recording_url != event.url:
            log.warning("call %s already has a recording; ignoring a different one", call.id)
        return False
    return call.status not in (CallStatus.FAILED, CallStatus.PROCESSED)
