# Pehchana Kaun?

**India's first public phone-line Turing test for voice AI.** Call a number, chat for
two minutes, and the moment you think you're talking to a bot, say *"tum bot ho!"*.
Sometimes it's a real person, sometimes it's an AI voice agent. We measure how many
seconds each AI voice survives before a real Indian caller catches it, what gave it
away, and how that changes by language.

Built by **Pehchaano Labs** (team of 3) for the [Bolna Symphony Buildathon](https://www.bolna.ai/symphony/buildathon)
(submissions close **31 Oct 2026**; finale 20 Nov 2026, Bengaluru).

**Play it live:** [pehchana-kaun.vercel.app](https://web-ten-mu-42.vercel.app) (browser call, no
phone number needed) · API: [pehchana-api.onrender.com](https://pehchana-api.onrender.com/healthz)

> Status: **built and deployed**. Routing, three AI voice arms (Kalpa / Cartesia /
> Sarvam), detection, giveaway tagging, and the public leaderboard are live. The
> browser-call path works end to end against production. The dial-in phone number
> is wired up but outbound calls from our Plivo account to Indian numbers are
> currently geo-barred by Plivo — pending their support. Start with
> [docs/plan.md](docs/plan.md).

## How it works

```
caller ──► Plivo number ──► our router (FastAPI) ──► one random arm
                                │                     ├─ human volunteer (control)
                                │                     └─ AI arm = Bolna agent
                                │                        (Kalpa / Cartesia / Sarvam voice)
                                ▼
                 stereo recording ──► Deepgram ──► "tum bot ho" detector ──► Turing Clock
                                                                  └─► giveaway tags (Claude)
                                                                        └─► public leaderboard (Next.js)
```

Details: [docs/architecture.md](docs/architecture.md). Metric definitions:
[docs/metrics.md](docs/metrics.md). Consent and data handling:
[docs/ethics.md](docs/ethics.md).

## Repo layout

| Path | What | Owner |
|---|---|---|
| `backend/` | FastAPI app: telephony webhooks, routing, Bolna callbacks, processing, stats API | all |
| `backend/src/pehchana/arms.py`, `telephony/`, `api/telephony.py` | Call routing and Plivo flow | WS1 |
| `backend/src/pehchana/integrations/`, `detection.py`, `tagging.py`, `pipeline.py`, `api/bolna.py` | Bolna agents, transcription, detection, tagging | WS2 |
| `backend/src/pehchana/scoring.py`, `api/leaderboard.py`, `api/webcall.py`, `web/` | Stats, website, web-call fallback, launch | WS3 |
| `bolna/` | Arms config, agent template, `accuse_bot` function, personas | WS2 |
| `docs/` | Context, architecture, plan, metrics, ethics, pitch | all |
| `docs/research/` | Full research notes with source links (hackathon, Bolna, judges, sponsors, competitors) | read-only |

## Quickstart (run it yourself)

Prereqs: Python 3.12+ with [uv](https://docs.astral.sh/uv/), Node 20+ with pnpm,
Docker (optional, for Postgres).

```bash
cp .env.example .env          # fill in what you have; everything is optional for local dev
make setup                    # uv sync + pnpm install
make dev-api                  # http://localhost:8000/docs  (SQLite by default)
make dev-web                  # http://localhost:3000
make check                    # lint + types + tests, same as CI
```

Plivo and Bolna need to reach your laptop: run a tunnel (`cloudflared tunnel --url
http://localhost:8000` or `ngrok http 8000`) and set `PUBLIC_BASE_URL` to it.

## Team workflow

Read [CONTRIBUTING.md](CONTRIBUTING.md). Short version: branch from `main`, small PRs,
signed commits, CI green, one review from another workstream before merge.

## Credits

"Turing Clock" is [Kalpa Labs' proposed metric](https://kalpalabs.ai/blog/towards-generalist-audio-models)
(how long a person can talk to a model before reliably telling it's an AI). This
project builds a public, phone-based version of it for Indian languages.

## License

[MIT](LICENSE) © 2026 Pehchaano Labs
