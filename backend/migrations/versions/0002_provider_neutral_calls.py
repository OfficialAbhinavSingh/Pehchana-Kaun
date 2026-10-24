"""Provider-neutral Call: plivo_call_uuid -> (provider, provider_call_id).

Existing rows are kept: every ``plivo_call_uuid`` becomes ``provider='plivo'`` plus the
same id in ``provider_call_id``. ``recording_caller_channel`` is added empty; the
telephony provider fills it for new recordings.

Downgrade is lossy for any call from a vendor other than Plivo: the old schema has no
column for its id, so that id is dropped.

Revision ID: 0002
Revises: 0001
Create Date: 2026-10-24
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002"
down_revision: str | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("calls") as batch:
        batch.add_column(sa.Column("provider", sa.String(length=32), nullable=True))
        batch.add_column(sa.Column("provider_call_id", sa.String(length=64), nullable=True))
        batch.add_column(sa.Column("recording_caller_channel", sa.Integer(), nullable=True))
    op.execute(
        "UPDATE calls SET provider = 'plivo', provider_call_id = plivo_call_uuid "
        "WHERE plivo_call_uuid IS NOT NULL"
    )
    # Dropping the column also drops its unique constraint.
    with op.batch_alter_table("calls") as batch:
        batch.drop_column("plivo_call_uuid")
        batch.create_unique_constraint(
            "uq_calls_provider_call_id", ["provider", "provider_call_id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("calls") as batch:
        batch.drop_constraint("uq_calls_provider_call_id", type_="unique")
        batch.add_column(sa.Column("plivo_call_uuid", sa.String(length=64), nullable=True))
    op.execute(
        "UPDATE calls SET plivo_call_uuid = provider_call_id "
        "WHERE provider = 'plivo' AND provider_call_id IS NOT NULL"
    )
    with op.batch_alter_table("calls") as batch:
        batch.drop_column("recording_caller_channel")
        batch.drop_column("provider_call_id")
        batch.drop_column("provider")
        batch.create_unique_constraint("uq_calls_plivo_call_uuid", ["plivo_call_uuid"])
