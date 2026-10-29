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

import re
from enum import StrEnum
from typing import Any

from sqlalchemy import delete
from sqlalchemy.orm import Session

from pehchana.detection import Word
from pehchana.models import Call, Giveaway

# Dead air between the caller's last word and the arm's next one, in the window.
SLOW_REPLY_THRESHOLD_S = 1.5
# How far back from the first accusation (or the call's end, if none) to look.
WINDOW_S = 30.0
METHOD = "heuristic"

_NUMBER_WORDS = frozenset(
    [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
        "hundred",
        "thousand",
        "lakh",
        "crore",
    ]
)
_HAS_DIGIT = re.compile(r"\d")


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


def _channel_words(transcript: list[dict[str, Any]], index: int) -> list[Word]:
    for channel in transcript:
        if channel.get("channel") == index:
            return [Word(text=w["text"], start=w["start"], end=w["end"]) for w in channel["words"]]
    return []


def _channel_language(transcript: list[dict[str, Any]], index: int) -> str | None:
    for channel in transcript:
        if channel.get("channel") == index:
            return channel.get("language")
    return None


def _in_window(words: list[Word], start: float, end: float) -> list[Word]:
    return sorted((w for w in words if start <= w.start <= end), key=lambda w: w.start)


def _looks_like_a_number(text: str) -> bool:
    return bool(_HAS_DIGIT.search(text)) or text.strip(".,!?").lower() in _NUMBER_WORDS


def _detect_slow_replies(caller: list[Word], arm: list[Word]) -> list[tuple[float, str]]:
    """One hit per arm turn (an arm word preceded, in time, only by caller words)
    where the gap since the caller's last word exceeds the threshold."""
    hits: list[tuple[float, str]] = []
    merged = sorted(
        [("caller", w) for w in caller] + [("arm", w) for w in arm], key=lambda t: t[1].start
    )
    last_caller_end: float | None = None
    prev_speaker: str | None = None
    for speaker, word in merged:
        if speaker == "arm" and prev_speaker != "arm" and last_caller_end is not None:
            gap = word.start - last_caller_end
            if gap > SLOW_REPLY_THRESHOLD_S:
                hits.append(
                    (
                        word.start,
                        f"{gap:.1f}s gap before the arm said {word.text!r} at {word.start:.1f}s",
                    )
                )
        if speaker == "caller":
            last_caller_end = word.end
        prev_speaker = speaker
    return hits


def _detect_talked_over(caller: list[Word], arm: list[Word]) -> list[tuple[float, str]]:
    hits = []
    for a in arm:
        for c in caller:
            if c.start <= a.start < c.end:
                hits.append(
                    (
                        a.start,
                        f"arm said {a.text!r} at {a.start:.1f}s while the caller was still "
                        f"saying {c.text!r} (until {c.end:.1f}s)",
                    )
                )
                break
    return hits


def _detect_number_reading(arm: list[Word]) -> list[tuple[float, str]]:
    return [
        (w.start, f"arm said {w.text!r} at {w.start:.1f}s")
        for w in arm
        if _looks_like_a_number(w.text)
    ]


def tag_call(call_id: str, *, session: Session) -> list[Giveaway]:
    """Compute and store heuristic giveaway tags for one processed call.

    Idempotent: replaces this call's ``method="heuristic"`` rows. The LLM pass (#19)
    is separate and untouched here.
    """
    call = session.get(Call, call_id)
    if call is None:
        raise LookupError(f"no such call: {call_id}")
    if not call.transcript:
        raise ValueError(f"call {call_id} has no transcript yet (not processed?)")

    caller_index = call.recording_caller_channel if call.recording_caller_channel is not None else 0
    arm_index = 1 - caller_index

    window_end = call.first_accusation_s
    if window_end is None:
        window_end = call.duration_s if call.duration_s is not None else float("inf")
    window_start = max(0.0, window_end - WINDOW_S)

    caller_words = _in_window(
        _channel_words(call.transcript, caller_index), window_start, window_end
    )
    arm_words = _in_window(_channel_words(call.transcript, arm_index), window_start, window_end)

    rows: list[Giveaway] = []
    for _at_s, evidence in _detect_slow_replies(caller_words, arm_words):
        rows.append(_row(call_id, GiveawayTag.SLOW_REPLY, evidence))
    for _at_s, evidence in _detect_talked_over(caller_words, arm_words):
        rows.append(_row(call_id, GiveawayTag.TALKED_OVER, evidence))
    for _at_s, evidence in _detect_number_reading(arm_words):
        rows.append(_row(call_id, GiveawayTag.NUMBER_READING, evidence))

    caller_lang = _channel_language(call.transcript, caller_index)
    arm_lang = _channel_language(call.transcript, arm_index)
    if caller_words and arm_words and caller_lang and arm_lang and caller_lang != arm_lang:
        rows.append(
            _row(
                call_id,
                GiveawayTag.WRONG_LANGUAGE,
                f"caller spoke {caller_lang!r}, arm spoke {arm_lang!r}",
            )
        )

    session.execute(delete(Giveaway).where(Giveaway.call_id == call_id, Giveaway.method == METHOD))
    session.add_all(rows)
    session.commit()
    return rows


def _row(call_id: str, tag: GiveawayTag, evidence: str) -> Giveaway:
    return Giveaway(
        call_id=call_id, tag=tag.value, method=METHOD, evidence=evidence, confidence=1.0
    )
