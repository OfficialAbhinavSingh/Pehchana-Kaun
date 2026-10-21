from fastapi import APIRouter
from sqlalchemy import text

from pehchana import __version__
from pehchana.api.deps import SessionDep

router = APIRouter(tags=["health"])


@router.get("/healthz")
def healthz(session: SessionDep) -> dict[str, str]:
    session.execute(text("select 1"))
    return {"status": "ok", "version": __version__}
