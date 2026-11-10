"""Persistent data model (DRAFT, shared by all workstreams).

Changing a field other workstreams read? Say so in the PR description.

One row in ``calls`` is one game: a caller talking to one arm (a human volunteer or
one AI voice stack). Time zero for every timing field is the moment the arm picked
up, which is also when the Plivo session recording starts.
"""

from __future__ import annotations

import enum
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import (
    JSON,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pehchana.db import Base

log = logging.getLogger(__name__)


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


# A call still in progress: the only states a live callback (accusation, Bolna execution
# link, answer-URL retry) may attach to.
OPEN_STATUSES = (CallStatus.ROUTED, CallStatus.LIVE)


class CallStage(enum.StrEnum):
    """Where a call is in its life, read off its fields (see ``Call.stage``). Not stored."""

    IN_CALL = "in_call"  # routed or live
    AWAITING_RECORDING = "awaiting_recording"  # ended, no recording yet
    QUEUED = "queued"  # ended with a recording, not processed yet (or its job was lost)
    PROCESSING_ERROR = "processing_error"  # ended, last processing run failed; rerunnable
    PROCESSED = "processed"
    FAILED = "failed"


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

    # Telephony vendor ("plivo", ...) and its id for this call leg. Vendor-neutral so
    # switching providers needs no schema change (see telephony/base.py).
    provider: Mapped[str | None] = mapped_column(String(32))
    provider_call_id: Mapped[str | None] = mapped_column(String(64))
    bolna_execution_id: Mapped[str | None] = mapped_column(String(64), unique=True)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    duration_s: Mapped[float | None] = mapped_column(Float)

    # A bearer secret: whoever holds it can play the call. Validated against
    # RECORDING_HOST_ALLOWLIST before it is stored; never log it or return it from an API.
    recording_url: Mapped[str | None] = mapped_column(Text)
    # 0-based channel of the caller in the recording; set by the telephony provider.
    recording_caller_channel: Mapped[int | None] = mapped_column(Integer)
    language: Mapped[str | None] = mapped_column(String(16))
    # Word-level transcript of both channels (Deepgram), see integrations/deepgram.py.
    transcript: Mapped[list[dict[str, object]] | None] = mapped_column(JSON)
    bolna_payload: Mapped[dict[str, object] | None] = mapped_column(JSON)
    processing_error: Mapped[str | None] = mapped_column(Text)

    # Named so create_all and migration 0002 give the constraint the same name.
    __table_args__ = (
        UniqueConstraint("provider", "provider_call_id", name="uq_calls_provider_call_id"),
    )

    accusations: Mapped[list[Accusation]] = relationship(
        back_populates="call", cascade="all, delete-orphan", order_by="Accusation.at_s"
    )
    giveaways: Mapped[list[Giveaway]] = relationship(
        back_populates="call", cascade="all, delete-orphan"
    )

    @property
    def stage(self) -> CallStage:
        """Why a call is or is not on the leaderboard yet, from status, recording and error."""
        if self.status == CallStatus.PROCESSED:
            return CallStage.PROCESSED
        if self.status == CallStatus.FAILED:
            return CallStage.FAILED
        if self.status in OPEN_STATUSES:
            return CallStage.IN_CALL
        if not self.recording_url:
            return CallStage.AWAITING_RECORDING
        if self.processing_error:
            return CallStage.PROCESSING_ERROR
        return CallStage.QUEUED

    def set_status(self, status: CallStatus, *, via: str) -> None:
        """Change ``status`` and log the move, so a call's history can be read from logs.

        ``via`` names what moved it (``"plivo.dial-status"``, ``"pipeline"``, ...). Logs no
        caller data. The caller decides whether the move is allowed and commits.
        """
        if status != self.status:
            log.info("call %s: %s -> %s via %s", self.id, _value(self.status), status.value, via)
        self.status = status

    @property
    def first_accusation_s(self) -> float | None:
        times = [a.at_s for a in self.accusations if a.at_s is not None]
        return min(times) if times else None


def _value(status: CallStatus | None) -> str:
    # A Call built in Python has no status until it is flushed (the column default).
    return status.value if status is not None else "new"


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
