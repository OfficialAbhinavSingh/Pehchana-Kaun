"""pipeline.process_call: Deepgram -> detection -> Call.status=processed.

detection.detect_accusations is still TODO(WS2): happy-path tests monkeypatch it with a
fake so the orchestration itself is covered without depending on the real detector.
"""

from datetime import UTC, datetime

import httpx
import pytest
import respx

from pehchana import db, pipeline
from pehchana.config import Settings
from pehchana.detection import Detection
from pehchana.models import Accusation, AccusationSource, Call, CallStatus, Channel, Source

URL = "https://api.deepgram.com/v1/listen"
SETTINGS = Settings(deepgram_api_key="dg-secret")


@pytest.fixture(autouse=True)
def _db_ready(client):
    """The ``client`` fixture creates the schema; these tests talk to the DB directly."""


RESPONSE = {
    "metadata": {"duration": 40.0},
    "results": {
        "channels": [
            {
                "detected_language": "hi",
                "alternatives": [
                    {
                        "words": [
                            {"word": "tum", "start": 10.0, "end": 10.2, "confidence": 0.9},
                            {"word": "bot", "start": 10.2, "end": 10.4, "confidence": 0.9},
                        ]
                    }
                ],
            },
            {
                "detected_language": "en",
                "alternatives": [{"words": [{"word": "yes", "start": 10.6, "end": 10.8}]}],
            },
        ]
    },
}


def make_call(
    *,
    recording_url: str | None = "https://media.plivo.com/recording.mp3",
    recording_caller_channel: int | None = 0,
    status: CallStatus = CallStatus.ENDED,
) -> Call:
    call = Call(
        channel=Channel.PHONE,
        source=Source.REAL,
        status=status,
        arm_id="kalpa",
        arm_kind="ai",
        caller_hash="hash123",
        started_at=datetime.now(UTC),
        answered_at=datetime.now(UTC),
        recording_url=recording_url,
        recording_caller_channel=recording_caller_channel,
    )
    with db.get_sessionmaker()() as s:
        s.add(call)
        s.commit()
        s.refresh(call)
        s.expunge(call)
    return call


def get_call(call_id: str) -> Call:
    with db.get_sessionmaker()() as s:
        call = s.get(Call, call_id)
        assert call is not None
        s.expunge(call)
        return call


@pytest.fixture
def fake_detector(monkeypatch):
    """detect_accusations -> one fixed Detection, so the orchestration is testable
    without the real detector existing yet."""
    monkeypatch.setattr(
        pipeline, "detect_accusations", lambda words: [Detection(at_s=10.0, phrase="tum bot ho")]
    )


# --- happy path -----------------------------------------------------------------------


@respx.mock
def test_processes_a_call_end_to_end(fake_detector):
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    call = make_call()
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)

    assert result.status == CallStatus.PROCESSED
    assert result.processing_error is None
    assert result.language == "hi"  # channel 0 = caller
    assert result.transcript is not None and len(result.transcript) == 2

    with db.get_sessionmaker()() as s:
        (acc,) = s.query(Accusation).filter(Accusation.call_id == call.id).all()
        assert acc.source == AccusationSource.TRANSCRIPT
        assert acc.at_s == 10.0 and acc.phrase == "tum bot ho"


@respx.mock
def test_uses_recording_caller_channel_not_always_zero(fake_detector):
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    call = make_call(recording_caller_channel=1)
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert result.language == "en"  # channel 1 is the caller here


# --- idempotent rerun -------------------------------------------------------------------


@respx.mock
def test_rerun_replaces_transcript_accusations_not_function_ones(fake_detector):
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    call = make_call()
    with db.get_sessionmaker()() as s:
        s.add(Accusation(call_id=call.id, source=AccusationSource.FUNCTION, at_s=5.0, phrase="x"))
        s.commit()

    with db.get_sessionmaker()() as s:
        pipeline.process_call(call.id, session=s, settings=SETTINGS)
    with db.get_sessionmaker()() as s:
        pipeline.process_call(call.id, session=s, settings=SETTINGS)  # rerun

    with db.get_sessionmaker()() as s:
        accs = s.query(Accusation).filter(Accusation.call_id == call.id).all()
        by_source = {a.source for a in accs}
        assert by_source == {AccusationSource.FUNCTION, AccusationSource.TRANSCRIPT}
        assert len([a for a in accs if a.source == AccusationSource.TRANSCRIPT]) == 1


# --- failure paths: processing_error set, status untouched, never raises ---------------


def test_no_recording_url_yet(fake_detector):
    call = make_call(recording_url=None)
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert result.status == CallStatus.ENDED  # unchanged
    assert result.processing_error == "no recording_url yet"


@respx.mock
def test_deepgram_failure_is_caught_not_raised(fake_detector):
    respx.post(URL).mock(return_value=httpx.Response(500, json={"error": "down"}))
    call = make_call()
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert result.status == CallStatus.ENDED
    assert result.processing_error is not None and "HTTPStatusError" in result.processing_error


@respx.mock
def test_detector_failure_fails_cleanly_not_silently(monkeypatch):
    """If detect_accusations raises an error, processing must fail loudly into
    processing_error rather than silently producing a processed call."""

    def _broken_detector(_words):
        raise RuntimeError("detector crashed")

    monkeypatch.setattr(pipeline, "detect_accusations", _broken_detector)
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    call = make_call()
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert result.status == CallStatus.ENDED
    assert result.processing_error is not None and "RuntimeError" in result.processing_error


@respx.mock
def test_real_detector_runs_end_to_end_without_mocks():
    """Runs process_call with the real detect_accusations implementation."""
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    call = make_call()
    with db.get_sessionmaker()() as s:
        result = pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert result.status == CallStatus.PROCESSED
    assert result.processing_error is None


def test_unknown_call_id_raises_lookup_error(fake_detector):
    with db.get_sessionmaker()() as s, pytest.raises(LookupError):
        pipeline.process_call("no-such-call", session=s, settings=SETTINGS)


def test_never_logs_the_caller_hash(fake_detector, caplog):
    call = make_call(recording_url=None)
    with db.get_sessionmaker()() as s:
        pipeline.process_call(call.id, session=s, settings=SETTINGS)
    assert "hash123" not in caplog.text


# --- process_all_failed -----------------------------------------------------------------


@respx.mock
def test_process_all_failed_retries_only_failed_calls(fake_detector):
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    failed_no_recording = make_call(recording_url=None)
    with db.get_sessionmaker()() as s:
        pipeline.process_call(failed_no_recording.id, session=s, settings=SETTINGS)

    already_processed = make_call()
    with db.get_sessionmaker()() as s:
        pipeline.process_call(already_processed.id, session=s, settings=SETTINGS)

    untouched = make_call(recording_url=None)  # never run, no processing_error yet -> not retried

    with db.get_sessionmaker()() as s:
        results = pipeline.process_all_failed(s, settings=SETTINGS)

    assert {c.id for c in results} == {failed_no_recording.id}
    assert get_call(untouched.id).processing_error is None
