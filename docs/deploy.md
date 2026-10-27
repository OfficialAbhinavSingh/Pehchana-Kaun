# Deploying the backend

Owner: WS1 (#9). The backend ships as one container (`Dockerfile`) that checks its
configuration, migrates the database and serves. It needs a public **HTTPS** URL (Plivo
and Bolna call back into it) and **Postgres**. The web site deploys separately (WS3-06).

## Choosing a host

Not chosen yet; record the choice in the table below. Any host that runs a Dockerfile and
offers Postgres works (Fly.io, Railway, Render, Cloud Run + a managed database, ...).
What matters:

- **Always on.** A free tier that sleeps makes Plivo time out on the first call of the day.
- **HTTPS with a stable domain.** Vendors sign and call this exact URL.
- **Postgres with backups**, and a way to run one instance during a deploy.
- **Secrets in the host's secret store**, not in the image or the repo.

| Decision | Value |
|---|---|
| Host | _to fill in_ |
| Domain (`PUBLIC_BASE_URL`) | _to fill in_ |
| Postgres | _to fill in_ |

## Environment

Set all of these as host secrets. `ENV=prod` is the image's default. In production the
app **refuses to boot** (and `pk check-config` fails) while any of the first block is
wrong, so a half-configured deploy never serves callers.

| Variable | Value |
|---|---|
| `DATABASE_URL` | The host's Postgres URL. `postgres://` and `postgresql://` are accepted and use the `psycopg` driver we ship |
| `PUBLIC_BASE_URL` | `https://<your domain>`, no trailing path. Vendors sign this URL |
| `ADMIN_TOKEN` | `openssl rand -hex 32`. At least 16 characters, never reused from dev |
| `CALLER_HASH_SALT` | `openssl rand -hex 32`. Changing it later breaks first-call-only stats, so set once |
| `BOLNA_SHARED_SECRET` | `openssl rand -hex 32`, then put the same value on the Bolna agents |
| `PLIVO_AUTH_TOKEN`, `PLIVO_AUTH_ID`, `PLIVO_NUMBER` | From the Plivo console (#1) |
| `INCLUDE_DEMO_DATA` | `false` (the check refuses `true`) |
| `CORS_ORIGINS` | `["https://<the site's domain>"]` (a warning if it is only localhost) |
| `CONSENT_AUDIO_URL` | Hosted consent mp3 (#7). Without it callers hear text-to-speech |
| `BOLNA_API_KEY` | Needed for browser games |
| `BOLNA_AGENT_ID_*`, `BOLNA_NUMBER_*`, `HUMAN_ARM_NUMBERS` | Arms, see `.env.example` |
| `REVEAL_VENDORS` | `false` until the team decides to name vendors |
| `RECORDING_HOST_ALLOWLIST` | Confirm on the first real call (#2) |

Check them from your laptop before pushing: export the host's values, then run
`cd backend && uv run pk check-config`.

## What the container does

`backend/start.sh` runs, in order:

1. `pk check-config` stops here on dev secrets, an `http://` base URL, SQLite, and so on.
2. `pk migrate` brings the schema to the latest Alembic revision (an empty database is
   built, a pre-Alembic one is stamped and upgraded keeping its rows).
3. `uvicorn pehchana.main:app --proxy-headers`, on `$PORT` (default 8000).

So a deploy either brings the schema up to date or never starts. Run **one instance**
while deploying: two starting together would migrate at the same time.

`FORWARDED_ALLOW_IPS=*` is set in the image so `/webcall/session` limits each real
client and not the host's proxy (without it every caller shares one bucket and the site
would stop at 3 browser games per 10 minutes). That is only safe because the host's proxy
is the only thing that can reach the container. Never publish the container's port
directly. The limits are per process, so keep one worker unless you accept N times the
limits.

## First deploy

1. Create Postgres and set the environment above.
2. Build and release the image: `make docker-build`, or let the host build from the repo
   root `Dockerfile` (the build context is the repo root, because `bolna/arms.yaml` is
   read from beside `backend/`).
3. `curl https://<domain>/healthz` returns `{"status":"ok",...}` (it also touches the DB).
4. Point the Plivo Application's answer URL at `https://<domain>/telephony/plivo/answer`
   (method POST). The dial-status and recording callbacks come from the answer XML, built
   from `PUBLIC_BASE_URL`, so nothing else is configured on Plivo.
5. Point the Bolna agents' webhook and function URLs at `https://<domain>/bolna/webhook`
   and `https://<domain>/bolna/fn/accuse`, with `BOLNA_SHARED_SECRET` as their secret
   (WS2 owns those routes; `pk sync-agents` will set them).
6. Rehearse: `pk simulate-call --target https://<domain> --calls 8` (needs the same
   `PLIVO_AUTH_TOKEN` and `PUBLIC_BASE_URL` exported). Its calls are stored as DEMO and
   never reach the stats.
7. Make one real call and read the row in Postgres.

## Updating

Deploy the new image: the entrypoint migrates before serving. Take a Postgres backup or
snapshot first when a release adds a revision. To roll back, redeploy the previous image;
only run `alembic downgrade` if the new revision broke the schema, and read the
revision's docstring first (0002 drops the ids of non-Plivo calls on the way down).

## Tested

`tests/test_migrations.py` runs on SQLite, and on Postgres when `TEST_POSTGRES_URL` is
set (CI does; locally `make test-postgres` uses the docker-compose database and wipes its
public schema). That covers a fresh upgrade matching the models, a pre-Alembic database
keeping its rows, and a full upgrade/downgrade/upgrade round trip including Postgres enum
types. The image itself is built by the host, not in CI.
