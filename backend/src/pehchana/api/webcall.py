"""Browser fallback: play from the website instead of a phone.  Owner: WS3.

AI arms only (a human can't join a Bolna web call). The browser SDK
(@bolna/web-call) POSTs here; we choose an AI arm, create a Call with
channel=web, and proxy Bolna's session mint. Never expose BOLNA_API_KEY.
"""

from fastapi import APIRouter, Request

from pehchana.api._stub import not_implemented

router = APIRouter(prefix="/webcall", tags=["webcall"])


@router.post("/session")
async def session(request: Request) -> dict[str, object]:
    raise not_implemented("WS3")
