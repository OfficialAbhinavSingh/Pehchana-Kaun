"""FastAPI app factory. Run: ``uv run uvicorn pehchana.main:app --reload``."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pehchana import __version__
from pehchana.api import admin, bolna, health, leaderboard, telephony, webcall
from pehchana.config import get_settings
from pehchana.migrate import upgrade


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    if get_settings().env == "dev":
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
