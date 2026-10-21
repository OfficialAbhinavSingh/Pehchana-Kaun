# Bolna (bolna.ai): GitHub presence, active work, and problems

Research date: 2026-10-21. Data pulled live with read-only `gh api` calls plus web search/fetch. Every fact has an inline source. **[INFERRED]** marks my own reading of the data. Third-party claims from competitors are labelled as such.

---

## 0. TL;DR

- **One real repo.** `bolna-ai/bolna` (798 stars, 377 forks, MIT, Python) holds the open-source orchestration engine. The other 9 org repos are SDKs, an MCP server, a CLI, n8n/skills integrations, a blog, or empty shells. ([org](https://github.com/bolna-ai), [repo](https://github.com/bolna-ai/bolna))
- **Very active, but mostly staff.** There were 165 commits to master from 2026-07-21 to 2026-10-20, and ~100 auto-tagged releases in under 2 months (0.10.207 on 2026-08-24, 0.10.306 on 2026-10-20). Three people wrote ~85% of recent commits: san0808, puneet-bolna and DeepBhupatkar. ([commits](https://github.com/bolna-ai/bolna/commits/master), [tags](https://github.com/bolna-ai/bolna/tags))
- **External contributions mostly go unreviewed.** 96 PRs are open, and 80 of them have zero reviews. 64 of those 96 come from first-time contributors (author_association NONE), and 52 of the 64 have zero comments. ([open PRs](https://github.com/bolna-ai/bolna/pulls))
- **The recent commits name the main pain points.** Nearly every fix in the last 3 months is about turn-taking/barge-in, TTS sockets dropping mid-reply (silent agent), multilingual/language-switch (LID) bugs, SIP/telephony hangup timing, and latency observability. ([commits](https://github.com/bolna-ai/bolna/commits/master))
- **Company context.** Bolna raised a $6.3M seed led by General Catalyst (Jan 2026; YC, Blume also participated). It handles 200k+ calls/day, has ~1,050 paying customers, approaches ~$700k ARR, and 75% of revenue is self-serve. ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/), [Entrepreneur India](https://india.entrepreneur.com/news-and-trends/voice-ai-startup-bolna-raises-usd-63-mn-funding-led-by/502062)). Their blog says the platform now processes 15M call minutes/day. ([Bolna blog](https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes))

---

## 1. GitHub organisation and repositories

Org: **github.com/bolna-ai**. Created 2024-08-19, 10 public repos, 49 followers, email hello@bolna.ai, blog link platform.bolna.ai. ([org](https://github.com/bolna-ai), [API](https://api.github.com/orgs/bolna-ai))
`bolna-ai/bolna` itself was created 2024-08-24 ([API](https://api.github.com/repos/bolna-ai/bolna)). HN posts point to earlier open-source activity from Dec 2023 ([HN 38634111](https://news.ycombinator.com/item?id=38634111)). A second org mirror, `voxos-ai/bolna`, is indexed by third parties ([sourcepulse](https://www.sourcepulse.org/projects/1827738)). **[INFERRED]** That is the pre-rename org.

### 1.1 All public repos (as of 2026-10-21)

| Repo | Stars | Forks | Lang | Last push | License | Open issues+PRs | Description |
|---|---|---|---|---|---|---|---|
| [bolna](https://github.com/bolna-ai/bolna) | 798 | 377 | Python | 2026-10-20 | MIT | 162 (66 issues + 96 PRs) | Conversational voice AI agents |
| [mcp](https://github.com/bolna-ai/mcp) | 1 | 3 | TypeScript | 2026-10-19 | MIT | 15 | Remote MCP server, 116 tools over api.bolna.ai, on Vercel |
| [blog](https://github.com/bolna-ai/blog) | 0 | 0 | MDX | 2026-10-19 | none | 0 | Next.js blog, migrated from blog.bolna.ai |
| [build-with-bolna](https://github.com/bolna-ai/build-with-bolna) | 0 | 0 | — | 2026-09-25 | none | 1 | Markdown blog/content dump |
| [n8n-nodes-bolna](https://github.com/bolna-ai/n8n-nodes-bolna) | 0 | 0 | TypeScript | 2026-09-07 | MIT | 0 | Official n8n node (calls, batches, trigger) |
| [skills](https://github.com/bolna-ai/skills) | 3 | 2 | Python | 2026-08-25 | MIT | 0 | Agent Skills for Claude Code/Cursor/Codex (`npx skills add bolna-ai/skills`) |
| [web-call](https://github.com/bolna-ai/web-call) | 1 | 2 | TypeScript | 2026-08-20 | MIT | 0 | `@bolna/web-call` WebRTC browser SDK (Opus, TURN) |
| [cli](https://github.com/bolna-ai/cli) | 0 | 1 | Go | 2026-07-31 | none | 8 | Beta CLI + Bubble Tea TUI dashboard |
| [self-hosted-bolna](https://github.com/bolna-ai/self-hosted-bolna) | 1 | 0 | — | 2025-06-28 | none | 0 | **Empty**: only a one-line README.md |
| [awesome-deepseek-integration](https://github.com/bolna-ai/awesome-deepseek-integration) | 0 | 2 | — | 2025-02-06 | CC0 | 0 | Fork |

Source: `gh api orgs/bolna-ai/repos` ([API](https://api.github.com/orgs/bolna-ai/repos?per_page=100)).

### 1.2 Main repo: `bolna-ai/bolna`

- **Default branch** `master`. Topics: deepgram, elevenlabs, twilio, plivo, cartesia, openai, deepseek, voice-agents, and more ([repo](https://github.com/bolna-ai/bolna)).
- **Contributors:** 39 ([contributors](https://github.com/bolna-ai/bolna/graphs/contributors)). Top 10 by commits: prateeksachan (co-founder) 1288, san0808 570, marmikcfc (co-founder) 461, deva-gopalani 173, puneet-bolna 95, RG-04 66, web1havv 40, amansrivstv 33, viplismism 33, saurabhjdsingh 25 ([API](https://api.github.com/repos/bolna-ai/bolna/contributors)). The founders are Maitreya Wagh, Prateek Sachan and Marmik ([HN Show HN](https://news.ycombinator.com/item?id=41234490)).
- **Releases:** semver tags `0.10.x` are auto-bumped on every same-repo PR by `.github/workflows/auto-release.yml` ([workflow](https://github.com/bolna-ai/bolna/blob/master/.github/workflows/auto-release.yml)). The latest is `0.10.306` (2026-10-20). The oldest of the last 100 releases is `0.10.207` (2026-08-24), so that is ~100 releases in 8 weeks ([releases](https://github.com/bolna-ai/bolna/releases)). Published to PyPI as `bolna` ([PyPI](https://pypi.org/project/bolna)).
- **CI:** lint (ruff), pytest, security (gitleaks/OSV), publish ([workflows dir](https://github.com/bolna-ai/bolna/tree/master/.github/workflows)). The test suite was made "runnable, hermetic, and enforced by CI" on 2026-08-21 ([PR #973](https://github.com/bolna-ai/bolna/pull/973)).
- **Branches:** 100+ branches, mostly Linear-style `BOLNA-####` ticket branches plus `devin/*` AI-agent branches ([branches](https://github.com/bolna-ai/bolna/branches/all)). **[INFERRED]** The team uses Linear internally and Devin for some PRs. That internal roadmap is not public.
- **Open-core model.** The README says the hosted APIs and the no-code playground at platform.bolna.ai are "currently closed source". Features land in OSS first, then the hosted API, then the UI ([README](https://github.com/bolna-ai/bolna/blob/master/README.md)). The README also admits: "We have fluctuated b/w maintaining this repository purely from a point of time crunch and not interest" and "We are actively looking for maintainers." ([README](https://github.com/bolna-ai/bolna/blob/master/README.md))

### 1.3 Architecture (from source tree + README)

The README describes the repo as the "entire orchestration platform… orchestrates voice conversations using combination of different ASR+LLM+TTS providers and models over websockets" ([README](https://github.com/bolna-ai/bolna/blob/master/README.md)). Agents are defined in JSON (`agent_config` → `tasks` → `tools_config` with `llm_agent`, `transcriber`, `synthesizer`, `input`/`output`) ([issue #260 example](https://github.com/bolna-ai/bolna/issues/260), [API.md](https://github.com/bolna-ai/bolna/blob/master/API.md)).

Key modules under [`bolna/`](https://github.com/bolna-ai/bolna/tree/master/bolna):

| Layer | Path | Notes |
|---|---|---|
| Entry | `assistant.py` | `Assistant.add_task(...)`, then `async for chunk in assistant.execute()` ([README example](https://github.com/bolna-ai/bolna/blob/master/README.md)) |
| Orchestrator | `agent_manager/task_manager.py` | **9,772 lines / 526 KB in one file**: the pipeline brain (turns, barge-in, hangup, fillers, recording) ([file](https://github.com/bolna-ai/bolna/blob/master/bolna/agent_manager/task_manager.py)). Issue [#187](https://github.com/bolna-ai/bolna/issues/187) "Breakdown task_manager into separate components" has been open since 2025-05 |
| Turn-taking | `agent_manager/interruption_manager.py` | Heuristic: `number_of_words_for_interruption=3`, an `accidental_interruption_phrases` set, `incremental_delay=900` ms ([file](https://github.com/bolna-ai/bolna/blob/master/bolna/agent_manager/interruption_manager.py)). **[INFERRED]** There is no audio-native turn/backchannel model; end-of-turn mostly comes from the ASR provider's endpointing |
| Voicemail | `agent_manager/voicemail_handler.py` | LLM-based voicemail detection ([PR #1122](https://github.com/bolna-ai/bolna/pull/1122)) |
| Agent types | `agent_types/` | contextual conversational, **graph agent** (node/edge flows, 88 KB), knowledgebase (RAG), extraction, summarization, webhook ([dir](https://github.com/bolna-ai/bolna/tree/master/bolna/agent_types)) |
| LLMs | `llms/` | OpenAI (incl. Responses API), Azure, Gemini, LiteLLM; `LLMProvider` enum lists openai, cohere, ollama, deepinfra, together, fireworks, azure-openai, perplexity, vllm, anyscale, custom, ola, groq, anthropic, deepseek, openrouter, azure, google, bolna ([enums.py](https://github.com/bolna-ai/bolna/blob/master/bolna/enums.py)) |
| Speech-to-speech | `s2s/` | OpenAI Realtime + Gemini Live, added 2026-08-19 ([PR #916](https://github.com/bolna-ai/bolna/pull/916)) |
| ASR (13) | `transcriber/` | Deepgram (incl. Flux), Azure, Sarvam, AssemblyAI, Google, Pixa, Gladia, ElevenLabs, Smallest, OpenAI, Soniox, Gemini, Realtime (self-hosted, OpenAI-Realtime protocol), plus `transcriber_pool` for multilingual ([providers.py](https://github.com/bolna-ai/bolna/blob/master/bolna/providers.py)) |
| TTS (15) | `synthesizer/` | Polly, ElevenLabs (+v3 dialogue), OpenAI, Deepgram, Azure, Cartesia, Smallest, Sarvam, Rime, Pixa, Maya, Kalpa, Gemini, Soniox, Custom (OpenAI-compatible), plus `synthesizer_pool` ([providers.py](https://github.com/bolna-ai/bolna/blob/master/bolna/providers.py)) |
| Language ID | `lid/` | Sarvam + Soniox language detection for mid-call language switching ([dir](https://github.com/bolna-ai/bolna/tree/master/bolna/lid)) |
| Telephony (6) | `input_handlers/telephony_providers`, `output_handlers/telephony_providers` | Twilio, Plivo, Exotel, Vobiz, SIP trunk (Asterisk), FreeSWITCH ([dir](https://github.com/bolna-ai/bolna/tree/master/bolna/input_handlers/telephony_providers)) |
| Web call | `input_handlers/default.py`, `output_handlers/default.py` | Browser/WebRTC path ([dir](https://github.com/bolna-ai/bolna/tree/master/bolna/output_handlers)) |

**Docker / self-host.** `local_setup/docker-compose.yml` runs 5 services: `bolna-app` (port 5001), `redis` (agent persistence), `ngrok` (tunnel), `twilio-app` (8001) and `plivo-app`. There are only Twilio and Plivo telephony servers, and `start.sh` is a quickstart ([compose](https://github.com/bolna-ai/bolna/blob/master/local_setup/docker-compose.yml), [local_setup](https://github.com/bolna-ai/bolna/tree/master/local_setup)). The README heading says the local setup "will be moved to a different repository" ([README](https://github.com/bolna-ai/bolna/blob/master/README.md)), but `self-hosted-bolna` is still empty ([repo](https://github.com/bolna-ai/self-hosted-bolna)).

---

## 2. What they're actively working on (last ~3 months, 2026-07-21 → 2026-10-20)

165 commits. By author: san0808 77, puneet-bolna 47, DeepBhupatkar 17, amansrivstv 6, SubhrajitPrusty 5, web1havv 4, others 1–2 each ([commits](https://github.com/bolna-ai/bolna/commits/master?since=2026-07-21)). Themes, grouped from commit titles **[INFERRED grouping]**:

1. **Turn-taking / barge-in correctness.**
   - "don't barge in on Deepgram re-delivering the caller's last sentence while the reply plays" ([#1089](https://github.com/bolna-ai/bolna/pull/1089))
   - "standby transcribers in a multilingual pool no longer interrupt the agent" ([#1117](https://github.com/bolna-ai/bolna/pull/1117))
   - "per-node overrides for interruption threshold" ([#1018](https://github.com/bolna-ai/bolna/pull/1018))
   - "answer callers who interrupt the reply after a tool call" ([#1101](https://github.com/bolna-ai/bolna/pull/1101))
   - "barge-in leaves an orphaned function_call… calls die mid-tool-call" ([#979](https://github.com/bolna-ai/bolna/pull/979))
   - open PR: Jev (TypeSafe) veto on eager end-of-turn speculative replies ([#1107](https://github.com/bolna-ai/bolna/pull/1107))
2. **Silent agent / TTS socket robustness.**
   - "Sarvam receiver survives a mid-call socket drop" ([#1052](https://github.com/bolna-ai/bolna/pull/1052))
   - "elevenlabs: end the turn and keep receiving when the multi-stream socket drops mid-reply" ([#1091](https://github.com/bolna-ai/bolna/pull/1091))
   - "send elevenlabs speech one sentence at a time" ([#1133](https://github.com/bolna-ai/bolna/pull/1133))
   - "remove agent-side clicks on Maya/Sarvam calls (lone μ-law byte padding + per-frame resampling)" ([#1121](https://github.com/bolna-ai/bolna/pull/1121))
3. **Latency and observability.**
   - "measure dead air inside each tts reply the caller hears" ([#1140](https://github.com/bolna-ai/bolna/pull/1140))
   - "report per-turn ASR/TTS + stream-connect latency" ([#859](https://github.com/bolna-ai/bolna/pull/859))
   - "make the reasoning summary request opt-in so it stops delaying the first token" ([#891](https://github.com/bolna-ai/bolna/pull/891))
   - "stream the graph routing call" ([#1046](https://github.com/bolna-ai/bolna/pull/1046))
   - "cache the resample FIR filter instead of redesigning it per audio chunk" ([#974](https://github.com/bolna-ai/bolna/pull/974))
4. **Multilingual / language switching (LID).**
   - "Lid/v2" ([#919](https://github.com/bolna-ai/bolna/pull/919))
   - "explicit-only language-switch mode" ([#983](https://github.com/bolna-ai/bolna/pull/983))
   - "drop the Responses chain on a language switch so the new system prompt reaches the model" ([#1013](https://github.com/bolna-ai/bolna/pull/1013))
   - "keyterm boosting for sarvam saaras:v4" ([#1088](https://github.com/bolna-ai/bolna/pull/1088))
5. **Telephony / SIP hangup timing.**
   - "hold sip-trunk hangup until Asterisk confirms playout drained" ([#926](https://github.com/bolna-ai/bolna/pull/926))
   - "stop HANGUP from clipping a goodbye" ([#942](https://github.com/bolna-ai/bolna/pull/942))
   - "FreeSWITCH DTMF and trunk transfer ringing gate" ([#1059](https://github.com/bolna-ai/bolna/pull/1059))
   - "cap silence re-prompts so silent callers are always hung up" ([#1113](https://github.com/bolna-ai/bolna/pull/1113))
6. **New providers and models.**
   - Speech-to-speech via OpenAI Realtime + Gemini Live ([#916](https://github.com/bolna-ai/bolna/pull/916))
   - Gemini TTS ([#1020](https://github.com/bolna-ai/bolna/pull/1020)), Soniox TTS ([#1056](https://github.com/bolna-ai/bolna/pull/1056)), Kalpa TTS ([#986](https://github.com/bolna-ai/bolna/pull/986)), Maya TTS ([#915](https://github.com/bolna-ai/bolna/pull/915)), custom OpenAI-compatible TTS ([#1109](https://github.com/bolna-ai/bolna/pull/1109))
   - Gemini 3.5 Transcribe ASR ([#996](https://github.com/bolna-ai/bolna/pull/996)), AssemblyAI universal-3.x ([#1053](https://github.com/bolna-ai/bolna/pull/1053)), self-hosted Realtime transcriber ([#1100](https://github.com/bolna-ai/bolna/pull/1100))
   - a Bolna-hosted LLM provider ([#1096](https://github.com/bolna-ai/bolna/pull/1096))
   - web search tool ([#1104](https://github.com/bolna-ai/bolna/pull/1104))
7. **Billing correctness.** "bill each ASR connection's own audio exactly once" ([#1111](https://github.com/bolna-ai/bolna/pull/1111)), "book each send for the audio it actually carries" ([#1047](https://github.com/bolna-ai/bolna/pull/1047)).
8. **Security hardening.** SSRF guard on custom LLM base_url ([#988](https://github.com/bolna-ai/bolna/pull/988)), "keep credentials out of the logs" ([#1048](https://github.com/bolna-ai/bolna/pull/1048)), Deepgram `mip_opt_out` for zero data retention ([#1064](https://github.com/bolna-ai/bolna/pull/1064)).

**Open staff PRs signalling next work** ([open PRs](https://github.com/bolna-ai/bolna/pulls)):
- TTS pronunciation dictionaries/rules ([#1081](https://github.com/bolna-ai/bolna/pull/1081))
- Gemini 3.8 Live ([#1076](https://github.com/bolna-ai/bolna/pull/1076))
- forwarding caller audio in 40 ms chunks to the Realtime transcriber ([#1103](https://github.com/bolna-ai/bolna/pull/1103))
- measuring user speech start/end on one clock ([#1136](https://github.com/bolna-ai/bolna/pull/1136))
- ending the call with the provider's reason when ASR/TTS rejects ([#1123](https://github.com/bolna-ai/bolna/pull/1123), [#1124](https://github.com/bolna-ai/bolna/pull/1124))
- a Jev language-switch judge ([#1146](https://github.com/bolna-ai/bolna/pull/1146))

**Public R&D signal.** The blog post "Testing Jev on real phone calls" evaluates the TypeSafe "Jev" model on routing (72.7% agreement, 8th of 10 models, 411 ms), call judging (κ=0.416) and field extraction. It reports that "When the call should move on, Jev moves only about half the time", which causes stuck conversations ([Bolna blog](https://www.bolna.ai/blog/testing-jev-on-real-phone-calls)).

**No public roadmap.** There are no ROADMAP file, GitHub Projects or milestones in the repo. The tree has no roadmap doc ([tree](https://github.com/bolna-ai/bolna)). Work tracking happens in internal `BOLNA-####` tickets (branch names; [branches](https://github.com/bolna-ai/bolna/branches/all)).

---

## 3. Problems: GitHub issues

### 3.1 Counts

| Metric | Value | Source |
|---|---|---|
| Open issues | 66 | [search](https://github.com/bolna-ai/bolna/issues?q=is%3Aissue+is%3Aopen) |
| Closed issues | 67 | [search](https://github.com/bolna-ai/bolna/issues?q=is%3Aissue+is%3Aclosed) |
| Open PRs | 96 | [search](https://github.com/bolna-ai/bolna/pulls?q=is%3Apr+is%3Aopen) |
| Merged PRs (all-time) | 748 | [search](https://github.com/bolna-ai/bolna/pulls?q=is%3Apr+is%3Amerged) |
| Closed-unmerged PRs | 168 | [search](https://github.com/bolna-ai/bolna/pulls?q=is%3Apr+is%3Aclosed+is%3Aunmerged) |
| Open issues with 0 comments | 32 / 66 (48%) | computed from `gh issue list` ([issues](https://github.com/bolna-ai/bolna/issues)) |
| Open issues with any label | 5 / 66 | same |
| Closed issues: median days to close | 5 (p75 = 30) | computed from the last 67 closed ([closed](https://github.com/bolna-ai/bolna/issues?q=is%3Aissue+is%3Aclosed)) |
| Open PRs with 0 reviews | 80 / 96 | `gh pr list --json reviews` ([PRs](https://github.com/bolna-ai/bolna/pulls)) |
| Open PRs from first-time contributors (NONE) | 64 / 96; 52 of those have 0 comments | search API ([PRs](https://github.com/bolna-ai/bolna/pulls)) |

**[INFERRED]** Issues that get closed close fast (median 5 days). The open backlog is mostly ignored, though: about half have no reply, labels are almost never used, and external PRs sit unreviewed for months. Examples include the Camb.ai TTS PR open since 2026-01-04 ([#427](https://github.com/bolna-ai/bolna/pull/427)) and an exec() removal PR open since 2026-03-23 ([#585](https://github.com/bolna-ai/bolna/pull/585)).

**Tone note.** One closed issue has a co-founder reply telling a user to "learn some manners… Use our hosted APIs if you're acting so anxious" after being tagged ([#245](https://github.com/bolna-ai/bolna/issues/245)). Another redirects latency questions to the paid hosted API ([#251](https://github.com/bolna-ai/bolna/issues/251)). **[INFERRED]** Self-hosters get low priority compared with hosted customers.

### 3.2 Open issues by category (with top quotes)

**A. Interruptions / barge-in / turn-taking** (most-discussed category)
- [#168](https://github.com/bolna-ai/bolna/issues/168) "High Token Usage, Interruption Threshold Logic, and Audio Stream Mixing" (12 comments). Reports "at least 150k input tokens… even for short interactions". With the threshold at 2 words, "if the user says just one word (like okay or proceed), the agent doesn't respond".
- [#223](https://github.com/bolna-ai/bolna/issues/223) "Avoid Voice Agent Answering To Itself": "it takes their 'hmm', 'yes', 'okay' as responses… and then start speaking again… It sometimes is very bad." (5 comments)
- [#476](https://github.com/bolna-ai/bolna/issues/476) "micro-acknowledgements vs semantic interruption": the same backchannel problem.
- [#295](https://github.com/bolna-ai/bolna/issues/295) "Interruptions and agent_welcome_message not working": "The agent does not get interrupted properly even when multiple interruption attempts are made."
- [#1001](https://github.com/bolna-ai/bolna/issues/1001) "Web-call barge-in trims the wrong text": the default output handler drops `turn_id/response_uid` from marks.

**B. Silent agent / audio not playing / TTS failures**
- [#1092](https://github.com/bolna-ai/bolna/issues/1092) "Multilingual calls go silent after TTS reconnect": "the agent is mute for the rest of the call". Open fix PRs: [#1093](https://github.com/bolna-ai/bolna/pull/1093), [#1130](https://github.com/bolna-ai/bolna/pull/1130).
- [#1126](https://github.com/bolna-ai/bolna/issues/1126) "a socket that closes mid-reply leaves the agent marked as speaking for the rest of the call". Affects Cartesia, Deepgram, Smallest, Maya, Pixa and Soniox. Fix PR [#1127](https://github.com/bolna-ai/bolna/pull/1127).
- [#1125](https://github.com/bolna-ai/bolna/issues/1125) "Rime streaming TTS plays no audio". Fix PR [#1139](https://github.com/bolna-ai/bolna/pull/1139).
- [#272](https://github.com/bolna-ai/bolna/issues/272) "Welcome message not firing" (7 comments).
- History: [#507](https://github.com/bolna-ai/bolna/issues/507) "Complete Silence on Twilio Calls (issue since 7+ months in git repo)" and [#498](https://github.com/bolna-ai/bolna/issues/498) "Audio not transmitted in self-built Docker images (works in pre-built image)". Both were closed in Feb–May 2026.

**C. Latency / ASR finalization**
- [#711](https://github.com/bolna-ai/bolna/issues/711) "OpenAI realtime whisper hears speech but final transcript comes too late, so agent never replies": "sometimes 20–35 seconds later".
- Closed: [#235](https://github.com/bolna-ai/bolna/issues/235) "Response time 4s?" ("for every sentence I say it takes exactly 4 secs… on the platform it is almost like a natural conversation"), [#251](https://github.com/bolna-ai/bolna/issues/251) "Help for production" (latency on VPS), and [#212](https://github.com/bolna-ai/bolna/issues/212) "Latency Summary for Transcriber and Synthesizer" ("its too complex for me, there is no proper beginning or end of any event").

**D. Telephony**
- [#614](https://github.com/bolna-ai/bolna/issues/614) "India Routing showing Black despite active Vobiz number — No audio on calls".
- [#928](https://github.com/bolna-ai/bolna/issues/928) WebSocketDisconnect gives "a spurious traceback on every normal hangup".
- [#149](https://github.com/bolna-ai/bolna/issues/149) local SIP / FreePBX support. [#867](https://github.com/bolna-ai/bolna/issues/867) native Telnyx; PR [#968](https://github.com/bolna-ai/bolna/pull/968) is open.
- [#16](https://github.com/bolna-ai/bolna/issues/16) "add inbound agent in local setup" (open since 2024-09).

**E. Language support / multilingual observability**
- [#659](https://github.com/bolna-ai/bolna/issues/659) "Auto Language Detection Works but No Visible Code in Transcripts/Logs/Call History" (Hinglish→Bengali).
- [#305](https://github.com/bolna-ai/bolna/issues/305) "Improve Audio Clarity for Better Transcription Accuracy": asks for denoise/gain normalization before ASR.

**F. LLM / tool-calling bugs**
- [#742](https://github.com/bolna-ai/bolna/issues/742) Groq via LiteLLM fails. [#224](https://github.com/bolna-ai/bolna/issues/224) Groq error in `check_for_completion`.
- [#879](https://github.com/bolna-ai/bolna/issues/879) `ToolCallAccumulator` KeyError "ends the call".
- [#1147](https://github.com/bolna-ai/bolna/issues/1147) Gemini dispatches a url-less call. [#1149](https://github.com/bolna-ai/bolna/issues/1149) "Tool argument `url` overrides the configured endpoint" **[INFERRED: an SSRF-class risk]**.
- [#902](https://github.com/bolna-ai/bolna/issues/902) graph/knowledge agents "silently fall back to OpenAI on initialization errors".

**G. Self-hosting / packaging pain**
- [#1000](https://github.com/bolna-ai/bolna/issues/1000) "Call recording crashes: save_audio_file_to_s3 uses torch/torchaudio, which are never imported or declared". Fix PR [#1002](https://github.com/bolna-ai/bolna/pull/1002) is open.
- [#196](https://github.com/bolna-ai/bolna/issues/196) "Dockerize package + quickstart server" (open since 2025-05). [#231](https://github.com/bolna-ai/bolna/issues/231) "Which is the Best Python version". [#204](https://github.com/bolna-ai/bolna/issues/204) "web call not working in Firefox".
- Quickstart server bugs [#904](https://github.com/bolna-ai/bolna/issues/904) and [#905](https://github.com/bolna-ai/bolna/issues/905), plus a batch of 9 code-audit issues [#896](https://github.com/bolna-ai/bolna/issues/896)–[#905](https://github.com/bolna-ai/bolna/issues/905) filed 2026-07-30 by one user with no maintainer replies.
- Closed: [#261](https://github.com/bolna-ai/bolna/issues/261) Windows install fails on uvloop.

**H. Security**
- [#407](https://github.com/bolna-ai/bolna/issues/407) "dynamic exec usage in function_calling_helpers.py" (open). **[INFERRED]** It may already be fixed: `grep 'exec('` on current master [function_calling_helpers.py](https://github.com/bolna-ai/bolna/blob/master/bolna/helpers/function_calling_helpers.py) returns nothing. The issue and PR [#585](https://github.com/bolna-ai/bolna/pull/585) were never closed.
- [#899](https://github.com/bolna-ai/bolna/issues/899) "Follow-up WebhookAgent bypasses outbound SSRF validation".
- In the `mcp` repo, 12 audit issues were filed 2026-07-30 and all are still open. They include "#1 Environment-key fallback is a full auth bypass in production" and "#2 Supabase access tokens are accepted without audience validation" ([mcp issues](https://github.com/bolna-ai/mcp/issues)).

**I. Code health / refactor asks**
- [#187](https://github.com/bolna-ai/bolna/issues/187) split task_manager (now 9.8k lines), [#371](https://github.com/bolna-ai/bolna/issues/371) split models.py, [#265](https://github.com/bolna-ai/bolna/issues/265) hardcoded values → enums, [#186](https://github.com/bolna-ai/bolna/issues/186) common synthesizer class.
- [#896](https://github.com/bolna-ai/bolna/issues/896) "TaskManager.run suppresses call-breaking exceptions by returning from finally". [#900](https://github.com/bolna-ai/bolna/issues/900) "SynthesizerPool swallows provider errors". [#1004](https://github.com/bolna-ai/bolna/issues/1004) fire-and-forget tasks dropped.

**J. Docs gaps** (verified against the repo)
- The README badge links `CONTRIBUTING.md`, which **does not exist**. GitHub community profile health is 37%, with no CONTRIBUTING, CoC, issue templates or PR template ([community profile](https://api.github.com/repos/bolna-ai/bolna/community/profile), [README](https://github.com/bolna-ai/bolna/blob/master/README.md)).
- The README points to `examples.bolna.dev` for example agents, but that hostname **does not resolve in DNS** (checked 2026-10-21). Issues [#553](https://github.com/bolna-ai/bolna/issues/553) and [#398](https://github.com/bolna-ai/bolna/issues/398) and PRs [#584](https://github.com/bolna-ai/bolna/pull/584) and [#673](https://github.com/bolna-ai/bolna/pull/673) all report this.
- The README still says Exotel is "coming soon", but `exotel.py` handlers exist. Its ASR table lists only Deepgram + Realtime even though 13 transcribers ship, and its telephony table lists only Twilio/Plivo even though 6 handlers ship ([README](https://github.com/bolna-ai/bolna/blob/master/README.md) vs [providers.py](https://github.com/bolna-ai/bolna/blob/master/bolna/providers.py)).
- [#58](https://github.com/bolna-ai/bolna/issues/58) cal.com integration docs wrong. [#16](https://github.com/bolna-ai/bolna/issues/16) inbound in local setup is undocumented.

**K. Noise.** [#854](https://github.com/bolna-ai/bolna/issues/854) is ad spam. [#666](https://github.com/bolna-ai/bolna/issues/666) asks "was this a fork of vapi ?". [#1078](https://github.com/bolna-ai/bolna/issues/1078) and [#1026](https://github.com/bolna-ai/bolna/issues/1026) are vendor self-promo integrations.

---

## 4. User complaints and pain points outside GitHub

Off-GitHub public complaint volume is **low**. No Reddit threads about Bolna turned up in web search ([search attempted](https://www.google.com/search?q=site%3Areddit.com+bolna+voice+agent)). Reddit's JSON API was blocked from this environment. Hacker News has only Bolna's own Show HN/launch posts with 0–2 comments ([HN Algolia search](https://hn.algolia.com/?q=bolna)). G2 returned 403 to the fetcher ([G2](https://www.g2.com/products/bolna-ai/reviews)). What does exist:

- **Hacker News.** The only substantive user question, on the Aug 2024 Show HN, was about latency: "how do you handle latency issues in real-time voice conversations?" ([HN 41234490](https://news.ycombinator.com/item?id=41234490)).
- **Product Hunt.** 5.0/5 from only 2 reviews, no complaints ([Product Hunt](https://www.producthunt.com/products/bolna/reviews)).
- **Third-party review (aiindigo, 2026).**
  - On complex flows: "the visual map becomes a 'spaghetti' of lines that is harder to manage than a traditional script"
  - On hallucination: "the agent can still occasionally misinterpret a nuance… leading to a confident but incorrect answer"
  - On latency: "you may still notice a slight pause… especially when the agent has to call an external API"
  - ([aiindigo](https://aiindigo.com/blog/bolna-agent-studio-review-2026-the-reality-of-no-code-voice-ai))
- **Review summary in web search.** "failover behavior when the auto-picked model has an outage mid-call isn't clearly documented" ([G2 via search snippet](https://www.g2.com/products/bolna-ai/reviews)). **[INFERRED]** I could not verify this verbatim because G2 returned 403.
- **Competitor critique (Ringg AI, a direct competitor, so biased).** Bolna is "an orchestration layer only" with separate billing per vendor, so "costs scale unpredictably". Also: "Managing multiple providers introduces significant coordination overhead and slows down critical issue resolution during system outages" ([Ringg blog](https://www.ringg.ai/blogs/bolna-ai-pricing)).
- **Pricing facts.** Bolna charges a flat per-minute platform fee on top of provider costs. Bundled "preferred" ASR/LLM/TTS models keep a flat per-minute rate, other models are billed separately, and BYOK removes Bolna's provider charges ([Bolna call pricing docs](https://www.bolna.ai/docs/pricing/call-pricing), [pricing page](https://www.bolna.ai/pricing)). A search snippet citing the Bolna docs gives a "flat 2 cents platform fee per minute" and 5–10¢/min bundles ([docs.bolna.ai/pricing](https://docs.bolna.ai/pricing)). **[INFERRED]** I did not see these figures verbatim on the fetched page.
- **Bolna's own stated India-specific challenges** (TechCrunch): noise cancellation, Truecaller caller-ID verification, mixed-language handling, and "speaking numbers in English regardless of core language" ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)).
- **Bolna's internal analytics pain** (own blog): "A call would be finished, but the analytics for it were not there yet". The delay was 5–15 min before the ClickHouse migration, which cut analytics cost ~6x ([Bolna blog](https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes)).
- **Bolna's latency target:** "sub-600ms end-to-end". The budget is endpointing 50–300 ms, transcription 50–150 ms, LLM first token 100–400 ms, and TTS first chunk 80–200 ms ([Bolna latency docs](https://www.bolna.ai/docs/concepts/latency)). Troubleshooting flags fire at ASR >100 ms/sequence, LLM TTFT >1000 ms and TTS >500 ms ([call latencies docs](https://www.bolna.ai/docs/concepts/call-latencies)).
- **Discord** is linked from the README ([discord.gg/59kQWGgnm8](https://discord.gg/59kQWGgnm8)), but I could not read it without logging in. I found no X/Twitter or YouTube complaint threads ([search attempted](https://www.google.com/search?q=bolna+voice+ai+twitter+complaint)).

---

## 5. Industry-wide voice-AI problems relevant to Bolna, framed as hackathon opportunities

| # | Problem (evidence) | Bolna-specific evidence | Hackathon build idea **[INFERRED]** |
|---|---|---|---|
| 1 | **Backchannels misread as interruptions.** "VAD alone is not sufficient… brief backchannels ('mm-hmm', 'yeah'), user noises like sighs or coughs, or background sounds." LiveKit's model rejects 51% of false VAD barge-ins at ≤30 ms inference ([LiveKit, 2026-03-19](https://livekit.com/blog/adaptive-interruption-handling)). Twilio's view on handling interruptions is at ([Twilio blog](https://www.twilio.com/en-us/blog/insights/ai-voice-agent-interruption-handling)). | Bolna uses a word-count threshold + phrase list ([interruption_manager.py](https://github.com/bolna-ai/bolna/blob/master/bolna/agent_manager/interruption_manager.py)). Issues [#223](https://github.com/bolna-ai/bolna/issues/223), [#168](https://github.com/bolna-ai/bolna/issues/168), [#476](https://github.com/bolna-ai/bolna/issues/476) | A lightweight backchannel-vs-barge-in classifier for **Hinglish/Indic** fillers ("haan", "achha", "hmm", "ji"), as a drop-in `InterruptionManager` strategy |
| 2 | **End-of-turn detection.** Silence timers either cut users off or feel slow. In LiveKit's June 2026 eval, lower latency means more false cutoffs ([Lorikeet](https://www.lorikeetcx.ai/blog/if-your-voice-ai-cant-wait-it-cant-listen), [Soniox wiki](https://soniox.com/wiki/turn-taking-barge-in)). Open-source audio-native model: Pipecat Smart Turn v3, 23 languages, ~10 ms CPU, BSD-2 ([smart-turn](https://github.com/pipecat-ai/smart-turn)) | No local turn model in requirements. Silero-VAD PR [#656](https://github.com/bolna-ai/bolna/pull/656) has gone unreviewed since April. Late-final-transcript bug [#711](https://github.com/bolna-ai/bolna/issues/711) | Integrate Smart Turn / VAD as a provider-agnostic endpointing layer and benchmark it on 8 kHz μ-law Indic calls |
| 3 | **Indic + code-mixed ASR accuracy on phone audio.** On the Voice of India benchmark (536 h of unscripted telephonic speech, 15 languages), top WER is ~5% on Hindi but 20.9% on Bhojpuri. District-level WER ranges from 4% to 44%. Some commercial models exceed 100% WER on several languages ([arXiv 2604.19151](https://arxiv.org/html/2604.19151)). Code-switching raises WER 30–50% relative ([Gnani blog](https://gnani.ai/resources/blogs/blog-code-switching-speech-recognition-hinglish-asr)) | Bolna's pitch is 10+ Indian languages ([Entrepreneur](https://india.entrepreneur.com/news-and-trends/voice-ai-startup-bolna-raises-usd-63-mn-funding-led-by/502062)). LID/multilingual is the most-patched area (§2.4). [#659](https://github.com/bolna-ai/bolna/issues/659) asks for language-detection observability | Per-call ASR router that picks a provider by detected language/region/audio quality. Or a keyterm-boost auto-generator from the agent prompt (Bolna already supports keyterms, [#1088](https://github.com/bolna-ai/bolna/pull/1088)) |
| 4 | **TTS text normalization for Indian content** (numbers, currency, dates, emails in mixed scripts) | Bolna names "speaking numbers in English regardless of core language" as a core challenge ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)). Open PRs: text_chunker splitting prices/times/emails ([#1083](https://github.com/bolna-ai/bolna/pull/1083)) and pronunciation dictionaries ([#1081](https://github.com/bolna-ai/bolna/pull/1081)) | An Indic TTS normalizer (₹, lakh/crore, phone numbers, PIN codes, Hinglish) with a test set |
| 5 | **Cost per minute is opaque.** Real all-in cost is ~$0.10–0.31/min vs advertised platform fees of $0.05 (Vapi) and $0.07 (Retell) ([Fora Soft](https://www.forasoft.com/blog/article/vapi-vs-retell-vs-custom), [Retell pricing blog](https://retellai.com/blog/ai-voice-agent-pricing-full-cost-breakdown-platform-comparison-roi-analysis)) | Multi-vendor billing critique ([Ringg](https://www.ringg.ai/blogs/bolna-ai-pricing)). 150k input tokens per short call ([#168](https://github.com/bolna-ai/bolna/issues/168)). Billing-correctness fixes [#1111](https://github.com/bolna-ai/bolna/pull/1111), [#1047](https://github.com/bolna-ai/bolna/pull/1047). Cost caps requested in [#933](https://github.com/bolna-ai/bolna/issues/933) | Per-call cost estimator/guardrail (live ₹/min meter, budget cap, prompt-token diet via history trimming) |
| 6 | **Hallucination / wrong commitments / tool misuse.** Failure modes include hallucinated commitments, persona drift, accent bias and prompt injection ([SoftwareSeni](https://www.softwareseni.com/when-voice-agents-go-wrong-production-failure-modes-and-how-to-prevent-them/)). Text evals miss ~40% of voice-specific failures, per Hamming's proprietary data ([Hamming](https://hamming.ai/blog/why-voice-agents-need-simulations-and-evaluations)) | Tool-call bugs [#1147](https://github.com/bolna-ai/bolna/issues/1147), [#1149](https://github.com/bolna-ai/bolna/issues/1149), [#879](https://github.com/bolna-ai/bolna/issues/879). Review notes "confident but incorrect" answers ([aiindigo](https://aiindigo.com/blog/bolna-agent-studio-review-2026-the-reality-of-no-code-voice-ai)). PII/tool-auth governance in [#933](https://github.com/bolna-ai/bolna/issues/933) / PR [#1029](https://github.com/bolna-ai/bolna/pull/1029) | Post-call "claim checker" that compares agent statements with KB/tool results and flags unauthorized promises. Or a PII redactor for Indic numbers (Aadhaar/PAN/UPI) |
| 7 | **Telephony audio quality and robustness** (8 kHz μ-law, noise, socket drops) | Clicks from μ-law padding ([#1121](https://github.com/bolna-ai/bolna/pull/1121)), silent-agent-after-reconnect ([#1092](https://github.com/bolna-ai/bolna/issues/1092), [#1126](https://github.com/bolna-ai/bolna/issues/1126)), audio clarity request ([#305](https://github.com/bolna-ai/bolna/issues/305)). Voice of India shows WER rising with poorer audio quality (ElevenLabs Scribe 15.3% → 25.2%) ([arXiv](https://arxiv.org/html/2604.19151)) | Pre-ASR denoise + AGC stage for telephony streams with a before/after WER demo. Or a chaos tester that drops TTS/ASR sockets mid-reply and asserts recovery |
| 8 | **Testing and observability.** Teams find failures only after production ([Hamming](https://hamming.ai/blog/why-voice-agents-need-simulations-and-evaluations)) | Latency logs "too complex… no proper beginning or end of any event" ([#212](https://github.com/bolna-ai/bolna/issues/212)). Bolna is adding dead-air metrics ([#1140](https://github.com/bolna-ai/bolna/pull/1140)) and needed real-time analytics ([blog](https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes)) | A simulated-caller test harness (accented/noisy/backchanneling synthetic callers) that scores TTFA, false barge-ins, task completion |
| 9 | **Conversation-flow routing gets stuck** | Jev only moves the call forward "about half the time" when it should ([Bolna blog](https://www.bolna.ai/blog/testing-jev-on-real-phone-calls)). Graph-agent routing fixes [#864](https://github.com/bolna-ai/bolna/pull/864), [#871](https://github.com/bolna-ai/bolna/pull/871). "spaghetti" visual flows ([aiindigo](https://aiindigo.com/blog/bolna-agent-studio-review-2026-the-reality-of-no-code-voice-ai)) | A fast routing classifier fine-tuned on call transcripts, or a "stuck-node" detector that flags repeated caller utterances |

---

## 6. Contribution entry points

- **Labels exist but are unused.** `good first issue`, `help wanted`, `bug`, `enhancement`, `feature`, `high-impact`, `sentry` and others are defined ([labels](https://github.com/bolna-ai/bolna/labels)). Open counts: good first issue **0**, help wanted **0**, bug **2** ([#462](https://github.com/bolna-ai/bolna/issues/462), [#234](https://github.com/bolna-ai/bolna/issues/234)), enhancement **0** ([search](https://github.com/bolna-ai/bolna/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)).
- **No CONTRIBUTING.md.** Guidance lives only in the README "Contributing" section: open an issue first for larger changes, small fixes go straight to a PR ([README](https://github.com/bolna-ai/bolna/blob/master/README.md#contributing)). The README also documents how to add a telephony provider, which is the clearest extension guide ([README](https://github.com/bolna-ai/bolna/blob/master/README.md#extending-with-other-telephony-providers)).
- **Recent external merges exist but are rare.** Examples: a stall-backstop fix by aasthachauhan-code ([#1009](https://github.com/bolna-ai/bolna/pull/1009)), the Cartesia sonic-3.6 migration by 23821 ([#1082](https://github.com/bolna-ai/bolna/pull/1082)), Maya TTS ([#915](https://github.com/bolna-ai/bolna/pull/915)) and Kalpa TTS ([#986](https://github.com/bolna-ai/bolna/pull/986), apparently vendor-contributed **[INFERRED]**).
- **Practical advice [INFERRED].** Issues filed with a precise root cause and file:line references do get fixed. Recent external reports like [#1092](https://github.com/bolna-ai/bolna/issues/1092), [#1126](https://github.com/bolna-ai/bolna/issues/1126) and [#1125](https://github.com/bolna-ai/bolna/issues/1125) all have fix PRs and one comment within days. Generic feature requests and new-vendor integrations sit unreviewed. Time-sensitive fixes also move: OpenAI gpt-3.5-turbo shuts down Oct 23, so [#1102](https://github.com/bolna-ai/bolna/pull/1102) is open.

---

## Sources

GitHub
- https://github.com/bolna-ai
- https://api.github.com/orgs/bolna-ai/repos?per_page=100
- https://github.com/bolna-ai/bolna
- https://github.com/bolna-ai/bolna/blob/master/README.md
- https://github.com/bolna-ai/bolna/blob/master/API.md
- https://github.com/bolna-ai/bolna/blob/master/bolna/providers.py
- https://github.com/bolna-ai/bolna/blob/master/bolna/enums.py
- https://github.com/bolna-ai/bolna/blob/master/bolna/agent_manager/task_manager.py
- https://github.com/bolna-ai/bolna/blob/master/bolna/agent_manager/interruption_manager.py
- https://github.com/bolna-ai/bolna/blob/master/local_setup/docker-compose.yml
- https://github.com/bolna-ai/bolna/blob/master/.github/workflows/auto-release.yml
- https://github.com/bolna-ai/bolna/commits/master
- https://github.com/bolna-ai/bolna/releases , https://github.com/bolna-ai/bolna/tags
- https://github.com/bolna-ai/bolna/graphs/contributors
- https://github.com/bolna-ai/bolna/branches/all
- https://github.com/bolna-ai/bolna/issues , https://github.com/bolna-ai/bolna/pulls , https://github.com/bolna-ai/bolna/labels
- https://api.github.com/repos/bolna-ai/bolna/community/profile
- https://github.com/bolna-ai/mcp , https://github.com/bolna-ai/mcp/issues
- https://github.com/bolna-ai/cli , https://github.com/bolna-ai/skills , https://github.com/bolna-ai/web-call , https://github.com/bolna-ai/n8n-nodes-bolna , https://github.com/bolna-ai/self-hosted-bolna , https://github.com/bolna-ai/build-with-bolna , https://github.com/bolna-ai/blog
- https://pypi.org/project/bolna

Bolna official
- https://www.bolna.ai/docs/concepts/latency
- https://www.bolna.ai/docs/concepts/call-latencies
- https://www.bolna.ai/docs/pricing/call-pricing , https://www.bolna.ai/pricing , https://docs.bolna.ai/pricing
- https://www.bolna.ai/blog/testing-jev-on-real-phone-calls
- https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes

News / reviews / community
- https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/
- https://india.entrepreneur.com/news-and-trends/voice-ai-startup-bolna-raises-usd-63-mn-funding-led-by/502062
- https://news.ycombinator.com/item?id=41234490 , https://news.ycombinator.com/item?id=44168791 , https://news.ycombinator.com/item?id=38634111 , https://hn.algolia.com/?q=bolna
- https://www.producthunt.com/products/bolna/reviews
- https://www.g2.com/products/bolna-ai/reviews (403 to fetcher)
- https://aiindigo.com/blog/bolna-agent-studio-review-2026-the-reality-of-no-code-voice-ai
- https://www.ringg.ai/blogs/bolna-ai-pricing (competitor)
- https://dasha.ai/blog/bolna-ai-alternatives (competitor)
- https://www.sourcepulse.org/projects/1827738

Industry
- https://livekit.com/blog/adaptive-interruption-handling
- https://www.lorikeetcx.ai/blog/if-your-voice-ai-cant-wait-it-cant-listen
- https://soniox.com/wiki/turn-taking-barge-in
- https://www.twilio.com/en-us/blog/insights/ai-voice-agent-interruption-handling
- https://github.com/pipecat-ai/smart-turn
- https://arxiv.org/abs/2604.19151 , https://arxiv.org/html/2604.19151 (Voice of India benchmark)
- https://gnani.ai/resources/blogs/blog-code-switching-speech-recognition-hinglish-asr
- https://www.forasoft.com/blog/article/vapi-vs-retell-vs-custom
- https://retellai.com/blog/ai-voice-agent-pricing-full-cost-breakdown-platform-comparison-roi-analysis
- https://hamming.ai/blog/why-voice-agents-need-simulations-and-evaluations
- https://www.softwareseni.com/when-voice-agents-go-wrong-production-failure-modes-and-how-to-prevent-them/
