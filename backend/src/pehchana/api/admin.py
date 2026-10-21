"""Operator endpoints, guarded by the ADMIN_TOKEN bearer token.  Owner: WS1."""

from fastapi import APIRouter

from pehchana.api._stub import not_implemented

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/shift")
def set_shift() -> dict[str, object]:
    """Turn the human arm on/off until a given time (volunteers going live)."""
    raise not_implemented("WS1")


@router.post("/calls/{call_id}/reprocess")
def reprocess(call_id: str) -> dict[str, str]:
    """Re-run pipeline.process_call (after fixing detection, for example)."""
    raise not_implemented("WS2")
