"""Call.stage and Call.set_status: the call lifecycle, readable without the database."""

import logging

import pytest

from pehchana.models import Call, CallStage, CallStatus

REC = "https://media.plivo.com/recording.mp3"


@pytest.mark.parametrize(
    ("status", "recording_url", "processing_error", "stage"),
    [
        (CallStatus.ROUTED, None, None, CallStage.IN_CALL),
        (CallStatus.LIVE, None, None, CallStage.IN_CALL),
        (CallStatus.ENDED, None, None, CallStage.AWAITING_RECORDING),
        (CallStatus.ENDED, None, "no recording_url yet", CallStage.AWAITING_RECORDING),
        (CallStatus.ENDED, REC, None, CallStage.QUEUED),
        (CallStatus.ENDED, REC, "DeepgramError: 500", CallStage.PROCESSING_ERROR),
        (CallStatus.PROCESSED, REC, None, CallStage.PROCESSED),
        (CallStatus.PROCESSED, REC, "rerun failed", CallStage.PROCESSED),  # old score stands
        (CallStatus.FAILED, None, None, CallStage.FAILED),
        (CallStatus.FAILED, REC, None, CallStage.FAILED),
    ],
)
def test_stage(status, recording_url, processing_error, stage):
    call = Call(status=status, recording_url=recording_url, processing_error=processing_error)
    assert call.stage == stage


def test_set_status_logs_the_move_without_caller_data(caplog):
    call = Call(id="c1", status=CallStatus.ROUTED, caller_hash="secret-hash")
    with caplog.at_level(logging.INFO, logger="pehchana.models"):
        call.set_status(CallStatus.ENDED, via="plivo.dial-status")
        call.set_status(CallStatus.ENDED, via="bolna.webhook")  # no move, no line
    assert call.status == CallStatus.ENDED
    assert [r.getMessage() for r in caplog.records] == [
        "call c1: routed -> ended via plivo.dial-status"
    ]
    assert "secret-hash" not in caplog.text
