"""Tests for pehchana.audit (WS2-10)."""

import json
from pathlib import Path

import pytest

from pehchana.audit import AuditCase, load_audit_cases, run_audit
from pehchana.detection import Word


def test_load_audit_cases(tmp_path: Path) -> None:
    data = [
        {
            "id": "case-pos",
            "text": "tum bot ho na",
            "is_accusation": True,
            "expected_phrase": "tum bot ho",
            "expected_at_s": 5.2,
            "words": [
                {"text": "tum", "start": 5.2, "end": 5.4},
                {"text": "bot", "start": 5.5, "end": 5.8},
                {"text": "ho", "start": 5.9, "end": 6.1},
            ],
        },
        {
            "id": "case-neg",
            "text": "kal maine bot dekha",
            "is_accusation": False,
            "words": [
                {"text": "kal", "start": 1.0, "end": 1.2},
                {"text": "dekha", "start": 1.3, "end": 1.5},
            ],
        },
    ]
    file = tmp_path / "cases.json"
    file.write_text(json.dumps(data))

    cases = load_audit_cases(file)
    assert len(cases) == 2
    assert cases[0].case_id == "case-pos"
    assert cases[0].is_accusation is True
    assert len(cases[0].words) == 3
    assert cases[1].case_id == "case-neg"
    assert cases[1].is_accusation is False


def test_run_audit_metrics_computation(monkeypatch: pytest.MonkeyPatch) -> None:
    # Construct 4 controlled cases: 2 positive, 2 negative
    c1 = AuditCase(
        case_id="tp",
        text="tum bot ho",
        is_accusation=True,
        words=[Word("tum", 1.0, 1.2), Word("bot", 1.3, 1.5)],
    )
    c2 = AuditCase(
        case_id="fn",
        text="kya tum ai ho",
        is_accusation=True,
        words=[Word("ai", 2.0, 2.2)],
    )
    c3 = AuditCase(
        case_id="tn",
        text="mausam kaisa hai",
        is_accusation=False,
        words=[Word("mausam", 3.0, 3.2)],
    )
    c4 = AuditCase(
        case_id="fp",
        text="mera bot chal raha hai",
        is_accusation=False,
        words=[Word("chal", 4.0, 4.2)],
    )

    from pehchana.detection import Detection

    def mock_detect(words: list[Word]) -> list[Detection]:
        # Detect for c1 (TP) and c4 (FP)
        if any(w.text == "tum" for w in words):
            return [Detection(at_s=1.0, phrase="tum bot ho")]
        if any(w.text == "chal" for w in words):
            return [Detection(at_s=4.0, phrase="bot chal raha hai")]
        return []

    import pehchana.audit

    monkeypatch.setattr(pehchana.audit, "detect_accusations", mock_detect)

    report = run_audit([c1, c2, c3, c4])

    assert report.total_cases == 4
    assert report.tp == 1
    assert report.fp == 1
    assert report.tn == 1
    assert report.fn == 1

    # Precision = 1 / (1 + 1) = 0.5
    assert report.precision == 0.5
    # Recall = 1 / (1 + 1) = 0.5
    assert report.recall == 0.5
    # F1 = 0.5
    assert report.f1 == 0.5

    md = report.summary_markdown()
    assert "Detector Quality Audit Summary" in md
    assert "FALSE POSITIVE" in md
    assert "MISSED (FN)" in md
