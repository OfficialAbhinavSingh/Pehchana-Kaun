"""Plivo webhooks.  Owner: WS1 (Calls).

Every handler must verify X-Plivo-Signature-V3 (telephony/plivo.verify_signature)
before trusting the request. Plivo sends form-encoded POSTs.
"""

from fastapi import APIRouter, Request, Response

from pehchana.api._stub import not_implemented

router = APIRouter(prefix="/telephony/plivo", tags=["telephony"])


@router.post("/answer")
async def answer(request: Request) -> Response:
    """Caller dialled in. Create a Call, choose an arm, return answer XML
    (consent -> stereo session recording -> Dial arm). If no arm: busy XML."""
    raise not_implemented("WS1")


@router.post("/dial-status")
async def dial_status(request: Request, call_id: str) -> Response:
    """Dial finished. Record answered/ended times and duration; mark FAILED if the
    arm never picked up (that call must not count in the stats)."""
    raise not_implemented("WS1")


@router.post("/recording")
async def recording(request: Request, call_id: str) -> Response:
    """Session recording is ready. Store recording_url and queue pipeline.process_call."""
    raise not_implemented("WS1")
