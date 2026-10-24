"""Baseline: the schema as it was on main before the provider-neutral Call.

This is the exact schema ``create_all`` produced for every database created from
``2899d12`` (scaffold) up to ``722d01e``, so an existing dev database can be stamped
here and upgraded. Do not edit it; change the schema in a new revision.

Revision ID: 0001
Revises:
Create Date: 2026-10-24
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "calls",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("channel", sa.Enum("PHONE", "WEB", name="channel"), nullable=False),
        sa.Column("source", sa.Enum("REAL", "DEMO", name="source"), nullable=False),
        sa.Column(
            "status",
            sa.Enum("ROUTED", "LIVE", "ENDED", "PROCESSED", "FAILED", name="callstatus"),
            nullable=False,
        ),
        sa.Column("arm_id", sa.String(length=64), nullable=False),
        sa.Column("arm_kind", sa.String(length=16), nullable=False),
        sa.Column("caller_hash", sa.String(length=64), nullable=True),
        sa.Column("plivo_call_uuid", sa.String(length=64), nullable=True),
        sa.Column("bolna_execution_id", sa.String(length=64), nullable=True),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("answered_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("ended_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("duration_s", sa.Float(), nullable=True),
        sa.Column("recording_url", sa.Text(), nullable=True),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("transcript", sa.JSON(), nullable=True),
        sa.Column("bolna_payload", sa.JSON(), nullable=True),
        sa.Column("processing_error", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("bolna_execution_id"),
        sa.UniqueConstraint("plivo_call_uuid"),
    )
    op.create_index(op.f("ix_calls_arm_id"), "calls", ["arm_id"], unique=False)
    op.create_index(op.f("ix_calls_caller_hash"), "calls", ["caller_hash"], unique=False)
    op.create_table(
        "shift_overrides",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("humans_on_shift", sa.Boolean(), nullable=False),
        sa.Column("until", sa.DateTime(timezone=True), nullable=False),
        sa.Column("set_by", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "accusations",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("call_id", sa.String(length=36), nullable=False),
        sa.Column(
            "source", sa.Enum("TRANSCRIPT", "FUNCTION", name="accusationsource"), nullable=False
        ),
        sa.Column("at_s", sa.Float(), nullable=True),
        sa.Column("phrase", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["call_id"], ["calls.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_accusations_call_id"), "accusations", ["call_id"], unique=False)
    op.create_table(
        "giveaways",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("call_id", sa.String(length=36), nullable=False),
        sa.Column("tag", sa.String(length=48), nullable=False),
        sa.Column("method", sa.String(length=16), nullable=False),
        sa.Column("evidence", sa.Text(), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["call_id"], ["calls.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_giveaways_call_id"), "giveaways", ["call_id"], unique=False)
    op.create_index(op.f("ix_giveaways_tag"), "giveaways", ["tag"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_giveaways_tag"), table_name="giveaways")
    op.drop_index(op.f("ix_giveaways_call_id"), table_name="giveaways")
    op.drop_table("giveaways")
    op.drop_index(op.f("ix_accusations_call_id"), table_name="accusations")
    op.drop_table("accusations")
    op.drop_table("shift_overrides")
    op.drop_index(op.f("ix_calls_caller_hash"), table_name="calls")
    op.drop_index(op.f("ix_calls_arm_id"), table_name="calls")
    op.drop_table("calls")
    # Postgres keeps enum types after their tables are gone; SQLite has none.
    bind = op.get_bind()
    for name in ("accusationsource", "callstatus", "source", "channel"):
        sa.Enum(name=name).drop(bind, checkfirst=True)
