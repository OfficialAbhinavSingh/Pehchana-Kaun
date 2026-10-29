"""Find the moment the caller accused the other side of being a bot.  Owner: WS2.

Input is the word-level transcript of the **caller's channel** of the stereo
recording (Deepgram output), so the same detector runs on human and AI arms.

Must handle Hinglish (romanized), Devanagari and English, e.g. "tum bot ho",
"तुम बॉट हो", "you're a bot". Collapse repeats said within a few seconds.
Build the phrase list from real test calls, not guesses (docs/plan.md, Day 3).
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Sequence
from dataclasses import dataclass

# Minimum separation (in seconds) between two distinct accusations.
# Accusations repeated within this window are treated as one conversational burst.
REPEAT_COLLAPSE_WINDOW_S = 3.0

# Characters to strip when normalizing word tokens.
# Includes standard ASCII punctuation, quotes, Hindi danda, and unicode quote variants.
_PUNCT_PATTERN = re.compile(
    r"""[!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~।॥\u2018\u2019\u201c\u201d'"]+"""
)


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
    """Lowercase, NFC-normalize, strip punctuation, collapse spaces.

    Handles abbreviations like "a.i." -> "ai", smart quotes, and punctuation attached
    to words by Deepgram (e.g. "ho!" -> "ho", "bot," -> "bot").
    """
    if not text:
        return ""
    # 1. Unicode NFC normalization and lowercasing
    text = unicodedata.normalize("NFC", text).lower()

    # 2. Handle common contractions and abbreviations
    text = re.sub(r"\ba\.i\.?\b", "ai", text)
    text = re.sub(r"\byou['\u2019]re\b", "youre", text)
    text = re.sub(r"\byou['\u2019]ve\b", "youve", text)

    # 3. Strip punctuation
    text = _PUNCT_PATTERN.sub(" ", text)

    # 4. Collapse consecutive whitespace
    return " ".join(text.split())


# Curated accusation phrases across Hinglish, Devanagari, and English.
# Each entry is stored in normalized form (lowercase, NFC, no punctuation, single space).
ACCUSATION_PHRASES: frozenset[str] = frozenset(
    {
        # --- Hinglish (Romanized) ---
        "tum bot ho",
        "tu bot hai",
        "aap bot ho",
        "aap bot hain",
        "tum ai ho",
        "tu ai hai",
        "aap ai ho",
        "aap ai hain",
        "tum robot ho",
        "tu robot hai",
        "aap robot ho",
        "aap robot hain",
        "kya tum bot ho",
        "kya tu bot hai",
        "kya aap bot ho",
        "kya aap bot hain",
        "kya tum ai ho",
        "kya tu ai hai",
        "kya aap ai ho",
        "kya aap ai hain",
        "kya tum robot ho",
        "kya tu robot hai",
        "kya aap robot ho",
        "kya aap robot hain",
        "bot hai kya",
        "ai hai kya",
        "robot hai kya",
        "bot ho kya",
        "ai ho kya",
        "robot ho kya",
        "yeh bot hai",
        "ye bot hai",
        "yeh ai hai",
        "ye ai hai",
        "yeh robot hai",
        "ye robot hai",
        "bot bol raha hai",
        "bot bol rahi hai",
        "ai bol raha hai",
        "ai bol rahi hai",
        "tu pakka bot hai",
        "tum pakka bot ho",
        "aap pakka bot hain",
        "arre tum bot ho",
        "are tum bot ho",
        "arey tum bot ho",
        "lagta hai bot ho",
        "lagta hai bot hai",
        "lagta hai ai hai",
        # --- English ---
        "you are a bot",
        "youre a bot",
        "you are an ai",
        "youre an ai",
        "you are a robot",
        "youre a robot",
        "you are bot",
        "youre bot",
        "you are ai",
        "youre ai",
        "are you a bot",
        "are you an ai",
        "are you a robot",
        "are you bot",
        "are you ai",
        "this is a bot",
        "this is an ai",
        "is this a bot",
        "is this an ai",
        "i think you are a bot",
        "i think youre a bot",
        # --- Devanagari ---
        "तुम बॉट हो",
        "तुम बोट हो",
        "तू बॉट है",
        "तू बोट है",
        "आप बॉट हैं",
        "आप बॉट हो",
        "आप बोट हैं",
        "आप बोट हो",
        "तुम एआई हो",
        "तू एआई है",
        "आप एआई हैं",
        "आप एआई हो",
        "तुम ai हो",
        "तू ai है",
        "आप ai हैं",
        "आप ai हो",
        "तुम रोबोट हो",
        "तू रोबोट है",
        "आप रोबोट हैं",
        "आप रोबोट हो",
        "क्या तुम बॉट हो",
        "क्या तुम बोट हो",
        "क्या तू बॉट है",
        "क्या तू बोट है",
        "क्या आप बॉट हैं",
        "क्या आप बोट हैं",
        "क्या तुम एआई हो",
        "क्या आप एआई हैं",
        "बॉट है क्या",
        "बोट है क्या",
        "एआई है क्या",
        "रोबोट है क्या",
        "बॉट हो क्या",
        "बोट हो क्या",
        "यह बॉट है",
        "ये बॉट है",
        "यह बोट है",
        "ये बोट है",
        "यह एआई है",
        "ये एआई है",
        "यह रोबोट है",
        "ये रोबोट है",
        "बॉट बोल रहा है",
        "बॉट बोल रही है",
        "बोट बोल रहा है",
        "बोट बोल रही है",
    }
)

# Maximum phrase length in words for sliding window search.
_MAX_WINDOW_WORDS = 6


def detect_accusations(words: Sequence[Word]) -> list[Detection]:
    """Every accusation in the caller channel, in time order.

    Scans words using a sliding window (1 to 6 words), matches normalized phrases
    against ACCUSATION_PHRASES, and collapses consecutive detections within 3.0s.
    """
    if not words:
        return []

    # Map words to normalized non-empty tokens with original Word references
    normalized_tokens: list[tuple[str, Word]] = []
    for w in words:
        norm = normalize(w.text)
        if norm:
            normalized_tokens.append((norm, w))

    n = len(normalized_tokens)
    raw_detections: list[Detection] = []
    i = 0

    while i < n:
        matched = False
        # Try longer phrases first for greedy matching (e.g. "kya tum bot ho" before "tum bot ho")
        max_k = min(_MAX_WINDOW_WORDS, n - i)
        for k in range(max_k, 0, -1):
            phrase = " ".join(normalized_tokens[i + j][0] for j in range(k))
            if phrase in ACCUSATION_PHRASES:
                start_time = normalized_tokens[i][1].start
                raw_detections.append(Detection(at_s=start_time, phrase=phrase))
                i += k  # Advance past matched words
                matched = True
                break
        if not matched:
            i += 1

    # Collapse repeated detections occurring within REPEAT_COLLAPSE_WINDOW_S (3.0s)
    collapsed: list[Detection] = []
    for d in raw_detections:
        if not collapsed or (d.at_s - collapsed[-1].at_s >= REPEAT_COLLAPSE_WINDOW_S):
            collapsed.append(d)

    return collapsed
