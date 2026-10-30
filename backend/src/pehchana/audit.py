"""Detector audit loop and evaluation tooling for real and test calls.

Owner: WS2 (WS2-10).
Measures detector precision and recall across real calls and benchmark evaluation suites,
flagging false positives and false negatives to keep measurement honest for judges.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pehchana.detection import Word, detect_accusations


@dataclass(frozen=True)
class AuditCase:
    case_id: str
    text: str
    is_accusation: bool
    words: Sequence[Word]
    expected_phrase: str | None = None
    expected_at_s: float | None = None


@dataclass(frozen=True)
class CaseResult:
    case: AuditCase
    detected: bool
    detected_at_s: float | None
    detected_phrase: str | None
    is_tp: bool
    is_fp: bool
    is_tn: bool
    is_fn: bool


@dataclass(frozen=True)
class AuditReport:
    total_cases: int
    tp: int
    fp: int
    tn: int
    fn: int
    precision: float
    recall: float
    f1: float
    results: list[CaseResult]

    def summary_markdown(self) -> str:
        """Render a readable markdown summary of audit metrics."""
        pos_denom = self.tp + self.fp
        rec_denom = self.tp + self.fn
        prec_str = f"{self.tp}/{pos_denom}" if pos_denom > 0 else "0/0"
        rec_str = f"{self.tp}/{rec_denom}" if rec_denom > 0 else "0/0"
        lines = [
            "### Detector Quality Audit Summary",
            f"- **Total Sampled**: {self.total_cases}",
            f"- **True Positives (TP)**: {self.tp}",
            f"- **False Positives (FP)**: {self.fp}",
            f"- **True Negatives (TN)**: {self.tn}",
            f"- **False Negatives (FN)**: {self.fn}",
            f"- **Precision**: {self.precision:.1%} ({prec_str})",
            f"- **Recall**: {self.recall:.1%} ({rec_str})",
            f"- **F1 Score**: {self.f1:.3f}",
        ]
        failures = [r for r in self.results if r.is_fp or r.is_fn]
        if failures:
            lines.append("\n#### Misclassifications:")
            for f in failures:
                label = "FALSE POSITIVE" if f.is_fp else "MISSED (FN)"
                lines.append(
                    f'- [{label}] `{f.case.case_id}`: "{f.case.text}" '
                    f"(detected: {f.detected_phrase} @ {f.detected_at_s}s)"
                )
        else:
            lines.append("\nZero misclassifications found on audited sample.")
        return "\n".join(lines)


def load_audit_cases(path: Path) -> list[AuditCase]:
    """Load audit evaluation cases from a JSON file."""
    data: list[dict[str, Any]] = json.loads(path.read_text(encoding="utf-8"))
    cases: list[AuditCase] = []
    for item in data:
        words = [
            Word(
                text=str(w["text"]),
                start=float(w["start"]),
                end=float(w["end"]),
            )
            for w in item.get("words", [])
        ]
        cases.append(
            AuditCase(
                case_id=str(item["id"]),
                text=str(item.get("text", "")),
                is_accusation=bool(item.get("is_accusation", False)),
                expected_phrase=item.get("expected_phrase"),
                expected_at_s=float(item["expected_at_s"])
                if item.get("expected_at_s") is not None
                else None,
                words=words,
            )
        )
    return cases


def run_audit(cases: Sequence[AuditCase]) -> AuditReport:
    """Evaluate detector accuracy across a collection of audit cases."""
    results: list[CaseResult] = []
    tp = fp = tn = fn = 0

    for case in cases:
        try:
            detections = detect_accusations(case.words)
        except NotImplementedError:
            # Detector stub in progress
            detections = []

        has_detection = len(detections) > 0
        detected_at = detections[0].at_s if has_detection else None
        detected_phrase = detections[0].phrase if has_detection else None

        is_tp = bool(case.is_accusation and has_detection)
        is_fp = bool(not case.is_accusation and has_detection)
        is_tn = bool(not case.is_accusation and not has_detection)
        is_fn = bool(case.is_accusation and not has_detection)

        if is_tp:
            tp += 1
        elif is_fp:
            fp += 1
        elif is_tn:
            tn += 1
        elif is_fn:
            fn += 1

        results.append(
            CaseResult(
                case=case,
                detected=has_detection,
                detected_at_s=detected_at,
                detected_phrase=detected_phrase,
                is_tp=is_tp,
                is_fp=is_fp,
                is_tn=is_tn,
                is_fn=is_fn,
            )
        )

    prec = tp / (tp + fp) if (tp + fp) > 0 else 1.0 if fp == 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 1.0 if fn == 0 else 0.0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

    return AuditReport(
        total_cases=len(cases),
        tp=tp,
        fp=fp,
        tn=tn,
        fn=fn,
        precision=prec,
        recall=rec,
        f1=f1,
        results=results,
    )
