"""Operator CLI: ``uv run pk --help``."""

import typer

app = typer.Typer(no_args_is_help=True, help="Pehchana Kaun? operator commands")


@app.command()
def migrate() -> None:
    """Create or upgrade the database schema to the latest Alembic revision."""
    from pehchana.migrate import upgrade

    upgrade()
    typer.echo("database is up to date")


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
