"""Deepgram pre-recorded transcription of the stereo session recording.  Owner: WS2.

Transcribed after the call, not live, because we need word timestamps on both
channels for every arm, including the human control arm that Bolna never sees.

Suggested request: ``POST https://api.deepgram.com/v1/listen`` with
``model=nova-3&language=multi&multichannel=true&punctuate=true&smart_format=false``
(keep numbers as spoken: misread numbers are a giveaway we want to catch) and body
``{"url": <recording_url>}``. Verify language coverage for Tamil etc. on Day 3.
"""

from __future__ import annotations

from dataclasses import dataclass

from pehchana.detection import Word


@dataclass(frozen=True)
class ChannelTranscript:
    index: int
    words: list[Word]
    language: str | None


@dataclass(frozen=True)
class Transcription:
    duration_s: float | None
    channels: list[ChannelTranscript]


def transcribe_url(recording_url: str, *, api_key: str) -> Transcription:
    """TODO(WS2)"""
    raise NotImplementedError
