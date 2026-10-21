# AGENTS.md

Context for AI coding assistants (Claude Code, Codex, Cursor) working in this repo.

## What this is

"Pehchana Kaun?" is a phone game for the Bolna Symphony Buildathon (submit by
2026-10-31). Callers chat with either a human volunteer or an AI voice agent and say
"tum bot ho!" when they think it's a bot. We measure seconds-to-detection per voice
stack and language (the "Turing Clock", a term coined by Kalpa Labs). Read in order:
`README.md`, `docs/context.md`, `docs/architecture.md`, `docs/plan.md`.

## Commands

```bash
make setup        # install backend (uv) + web (pnpm) deps
make dev-api      # FastAPI on :8000 (SQLite by default)
make dev-web      # Next.js on :3000
make check        # everything CI runs
cd backend && uv run pytest -k <name>
```

## Rules

- Backend: Python 3.12, FastAPI, SQLAlchemy 2, pydantic-settings. `ruff` + `mypy --strict`
  must pass. Use `SessionDep` from `pehchana.api.deps` for DB sessions.
- Web: Next.js 16 (App Router, Cache Components on). Read `web/AGENTS.md` first: this
  Next.js version differs from older training data.
- Stubs raise `NotImplementedError` and name an owner (`TODO(WS1)`). Implement against
  the docstring and the spec in `backend/tests/test_specs.py`. Don't change a shared
  contract (`models.py`, `bolna/arms.yaml`, `web/src/lib/api.ts`, route shapes)
  without saying so in the PR.
- Bolna API facts that break generated code are listed at the top of
  `backend/src/pehchana/integrations/bolna.py`. Trust those over memory.
- LLM calls (giveaway tagging) use the official Anthropic SDK with structured outputs;
  see the `tagging.py` docstring.
- Never commit secrets, phone numbers or call recordings. Never log raw caller numbers;
  hash with `CALLER_HASH_SALT`.
- Commits: Conventional Commits, signed, and **no `Co-Authored-By` trailers** for AI tools.
