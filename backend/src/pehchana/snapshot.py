"""Data freeze (#28): export the calls to one JSON file, and load it back for analysis.

The snapshot keeps what the numbers need and nothing that can identify or replay a
call: no recording URL (a bearer secret), no transcript, no accusation phrase, no
provider ids. Caller hashes stay so repeat callers can be counted. It still lives
outside git.

``load_snapshot`` rebuilds an in-memory database from the file, so the pitch numbers
come from the same ``build_leaderboard`` code as the live site.
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload, sessionmaker
from sqlalchemy.pool import StaticPool

from pehchana.db import Base
from pehchana.models import (
    Accusation,
    AccusationSource,
    Call,
    CallStatus,
    Channel,
    Giveaway,
    Source,
    utcnow,
)

VERSION = 1
CALL_FIELDS = (
    "id",
    "channel",
    "source",
    "status",
    "arm_id",
    "arm_kind",
    "caller_hash",
    "started_at",
    "answered_at",
    "ended_at",
    "duration_s",
    "language",
)
_TIMES = ("started_at", "answered_at", "ended_at")

CallRow = dict[str, Any]


def _iso(value: datetime | None) -> str | None:
    if value is None:
        return None
    return value.replace(tzinfo=value.tzinfo or UTC).isoformat()  # SQLite drops the zone


def export_snapshot(session: Session) -> dict[str, Any]:
    """Every call (all sources, channels and statuses) as plain JSON data."""
    calls = session.scalars(
        select(Call)
        .options(selectinload(Call.accusations), selectinload(Call.giveaways))
        .order_by(Call.started_at, Call.id)
    ).all()
    rows: list[CallRow] = []
    for call in calls:
        row: CallRow = {f: getattr(call, f) for f in CALL_FIELDS}
        for f in _TIMES:
            row[f] = _iso(row[f])
        for f in ("channel", "source", "status"):
            row[f] = row[f].value
        row["accusations"] = sorted(
            ({"source": a.source.value, "at_s": a.at_s} for a in call.accusations),
            key=lambda a: (a["at_s"] is None, a["at_s"] or 0.0, a["source"]),
        )
        row["giveaways"] = sorted(
            ({"tag": g.tag, "method": g.method} for g in call.giveaways),
            key=lambda g: (g["tag"], g["method"]),
        )
        rows.append(row)
    return {"version": VERSION, "exported_at": _iso(utcnow()), "calls": rows}


def load_snapshot(
    data: dict[str, Any], *, keep: Callable[[CallRow], bool] | None = None
) -> Session:
    """A session on a fresh in-memory database holding the snapshot's calls.

    ``keep`` filters calls on the way in (for sensitivity checks), so everything that
    reads the session sees one consistent set of calls.
    """
    if data.get("version") != VERSION:
        raise ValueError(f"unsupported snapshot version: {data.get('version')!r}")
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    for row in data["calls"]:
        if keep is not None and not keep(row):
            continue
        fields = {f: row[f] for f in CALL_FIELDS}
        for f in _TIMES:
            fields[f] = datetime.fromisoformat(row[f]) if row[f] else None
        fields["channel"] = Channel(row["channel"])
        fields["source"] = Source(row["source"])
        fields["status"] = CallStatus(row["status"])
        call = Call(**fields)
        call.accusations = [
            Accusation(source=AccusationSource(a["source"]), at_s=a["at_s"])
            for a in row["accusations"]
        ]
        call.giveaways = [Giveaway(tag=g["tag"], method=g["method"]) for g in row["giveaways"]]
        session.add(call)
    session.commit()
    return session
