"""Browser fallback: play from the website instead of a phone.  Owner: WS3.

AI arms only (a human can't join a Bolna web call). The site mints a session through
the browser SDK (@bolna/web-call, ``getSession`` mode) by POSTing ``{"consent": true}``
here; we choose an AI arm, create a Call with channel=web, and proxy Bolna's session
mint. Never expose BOLNA_API_KEY.

``user_data`` is built here, never taken from the browser: Bolna stores it on the call
and substitutes it into the agent prompt, so a client must not be able to set it.
"""

from __future__ import annotations

import logging
import threading
import time
from collections import deque
from typing import Any, Literal

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from pehchana.api.deps import ArmsDep, BolnaDep, SessionDep, SettingsDep
from pehchana.arms import NoArmAvailable, choose_arm, eligible_arms
from pehchana.models import Call, CallStatus, Channel, utcnow
from pehchana.telephony.call_flow import _recent_counts

log = logging.getLogger(__name__)

router = APIRouter(prefix="/webcall", tags=["webcall"])

HOUR_S = 3600.0
ALL_CLIENTS = "*"


class WebCallIn(BaseModel):
    # The site shows the consent notice next to the button; no tick, no session.
    consent: Literal[True]


# Per-process sliding windows of session mints: client key -> monotonic times.
_minted: dict[str, deque[float]] = {}
_lock = threading.Lock()
_clock = time.monotonic


def reset_limits() -> None:
    with _lock:
        _minted.clear()


def _take(key: str, limit: int, window_s: float, now: float) -> bool:
    """Record one mint for ``key`` unless it already has ``limit`` inside the window."""
    times = _minted.setdefault(key, deque())
    while times and times[0] <= now - window_s:
        times.popleft()
    if len(times) >= limit:
        return False
    times.append(now)
    return True


def _too_many(detail: str) -> HTTPException:
    return HTTPException(status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)


@router.post("/session")
def mint_session(
    body: WebCallIn,
    request: Request,
    db: SessionDep,
    settings: SettingsDep,
    arms: ArmsDep,
    bolna: BolnaDep,
) -> JSONResponse:
    """Mint a one-off Bolna web-call session for a random AI arm.

    Returns Bolna's session JSON unchanged (what the SDK's ``getSession`` expects).
    429 when this client or the whole site is over its limit, 503 when no AI arm can
    take a web call.
    """
    # Behind a proxy this is the proxy's address unless uvicorn runs with
    # --proxy-headers (see docs/architecture.md).
    client = request.client.host if request.client else "unknown"
    now = _clock()
    with _lock:
        if not _take(client, settings.webcall_per_ip, settings.webcall_per_ip_window_s, now):
            raise _too_many("too many games from this network, try again in a few minutes")
        if not _take(ALL_CLIENTS, settings.webcall_per_hour, HOUR_S, now):
            _minted[client].pop()  # the site is full: this client's try doesn't count
            raise _too_many("the browser game is full right now, try again later")

    started = utcnow()
    candidates = eligible_arms(arms, channel="web", now=started)
    try:
        arm = choose_arm(candidates, _recent_counts(db, started))
    except NoArmAvailable:
        raise HTTPException(
            status.HTTP_503_SERVICE_UNAVAILABLE, detail="no voice is free for the browser game"
        ) from None
    assert arm.bolna_agent_id is not None  # eligible_arms(channel="web") requires one

    call = Call(channel=Channel.WEB, arm_id=arm.id, arm_kind=arm.kind, started_at=started)
    db.add(call)
    db.commit()

    try:
        minted: Any = bolna.mint_web_call_session(arm.bolna_agent_id, {"call_id": call.id})
    except NotImplementedError:
        _fail(db, call, "BolnaClient.mint_web_call_session is not built yet")
        raise HTTPException(
            status.HTTP_501_NOT_IMPLEMENTED, detail="browser game not ready yet"
        ) from None
    except Exception as e:  # any vendor failure; the browser only needs to know it failed
        log.exception("web call %s: Bolna session mint failed", call.id)
        _fail(db, call, f"session mint failed: {type(e).__name__}")
        raise HTTPException(
            status.HTTP_502_BAD_GATEWAY, detail="could not start the call, try again"
        ) from None
    return JSONResponse(minted)


def _fail(db: Session, call: Call, reason: str) -> None:
    call.status = CallStatus.FAILED  # never counts in the stats
    call.ended_at = utcnow()
    call.processing_error = reason
    db.commit()
