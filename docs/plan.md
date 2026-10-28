# Plan: 23 to 31 Oct 2026

The task-level plan lives in GitHub issues: start from the pinned
[Roadmap issue #31](https://github.com/OfficialAbhinavSingh/Pehchana-Kaun/issues/31).
Each issue has steps, acceptance criteria, dependencies and the PR workflow.

## Team: Pehchaano Labs

| Workstream | Person | Owns |
|---|---|---|
| WS1 Calls | Mahak (@mahakagarwal7) | Plivo number, routing, Plivo webhooks, human-arm shifts, backend deploy |
| WS2 Agents & analysis | Soham (@Aspirant200715) | Bolna agents + persona, `accuse_bot`, Bolna webhook, Deepgram, detection, tagging |
| WS3 Web, stats & launch | Abhinav (@OfficialAbhinavSingh) | Kaplan-Meier stats, leaderboard API, website, web-call fallback, launch, deck + video |

Daily: 15-minute sync (blockers only), everyone posts one line in the team chat at
night: done / next / blocked.

## Milestones

| Due (IST, end of day) | Milestone | Proof |
|---|---|---|
| **24 Oct** | M0 · Unknowns resolved | Phone number decided, Bolna bridge tested, caller channel + Deepgram params known |
| **26 Oct** | M1 · First call scored end-to-end | One `processed` call with an accusation time, visible in `/leaderboard` |
| **27 Oct** | **M2 · Public launch** | Number + site live, consent in place, first posts out |
| **29 Oct** | M3 · Data freeze | Numbers and consented clips for the pitch exported |
| **31 Oct, before noon** | M4 · Submitted | Confirmation screenshot in team chat |

Dates moved one day from the first draft because work started on 23 Oct.

## Day 1 (23 to 24 Oct): kill the unknowns

Everyone:
- [ ] Join Bolna Builders Slack. Request credits (form).
- [ ] `make setup && make check` passes on your machine.

WS1:
- [ ] Plivo account; find out if an Indian inbound number needs DLT/company docs. If
      blocked in 4 hours, switch plan: web-call first, phone later (tell WS3).
- [ ] Tunnel to local backend; hard-coded answer XML that dials one teammate's phone.
- [ ] Record a test call, find which stereo channel is the caller.

WS2:
- [x] First-agent spike for [issue #11](https://github.com/OfficialAbhinavSingh/Pehchana-Kaun/issues/11): Bolna Kalpa phone agent built with an inbound number, tested across real phone calls, listening notes posted, and reference export saved to `bolna/agents/reference-dashboard-export.json`.
- [ ] Deepgram on a test recording: are word timestamps sane on 8 kHz Hinglish audio?

WS3:
- [ ] Draft the landing page copy + leaderboard wireframe (paper is fine).
- [ ] Write the launch plan: which groups/posts, who posts when (target 300+ calls).
- [ ] Re-read `docs/context.md` "what the panel rewards" and draft pitch outline.

## Day 2 to 4 (24 to 26 Oct): make one call fully work

WS1 (`arms.py`, `telephony/plivo.py`, `api/telephony.py`, `api/admin.py`):
- [ ] `load_arms`, `eligible_arms`, `choose_arm` + their specs passing.
- [ ] `/answer` (signature check, Call row, consent, record, dial), `/dial-status`, `/recording`.
- [ ] Consent mp3 recorded by a teammate (Hindi + English), hosted.
- [ ] Human arm: volunteers' numbers via env, live hours, `/admin/shift`.
- [ ] Deploy backend to a stable HTTPS URL + Postgres; Alembic initial migration.

WS2 (`integrations/`, `detection.py`, `pipeline.py`, `tagging.py`, `api/bolna.py`, `bolna/`):
- [ ] Persona prompt `bolna/personas/priya-pune.md` + volunteer brief (same persona).
- [ ] `pk sync-agents`: one Bolna agent per AI arm from the template.
- [ ] `/bolna/fn/accuse` (auth, log, reveal line) and `/bolna/webhook` (idempotent).
- [ ] Deepgram client, accusation detector (phrase list from real test calls), pipeline.
- [ ] Heuristic giveaway tags first; Claude tagging after the pipeline is stable.

WS3 (`scoring.py`, `api/leaderboard.py`, `api/webcall.py`, `web/`):
- [ ] Kaplan-Meier + `arm_stats` with specs passing; per-language breakdown.
- [ ] `/leaderboard` endpoint matching `web/src/lib/api.ts`; demo seed for screenshots.
- [ ] Landing page (number, how to play, consent link), leaderboard page, privacy page.
- [ ] Web-call fallback button (`@bolna/web-call` + `/webcall/session`).

## Day 5 (27 Oct): launch

- [ ] Smoke test: 10 internal calls across all arms, all processed correctly.
- [ ] Human-arm live hours staffed for the first weekend.
- [ ] Posts go out (LinkedIn, X, college groups, Bolna Slack). Track calls/hour.

## Day 6 to 7 (28 to 29 Oct): grow and learn

- [ ] Fix whatever real callers break (detection misses are the likely one).
- [ ] Language-switch round: ask some callers to switch Hindi to Tamil mid-call (Bolna LiD).
- [ ] Kalpa conversation-aware mode as an extra arm, if time.
- [ ] Re-check competitors (two buildathon repos were empty on 21 Oct).
- [ ] **29 Oct: data freeze.** Export the numbers and best (consented) clips for the pitch.

## Day 8 to 9 (30 to 31 Oct): ship the submission

- [ ] 2 to 3 minute demo video (real call, live leaderboard, one "fooled" clip).
- [ ] Deck (≤10 slides, see `docs/pitch.md`), uploaded to Google Drive.
- [ ] README updated with real numbers and screenshots.
- [ ] Submit on 31 Oct morning IST. Screenshot the confirmation.

## Definition of done (any feature)

Spec test passes, `make check` green, tested with a real or recorded call where it
touches calls, no secrets or caller data in the diff, docs updated.
