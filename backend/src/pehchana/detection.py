"""Find the moment the caller accused the other side of being a bot.  Owner: WS2.

Input is the word-level transcript of the **caller's channel** of the stereo
recording (Deepgram output), so the same detector runs on human and AI arms.

Must handle Hinglish (romanized), Devanagari and English, e.g. "tum bot ho",
"तुम बॉट हो", "you're a bot". Collapse repeats said within a few seconds.
Build the phrase list from real test calls, not guesses (docs/plan.md, Day 3).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    text: str
    start: float  # seconds since the arm answered
    end: float


@dataclass(frozen=True)
class Detection:
    at_s: float  # start time of the first word of the accusation
    phrase: str


def normalize(text: str) -> str:
    """Lowercase, NFC-normalize, strip punctuation, collapse spaces. TODO(WS2)"""
    raise NotImplementedError


def detect_accusations(words: Sequence[Word]) -> list[Detection]:
    """Every accusation in the caller channel, in time order. TODO(WS2)"""
    raise NotImplementedError
