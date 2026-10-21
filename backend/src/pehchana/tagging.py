"""Post-call "giveaway" tagging: what made the caller suspicious.  Owner: WS2.

Two passes, both stored as ``Giveaway`` rows:

1. Heuristics from the stereo word timings (no LLM): long gaps before the arm
   replies, the arm talking over the caller, numbers in the arm's speech, etc.
2. An LLM pass over the ~30 s before the accusation that picks tags from a fixed
   list and quotes the evidence.

For the LLM pass use the official Anthropic SDK (already a dependency) with
structured outputs: ``client.beta.messages.parse(..., output_format=<pydantic model>)``.
Default model is ``TAGGER_MODEL`` (``claude-opus-5``); server-side refusal fallback:
``betas=["server-side-fallback-2026-07-01"], fallbacks="default"``. Always check
``stop_reason`` before reading the parsed output.
"""

from __future__ import annotations

from enum import StrEnum


class GiveawayTag(StrEnum):
    SLOW_REPLY = "slow_reply"  # dead air before the arm answered
    TALKED_OVER = "talked_over"  # arm interrupted / didn't yield
    NUMBER_READING = "number_reading"  # phone numbers, amounts, dates said oddly
    PRONUNCIATION = "pronunciation"  # names, Indian words, Hinglish said wrong
    FLAT_EMOTION = "flat_emotion"  # no laugh, no reaction, monotone
    TOO_PERFECT = "too_perfect"  # no "umm", no stumbles, over-polite
    WRONG_LANGUAGE = "wrong_language"  # didn't follow a language switch
    CONTENT = "content"  # said something no human would (knowledge, refusal)
    OTHER = "other"


def tag_call(call_id: str) -> None:
    """Compute and store giveaway tags for one processed call. TODO(WS2)"""
    raise NotImplementedError
