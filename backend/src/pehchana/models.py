"""Persistent data model (DRAFT, shared by all workstreams).

Changing a field other workstreams read? Say so in the PR description.

One row in ``calls`` is one game: a caller talking to one arm (a human volunteer or
one AI voice stack). Time zero for every timing field is the moment the arm picked
up, which is also when the Plivo session recording starts.
"""

from __future__ import annotations

import enum
import uuid
from datetime import UTC, datetime

from sqlalchemy import JSON, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pehchana.db import Base


def _uuid() -> str:
    return str(uuid.uuid4())


def utcnow() -> datetime:
    return datetime.now(UTC)


class Channel(enum.StrEnum):
    PHONE = "phone"
    WEB = "web"


class CallStatus(enum.StrEnum):
    ROUTED = "routed"  # arm chosen, dialing
    LIVE = "live"  # arm answered
    ENDED = "ended"  # hung up, waiting for recording/processing
    PROCESSED = "processed"  # transcript + detection done
    FAILED = "failed"  # nobody answered, or processing failed permanently


class Source(enum.StrEnum):
    REAL = "real"
    DEMO = "demo"  # seeded for local development; excluded from public stats


class Call(Base):
    __tablename__ = "calls"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    channel: Mapped[Channel] = mapped_column(Enum(Channel), default=Channel.PHONE)
    source: Mapped[Source] = mapped_column(Enum(Source), default=Source.REAL)
    status: Mapped[CallStatus] = mapped_column(Enum(CallStatus), default=CallStatus.ROUTED)

    arm_id: Mapped[str] = mapped_column(String(64), index=True)
    arm_kind: Mapped[str] = mapped_column(String(16))  # "human" | "ai"
    caller_hash: Mapped[str | None] = mapped_column(String(64), index=True)

    plivo_call_uuid: Mapped[str | None] = mapped_column(String(64), unique=True)
    bolna_execution_id: Mapped[str | None] = mapped_column(String(64), unique=True)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    duration_s: Mapped[float | None] = mapped_column(Float)

    recording_url: Mapped[str | None] = mapped_column(Text)
    language: Mapped[str | None] = mapped_column(String(16))
    # Word-level transcript of both channels (Deepgram), see integrations/deepgram.py.
    transcript: Mapped[list[dict[str, object]] | None] = mapped_column(JSON)
    bolna_payload: Mapped[dict[str, object] | None] = mapped_column(JSON)
    processing_error: Mapped[str | None] = mapped_column(Text)

    accusations: Mapped[list[Accusation]] = relationship(
        back_populates="call", cascade="all, delete-orphan", order_by="Accusation.at_s"
    )
    giveaways: Mapped[list[Giveaway]] = relationship(
        back_populates="call", cascade="all, delete-orphan"
    )

    @property
    def first_accusation_s(self) -> float | None:
        times = [a.at_s for a in self.accusations if a.at_s is not None]
        return min(times) if times else None


class AccusationSource(enum.StrEnum):
    TRANSCRIPT = "transcript"  # found in the caller channel of the recording (all arms)
    FUNCTION = "function"  # Bolna agent called accuse_bot live (AI arms only)


class Accusation(Base):
    """The caller said some version of "tum bot ho!"."""

    __tablename__ = "accusations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    call_id: Mapped[str] = mapped_column(ForeignKey("calls.id", ondelete="CASCADE"), index=True)
    source: Mapped[AccusationSource] = mapped_column(Enum(AccusationSource))
    at_s: Mapped[float | None] = mapped_column(Float)  # seconds since the arm answered
    phrase: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    call: Mapped[Call] = relationship(back_populates="accusations")


class Giveaway(Base):
    """What made the caller suspicious, tagged after the call."""

    __tablename__ = "giveaways"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    call_id: Mapped[str] = mapped_column(ForeignKey("calls.id", ondelete="CASCADE"), index=True)
    tag: Mapped[str] = mapped_column(String(48), index=True)
    method: Mapped[str] = mapped_column(String(16))  # "heuristic" | "llm"
    evidence: Mapped[str | None] = mapped_column(Text)
    confidence: Mapped[float | None] = mapped_column(Float)

    call: Mapped[Call] = relationship(back_populates="giveaways")


class ShiftOverride(Base):
    """Manual on/off switch for the human arm, set from the admin endpoint."""

    __tablename__ = "shift_overrides"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    humans_on_shift: Mapped[bool] = mapped_column()
    until: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    set_by: Mapped[str | None] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
