"""Database engine and session helpers."""

from __future__ import annotations

from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import StaticPool

from pehchana.config import get_settings


class Base(DeclarativeBase):
    pass


@lru_cache
def get_engine() -> Engine:
    url = get_settings().database_url
    if url in ("sqlite://", "sqlite:///:memory:"):
        # In-memory SQLite (tests): one shared connection, or every session sees an empty DB.
        return create_engine(url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args, pool_pre_ping=True)


@lru_cache
def get_sessionmaker() -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine(), expire_on_commit=False)


def get_session() -> Iterator[Session]:
    """FastAPI dependency: one session per request."""
    with get_sessionmaker()() as session:
        yield session


def create_all() -> None:
    """Dev/test convenience. Production schema changes go through Alembic."""
    from pehchana import models  # noqa: F401  (register tables)

    Base.metadata.create_all(get_engine())
