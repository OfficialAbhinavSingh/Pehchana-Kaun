"""Apply Alembic migrations to the app database.

Databases created before Alembic existed came from ``create_all``, so they have tables
but no ``alembic_version``. ``upgrade`` recognises the two schemas that were ever
created that way and stamps them before upgrading, so existing rows are kept and
``upgrade head`` never tries to create a table that is already there.
"""

from __future__ import annotations

from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import Connection, Engine, inspect

from pehchana.db import get_engine

ALEMBIC_INI = Path(__file__).resolve().parents[2] / "alembic.ini"

# Revision whose schema is the one on main before the provider-neutral Call.
LEGACY_REVISION = "0001"


class UnknownSchema(RuntimeError):
    """The database has tables Alembic cannot place on its revision history."""


def _config(connection: Connection) -> Config:
    cfg = Config(str(ALEMBIC_INI))
    cfg.attributes["connection"] = connection
    cfg.attributes["configure_logging"] = False  # keep the API's own logging
    return cfg


def _stamp_unversioned(cfg: Config, connection: Connection) -> None:
    tables = set(inspect(connection).get_table_names())
    if "alembic_version" in tables or "calls" not in tables:
        return  # already versioned, or an empty database that upgrade will build
    columns = {c["name"] for c in inspect(connection).get_columns("calls")}
    if "plivo_call_uuid" in columns:
        command.stamp(cfg, LEGACY_REVISION)
    elif {"provider_call_id", "recording_caller_channel"} <= columns:
        command.stamp(cfg, "head")  # create_all from the current models
    else:
        raise UnknownSchema(
            "calls table matches no known revision (columns: "
            + ", ".join(sorted(columns))
            + "). It is likely a dev database from an unmerged branch: delete it and rerun."
        )


def upgrade(engine: Engine | None = None, revision: str = "head") -> None:
    """Bring the database to ``revision`` (default: latest)."""
    engine = engine or get_engine()
    with engine.begin() as connection:
        cfg = _config(connection)
        _stamp_unversioned(cfg, connection)
        command.upgrade(cfg, revision)
