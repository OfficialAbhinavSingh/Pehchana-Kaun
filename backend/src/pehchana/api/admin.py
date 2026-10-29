"""Operator endpoints, guarded by the ADMIN_TOKEN bearer token.  Owner: WS1."""

import secrets
from datetime import UTC, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import BaseModel, Field

from pehchana.api.deps import ArmsDep, SessionDep, SettingsDep
from pehchana.arms import eligible_arms
from pehchana.models import ShiftOverride, utcnow
from pehchana.pipeline import process_call
from pehchana.telephony.call_flow import current_shift_override


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


@router.get("/shift")
def get_shift(session: SessionDep, arms: ArmsDep) -> dict[str, object]:
    """Current override and whether a human arm can take a call right now."""
    now = utcnow()
    row = current_shift_override(session, now)
    open_now = any(
        a.is_human
        for a in eligible_arms(
            arms,
            channel="phone",
            now=now,
            humans_override=row.humans_on_shift if row else None,
        )
    )
    return {
        "override": None
        if row is None
        else {
            "humans_on_shift": row.humans_on_shift,
            # SQLite hands back naive datetimes; they were stored as UTC.
            "until": row.until.replace(tzinfo=row.until.tzinfo or UTC).isoformat(),
            "set_by": row.set_by,
        },
        "humans_open_now": open_now,
    }


@router.post("/calls/{call_id}/reprocess")
def reprocess(call_id: str, session: SessionDep, settings: SettingsDep) -> dict[str, object]:
    """Re-run pipeline.process_call (after fixing the detector, for example)."""
    try:
        call = process_call(call_id, session=session, settings=settings)
    except LookupError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e)) from None
    return {
        "call_id": call.id,
        "status": call.status.value,
        "processing_error": call.processing_error,
    }
