"""Bolna callbacks.  Owner: WS2 (Agents & analysis).

Bolna does not sign requests, so both routes check a shared secret instead:

- ``/fn/accuse``: the custom function sends ``Authorization: Bearer <BOLNA_SHARED_SECRET>``
  (``api_token`` in ``bolna/functions/accuse_bot.json``, the function's own config).
- ``/webhook``: the execution-status webhook sends whatever custom header is set on the
  agent's Extractions tab. Set that header to ``X-Bolna-Webhook-Secret`` with the same
  ``BOLNA_SHARED_SECRET`` value -- Bolna does not fix this header's name, we chose it.

Optional source-IP allowlist (13.203.39.153, 13.126.9.249, 13.202.133.53) behind
``ENFORCE_BOLNA_IP_ALLOWLIST``, same allowlist-checking pattern used elsewhere in
``telephony/``.
"""

from __future__ import annotations

import logging
import secrets
from datetime import UTC, datetime, timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Header, HTTPException, Request, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from pehchana.api.deps import ArmsDep, SessionDep, SettingsDep
from pehchana.config import Settings
from pehchana.integrations.bolna import TERMINAL_STATUSES
from pehchana.models import Accusation, AccusationSource, Call, CallStatus, utcnow
from pehchana.telephony.call_flow import hash_caller

log = logging.getLogger(__name__)

router = APIRouter(prefix="/bolna", tags=["bolna"])

# A live call: look for an open Call for this arm no older than this when the caller
# accuses it. Calls are capped at a few minutes by the persona brief, so this is generous.
ACCUSE_LOOKBACK = timedelta(minutes=10)
# Matching a terminal execution back to the Call it belongs to (docs/architecture.md
# > Linking a Plivo call to its Bolna execution).
LINK_WINDOW_BEFORE = timedelta(seconds=30)
LINK_WINDOW_AFTER = timedelta(seconds=60)
_OPEN = (CallStatus.ROUTED, CallStatus.LIVE)

# Example wording straight from #15; the agent's own persona prompt also knows to
# reveal honestly, this is the belt to that braces.
_REVEAL = "Sahi pakda! Main AI hoon. Thanks for playing!"


def _require_secret(expected: str, given: str | None) -> None:
    if not given or not secrets.compare_digest(given, expected):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="bad shared secret")


def _require_known_ip(request: Request, settings: Settings) -> None:
    if not settings.enforce_bolna_ip_allowlist:
        return
    host = request.client.host if request.client else None
    if host not in settings.bolna_webhook_ips:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="unrecognized source")


def _bearer(authorization: str | None) -> str | None:
    scheme, _, token = (authorization or "").partition(" ")
    return token if scheme.lower() == "bearer" else None


class AccuseIn(BaseModel):
    caller_phrase: str
    agent_id: str
    from_number: str


@router.post("/fn/accuse")
def accuse_bot(
    request: Request,
    body: AccuseIn,
    session: SessionDep,
    settings: SettingsDep,
    arms: ArmsDep,
    authorization: Annotated[str | None, Header()] = None,
) -> dict[str, str]:
    """The agent calls this the moment a caller says "tum bot ho". Logs a FUNCTION
    accusation with the server-side time and returns the line to say next (the honest
    reveal). The reveal is returned even when nothing could be linked server-side --
    the in-call moment matters more than our bookkeeping succeeding."""
    _require_known_ip(request, settings)
    _require_secret(settings.bolna_shared_secret, _bearer(authorization))

    arm = next((a for a in arms if a.bolna_agent_id == body.agent_id), None)
    if arm is None:
        log.warning("accuse_bot: agent_id %s matches no arm", body.agent_id)
        return {"result": "caught", "say": _REVEAL}

    now = utcnow()
    caller_hash = hash_caller(body.from_number, settings.caller_hash_salt)
    call = session.scalars(
        select(Call)
        .where(
            Call.arm_id == arm.id,
            Call.caller_hash == caller_hash,
            Call.status.in_(_OPEN),
            Call.started_at >= now - ACCUSE_LOOKBACK,
        )
        .order_by(Call.started_at.desc())
    ).first()
    if call is None:
        log.warning("accuse_bot: no open call for arm %s in the last %s", arm.id, ACCUSE_LOOKBACK)
        return {"result": "caught", "say": _REVEAL}

    # SQLite hands back naive datetimes; they were stored as UTC (same fix as admin.py).
    answered_at = call.answered_at
    if answered_at is not None and answered_at.tzinfo is None:
        answered_at = answered_at.replace(tzinfo=UTC)
    at_s = (now - answered_at).total_seconds() if answered_at else None
    session.add(
        Accusation(
            call_id=call.id, source=AccusationSource.FUNCTION, at_s=at_s, phrase=body.caller_phrase
        )
    )
    session.commit()
    return {"result": "caught", "say": _REVEAL}


def _parsed_created_at(payload: dict[str, Any]) -> datetime | None:
    created_at = payload.get("created_at")
    if not isinstance(created_at, str):
        return None
    try:
        parsed = datetime.fromisoformat(created_at)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def _find_call_for_execution(
    session: Session, arm_id: str, caller_hash_salt: str, payload: dict[str, Any]
) -> Call | None:
    """docs/architecture.md > Linking a Plivo call to its Bolna execution."""
    created_at = _parsed_created_at(payload) or utcnow()
    window = (created_at - LINK_WINDOW_BEFORE, created_at + LINK_WINDOW_AFTER)
    telephony = payload.get("telephony_data") or {}
    user_number = payload.get("user_number") or telephony.get("from_number")

    if user_number:
        caller_hash = hash_caller(str(user_number), caller_hash_salt)
        call = session.scalars(
            select(Call).where(
                Call.arm_id == arm_id,
                Call.caller_hash == caller_hash,
                Call.started_at >= window[0],
                Call.started_at <= window[1],
            )
        ).first()
        if call is not None:
            return call

    # Carrier CLI fallback: caller id suppressed, so fall back to "the one open call for
    # this arm in the window", confirmed by duration consistency.
    candidates = list(
        session.scalars(
            select(Call).where(
                Call.arm_id == arm_id,
                Call.status.in_(_OPEN),
                Call.started_at >= window[0],
                Call.started_at <= window[1],
            )
        )
    )
    if len(candidates) != 1:
        return None
    duration = telephony.get("duration")
    if (
        isinstance(duration, int | float)
        and candidates[0].duration_s is not None
        and abs(candidates[0].duration_s - duration) > 3
    ):
        return None
    return candidates[0]


@router.post("/webhook")
async def execution_webhook(
    request: Request,
    session: SessionDep,
    settings: SettingsDep,
    arms: ArmsDep,
    x_bolna_webhook_secret: Annotated[str | None, Header()] = None,
) -> dict[str, str]:
    """Execution status updates (fires several times per call; idempotent on ``id``).
    Non-terminal statuses are ignored. On a terminal one, the payload is attached to the
    matching Call unless it is a never-picked-up execution (``conversation_duration == 0``)."""
    _require_known_ip(request, settings)
    _require_secret(settings.bolna_shared_secret, x_bolna_webhook_secret)
    payload: dict[str, Any] = await request.json()

    if payload.get("status") not in TERMINAL_STATUSES:
        return {"ignored": "non-terminal status"}
    if not payload.get("conversation_duration"):
        return {"ignored": "nobody talked"}

    execution_id = payload.get("id")
    if (
        execution_id
        and session.scalars(select(Call).where(Call.bolna_execution_id == execution_id)).first()
    ):
        return {"ignored": "already attached (idempotent)"}

    agent_id = payload.get("agent_id")
    arm = next((a for a in arms if a.bolna_agent_id == agent_id), None)
    if arm is None:
        log.warning("bolna webhook: agent_id %s matches no arm", agent_id)
        return {"ignored": "unknown agent_id"}

    call = _find_call_for_execution(session, arm.id, settings.caller_hash_salt, payload)
    if call is None:
        log.warning("bolna webhook: no matching call for execution %s", execution_id)
        return {"ignored": "no matching call"}

    call.bolna_execution_id = execution_id
    call.bolna_payload = payload
    session.commit()
    return {"attached": call.id}
