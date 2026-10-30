"""Operator CLI: ``uv run pk --help``."""

from pathlib import Path
from typing import Annotated

import typer

from pehchana.simulate import SCENARIOS, Simulator, UnknownDialect, get_dialect, verify_db

app = typer.Typer(no_args_is_help=True, help="Pehchana Kaun? operator commands")


@app.command()
def migrate() -> None:
    """Create or upgrade the database schema to the latest Alembic revision."""
    from pehchana.migrate import upgrade

    upgrade()
    typer.echo("database is up to date")


@app.command("check-consent")
def check_consent(
    allow_tts: bool = typer.Option(
        False, help="Accept an unset CONSENT_AUDIO_URL (callers hear the text-to-speech fallback)."
    ),
) -> None:
    """Fetch CONSENT_AUDIO_URL the way the vendor will and report what is wrong with it."""
    from pehchana.config import get_settings
    from pehchana.consent import check_consent_audio

    url = get_settings().consent_audio_url
    if not url:
        if allow_tts:
            typer.echo("no recorded notice set: callers hear the text-to-speech fallback")
            return
        typer.echo("error: CONSENT_AUDIO_URL is unset (record the notice, #7)", err=True)
        raise typer.Exit(code=1)
    result = check_consent_audio(url)
    for problem in result.problems:
        typer.echo(f"error: {problem}", err=True)
    if not result.ok:
        raise typer.Exit(code=1)
    typer.echo(f"consent audio reachable: {result.content_type}, {result.size:,} bytes")
    typer.echo("now listen to it and time it: docs/consent-audio.md")


@app.command("check-config")
def check_config() -> None:
    """Check the environment is safe to serve real callers (run before a deploy).

    Judges the settings as production settings whatever ENV says, so it works from a
    laptop: ``ENV=... pk check-config`` with the host's variables exported.
    """
    from pehchana.config import get_settings

    settings = get_settings()
    for warning in settings.production_warnings():
        typer.echo(f"warning: {warning}", err=True)
    problems = settings.production_problems()
    for problem in problems:
        typer.echo(f"error: {problem}", err=True)
    if problems:
        raise typer.Exit(code=1)
    typer.echo("configuration is fit for production")


@app.command("seed-demo")
def seed_demo(
    n: int = typer.Option(200, "--n", help="How many demo calls to insert."),
    seed: int = typer.Option(7, help="Random seed, so screenshots are reproducible."),
    keep: bool = typer.Option(False, help="Keep existing demo calls instead of replacing them."),
    force: bool = typer.Option(False, help="Allow seeding outside ENV=dev/test."),
) -> None:
    """Insert synthetic DEMO calls for UI work (shown only with INCLUDE_DEMO_DATA=true)."""
    import random

    from pehchana.arms import load_arm_labels
    from pehchana.config import get_settings
    from pehchana.db import get_sessionmaker
    from pehchana.demo import clear_demo_calls, seed_demo_calls

    settings = get_settings()
    if settings.env not in ("dev", "test") and not force:
        typer.echo(f"refusing to seed demo data with ENV={settings.env} (use --force)", err=True)
        raise typer.Exit(code=1)
    with get_sessionmaker()() as session:
        removed = 0 if keep else clear_demo_calls(session)
        added = seed_demo_calls(
            session, load_arm_labels(settings.arms_file), n, random.Random(seed)
        )
    typer.echo(f"demo calls: {removed} removed, {added} added")


@app.command("export-snapshot")
def export_snapshot(
    out: Annotated[Path, typer.Argument(help="JSON file to write, outside the repo.")],
) -> None:
    """Data freeze: write every call (no recordings, transcripts or phrases) to OUT."""
    import hashlib
    import json

    from pehchana.config import REPO_ROOT
    from pehchana.db import get_sessionmaker
    from pehchana.snapshot import export_snapshot as export

    out = out.resolve()
    if out.is_relative_to(REPO_ROOT):
        typer.echo("refusing to write call data inside the repo; pick a path outside it", err=True)
        raise typer.Exit(code=1)
    with get_sessionmaker()() as session:
        data = export(session)
    text = json.dumps(data, indent=1, sort_keys=True)
    out.write_text(text)
    digest = hashlib.sha256(text.encode()).hexdigest()
    typer.echo(f"{len(data['calls'])} calls -> {out} (sha256 {digest})")


@app.command()
def numbers(
    snapshot: Annotated[Path, typer.Argument(help="File from `pk export-snapshot`.")],
    short_call_s: float = typer.Option(10.0, help="Short-call cutoff for the check table."),
) -> None:
    """Print the pitch numbers sheet (markdown) for a snapshot."""
    import json

    from pehchana.arms import load_arm_labels
    from pehchana.config import get_settings
    from pehchana.numbers import numbers_sheet

    settings = get_settings()
    data = json.loads(snapshot.read_text())
    labels = load_arm_labels(settings.arms_file)
    typer.echo(numbers_sheet(data, labels, settings, short_call_s=short_call_s))


@app.command("simulate-call")
def simulate_call(
    target: str = typer.Option(
        "http://localhost:8000",
        help="Backend to send the webhooks to (its PUBLIC_BASE_URL is signed).",
    ),
    provider: str | None = typer.Option(
        None, help="Telephony vendor to imitate (default: TELEPHONY_PROVIDER)."
    ),
    scenario: str = typer.Option("all", help="all, or one of: " + ", ".join(SCENARIOS)),
    calls: int = typer.Option(
        1, min=1, help="How many times to run the happy path (arm coverage)."
    ),
    check_db: bool = typer.Option(
        False, help="Also check the rows in DATABASE_URL (same database as the backend)."
    ),
) -> None:
    """Rehearse the phone flow with signed fake Plivo webhooks. See docs/runbook.md."""
    import httpx

    from pehchana.arms import load_arms
    from pehchana.config import arm_env, get_settings
    from pehchana.db import get_sessionmaker

    settings = get_settings()
    if scenario != "all" and scenario not in SCENARIOS:
        typer.echo(f"unknown scenario {scenario!r}", err=True)
        raise typer.Exit(code=2)
    try:
        dialect = get_dialect(provider or settings.telephony_provider)
    except UnknownDialect as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(code=2) from e
    if not dialect.token(settings):
        typer.echo(
            f"no {dialect.name} signing token is set: the webhooks cannot be signed", err=True
        )
        raise typer.Exit(code=2)
    arms = load_arms(settings.arms_file, arm_env())
    names = list(SCENARIOS) if scenario == "all" else [scenario]
    plan = names + ["happy"] * (calls - 1) if "happy" in names else names
    reports = []
    with httpx.Client(base_url=target, timeout=15) as client:
        sim = Simulator(client, settings, arms, dialect)
        for name in plan:
            try:
                reports.append(sim.run(name))
            except httpx.HTTPError as e:
                typer.echo(f"cannot reach {target}: {e}", err=True)
                raise typer.Exit(code=2) from e
    if check_db:
        with get_sessionmaker()() as session:
            for report in reports:
                verify_db(session, report)
    for report in reports:
        typer.echo(
            f"{'ok  ' if report.ok else 'FAIL'} {report.scenario}"
            + (f"  arm={report.arm_id}" if report.arm_id else "")
        )
        for step in report.steps:
            if not step.ok:
                typer.echo(f"       - {step.name}: {step.detail}")
    seen = {r.arm_id for r in reports if r.arm_id}
    missing = [a.id for a in arms if a.id not in seen]
    if missing and any(r.scenario == "happy" for r in reports):
        hint = (
            " The human arm only answers inside its live hours or with an admin override."
            if "human" in missing
            else ""
        )
        typer.echo(
            f"arms not reached in this run: {', '.join(missing)} (run more with --calls).{hint}"
        )
    if not all(r.ok for r in reports):
        raise typer.Exit(code=1)


@app.command("sync-agents")
def sync_agents(
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Print the rendered JSON without calling Bolna."
    ),
) -> None:
    """Create or update one Bolna agent per AI arm from bolna/arms.yaml."""
    import json
    import os

    from pehchana.arms import _read_arms_file
    from pehchana.config import REPO_ROOT, arm_env, get_settings
    from pehchana.integrations.bolna import BolnaClient, build_agent_payload

    settings = get_settings()
    arms = [a for a in _read_arms_file(settings.arms_file) if a.get("kind") == "ai"]
    if not arms:
        typer.echo("no AI arms found in arms.yaml")
        return

    persona_path = REPO_ROOT / "bolna" / "personas" / "priya-pune.md"
    accuse_path = REPO_ROOT / "bolna" / "functions" / "accuse_bot.json"

    persona_prompt = persona_path.read_text(encoding="utf-8")
    accuse_tool = json.loads(accuse_path.read_text(encoding="utf-8"))

    if not dry_run and not settings.bolna_api_key:
        typer.echo("error: BOLNA_API_KEY is not set in environment or .env", err=True)
        raise typer.Exit(code=2)

    client = BolnaClient(settings.bolna_api_key, settings.bolna_base_url)
    current_env = arm_env()

    for arm in arms:
        arm_id = arm["id"]
        env_var_name = str(arm.get("bolna_agent_id_env") or "")
        existing_id = (
            (current_env.get(env_var_name) or os.environ.get(env_var_name))
            if env_var_name
            else None
        )

        payload = build_agent_payload(
            arm,
            public_base_url=settings.public_base_url,
            bolna_shared_secret=settings.bolna_shared_secret,
            persona_prompt=persona_prompt,
            accuse_tool=accuse_tool,
        )

        if dry_run:
            typer.echo(f"=== {arm_id} ({env_var_name}={existing_id or '<unset>'}) ===")
            typer.echo(json.dumps(payload, indent=2))
            continue

        try:
            if existing_id:
                client.update_agent(existing_id, payload)
                typer.echo(f"updated {arm_id}: {existing_id}")
            else:
                new_id = client.create_agent(payload)
                typer.echo(f"created {arm_id}: {env_var_name}={new_id}")
        except Exception as e:
            typer.echo(f"error syncing {arm_id}: {e}", err=True)
            raise typer.Exit(code=1) from e


@app.command()
def process(
    call_id: str = typer.Argument(None, help="A single call to (re)process."),
    all_failed: bool = typer.Option(
        False, "--all-failed", help="Rerun every call that previously failed processing."
    ),
) -> None:
    """(Re-)run post-call processing: Deepgram, accusation detection, status=processed."""
    if bool(call_id) == all_failed:
        typer.echo("error: pass exactly one of CALL_ID or --all-failed", err=True)
        raise typer.Exit(code=2)

    from pehchana import pipeline
    from pehchana.db import get_sessionmaker

    with get_sessionmaker()() as session:
        try:
            calls = (
                pipeline.process_all_failed(session)
                if all_failed
                else [pipeline.process_call(call_id, session=session)]
            )
        except LookupError as e:
            typer.echo(f"error: {e}", err=True)
            raise typer.Exit(code=2) from e
    if not calls:
        typer.echo("nothing to process")
        return
    for call in calls:
        ok = call.processing_error is None
        detail = "" if ok else f": {call.processing_error}"
        typer.echo(f"{'ok  ' if ok else 'FAIL'} {call.id}{detail}")
    if any(c.processing_error is not None for c in calls):
        raise typer.Exit(code=1)


@app.command("audit-detector")
def audit_detector(
    dataset: Annotated[
        Path | None,
        typer.Option(
            "--dataset",
            "-d",
            help="Path to an eval JSON dataset (default: tests/data/detector_cases.json).",
        ),
    ] = None,
) -> None:
    """Run detector accuracy audit (precision, recall, F1, and misclassifications)."""
    from pehchana.audit import load_audit_cases, run_audit

    tests_dir = Path(__file__).resolve().parent.parent.parent / "tests"
    eval_path = dataset or tests_dir / "data" / "detector_cases.json"
    if not eval_path.exists():
        typer.echo(f"audit dataset not found at {eval_path}", err=True)
        raise typer.Exit(code=2)

    cases = load_audit_cases(eval_path)
    report = run_audit(cases)
    typer.echo(report.summary_markdown())


def _todo(owner: str) -> int:
    typer.echo(f"not implemented yet ({owner})", err=True)
    return 1


if __name__ == "__main__":
    app()
