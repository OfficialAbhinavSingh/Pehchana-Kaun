"""Bolna callbacks.  Owner: WS2 (Agents & analysis).

Bolna does not sign requests: check the shared-secret header configured on the
agent (BOLNA_SHARED_SECRET), and optionally the source IP allowlist.
"""

from fastapi import APIRouter, Request

from pehchana.api._stub import not_implemented

router = APIRouter(prefix="/bolna", tags=["bolna"])


@router.post("/webhook")
async def execution_webhook(request: Request) -> dict[str, str]:
    """Execution status updates (fires several times per call; idempotent on id).
    On a terminal status, attach the Bolna payload (latency, interruptions, cost)
    to the matching Call."""
    raise not_implemented("WS2")


@router.post("/fn/accuse")
async def accuse_bot(request: Request) -> dict[str, str]:
    """Custom function the AI agent calls the moment a caller says "tum bot ho".
    Log a FUNCTION accusation with the server-side time, and return the line the
    agent should say next (the reveal). Schema: bolna/functions/accuse_bot.json."""
    raise not_implemented("WS2")
