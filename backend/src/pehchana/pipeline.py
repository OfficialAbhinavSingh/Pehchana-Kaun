"""Post-call processing.  Owner: WS2.

Triggered when Plivo reports the recording is ready (and re-runnable from the CLI):

    recording_url
      -> Deepgram (both channels, word timestamps)        integrations/deepgram.py
      -> accusations in the caller channel               detection.py
      -> merge with live accuse_bot function hits (AI arms)
      -> giveaway tags                                    tagging.py
      -> Call.status = processed

Must be idempotent: re-running on a call replaces its TRANSCRIPT accusations (FUNCTION
ones, from a live accuse_bot call, are untouched) and tags.

``detection.detect_accusations`` and ``tagging.tag_call`` are still TODO(WS2): until
they exist, ``process_call`` fails cleanly (``processing_error`` set, status untouched,
safe to rerun) rather than silently producing a call with no accusations.
"""

from __future__ import annotations

import logging

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from pehchana.config import Settings, get_settings
from pehchana.detection import detect_accusations
from pehchana.integrations.deepgram import ChannelTranscript, transcribe_url
from pehchana.models import Accusation, AccusationSource, Call, CallStatus, utcnow

log = logging.getLogger(__name__)


class ProcessingError(Exception):
    """A call could not be processed. ``processing_error`` already holds the message."""


def _store_transcript(channels: list[ChannelTranscript]) -> list[dict[str, object]]:
    """Compact word transcript for both channels, in Call.transcript's JSON shape."""
    return [
        {
            "channel": c.index,
            "language": c.language,
            "words": [{"text": w.text, "start": w.start, "end": w.end} for w in c.words],
        }
        for c in channels
    ]


def process_call(call_id: str, *, session: Session, settings: Settings | None = None) -> Call:
    """Transcribe, detect accusations, and mark ``call`` processed.

    Raises ``LookupError`` for an unknown ``call_id`` (a programming error, not a
    retryable failure). Every other failure (no recording yet, Deepgram down, the
    detector not built yet) is caught, stored in ``processing_error``, and does not
    raise: the call's ``status`` is left as it was, safe to rerun once the problem is
    fixed. The caller_hash and any raw transcript text are never logged.
    """
    settings = settings or get_settings()
    call = session.get(Call, call_id)
    if call is None:
        raise LookupError(f"no such call: {call_id}")

    if not call.recording_url:
        call.processing_error = "no recording_url yet"
        session.commit()
        return call

    caller_index = call.recording_caller_channel if call.recording_caller_channel is not None else 0

    try:
        transcription = transcribe_url(
            call.recording_url,
            api_key=settings.deepgram_api_key,
            model=settings.deepgram_model,
            language=settings.deepgram_language,
        )
        caller = next((c for c in transcription.channels if c.index == caller_index), None)
        if caller is None:
            raise ProcessingError(f"no channel {caller_index} in the Deepgram response")
        detections = detect_accusations(caller.words)
    except Exception as e:  # Deepgram down, detector not built yet, bad response shape, ...
        log.exception("processing failed for call %s", call_id)
        call.processing_error = f"{type(e).__name__}: {e}"
        session.commit()
        return call

    call.transcript = _store_transcript(transcription.channels)
    call.language = caller.language
    if transcription.duration_s is not None:
        call.duration_s = transcription.duration_s

    session.execute(
        delete(Accusation).where(
            Accusation.call_id == call.id, Accusation.source == AccusationSource.TRANSCRIPT
        )
    )
    for d in detections:
        session.add(
            Accusation(
                call_id=call.id, source=AccusationSource.TRANSCRIPT, at_s=d.at_s, phrase=d.phrase
            )
        )

    call.processing_error = None
    call.status = CallStatus.PROCESSED
    call.ended_at = call.ended_at or utcnow()
    session.flush()

    try:
        from pehchana import tagging

        tagging.tag_call(call.id, session=session)
        tagging.tag_call_llm(call.id, session=session, settings=settings)
    except Exception:
        log.exception("tagging failed for call %s", call_id)

    session.commit()
    return call


def process_all_failed(session: Session, *, settings: Settings | None = None) -> list[Call]:
    """Rerun every call that previously failed processing (``processing_error`` set,
    never reached ``PROCESSED``). Used by ``pk process --all-failed``."""
    ids = session.scalars(
        select(Call.id).where(
            Call.processing_error.is_not(None), Call.status != CallStatus.PROCESSED
        )
    ).all()
    return [process_call(call_id, session=session, settings=settings) for call_id in ids]
