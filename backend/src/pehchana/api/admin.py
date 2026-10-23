"""Operator endpoints, guarded by the ADMIN_TOKEN bearer token.  Owner: WS1."""

import secrets
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import BaseModel, Field

from pehchana.api._stub import not_implemented
from pehchana.api.deps import SessionDep, SettingsDep
from pehchana.models import ShiftOverride, utcnow


def require_admin(settings: SettingsDep, authorization: Annotated[str, Header()] = "") -> None:
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not secrets.compare_digest(token, settings.admin_token):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="admin token required")


router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(require_admin)])


class ShiftIn(BaseModel):
    humans_on_shift: bool
    hours: float = Field(gt=0, le=24, description="how long the override lasts")
    set_by: str | None = Field(default=None, max_length=64)


@router.post("/shift")
def set_shift(body: ShiftIn, session: SessionDep) -> dict[str, object]:
    """Turn the human arm on/off until a given time (volunteers going live)."""
    until = utcnow() + timedelta(hours=body.hours)
    session.add(
        ShiftOverride(humans_on_shift=body.humans_on_shift, until=until, set_by=body.set_by)
    )
    session.commit()
    return {"humans_on_shift": body.humans_on_shift, "until": until.isoformat()}


@router.post("/calls/{call_id}/reprocess")
def reprocess(call_id: str) -> dict[str, str]:
    """Re-run pipeline.process_call (after fixing detection, for example)."""
    raise not_implemented("WS2")
