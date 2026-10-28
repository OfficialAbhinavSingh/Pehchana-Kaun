"""FastAPI app factory. Run: ``uv run uvicorn pehchana.main:app --reload``."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pehchana import __version__
from pehchana.api import admin, bolna, health, leaderboard, telephony, webcall
from pehchana.config import get_settings
from pehchana.migrate import upgrade

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    if settings.env == "prod":
        # Fail at boot, not on the first real call: a prod deploy with dev secrets is open.
        problems = settings.production_problems()
        if problems:
            raise RuntimeError("refusing to start in production: " + "; ".join(problems))
        for warning in settings.production_warnings():
            log.warning(warning)
    if settings.env == "dev":
        upgrade()  # dev only; elsewhere run `pk migrate` as a deploy step
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="Pehchana Kaun? API", version=__version__, lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )
    for module in (health, telephony, bolna, webcall, leaderboard, admin):
        app.include_router(module.router)
    return app


app = create_app()
