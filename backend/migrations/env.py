"""Alembic environment. The URL and metadata come from the app, never from alembic.ini."""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import Connection

from pehchana import models  # noqa: F401  (register tables on Base.metadata)
from pehchana.config import get_settings
from pehchana.db import Base, get_engine

config = context.config
# fileConfig would reset the app's logging when migrations run inside the API process.
if config.config_file_name is not None and config.attributes.get("configure_logging", True):
    fileConfig(config.config_file_name, disable_existing_loggers=False)

target_metadata = Base.metadata


def _configure(connection: Connection | None = None, url: str | None = None) -> None:
    context.configure(
        connection=connection,
        url=url,
        target_metadata=target_metadata,
        literal_binds=connection is None,
        dialect_opts={"paramstyle": "named"} if connection is None else {},
        # SQLite cannot ALTER most things in place; batch mode recreates the table.
        render_as_batch=True,
        compare_type=True,
    )


def run_migrations_offline() -> None:
    """Emit SQL without a DB connection (``alembic upgrade head --sql``)."""
    _configure(url=get_settings().database_url)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # A caller (tests, ``pk migrate``) may hand us an open connection so the migration
    # runs on exactly the engine it inspected.
    connection = config.attributes.get("connection")
    if connection is not None:
        _configure(connection)
        with context.begin_transaction():
            context.run_migrations()
        return
    with get_engine().connect() as connection:
        _configure(connection)
        with context.begin_transaction():
            context.run_migrations()
        connection.commit()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
