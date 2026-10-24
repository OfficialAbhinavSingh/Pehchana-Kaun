"""Operator CLI: ``uv run pk --help``."""

import typer

app = typer.Typer(no_args_is_help=True, help="Pehchana Kaun? operator commands")


@app.command()
def migrate() -> None:
    """Create or upgrade the database schema to the latest Alembic revision."""
    from pehchana.migrate import upgrade

    upgrade()
    typer.echo("database is up to date")


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


@app.command("sync-agents")
def sync_agents() -> None:
    """Create/update one Bolna agent per AI arm from bolna/agents/*.json. TODO(WS2)"""
    raise typer.Exit(code=_todo("WS2"))


@app.command()
def process(call_id: str) -> None:
    """Re-run post-call processing for one call. TODO(WS2)"""
    raise typer.Exit(code=_todo("WS2"))


def _todo(owner: str) -> int:
    typer.echo(f"not implemented yet ({owner})", err=True)
    return 1


if __name__ == "__main__":
    app()
