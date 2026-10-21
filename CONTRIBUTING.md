# Contributing

Three people, ten days, one `main`. These rules keep us from stepping on each other.

## Workstreams

| WS | Name | Owns |
|---|---|---|
| WS1 | Calls | Plivo number, routing, answer/dial/recording webhooks, human-arm shifts, backend deploy |
| WS2 | Agents & analysis | Bolna agents + personas, `accuse_bot`, Bolna webhook, Deepgram, detection, tagging, pipeline |
| WS3 | Web, stats & launch | Turing Clock stats, leaderboard API, website, web-call fallback, launch, deck + video |

Who is on which workstream: see the table at the top of [docs/plan.md](docs/plan.md).
Each stub in the code says its owner (`TODO(WS1)` etc.). Touching another
workstream's module is fine, just tag its owner on the PR.

## Branches and PRs

- Branch from `main`: `ws1/plivo-answer-xml`, `ws2/detector`, `ws3/leaderboard-page`.
- Keep PRs small (one feature or fix). Draft PRs early are welcome.
- Fill in the PR template, including **how you tested it** (a real test call counts).
- CI must be green. One approval from someone on a different workstream, then the
  author merges with **squash merge**.
- Changing a shared contract (`models.py`, `arms.yaml`, `web/src/lib/api.ts`,
  any API route shape)? Say so in the PR title, e.g. `feat(contract): ...`.

## Commits

- [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`,
  `docs:`, `test:`, `chore:`, `refactor:`.
- **Signed commits** (`git config commit.gpgsign true` with a GPG or SSH signing key).
- No `Co-Authored-By` trailers for AI tools.

## Secrets and data

- Never commit `.env`, API keys, phone numbers or call recordings. `.gitignore`
  covers the usual paths; double-check `git status` before committing.
- Volunteer phone numbers go only in env vars (`HUMAN_ARM_NUMBERS`).
- Real call data stays in the database, never in the repo, issues or screenshots.
  Use the demo seed for screenshots. See [docs/ethics.md](docs/ethics.md).

## Local checks

```bash
make check      # backend: ruff, mypy, pytest | web: eslint, tsc, next build
```

`backend/tests/test_specs.py` holds executable specs for the stubs, marked `xfail`
until implemented. When you implement a stub, its spec must pass; add more cases
from real test calls.
