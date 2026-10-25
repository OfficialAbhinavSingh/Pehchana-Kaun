"""The numbers sheet for the pitch (#28), computed from a data-freeze snapshot.

Every Turing Clock figure comes from ``build_leaderboard`` on the snapshot, the same
code as the live site, so a number on a slide can be traced to the leaderboard rules
in docs/metrics.md. Demo rows never count here, whatever INCLUDE_DEMO_DATA says.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Sequence
from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

from pehchana.api.leaderboard import ArmStatsOut, build_leaderboard, top_tags
from pehchana.arms import ArmLabel
from pehchana.config import Settings
from pehchana.snapshot import CallRow, load_snapshot

IST = ZoneInfo("Asia/Kolkata")


def _clock(seconds: float | None) -> str:
    if seconds is None:
        return "-"
    whole = round(seconds)
    return f"{whole // 60}:{whole % 60:02d}"


def _pct(share: float | None) -> str:
    return "-" if share is None else f"{share:.0%}"


def _turing_clock(arm: ArmStatsOut) -> str:
    if arm.median_turing_clock_s is None:
        if arm.max_observed_s is None:
            return "-"
        return f"> {_clock(arm.max_observed_s)} (not reached)"
    text = _clock(arm.median_turing_clock_s)
    if arm.median_ci_low_s is not None and arm.median_ci_high_s is not None:
        text += f" ({_clock(arm.median_ci_low_s)} to {_clock(arm.median_ci_high_s)})"
    return text


def _arm_table(arms: Iterable[ArmStatsOut]) -> list[str]:
    lines = [
        "| Voice | n | Caught | Turing Clock (95% CI) | Fooled at 60 s | Ranked |",
        "|---|---|---|---|---|---|",
    ]
    for a in arms:
        if a.kind == "human":
            continue
        lines.append(
            f"| {a.display_name} | {a.n_calls} | {_pct(a.accusation_rate)} | "
            f"{_turing_clock(a)} | {_pct(a.fooled_at_60s)} | {'yes' if a.ranked else 'no'} |"
        )
    return lines


def _human(arms: Sequence[ArmStatsOut]) -> str:
    """The false-accusation rate: how often callers called the real person a bot."""
    human = next((a for a in arms if a.kind == "human"), None)
    if human is None or human.n_calls == 0:
        return "no human-arm calls"
    return f"{_pct(human.accusation_rate)} of {human.n_calls} calls"


def _counted(row: CallRow) -> bool:
    """The calls the headline counts: real, phone, processed."""
    return (row["source"], row["channel"], row["status"]) == ("real", "phone", "processed")


def _short_and_silent(row: CallRow, short_call_s: float) -> bool:
    """Ended before ``short_call_s`` with no accusation: the caller never really played."""
    return not row["accusations"] and (row["duration_s"] or 0.0) < short_call_s


def numbers_sheet(
    data: dict[str, Any],
    labels: Sequence[ArmLabel],
    settings: Settings,
    *,
    short_call_s: float = 10.0,
) -> str:
    """Markdown with every number the deck may use, from one snapshot."""
    settings = settings.model_copy(update={"include_demo_data": False})
    session = load_snapshot(data)
    board = build_leaderboard(session, settings, labels)
    first = build_leaderboard(session, settings, labels, first_call_only=True)
    trimmed = build_leaderboard(
        load_snapshot(data, keep=lambda r: not _short_and_silent(r, short_call_s)),
        settings,
        labels,
    )

    rows: list[CallRow] = data["calls"]
    real = [r for r in rows if r["source"] == "real"]
    known = {label.id for label in labels}
    counted = [r for r in real if _counted(r) and r["arm_id"] in known]
    per_caller = Counter(r["caller_hash"] for r in counted if r["caller_hash"])
    repeat = Counter(min(n, 3) for n in per_caller.values())
    per_day = Counter(
        datetime.fromisoformat(r["started_at"]).astimezone(IST).date().isoformat() for r in counted
    )
    ai_ids = {label.id for label in labels if label.kind == "ai"}
    tags = Counter(g["tag"] for r in counted if r["arm_id"] in ai_ids for g in r["giveaways"])
    web = [r for r in real if r["channel"] == "web" and r["status"] == "processed"]
    web_caught = sum(any(a["source"] == "function" for a in r["accusations"]) for r in web)
    short = sum(_short_and_silent(r, short_call_s) for r in counted)

    out = [
        "# Pehchana Kaun? numbers sheet",
        "",
        f"Snapshot exported {data['exported_at']}. Real calls only; demo rows ignored "
        f"({sum(r['source'] == 'demo' for r in rows)} in the file). "
        f"Ranking needs {settings.min_calls_for_ranking} calls.",
        "",
        "## Headline",
        "",
        f"- Calls counted (real, phone, processed): **{board.total_calls}**",
        f"- Unique callers: **{len(per_caller)}**, plus "
        f"{sum(not r['caller_hash'] for r in counted)} calls with no caller id",
        f"- All real calls in the file: {len(real)} "
        f"({', '.join(f'{k} {v}' for k, v in sorted(Counter(r['status'] for r in real).items()))})",
        f"- Human called a bot by mistake: **{_human(board.arms)}**",
        "",
        "## Turing Clock per voice (all calls)",
        "",
        *_arm_table(board.arms),
        "",
        "## Check: first call per caller only",
        "",
        f"Human called a bot by mistake: {_human(first.arms)}.",
        "",
        *_arm_table(first.arms),
        "",
        f"## Check: without calls under {short_call_s:g} s that ended with no accusation",
        "",
        f"{short} such calls dropped. Human called a bot by mistake: {_human(trimmed.arms)}.",
        "",
        *_arm_table(trimmed.arms),
        "",
        "## By language",
        "",
    ]
    for language, arms in board.by_language.items():
        out += [f"### {language}", "", f"Human called a bot: {_human(arms)}", ""]
        out += [*_arm_table(arms), ""]
    out += [
        "## Top giveaways (AI voices)",
        "",
        *([f"- {tag}: {n}" for tag, n in top_tags(tags)] if tags else ["- none tagged"]),
        "",
        "## Repeat callers",
        "",
        f"- 1 call: {repeat[1]} callers, 2 calls: {repeat[2]}, 3 or more: {repeat[3]}",
        "",
        "## Calls per day (IST)",
        "",
        *([f"- {day}: {n}" for day, n in sorted(per_day.items())] or ["- none"]),
        "",
        "## Browser games (not in the numbers above)",
        "",
        f"- Processed: {len(web)}; ended with a live `accuse_bot` call: {web_caught}",
        "",
    ]
    return "\n".join(out)
