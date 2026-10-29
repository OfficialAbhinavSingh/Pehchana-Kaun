"""test_detection.py: Tests for pehchana.detection (WS2-06)."""

import json
from pathlib import Path

import pytest

from pehchana.detection import (
    Word,
    detect_accusations,
    normalize,
)

CASES_PATH = Path(__file__).parent / "data" / "detector_cases.json"
FIXTURE_PATH = Path(__file__).parent / "fixtures" / "deepgram" / "stereo_hinglish.json"


# --- 1. Normalization unit tests -----------------------------------------------------


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("tum", "tum"),
        ("TUM", "tum"),
        ("ho!", "ho"),
        ("bot?", "bot"),
        ("bot,", "bot"),
        ("a.i.", "ai"),
        ("A.I.", "ai"),
        ("you're", "youre"),
        ("you\u2019re", "youre"),  # Smart / curly quote
        ("तुम बॉट हो!", "तुम बॉट हो"),
        ("  aap   AI   ho  ", "aap ai ho"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(raw: str, expected: str) -> None:
    assert normalize(raw) == expected


# --- 2. Evaluation on labelled test suite (precision & recall) ----------------------


def test_eval_dataset_precision_and_recall() -> None:
    """Evaluate against the 30+ labelled test cases in backend/tests/data/detector_cases.json.

    Requires precision >= 0.9 and recall >= 0.9.
    """
    assert CASES_PATH.exists(), f"Missing eval dataset at {CASES_PATH}"
    with open(CASES_PATH) as f:
        cases = json.load(f)

    assert len(cases) >= 30, f"Expected at least 30 cases, found {len(cases)}"

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for case in cases:
        words = [Word(w["text"], w["start"], w["end"]) for w in case["words"]]
        detections = detect_accusations(words)
        is_detected = len(detections) > 0
        is_true_accusation = case["is_accusation"]

        if is_true_accusation:
            if is_detected:
                tp += 1
                if case["expected_at_s"] is not None:
                    assert round(detections[0].at_s, 1) == round(case["expected_at_s"], 1)
            else:
                fn += 1
        else:
            if is_detected:
                fp += 1
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    print(
        f"\nDetector Eval: TP={tp}, FP={fp}, TN={tn}, FN={fn} | "
        f"Precision={precision:.3f}, Recall={recall:.3f}"
    )

    assert precision >= 0.9, f"Precision below 0.9: {precision:.3f} (FP={fp})"
    assert recall >= 0.9, f"Recall below 0.9: {recall:.3f} (FN={fn})"


# --- 3. Repetition collapsing tests --------------------------------------------------


def test_collapses_repeats_within_three_seconds() -> None:
    """Accusations repeated in quick succession (e.g. burst 'tum bot ho, bot ho') collapse."""
    words = [
        Word("tum", 10.0, 10.2),
        Word("bot", 10.3, 10.5),
        Word("ho", 10.6, 10.8),
        # Immediate repetition within 1.2s
        Word("tum", 11.5, 11.7),
        Word("bot", 11.8, 12.0),
        Word("ho", 12.1, 12.3),
    ]
    detections = detect_accusations(words)
    assert len(detections) == 1
    assert detections[0].at_s == 10.0


def test_detects_separate_accusations_after_window() -> None:
    """Accusations separated by more than 3 seconds are recorded as distinct events."""
    words = [
        Word("tum", 10.0, 10.2),
        Word("bot", 10.3, 10.5),
        Word("ho", 10.6, 10.8),
        # Second accusation after 15 seconds
        Word("aap", 25.0, 25.2),
        Word("ai", 25.3, 25.5),
        Word("ho", 25.6, 25.8),
    ]
    detections = detect_accusations(words)
    assert len(detections) == 2
    assert detections[0].at_s == 10.0
    assert detections[1].at_s == 25.0


# --- 4. Deepgram stereo Hinglish fixture test ---------------------------------------


def test_detects_accusation_in_deepgram_stereo_fixture() -> None:
    """Verifies accusation detection against the canonical Deepgram stereo fixture."""
    assert FIXTURE_PATH.exists()
    with open(FIXTURE_PATH) as f:
        data = json.load(f)

    # Channel 0 is the caller channel
    caller_data = data["results"]["channels"][0]["alternatives"][0]
    words = [Word(w["word"], w["start"], w["end"]) for w in caller_data["words"]]

    detections = detect_accusations(words)
    assert len(detections) == 1
    assert round(detections[0].at_s, 1) == 18.2
    assert detections[0].phrase == "tum bot ho"


# --- 5. Empty and edge cases ---------------------------------------------------------


def test_empty_words() -> None:
    assert detect_accusations([]) == []


def test_words_with_no_accusation() -> None:
    words = [Word("hello", 1.0, 1.2), Word("kaise", 1.3, 1.5), Word("ho", 1.6, 1.8)]
    assert detect_accusations(words) == []
