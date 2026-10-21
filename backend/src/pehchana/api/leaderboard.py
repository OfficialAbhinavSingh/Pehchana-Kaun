"""Public stats.  Owner: WS3 (Leaderboard).

Response shape is the contract with web/: keep it in sync with
web/src/lib/api.ts. Only REAL calls with status=processed count; demo rows only
when INCLUDE_DEMO_DATA=true (and the response must say so). Vendor names only when
REVEAL_VENDORS=true, otherwise public_label from bolna/arms.yaml.
"""

from fastapi import APIRouter

from pehchana.api._stub import not_implemented

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])


@router.get("")
def leaderboard() -> dict[str, object]:
    """Per-arm ArmStats (+ per-language breakdown, top giveaway tags, totals)."""
    raise not_implemented("WS3")
