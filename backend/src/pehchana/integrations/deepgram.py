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
from typing import Any

import httpx

from pehchana.detection import Word

# Connect/write/pool, then a generous read cap: pre-recorded transcription on
# Deepgram's side can take a while for a several-minute call.
_TIMEOUT = httpx.Timeout(10.0, read=60.0)

_PARAMS = {
    "model": "nova-3",
    "language": "multi",
    "multichannel": "true",
    "punctuate": "true",
    "smart_format": "false",
}


@dataclass(frozen=True)
class ChannelTranscript:
    index: int
    words: list[Word]
    language: str | None


@dataclass(frozen=True)
class Transcription:
    duration_s: float | None
    channels: list[ChannelTranscript]


def _channel(index: int, raw: dict[str, Any]) -> ChannelTranscript:
    alt = (raw.get("alternatives") or [{}])[0]
    words = [
        Word(text=w["word"], start=float(w["start"]), end=float(w["end"]))
        for w in alt.get("words", [])
    ]
    return ChannelTranscript(index=index, words=words, language=raw.get("detected_language"))


def transcribe_url(
    recording_url: str, *, api_key: str, model: str | None = None, language: str | None = None
) -> Transcription:
    """POST /v1/listen on the stereo session recording. Both channels come back in one
    response (``results.channels``), in the same order as the recording.

    ``model``/``language`` override the project defaults (see ``_PARAMS``) without
    needing a code change, for #12's spike comparisons (``language=hi`` vs ``multi``
    vs ``detect_language=true``).

    Not yet verified against a real response (no Deepgram key to hand): shapes are
    taken from Deepgram's own docs (word fields, ``results.channels[i].detected_language``,
    ``Authorization: Token`` scheme), not a live call like ``integrations/bolna.py``.
    Confirm against a real recording before trusting this for #12/#16.
    """
    params = dict(_PARAMS)
    if model:
        params["model"] = model
    if language:
        params["language"] = language
    with httpx.Client(timeout=_TIMEOUT) as client:
        response = client.post(
            "https://api.deepgram.com/v1/listen",
            params=params,
            json={"url": recording_url},
            headers={"Authorization": f"Token {api_key}"},
        )
        response.raise_for_status()
        data = response.json()
    channels = data.get("results", {}).get("channels", [])
    return Transcription(
        duration_s=data.get("metadata", {}).get("duration"),
        channels=[_channel(i, c) for i, c in enumerate(channels)],
    )
