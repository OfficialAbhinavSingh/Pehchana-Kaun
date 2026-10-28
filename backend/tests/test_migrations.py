"""Alembic migrations against real SQLite files, including a copy of the old schema.

Set TEST_POSTGRES_URL (a throwaway database; its public schema is wiped) to run every
test again on Postgres, which is what production uses.
"""

import os

import pytest
from alembic import command
from alembic.autogenerate import compare_metadata
from alembic.migration import MigrationContext
from sqlalchemy import UniqueConstraint, create_engine, inspect, text
from sqlalchemy.exc import IntegrityError

from pehchana import migrate, models  # noqa: F401  (register tables)
from pehchana.db import Base

NOW = "2026-10-23 10:00:00"
PAIR = {"provider", "provider_call_id"}


POSTGRES_URL = os.environ.get("TEST_POSTGRES_URL")


def _wipe(eng) -> None:
    with eng.begin() as c:
        c.execute(text("DROP SCHEMA public CASCADE"))
        c.execute(text("CREATE SCHEMA public"))


@pytest.fixture(
    params=[
        "sqlite",
        pytest.param(
            "postgres",
            marks=pytest.mark.skipif(not POSTGRES_URL, reason="TEST_POSTGRES_URL not set"),
        ),
    ]
)
def engine(request, tmp_path):
    if request.param == "sqlite":
        eng = create_engine(f"sqlite:///{tmp_path / 'pk.db'}")
        yield eng
    else:
        eng = create_engine(POSTGRES_URL)
        _wipe(eng)
        yield eng
        _wipe(eng)
    eng.dispose()


def _insert_legacy_call(conn, id_: str, uuid: str | None) -> None:
    conn.execute(
        text(
            "INSERT INTO calls (id, channel, source, status, arm_id, arm_kind, plivo_call_uuid, "
            "started_at) VALUES (:id, 'PHONE', 'REAL', 'PROCESSED', 'kalpa', 'ai', :uuid, :now)"
        ),
        {"id": id_, "uuid": uuid, "now": NOW},
    )


def _rows(engine) -> dict[str, tuple[str | None, str | None]]:
    with engine.connect() as c:
        rows = c.execute(text("SELECT id, provider, provider_call_id FROM calls")).all()
    return {r[0]: (r[1], r[2]) for r in rows}


def _legacy_db(engine) -> None:
    """A database as main's create_all left it: old schema, rows, no alembic_version."""
    migrate.upgrade(engine, migrate.LEGACY_REVISION)
    with engine.begin() as c:
        _insert_legacy_call(c, "c1", "plivo-uuid-1")
        _insert_legacy_call(c, "c2", None)
        c.execute(text("DROP TABLE alembic_version"))


def test_fresh_database_matches_the_models(engine):
    migrate.upgrade(engine)
    with engine.connect() as c:
        ctx = MigrationContext.configure(c, opts={"compare_type": True})
        assert compare_metadata(ctx, Base.metadata) == []


def test_provider_call_id_constraint_has_the_same_name_in_models_and_migrations(engine):
    # Unnamed in the model, create_all and Alembic would give it different names, and a
    # later migration dropping it by name would break on one of them.
    declared = {
        c.name
        for c in Base.metadata.tables["calls"].constraints
        if isinstance(c, UniqueConstraint) and {col.name for col in c.columns} == PAIR
    }
    migrate.upgrade(engine)
    migrated = {
        uc["name"]
        for uc in inspect(engine).get_unique_constraints("calls")
        if set(uc["column_names"]) == PAIR
    }
    assert declared == migrated == {"uq_calls_provider_call_id"}


def test_upgrade_keeps_existing_calls(engine):
    migrate.upgrade(engine, migrate.LEGACY_REVISION)
    with engine.begin() as c:
        _insert_legacy_call(c, "c1", "plivo-uuid-1")
        _insert_legacy_call(c, "c2", None)
    migrate.upgrade(engine)
    assert _rows(engine) == {"c1": ("plivo", "plivo-uuid-1"), "c2": (None, None)}
    columns = {c["name"] for c in inspect(engine).get_columns("calls")}
    assert "plivo_call_uuid" not in columns
    assert {"provider", "provider_call_id", "recording_caller_channel"} <= columns


def test_unversioned_legacy_database_is_stamped_then_upgraded(engine):
    _legacy_db(engine)
    migrate.upgrade(engine)
    assert _rows(engine) == {"c1": ("plivo", "plivo-uuid-1"), "c2": (None, None)}
    with engine.connect() as c:
        assert c.execute(text("SELECT version_num FROM alembic_version")).scalar() == "0002"


def test_unversioned_database_from_current_models_is_stamped_at_head(engine):
    Base.metadata.create_all(engine)
    migrate.upgrade(engine)  # must not try to create tables that exist
    with engine.connect() as c:
        assert c.execute(text("SELECT version_num FROM alembic_version")).scalar() == "0002"


def test_unrecognised_calls_table_is_rejected(engine):
    with engine.begin() as c:
        c.execute(text("CREATE TABLE calls (id VARCHAR(36) PRIMARY KEY, mystery TEXT)"))
    with pytest.raises(migrate.UnknownSchema):
        migrate.upgrade(engine)


def test_provider_and_call_id_stay_unique_together(engine):
    migrate.upgrade(engine)
    insert = text(
        "INSERT INTO calls (id, channel, source, status, arm_id, arm_kind, provider, "
        "provider_call_id, started_at) VALUES (:id, 'PHONE', 'REAL', 'ROUTED', 'a', 'ai', "
        ":provider, 'x', :now)"
    )
    with engine.begin() as c:
        c.execute(insert, {"id": "1", "provider": "plivo", "now": NOW})
        c.execute(insert, {"id": "2", "provider": "exotel", "now": NOW})  # other vendor: fine
    with pytest.raises(IntegrityError), engine.begin() as c:
        c.execute(insert, {"id": "3", "provider": "plivo", "now": NOW})


def test_downgrade_restores_plivo_ids_and_drops_other_vendors(engine):
    migrate.upgrade(engine)
    with engine.begin() as c:
        for id_, provider in (("1", "plivo"), ("2", "exotel")):
            c.execute(
                text(
                    "INSERT INTO calls (id, channel, source, status, arm_id, arm_kind, provider, "
                    "provider_call_id, started_at) VALUES (:id, 'PHONE', 'REAL', 'ROUTED', 'a', "
                    "'ai', :provider, :pid, :now)"
                ),
                {"id": id_, "provider": provider, "pid": f"id-{id_}", "now": NOW},
            )
    with engine.begin() as c:
        command.downgrade(migrate._config(c), migrate.LEGACY_REVISION)
    with engine.connect() as c:
        rows = dict(c.execute(text("SELECT id, plivo_call_uuid FROM calls")).all())
    assert rows == {"1": "id-1", "2": None}


def test_full_round_trip_leaves_nothing_behind(engine):
    """upgrade, downgrade to nothing, upgrade again: a failed deploy can be rolled back
    and retried. On Postgres this also catches enum types a downgrade forgets to drop."""
    migrate.upgrade(engine)
    with engine.begin() as c:
        command.downgrade(migrate._config(c), "base")
    assert set(inspect(engine).get_table_names()) <= {"alembic_version"}
    if engine.dialect.name == "postgresql":
        assert inspect(engine).get_enums() == []
    migrate.upgrade(engine)
    with engine.connect() as c:
        ctx = MigrationContext.configure(c, opts={"compare_type": True})
        assert compare_metadata(ctx, Base.metadata) == []
