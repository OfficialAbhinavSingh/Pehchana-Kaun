# Bolna (bolna.ai / bolna.dev): Company Research

Research date: 2026-10-21. Read-only, public sources only. Every fact has an inline source. Anything marked **[INFERRED]** is my reading, not a published fact. Where sources disagree, the conflict is shown instead of being resolved quietly.

---

## 0. TL;DR

- **What it is:** A voice AI **orchestration** platform, branded "Voice AI Built for India". It wires STT + LLM + TTS + telephony into phone agents for inbound and outbound calls, with no-code (Agent Studio, agent builder, graph agents, workflows) and developer surfaces (REST API, CLI, MCP server, Skills, Web Call SDK). It also has an MIT-licensed open-source core. ([bolna.ai](https://www.bolna.ai), [docs: choose how to build](https://www.bolna.ai/docs/get-started/choose-how-to-build.md), [GitHub](https://github.com/bolna-ai/bolna))
- **Company:** Legal entity is Whismurwave Inc. ([bolna.ai footer](https://www.bolna.ai), [llms.txt](https://www.bolna.ai/llms.txt)). Founded 2024 by Maitreya Wagh (CEO) and Prateek Sachan (CTO). Operates from Bengaluru. YC **Fall 2025 (F25)**, primary partner Tom Blomfield. ([YC](https://www.ycombinator.com/companies/bolna-ai))
- **Funding:** **$6.3M seed** (about INR 57.3 Cr), announced 2026-01-20, led by **General Catalyst**, with YC, Blume Ventures, Orange Collective, Pioneer Fund, Transpose Capital, Eight Capital and angels. ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/), [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/)). No Series A found as of 2026-10-21.
- **Traction:** About $700K ARR at the Jan 2026 seed ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)). By July 2026: "nearly $175K in monthly revenue" (about $2.1M run-rate **[INFERRED]**), 2,500+ paying customers (about 100 enterprises), gross margin above 50%, profitable ([Inc42, 15 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)).
- **Pricing:** Pay-as-you-go from **$0.06/min (INR 5.52)**, falling to about 4.5¢ with larger top-ups. Pilot plan is $300 for 6,500 min or $500 for 12,000 min. Enterprise is custom. It is also sold on AWS Marketplace. ([pricing](https://www.bolna.ai/pricing), [AWS doc](https://www.bolna.ai/docs/enterprise/aws-marketplace.md))
- **"Symphony"** is **not a product**. It is Bolna's Voice AI **summit**: "Symphony 2026", 20 Nov 2026, The Lalit Ashok, Bengaluru. ([symphony](https://www.bolna.ai/symphony))
- **Direction [INFERRED]:** Bolna is moving up-market into BFSI and large enterprise (FDE teams, enterprise sales hires, AWS Marketplace, on-prem, India data residency, GFF presence). It is also becoming the default "model router/distribution layer" for India, with day-one integrations of new STT/TTS/LLM models, going deep on agent-native developer tooling (MCP, Claude connector, Skills, CLI), building ecosystem leadership through Symphony, and starting to talk about going global ("now for the world").

---

## 1. Company basics

| Field | Value | Source |
|---|---|---|
| Brand | Bolna / Bolna AI. `bolna.dev` and `www.bolna.dev` 301-redirect to `https://www.bolna.ai/` (checked 2026-10-20 via curl) | curl `-I https://bolna.dev` |
| Legal entity | Whismurwave Inc. ("© 2026 Whismurwave Inc.") | [bolna.ai](https://www.bolna.ai), [llms.txt](https://www.bolna.ai/llms.txt) |
| Founded | 2024 ("early 2024" per Inc42) | [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/), [Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform), [LinkedIn](https://www.linkedin.com/company/bolna-ai/) |
| Pre-history | The open-source `bolna` PyPI package has been around since at least **2024-01-01** (v0.6.3, author Prateek Sachan). It has 329 releases, the latest being v0.10.306 on 2026-10-20 | [PyPI JSON](https://pypi.org/pypi/bolna/json) |
| HQ / operations | Bengaluru (YC, job posts, press). LinkedIn lists HQ as **San Francisco, CA 94016**, which is consistent with a US Inc. parent **[INFERRED]**. One TechCrunch-derived snippet said "Mumbai-based"; the TechCrunch article text itself does not name a city | [YC](https://www.ycombinator.com/companies/bolna-ai), [LinkedIn](https://www.linkedin.com/company/bolna-ai/), [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| YC batch | Fall 2025 (F25). Primary partner Tom Blomfield. YC page shows team size 21 | [YC](https://www.ycombinator.com/companies/bolna-ai) |
| YC story | Rejected **five times** before F25 acceptance. YC's objection: "Indian enterprises are not going to pay, and you are not going to make money." | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| YC launch post | "Bolna: Voice AI for India", created 2025-09-30 | [YC launch](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india) |
| Headcount | YC: 21. Ashby job posts (Jul–Aug 2026): "Our team of ~25 is based in Bengaluru". LinkedIn: 62 associated members, size band 51–200, 17,692 followers (2026-10-20) | [YC](https://www.ycombinator.com/companies/bolna-ai), [Ashby: AI Solutions Engineer](https://jobs.ashbyhq.com/bolna/131e206f-3fd9-4905-9f4c-c3fdc4c32cc9), [LinkedIn](https://www.linkedin.com/company/bolna-ai/) |
| FDE team | "Nine forward-deployed engineers; adding 2-3 monthly" (Jan 2026) | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| Recognition | YourStory **Tech30 2025** (announced at TechSparks, Nov 2025; picked from 2,000+ applications) | [Bolna newsroom](https://www.bolna.ai/newsroom/bolna-ai-recognized-among-indias-most-promising-startups-in-yourstorys-tech30-2025) |

---

## 2. Founders and team

### Maitreya Wagh: Co-founder and CEO
- YC bio: "Engineer turned Consultant turned AI Founder. Building the Total Voice AI Ochestration for India." X handle [@maitreya_wagh](https://x.com/maitreya_wagh). ([YC](https://www.ycombinator.com/companies/bolna-ai))
- IIT Delhi alumnus, ex-Bain & Company, ex-Probo (Founder's Office). ([Bolna Tech30 PR](https://www.bolna.ai/newsroom/bolna-ai-recognized-among-indias-most-promising-startups-in-yourstorys-tech30-2025), [AIM](https://analyticsindiamag.com/ai-news-updates/bengaluru-voice-ai-startup-bolna-grabs-6-3-mn-to-enhance-vernacular-calls))
- **Forbes 30 Under 30 Asia** is claimed by third-party profiles ([everydev](https://www.everydev.ai/developers/whismurwave)). **Not verified** against a Forbes list page.
- Spoke on the Inc42 AI Summit 2026 panel "How Companies Are Using Voice AI To Reach The Next 500 Mn Users" (from a search-result snippet, not verified on Inc42) and on a Luma panel, "Voice AI Goes Global — A Panel on Multilingual & Multiregional Deployment" ([luma](https://luma.com/f4ge0txz)).

### Prateek Sachan: Co-founder and CTO
- YC bio: "Building the Voice API infrastructure platform for India. Previously built and scaled Zomato, Tata 1MG, BrowserStack & Atlassian." LinkedIn [prateek-sachan](https://linkedin.com/in/prateek-sachan), X handle [@xan_ps](https://x.com/xan_ps). ([YC](https://www.ycombinator.com/companies/bolna-ai))
- He is the top contributor to the open-source repo (1,288 commits) and the PyPI author. ([GitHub contributors](https://github.com/bolna-ai/bolna/graphs/contributors), [PyPI](https://pypi.org/pypi/bolna/json))
- Education conflict: [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/) calls Prateek the IIT Delhi alumnus. [Inc42 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/) and [everydev](https://www.everydev.ai/developers/whismurwave) say **both** founders are IIT Delhi. Bolna's own PR attributes IIT Delhi only to Maitreya.

### Others
- **Marmik Pandya** (GitHub `marmikcfc`, 461 commits, third-largest contributor) is listed as an early contributor ([GitHub](https://github.com/bolna-ai/bolna/graphs/contributors)). A search-result snippet says Bolna had "early support from Marmik Kartik Pandya". His formal role is **not confirmed** by any primary source.
- Other top OSS contributors: san0808 (570), deva-gopalani (173), puneet-bolna (95). ([GitHub API contributors](https://api.github.com/repos/bolna-ai/bolna/contributors))
- Team background per a job post: "IIT alumni with experience at Bain, Atlassian, Uber, Zomato, and LinkedIn". ([Ashby: Product Growth Lead](https://jobs.ashbyhq.com/bolna/bcd5eb6f-91e0-4f76-9b49-4a810b8324c6))

---

## 3. Funding

| Round | Date | Amount | Investors | Source |
|---|---|---|---|---|
| YC (standard deal; amount not disclosed) | PR dated 2025-08-31 | Not stated | Y Combinator | [Bolna PR](https://www.bolna.ai/newsroom/bolna-ai-raises-funding-from-y-combinator-to-revolutionize-voice-ai-for-indias-next-billion) |
| Seed | 2026-01-20 | **$6.3M** (INR 57.3 Cr) | **Lead: General Catalyst.** Existing: Y Combinator, Blume Ventures. New: Orange Collective, Pioneer Fund, Transpose Capital, Eight Capital. Angels: Aarthi Ramamurthy, Arpan Sheth, Sriwatsan Krishnan, Ravi Iyer, Taro Fukuyama | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/), [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/), [Entrackr](https://entrackr.com/snippets/voice-ai-startup-bolna-raises-63-mn-in-seed-round-led-by-general-catalyst-11017620) |

- Inc42 calls Blume an "existing investor", which implies Blume came in before the seed. **No standalone pre-seed announcement found.** ([Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/))
- Use of funds: expand engineering and deployment teams, build "proprietary AI/ML systems for vernacular voice", and harden enterprise infrastructure. ([Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/))
- Quotes ([Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform)):
  - Neeraj Arora (General Catalyst, India/MENA): Bolna is likely to become "the go-to platform whenever any business thinks about automating their calls with Voice AI."
  - Prateek Sachan: "We don't believe a single foundational model can meet enterprise Voice AI needs. Our orchestration layer routes every call to the best-fit model."
  - Tom Blomfield (YC): "lean into it. India has 22 official languages and hundreds of dialects."
- **Series A:** none found as of 2026-10-21 (searched "Bolna AI Series A 2026"; [seedtable](https://seedtable.com/companies/bolna-ai/funding-rounds/seed-2026-01) shows the seed as the latest round).

---

## 4. Traction and metrics (chronological; sources often conflict)

| Date | Metric | Source |
|---|---|---|
| H2 2024 | 1,300+ users across 12+ countries | [Blog: Bolna Turns One (2 May 2025)](https://www.bolna.ai/blog/bolna-turns-one-reflecting-on-a-year-of-growth-and-innovation) |
| May 2025 | First commercial deployment, about 1,500 calls/day | [Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform) |
| Pre-YC | More than $25K/month from pilots (search-result snippet; not verified on a primary page) | snippet of [mexc/TechCrunch repost](https://www.mexc.com/news/521627) |
| Aug–Sep 2025 | 500K+ call minutes/month; 250+ peak concurrent calls | [Bolna YC PR](https://www.bolna.ai/newsroom/bolna-ai-raises-funding-from-y-combinator-to-revolutionize-voice-ai-for-indias-next-billion), [YC launch](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india) |
| Sep 2025 → Dec 2025 | Monthly revenue $20K → $56K | [AIM](https://analyticsindiamag.com/ai-news-updates/bengaluru-voice-ai-startup-bolna-grabs-6-3-mn-to-enhance-vernacular-calls) |
| Jan 2026 | 200K+ calls/day; 1,050+ paying customers; about $700K ARR; 75% of revenue self-serve; 60–70% of call volume in English/Hindi; 2 large paying enterprises plus 4 in pilot | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| Jan 2026 | Monthly revenue about INR 50 lakh. Targets: FY26 INR 3–4 Cr, FY27 INR 45–50 Cr. Customer mix: ecommerce 40%, BFSI 20–25% | [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/) |
| Jan 2026 | Targets "$5 million ARR by June [2026]"; $3M ARR enterprise pipeline | [AIM](https://analyticsindiamag.com/ai-news-updates/bengaluru-voice-ai-startup-bolna-grabs-6-3-mn-to-enhance-vernacular-calls) |
| 15 Jul 2026 | "over 2,500 paying customers… including around 100 enterprises"; "more than 2,000 signups daily"; "nearly $175K in monthly revenue"; "gross margins above 50%"; "profitable"; "expects to reach an ARR of $5 Mn in the coming months" | [Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/) |
| Jul–Sep 2026 (job posts) | "1,050+ paying customers" (stale boilerplate); "profitable… more than 4 million minutes of real conversations every week"; "powering 33M+ calls every month" | [Ashby: Product Growth Lead](https://jobs.ashbyhq.com/bolna/bcd5eb6f-91e0-4f76-9b49-4a810b8324c6), [Ashby: PMM](https://jobs.ashbyhq.com/bolna/ba3456a1-3254-4067-8088-dec2508cb803) |
| Sep 2026 | "1M+ daily calls", "100+ enterprise clients" | [GFF 2026 page](https://www.bolna.ai/gff-2026) |
| 28 Sep 2026 | Engineering blog: "15 million call minutes a day" | [Blog: BigQuery→ClickHouse](https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes) |

**Consistency check [INFERRED]:** 33M calls/month and 1M+ calls/day agree with each other. But "4M minutes/week" (about 0.57M min/day) is far below "15M call minutes a day". Either the job post is stale, or the 15M figure counts something else (for example call-minute *records* or aggregate rows). Treat 15M/day as unverified. The most defensible current scale claim is roughly **1M calls/day**. Also note that the llms.txt still says "Monthly Call Volume: 400,000+ calls" and "900 concurrent call capability" ([llms.txt](https://www.bolna.ai/llms.txt)), which is clearly stale.

---

## 5. Product

### 5.1 Positioning
- Homepage: "Bolna AI: Voice AI Built for India… power thousands of inbound and outbound calls every minute with human-like, multilingual intelligence"; "1000+ Companies… across 10+ vernacular Indian languages including Hinglish, Hindi, Tamil, Telugu." OG image alt text: "The Complete Platform for Voice AI Orchestration". ([bolna.ai](https://www.bolna.ai))
- In TechCrunch's framing, Bolna is "an orchestration layer… akin to startups like Vapi, LiveKit, and VoiceRun, to suit the idiosyncrasies of interactions in India." ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/))
- Pivot history: Bolna first experimented with applications (an AI recruitment platform, CRM-focused products). Around **mid-2025** it moved from the application layer to the **orchestration layer**, after seeing that enterprises struggled to take voice AI from demo to production. ([Inc42 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)) The 2025 plan was "The Agents of Bolna": fine-tuned end-to-end workflow agents with about 300ms latency. ([Blog, May 2025](https://www.bolna.ai/blog/bolna-turns-one-reflecting-on-a-year-of-growth-and-innovation))
- AIM headline (Sep 2025): "Bolna AI's Bold Bet: Becoming the Distribution Layer for Every Voice Model" (listed on the [YC page](https://www.ycombinator.com/companies/bolna-ai) news section; the article URL returned 404 when fetched).

### 5.2 Product lineup (as of Oct 2026)
From [llms.txt](https://www.bolna.ai/llms.txt) and the [docs index](https://www.bolna.ai/docs/llms.txt):

| Product | What it is | First shipped | Source |
|---|---|---|---|
| Voice AI Platform / Dashboard | No-code agent builder with 7 config tabs, call history, batches | — | [platform-concepts](https://www.bolna.ai/docs/platform-concepts.md) |
| **Agent Studio** ("Auto Build") | Generates a call-ready agent from a brief or uploaded document in 5–8 minutes, "no prompt writing required" | Jun 13, 2026 changelog; Product Hunt launch Jul 21, 2026 (#10 of the day, about 152 upvotes) | [Jun 2026 changelog](https://www.bolna.ai/docs/changelog/june-2026.md), [studio doc](https://www.bolna.ai/docs/agent-setup/studio.md), [hunted.space](https://www.hunted.space/dashboard/bolna-2), [PH](https://www.producthunt.com/posts/bolna-agent-studio) |
| **Graph Agents** | Node-based flows with LLM, expression and event edges, router nodes, typed variables, a visual editor, per-node tools | May 4, 2026; visual editor Jun 22, 2026 | [May 2026](https://www.bolna.ai/docs/changelog/may-2026.md), [Jun 2026](https://www.bolna.ai/docs/changelog/june-2026.md) |
| **Workflows (beta)** | Multi-step outreach sequences: retry, WhatsApp fallback, sentiment branching | Revamped Nov 2025; chat/MCP-driven Aug 23, 2026; webhooks Sep 22, 2026 | [Aug 2026](https://www.bolna.ai/docs/changelog/august-2026.md), [Sep 2026](https://www.bolna.ai/docs/changelog/september-2026.md) |
| IVR agents | DTMF routing, no LLM | Jan 26, 2026 | [agent types](https://www.bolna.ai/docs/concepts/agent-types.md), [Jan 2026](https://www.bolna.ai/docs/changelog/january-2026.md) |
| Speech-to-speech agents | OpenAI Realtime and Gemini Live, single-model agents | Aug 31, 2026 | [Aug 2026](https://www.bolna.ai/docs/changelog/august-2026.md) |
| REST API | Bearer-key auth (`api.bolna.ai`) | — | [API intro](https://www.bolna.ai/docs/api-reference/introduction) |
| **Bolna CLI** (beta, Go) | Includes a full-screen TUI dashboard | Jul 19, 2026 | [Jul 2026](https://www.bolna.ai/docs/changelog/july-2026.md), [CLI docs](https://www.bolna.ai/docs/cli/introduction) |
| **MCP server** | `mcp.bolna.ai`; tools for agents, calls, batches, KBs, numbers, SIP trunks | Jul 17, 2026; "controls nearly your whole account" Aug 5, 2026 | [Jul 2026](https://www.bolna.ai/docs/changelog/july-2026.md), [Aug 2026](https://www.bolna.ai/docs/changelog/august-2026.md) |
| **Claude connector** | Listed in Claude's connector directory; manages agents and reads executions, but cannot place calls | Oct 9, 2026 | [Oct 2026](https://www.bolna.ai/docs/changelog/october-2026.md) |
| **Bolna Skills** | 20 open-source Agent Skills for Claude Code, Cursor, Codex (`npx skills add bolna-ai/skills`) | Jun 5, 2026 | [Jun 2026](https://www.bolna.ai/docs/changelog/june-2026.md), [GitHub skills](https://github.com/bolna-ai/skills) |
| **Web Call SDK** | Browser voice calls (built on Kamailio + FreeSWITCH) | Jul 23, 2026 | [Jul 2026](https://www.bolna.ai/docs/changelog/july-2026.md), [blog](https://www.bolna.ai/blog/browser-calls-kamailio-freeswitch) |
| n8n community node | `n8n-nodes-bolna` | 2026 | [docs](https://www.bolna.ai/docs/tutorials/n8n/community-node.md), [GitHub](https://github.com/bolna-ai/n8n-nodes-bolna) |
| Ask Bolna | In-dashboard AI assistant | — | [docs](https://www.bolna.ai/docs/ask-bolna.md) |
| Agents Library | Templates (recruitment, support, lead-gen, COD confirmation, cart abandonment, dentist booking…) | Sep 15, 2025 | [Sep 2025](https://www.bolna.ai/docs/changelog/september-2025.md), [llms.txt](https://www.bolna.ai/llms.txt) |
| On-prem / self-hosted | Docker/K8s; container images `ghcr.io/bolna-ai/{api_server, ws_server, telephone_server, q_manager, q_worker, arq_worker}` | Private beta Jun 2025; images Sep 2025 | [on-prem](https://www.bolna.ai/docs/enterprise/on-premise-deployments.md), [self-hosted release](https://www.bolna.ai/docs/changelog/self-hosted/september-2025.md) |
| Open-source core | `bolna-ai/bolna`, MIT, Python. 798 stars, 377 forks, 162 open issues, last push 2026-10-20. README: "End-to-end open-source voice agents platform"; hosted APIs and dashboard are "currently closed source"; "We are actively looking for maintainers." | — | [GitHub](https://github.com/bolna-ai/bolna) (gh API, 2026-10-21) |
| Beta Community, Builders community, Slack | — | — | [bolna.ai footer](https://www.bolna.ai) |

**Features listed on the homepage** ([bolna.ai](https://www.bolna.ai)): bulk calling at scale, custom API triggers mid-call, human-in-the-loop transfer, workflow integrations (n8n/Make/Zapier), 10+ languages, "<300ms latency", 20+ ASR/LLM/TTS models, enterprise plans with a "Forward Deployed service", India/USA data residency and on-prem, per-call model switching.

**Other differentiating features found in changelogs:**
- Truecaller verification (Feb 3, 2026)
- Noise cancellation (Jan 5, 2026)
- Ambient noise tracks (Mar 2026)
- Auto-retry and auto-reschedule (Jan 2026)
- Indian 140/160-series number purchase (Mar 3, 2026)
- DLT compliance applications (Sep 2025; API Oct 2026)
- AiSensy WhatsApp (Nov 26, 2025)
- Extractions with confidence and reasoning (Mar–Apr 2026)
- Conversation rating (Apr 2026)
- Web search tool via OpenAI/Exa/Firecrawl/Parallel (Oct 8, 2026)
- SIP trunks / BYO carrier (May and Oct 2026)

Sources: [Jan 2026](https://www.bolna.ai/docs/changelog/january-2026.md), [Feb 2026](https://www.bolna.ai/docs/changelog/february-2026.md), [Mar 2026](https://www.bolna.ai/docs/changelog/march-2026.md), [Apr 2026](https://www.bolna.ai/docs/changelog/april-2026.md), [Nov 2025](https://www.bolna.ai/docs/changelog/november-2025.md), [Oct 2026](https://www.bolna.ai/docs/changelog/october-2026.md).

### 5.3 Latency claims (inconsistent across Bolna's own pages)

| Claim | Where |
|---|---|
| "<300ms latency" | [Homepage](https://www.bolna.ai) |
| "sub-500ms latency" | [YC launch](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india), [YC PR Aug 2025](https://www.bolna.ai/newsroom/bolna-ai-raises-funding-from-y-combinator-to-revolutionize-voice-ai-for-indias-next-billion), [India companies page](https://www.bolna.ai/ai-voice-agent-companies-india) |
| "under 600ms" for the whole pipeline | [Docs: platform-concepts](https://www.bolna.ai/docs/platform-concepts.md) |
| "500 to 800 milliseconds" | [Blog: Bolna vs Vapi (May 2025)](https://www.bolna.ai/blog/bolna-vs-vapi-voice-ai-platform) |

Detailed per-call latency metrics have been exposed in the product since Nov 7, 2025 ([Nov 2025 changelog](https://www.bolna.ai/docs/changelog/november-2025.md)).

### 5.4 Languages
- **Configurable languages (18):** en, hi, bn, as, fr, gu, id, kn, ms, ml, mr, od, pa, es, ta, te, ur, nl.
- **Automatic mid-call detection** is tuned for English plus 10 Indian languages: hi, ta, te, kn, ml, mr, bn, gu, pa, ur.
- Source: [Docs: supported languages](https://www.bolna.ai/docs/customizations/supported-languages.md).
- Marketing figures vary: "10+ Indian languages" ([homepage](https://www.bolna.ai)), "20+ Languages" ([GFF](https://www.bolna.ai/gff-2026)), "50+ languages" ([llms.txt](https://www.bolna.ai/llms.txt)), "50+ accents" ([YC](https://www.ycombinator.com/companies/bolna-ai)).
- **Per-language provider choice:** for example Deepgram for English STT and Sarvam for Hindi, each language with its own prompt and voice. ([multilingual doc](https://www.bolna.ai/docs/customizations/multilingual-languages-support.md))
- Language-switching accuracy was improved so that a borrowed English word no longer flips the language (Sep 1, 2026). Calls can now start in a chosen language (Sep 30, 2026). ([Sep 2026](https://www.bolna.ai/docs/changelog/september-2026.md))

### 5.5 Supported providers (docs index, Oct 2026)
Source: [docs llms.txt](https://www.bolna.ai/docs/llms.txt), [integrations page](https://www.bolna.ai/integrations).
- **STT:** Deepgram (Nova-2/3, Flux), OpenAI Realtime (gpt-realtime-whisper), Azure, AssemblyAI (Universal-3 / 3.6 Pro), ElevenLabs Scribe, Gladia, Sarvam (Saarika/Saaras v2.5–v4), Smallest (Pulse), Soniox, Gemini 3.5 Transcribe.
- **LLM:** OpenAI (GPT-5.6 incl. Sol/Terra/Luna, GPT-5.5, GPT-5.4, mini/nano), Azure OpenAI, Anthropic (Claude Sonnet 5, Opus 4.8, Haiku 4.5), Google Gemini (2.5, 3.x), DeepSeek (V4 Flash/Pro), OpenRouter, Perplexity.
  - Custom/BYO inference: Baseten, Cerebras, Fireworks, Groq, Modal, Nebius, Simplismart, Together.
- **TTS:** ElevenLabs (Flash/Turbo v2.5, v3, v4 Turbo), Cartesia (Sonic 3–3.6, voice cloning), Deepgram, Sarvam (Bulbul v2/v3/v4 Flash), Smallest (Lightning), Rime, AWS Polly, Azure, Soniox, **Kalpa Labs** (kalpa-tts-1, Oct 20 2026), **Maya Research** (Maya 2 Native), and custom OpenAI-compatible TTS (Oct 12 2026).
- **Speech-to-speech:** OpenAI Realtime, Gemini Live.
- **"Preferred models"** are bundled in the flat 6¢ rate:
  - STT: Deepgram nova-2/3, Azure, Sarvam saarika/saaras, ElevenLabs scribe_v2_realtime.
  - LLM: OpenAI gpt-4.1-mini, 4o-mini, 5-mini, 5.4-mini/nano, 5.6-luna, plus their Azure equivalents.
  - TTS: ElevenLabs flash/turbo/multilingual/v3-conversational, Sarvam bulbul v2–v4-flash, Cartesia sonic, Azure neural, maya.
  - Source: [preferred models](https://www.bolna.ai/docs/pricing/preferred-models.md).
- **OpenAI partnership:** "Bolna was the only official launch partner from India" for GPT-Realtime-2 and GPT-Realtime-Whisper (May 12, 2026). It claims GPT-Realtime-Whisper had 12.5% lower WER than the other models it tested on Hindi, Tamil and Telugu. ([blog](https://www.bolna.ai/blog/bolna-launches-openai-realtime-voice-ai-models-india))

### 5.6 Telephony
- **Native:** Twilio ("for calls outside India"), Plivo, Exotel and Vobiz ("for calls within India"). ([telephony doc](https://www.bolna.ai/docs/telephony-integrations.md))
- **Integration dates:** Exotel Oct 15, 2025 ([Oct 2025](https://www.bolna.ai/docs/changelog/october-2025.md)); Vobiz Jan 27, 2026 ([Jan 2026](https://www.bolna.ai/docs/changelog/january-2026.md)).
- **SIP / BYOT:** Acefone, Airtel SIP Trunking, Exotel SIP, Plivo Zentrunk, Twilio Elastic SIP, Telnyx, Vonage, generic SIP. Supports TCP/TLS/SRTP (May 2026) and custom carrier headers (Oct 2026). ([integrations](https://www.bolna.ai/integrations), [llms.txt](https://www.bolna.ai/llms.txt), [May 2026](https://www.bolna.ai/docs/changelog/may-2026.md), [Oct 2026](https://www.bolna.ai/docs/changelog/october-2026.md))
- **Bolna-sold numbers:** Indian numbers require a DLT/compliance application backed by CIN and GST documents. ([Oct 2026 changelog](https://www.bolna.ai/docs/changelog/october-2026.md))
- Exotel and Plivo are Diamond sponsors of Symphony, which points to close telco partnerships **[INFERRED]**. ([symphony](https://www.bolna.ai/symphony))

---

## 6. Docs and API structure (bolna.ai/docs, hosted on Mintlify)

- **Docs home:** `https://www.bolna.ai/docs`. Older `docs.bolna.ai` links appear in the README. There are AI-readable indexes: [llms.txt](https://www.bolna.ai/docs/llms.txt), llms-full.txt (about 1.9 MB), and an [AGENTS.md](https://www.bolna.ai/docs/agents-md.md). The docs have 165 Voice Agent pages and 156 API Reference pages, plus an OpenAPI spec at `/docs/api-reference/openapi.yml`. ([docs llms.txt](https://www.bolna.ai/docs/llms.txt))
- **Key concepts** ([glossary](https://www.bolna.ai/docs/concepts/glossary.md), [coming-from-another-platform](https://www.bolna.ai/docs/get-started/coming-from-another-platform.md)):
  - **Agent:** an assistant. Each agent has one `conversation` task made of `toolchain` + `tools_config` + `task_config`.
  - **Execution:** one call record.
  - **Batch:** a campaign.
  - **Extractions:** post-call structured data. These replaced the legacy extraction/custom analytics, which are now retired.
  - **Graph agent:** the equivalent of a "squad" or multi-agent flow.
  - **BYOT:** bring your own telephony or SIP trunk.
  - **Wallet:** prepaid credits.
  - **Sub-accounts:** enterprise multi-tenancy.
  - **Dispositions:** call outcome labels.
- **Call lifecycle gotcha:** wait for the `completed` status rather than `call-disconnected` before reading cost or recording. ([migration doc](https://www.bolna.ai/docs/get-started/coming-from-another-platform.md))
- **API groups** (page counts from the [API index](https://www.bolna.ai/docs/_llms/api-reference.txt)): agent (17), workflows (16), trunks (15), workflow-campaigns (14), sip-trunks (9), batches (9), user (8), dispositions (8), sub-accounts (7), phone-numbers (6), knowledgebase (5), extraction-categories (5), executions (5), compliance (5), providers (4), workflow-executions (3), voice (3), violations (3), inbound (3), calls (3), workflow-webhooks (2). It also has auth, errors, pagination, limits and rate-limiting pages.
- **Example call:** `POST https://api.bolna.ai/call` with `agent_id`, `recipient_phone_number`, `from_phone_number`, `user_data`, and a Bearer token. ([homepage code sample](https://www.bolna.ai))
- **Concurrency:** trial accounts get 2 concurrent calls; paid accounts start at 10 and scale with usage; enterprise is elevated. Calls over the limit are queued, and queues are split evenly per telephony provider. Inbound calls are unlimited. ([concurrency doc](https://www.bolna.ai/docs/pricing/outbound-calling-concurrency.md))
- **API rate limiting** was introduced Feb 7, 2026 ([Feb 2026](https://www.bolna.ai/docs/changelog/february-2026.md)); some endpoints are capped at 500 requests/minute ([API index](https://www.bolna.ai/docs/_llms/api-reference.txt)).
- **Security** ([security doc](https://www.bolna.ai/docs/concepts/security.md)):
  - TLS 1.2+.
  - Default region AWS **us-east-1**. India residency on **ap-south-1 (Mumbai)**.
  - **No HMAC signing** of webhooks or tool calls; trust relies on IP allow-listing three fixed IPs.
  - VAPT rated "A+".
  - For SOC 2 / HIPAA / GDPR the doc says "contact support". The [AWS Marketplace doc](https://www.bolna.ai/docs/enterprise/aws-marketplace.md), however, says the Enterprise tier "includes SOC 2 Type II, ISO 27001, and DPDP compliance certifications". These two pages contradict each other.

---

## 7. Pricing

Source: [bolna.ai/pricing](https://www.bolna.ai/pricing), [llms.txt](https://www.bolna.ai/llms.txt), [call-pricing doc](https://www.bolna.ai/docs/pricing/call-pricing.md).

| Plan | Price | Notes |
|---|---|---|
| Pay-as-you-go | **$0.06/min (INR 5.52)**, down to about **4.5¢ (INR 4.15)** with larger top-ups | Credits from $10 to $5,000. $5 free credit for new accounts. Covers STT+LLM+TTS on preferred models; **telephony and platform fee are added per minute** |
| Pilot | $300 for 6,500 min (about 4.6¢), or $500 for 12,000 min (about 4.2¢) | 25 concurrent calls, enterprise features, one month of WhatsApp support plus 1:1 calls with a POC; billed in 30-second pulses |
| Enterprise | Custom | Committed volume, custom integrations, dedicated account manager, FDE support |
| AWS Marketplace | Pilot $300/mo for 6,000 min (about $0.05); Enterprise $900/mo for 20,000 min (about $0.045); annual plans up to 750K min at about $0.04 | Live since Sep 2, 2026 ([AWS doc](https://www.bolna.ai/docs/enterprise/aws-marketplace.md), [Sep 2026 changelog](https://www.bolna.ai/docs/changelog/september-2026.md), [AWS listing](https://aws.amazon.com/marketplace/pp/prodview-b2zrltwmqdxey)) |

- **Cost model:** five components (STT by seconds, LLM by tokens, TTS by characters, telephony by minutes, platform fee by duration). On the Basic plan, using BYOK for any component drops the call off the flat rate. ([call-pricing](https://www.bolna.ai/docs/pricing/call-pricing.md))
- **Older or inconsistent price claims:** "$0.02/min" ([India companies page, updated Oct 11 2026](https://www.bolna.ai/ai-voice-agent-companies-india)); "Calls start at just $0.03 per minute" ([Bolna vs Vapi blog, May 2025](https://www.bolna.ai/blog/bolna-vs-vapi-voice-ai-platform)).
- **Business model:** usage-based, charged per minute of orchestration. Gross margin is above 50%. ([Inc42 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/))

---

## 8. Customers, case studies, use cases

**Logos and case studies**
- Homepage logos: Futwork, Physics Wallah, Knot Dating, GoKwik, Shop Labs, Spinny, Awign, Hyreo, Hypothesis. ([bolna.ai](https://www.bolna.ai))
- Case studies ([bolna.ai](https://www.bolna.ai), [llms.txt](https://www.bolna.ai/llms.txt)):

| Customer | Use case | Results claimed |
|---|---|---|
| **Awign** | Automated technical screening interviews | Average 6.8 min, longest 17.1 min, 65% cost reduction |
| **Hyreo** | 24x7 candidate helpline | 10,000+ conversations, 96.55% call-minute growth |
| **GoKwik** | Cart recovery, surveys, collections, WhatsApp links | 400,000+ unique engagements, 250+ peak concurrent calls |
| **Hypothesis** | Recovery calls | INR 2.5 Cr+ revenue recovered, 300+ SKUs, 24-hour turnaround |
| **Futwork** | National campaign | 10K+ calls/day, 250+ concurrent |

- Customer pages: [awign](https://www.bolna.ai/customer-story/awign), [hyreo](https://www.bolna.ai/customer-story/hyreo), [gokwik](https://www.bolna.ai/customer-story/gokwik), [hypothesis](https://www.bolna.ai/customer-story/hypothesis), [futwork](https://www.bolna.ai/customer-story/futwork).

**Customers named in press**
- Varun Beverages, Spinny, Snabbit. ([Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform), [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/))
- Alibaba, GoKwik, BiteSpeed, Meritto. ([Inc42 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/))
- BFSI logos at GFF 2026: IIFL, Navi, Cashfree Payments, Skydo, Ignosis AI, NJ Wealth, craftAI. ([GFF](https://www.bolna.ai/gff-2026))

**Use cases**
- Reminders (EMI and collections), customer support, lead qualification, announcements, recruitment screening, cart abandonment, COD confirmation, appointment booking (healthcare), loan and credit card sales. ([bolna.ai](https://www.bolna.ai), [llms.txt](https://www.bolna.ai/llms.txt))

**Industries**
- BFSI, Ecommerce/D2C, EdTech, HealthTech, Hospitality, Logistics, Recruitment. ([bolna.ai](https://www.bolna.ai), [Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform))
- Mix: ecommerce about 40%, BFSI 20–25% ([Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/)).

---

## 9. Competitors and positioning

### How Bolna positions itself
- **India-first orchestration.** It handles linguistic complexity ("20+ Languages, 200+ Accents/Dialects") and cost sensitivity ("every rupee matters") on the cost side, using pre-recorded inserts and routing across providers. ([YC launch](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india))
- **Model-agnostic.** "doesn't depend on a single model, so enterprises can easily switch when there is a better model available" ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)). A blog post, "Should your engineering team build Voice AI stack?", argues against building in-house because of model churn ([blog](https://www.bolna.ai/blog/should-your-engineering-team-build-voice-ai-stack)).
- **Head-to-head blog pages**, all from 2025:
  - [Bolna vs Vapi](https://www.bolna.ai/blog/bolna-vs-vapi-voice-ai-platform): Bolna for non-technical teams, Vapi for code-first developers; Bolna "$0.03/min" vs Vapi "about $0.08".
  - [Bolna vs Retell](https://www.bolna.ai/blog/bolna-vs-retell-voice-ai-platform).
  - [Bolna vs Bland](https://www.bolna.ai/blog/bolna-vs-bland-ai).
- **"Top Indian AI Voice Agents" page** ([updated Oct 11 2026](https://www.bolna.ai/ai-voice-agent-companies-india)) ranks Bolna #1 against Haptik, Yellow.ai, ElevenLabs, Google Cloud AI, Cognigy, Kore.ai, PolyAI and Verloop.io. It notably omits the direct Indian voice-native rivals (Sarvam, Gnani, Ringg, Smallest).
- **Migration guide** for teams leaving "another voice AI platform", which maps assistants and squads onto Bolna concepts. It is aimed at Vapi/Retell switchers **[INFERRED]**. ([doc](https://www.bolna.ai/docs/get-started/coming-from-another-platform.md))

### Competitor landscape (brief, with sources)

| Competitor | Type | Notes | Source |
|---|---|---|---|
| Vapi | Global dev-first orchestration | Named by TechCrunch as a peer. $20M Series A (Dec 2024) at about $130M post-money. Build plan $0.05/min hosting plus provider costs | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/), [Sacra](https://sacra.com/c/vapi) |
| LiveKit, VoiceRun | Infra / orchestration | Named by TechCrunch as peers | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| Retell AI | Global voice agent platform | About $80M annualized revenue in Aug 2026 (Sacra). Voice engine $0.07–0.08/min | [Sacra](https://sacra.com/c/retell-ai) |
| Bland AI | Global | Bolna comparison page only | [blog](https://www.bolna.ai/blog/bolna-vs-bland-ai) |
| Ringg AI | Indian voice agents | $15.5M Series A (Jan + Aug 2026, Peak XV led the extension). Customers include CRED, Flipkart, Shiprocket. Article names Bolna as a competitor | [Inc42](https://inc42.com/?p=545709) |
| Smallest.ai | Indian voice models + agents | $8M seed (per the Inc42 Ringg article). **Also a Bolna integration partner** (Pulse STT, Lightning TTS) | [Inc42](https://inc42.com/?p=545709), [integrations](https://www.bolna.ai/integrations), [smallest.ai/integrations/bolna](https://smallest.ai/integrations/bolna) |
| Sarvam AI | Indian models + agent platform | **Partner as well as competitor**: a Bolna STT/TTS provider and a Gold sponsor of Symphony | [integrations](https://www.bolna.ai/integrations), [symphony](https://www.bolna.ai/symphony), [edesy](https://edesy.in/blog/sarvam-ai-competitors-india-2026) |
| Gnani.ai, Skit.ai, Haptik, Yellow.ai | Indian incumbents | Named as alternatives in third-party roundups | [edesy](https://edesy.in/blog/gnani-ai-alternatives-2026), [Bolna page](https://www.bolna.ai/ai-voice-agent-companies-india) |
| Synthflow, Ultravox | Global | **No Bolna-authored comparison found** | — |

**[INFERRED] Strategic posture:** Bolna partners with model makers (Sarvam, Smallest, Kalpa, Maya, ElevenLabs, Cartesia, Deepgram, OpenAI) instead of competing with them, and sells itself as the neutral routing and distribution layer. Its real fight is with other orchestrators (Vapi, Retell, Ringg) and with in-house builds, on price (6¢ all-in on preferred models vs roughly $0.10–0.31 all-in on Vapi per [Sacra](https://sacra.com/c/vapi)), on India telephony and compliance (DLT, 140/160 numbers, Exotel/Vobiz, Truecaller), and on Indic language handling.

---

## 10. News, launches, events (timeline)

| Date | Event | Source |
|---|---|---|
| 2024-01-01 | Earliest PyPI release found (`bolna` 0.6.3) | [PyPI](https://pypi.org/pypi/bolna/json) |
| 2024-08-24 | `bolna-ai/bolna` GitHub repo created (current org repo) | [GitHub](https://github.com/bolna-ai/bolna) |
| 2024-09-17 | "Bolna Debuts on Product Hunt" | [newsroom](https://www.bolna.ai/newsroom/bolna-debuts-on-product-hunt-with-voice-ai-agents-for-automated-conversations) |
| 2025-05-02 | "Bolna Turns One" blog post | [blog](https://www.bolna.ai/blog/bolna-turns-one-reflecting-on-a-year-of-growth-and-innovation) |
| 2025-05 | First commercial deployment; a Product Hunt listing dated May 19, 2025 (214 upvotes) | [PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform), [PH](https://www.producthunt.com/posts/bolna-agent-studio) |
| 2025-06/07 | On-prem private beta; India data residency | [Jun 2025](https://www.bolna.ai/docs/changelog/june-2025.md), [Jul 2025](https://www.bolna.ai/docs/changelog/july-2025.md) |
| 2025-08-31 | YC funding PR (F25) | [newsroom](https://www.bolna.ai/newsroom/bolna-ai-raises-funding-from-y-combinator-to-revolutionize-voice-ai-for-indias-next-billion) |
| 2025-09 | Anthropic LLM support, Sarvam and AssemblyAI STT, template library, self-hosted container release | [Sep 2025](https://www.bolna.ai/docs/changelog/september-2025.md) |
| 2025-09-30 | YC Launch post | [YC launch](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india) |
| 2025-10-15 | Exotel integration | [Oct 2025](https://www.bolna.ai/docs/changelog/october-2025.md) |
| 2025-11-05 | YourStory Tech30 2025 | [newsroom](https://www.bolna.ai/newsroom/bolna-ai-recognized-among-indias-most-promising-startups-in-yourstorys-tech30-2025) |
| 2026-01-20 | $6.3M seed led by General Catalyst | [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/) |
| 2026-02-03 | Truecaller verification | [Feb 2026](https://www.bolna.ai/docs/changelog/february-2026.md) |
| 2026-05-04 | Graph Agents | [May 2026](https://www.bolna.ai/docs/changelog/may-2026.md) |
| 2026-05-12 | OpenAI Realtime launch partner (India) | [blog](https://www.bolna.ai/blog/bolna-launches-openai-realtime-voice-ai-models-india) |
| 2026-06 | Agent Studio, Bolna Skills, graph visual editor | [Jun 2026](https://www.bolna.ai/docs/changelog/june-2026.md) |
| 2026-07 | MCP server (Jul 17), CLI beta (Jul 19), Web Call SDK (Jul 23); Agent Studio on Product Hunt, #10 of the day (Jul 21) | [Jul 2026](https://www.bolna.ai/docs/changelog/july-2026.md), [hunted.space](https://www.hunted.space/dashboard/bolna-2) |
| 2026-07-15 | Inc42 profile: $175K MRR, 2,500+ customers, profitable | [Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/) |
| 2026-08 | Workflows via chat/MCP, BYO LLM endpoint, speech-to-speech agents, Maya TTS | [Aug 2026](https://www.bolna.ai/docs/changelog/august-2026.md) |
| 2026-09-02 | Listed on AWS Marketplace | [Sep 2026](https://www.bolna.ai/docs/changelog/september-2026.md) |
| 2026-09-08..11 | Global Fintech Fest 2026, Mumbai (Booth Z1) | [GFF page](https://www.bolna.ai/gff-2026) |
| 2026-09-28 | Engineering blog: BigQuery → ClickHouse, "15M call minutes a day", 6x cost cut | [blog](https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes) |
| 2026-10-09 | Bolna listed as a Claude connector | [Oct 2026](https://www.bolna.ai/docs/changelog/october-2026.md) |
| 2026-10-15 | SIP trunks: bring your own carrier | [Oct 2026](https://www.bolna.ai/docs/changelog/october-2026.md) |
| 2026-11-20 (upcoming) | **Symphony 2026** summit, Bengaluru | [symphony](https://www.bolna.ai/symphony) |

### Symphony 2026 (the "Symphony" brand)
Source: [bolna.ai/symphony](https://www.bolna.ai/symphony).
- **Format:** "India's flagship Voice AI summit", Fri 20 Nov 2026, The Lalit Ashok, Bengaluru. Expects 1,000+ attendees, 42+ speakers, 3 halls. Agenda covers keynotes, panels, product launches, awards, a buildathon and an expo.
- **Speakers:** Aarthi Ramamurthy, Dr. Manish Gupta (Google DeepMind), Srinivas Narayanan (ex-OpenAI), Grey Baker (YC), Sanjay Jain (Gates Foundation), Sachin Bhatia (Exotel).
- **Sponsors:**
  - Diamond: Google Cloud, Truecaller for Business, Exotel, Plivo.
  - Gold: Kalpa Labs, Sarvam.
  - Also: OpenAI, NVIDIA Inception, Deepgram.
- **Perks:** $100 Bolna credits, 3 months of Wispr Flow, 2,500 Sarvam credits.
- **Ticket price:** not visible in the page HTML.
- **History:** no prior edition found. The Marketing Manager job post calls it "India's first large-scale Voice AI conference… and this is just the beginning" ([Ashby](https://jobs.ashbyhq.com/bolna/6e4bc8c9-c2c4-4458-bd40-4aa8433b4316)).

**Podcasts and interviews:** no dedicated podcast episode found in this pass. Panels are listed in §2.

---

## 11. Hiring

**Careers page:** `bolna.ai/careers` 301-redirects to **Ashby** ([jobs.ashbyhq.com/bolna](https://jobs.ashbyhq.com/bolna)). The YC jobs page shows 0 openings ([YC jobs](https://www.ycombinator.com/companies/bolna-ai/jobs)). Wellfound was not checked (it needs login or JS); no listing was found via search.

**Open roles** (Ashby public API, 2026-10-21; 7 roles, all on-site, no compensation published):

| Role | Location | Posted | What it reveals | Link |
|---|---|---|---|---|
| AI Solutions Engineer | Bengaluru | 2026-07-03 | Prompt and tool engineering for customer agents; red-teaming; vernacular testing; "no heavy coding required". Mentions Vapi and ElevenLabs as tools candidates may know | [Ashby](https://jobs.ashbyhq.com/bolna/131e206f-3fd9-4905-9f4c-c3fdc4c32cc9) |
| Conversation Quality Analyst (intern) | Bengaluru | 2026-08-18 | They are building **LLM-as-judge call evals** and quantitative signal detection (barge-in, interruptions), with humans annotating in Label Studio and dashboards in Metabase. Multilingual annotators wanted | [Ashby](https://jobs.ashbyhq.com/bolna/ee75c3c6-ae7e-4ef8-842c-431295325d05) |
| Enterprise Lead | **Delhi** | 2026-09-04 | Leads a team of FDEs on the largest enterprise deployments, works with CXOs. 5+ years in consulting or enterprise | [Ashby](https://jobs.ashbyhq.com/bolna/3781a40c-abca-4c5a-881d-69b85ad08735) |
| Marketing Manager | Bengaluru | 2026-09-08 | Social, content, and running Symphony and future events | [Ashby](https://jobs.ashbyhq.com/bolna/6e4bc8c9-c2c4-4458-bd40-4aa8433b4316) |
| Product Growth Lead | Bengaluru | 2026-09-29 | Lifecycle, activation and PLG funnel. Cites "profitable… 4 million minutes… every week" | [Ashby](https://jobs.ashbyhq.com/bolna/bcd5eb6f-91e0-4f76-9b49-4a810b8324c6) |
| Product Marketing Manager | Bengaluru | 2026-10-13 | First PMM. Asks for "competitive intelligence, sales enablement, and battlecards" and "comparison pages". Cites "33M+ calls every month" | [Ashby](https://jobs.ashbyhq.com/bolna/ba3456a1-3254-4067-8088-dec2508cb803) |
| Enterprise Sales (BFSI) | Bengaluru | 2026-10-15 | Hunter for new BFSI logos (banks, NBFCs, insurers, fintechs). Sells "voice agents, workflows and analytics" | [Ashby](https://jobs.ashbyhq.com/bolna/386b48dd-4e7f-4c01-a0cc-ce6da16ca63b) |

**Other listing:** a "Founding ML Engineer" role (data pipelines for Indian-language telephony audio, fine-tuning, eval benchmarks, PyTorch) appears on the aggregator [joinsaarthi](https://joinsaarthi.com/jobs/bolna/founding-ml-engineer-bengaluru/c24c2677-4dd0-4c72-9843-0e6b510753c2). It is **not** on Ashby now, so its date and status are unknown.

**What the roles signal [INFERRED]:**
1. **Up-market and BFSI push:** an Enterprise Lead with an FDE team in Delhi, a BFSI sales hunter, and a GFF booth. Self-serve was 75% of revenue in Jan 2026; they are deliberately building the enterprise motion.
2. **Marketing is being built from zero:** the PMM, Marketing Manager and Growth Lead were all posted Sep–Oct 2026. The PMM post admits "too few people outside our existing customers know about [our products]."
3. **Quality and evals as a moat:** LLM-as-judge plus human verification of turn-taking and barge-in signals.
4. **Possible proprietary models:** the founding ML role and the seed use of funds ("proprietary AI/ML systems for vernacular voice") suggest Bolna may train its own Indic models (for example turn detection or ASR fine-tunes). This is not yet visible in the product.
5. **No open core-engineering roles** right now. Engineering velocity (near-daily changelog entries, 300+ PyPI releases) suggests the eng team is already in place.

---

## 12. Strategy signals and where Bolna is heading [INFERRED unless cited]

1. **Enterprise and BFSI.** Evidence: AWS Marketplace with SOC 2 / ISO 27001 / DPDP claims ([AWS doc](https://www.bolna.ai/docs/enterprise/aws-marketplace.md)), on-prem, India residency on ap-south-1, sub-accounts with concurrency pools, compliance APIs, GFF, and the BFSI sales and Enterprise Lead hires. Goal stated in press: "strengthen outbound enterprise sales" ([Inc42 Jul 2026](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)).
2. **Neutral model router / "distribution layer for every voice model".** Evidence: day-one integrations (OpenAI Realtime launch partner, Eleven v4, Cartesia 3.6, Gemini 3.5, Sarvam v4, Kalpa, Maya) and the "preferred models" bundle, which shows they negotiate provider rates and earn margin on the spread. Model makers appear as Symphony sponsors.
3. **Agent-native developer surface.** MCP server, Claude connector, 20 Skills, CLI, AGENTS.md and llms.txt, all shipped Jun–Oct 2026. The bet is that AI coding agents will build voice agents, and Bolna wants to be the default target.
4. **Moving from a single agent to a workflow/outcomes platform.** Graph agents, then workflows (multi-channel retries, WhatsApp fallback), extractions, dispositions, analytics. The BFSI job sells "voice agents, workflows and analytics".
5. **Ecosystem ownership through Symphony.** Positioning as the convener of Indian voice AI ("this is just the beginning"), co-branded with Google Cloud, Truecaller, Exotel, Plivo and Sarvam.
6. **Going global.** Job posts changed from "built for India" to "built for India — and now for the world" (Aug 2026, [Ashby](https://jobs.ashbyhq.com/bolna/ee75c3c6-ae7e-4ef8-842c-431295325d05)). There is a US Inc. with an SF HQ on LinkedIn, Twilio for non-India calls, and languages such as Spanish, French, Indonesian, Malay and Dutch. No international GTM hires seen yet.
7. **Financial position:** profitable with gross margin above 50% ([Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)). Revenue went from about $56K/mo (Dec 2025) to about $175K/mo (Jul 2026) on the cited figures. If they reach their own "$5M ARR" target, a **Series A in late 2026 or 2027** is likely. This is purely an inference; no evidence of a raise was found.
8. **Risks:**
   - Webhook security relies on IP allow-listing only, with no HMAC ([security doc](https://www.bolna.ai/docs/concepts/security.md)).
   - Public metrics are inconsistent (§4, §5.3), and the compliance pages contradict each other (§6).
   - Gross margin depends on provider pricing.
   - Partners such as Sarvam and Smallest also sell agent platforms.

---

## 13. Not found or unverified
- Exact YC investment amount, and any pre-seed or Blume round date and amount.
- Maitreya Wagh's Forbes 30 Under 30 Asia listing (claimed by third parties only).
- Marmik Pandya's formal role.
- Symphony ticket prices.
- Wellfound listing.
- Podcast interviews.
- The full AIM "distribution layer" article (404 when fetched).
- A Bolna-authored comparison against Synthflow, Ultravox, Sarvam (as an agent platform) or Gnani.
- The basis of the "15M call minutes a day" figure.

---

## Sources

**Bolna-owned**
- https://www.bolna.ai
- https://www.bolna.ai/pricing
- https://www.bolna.ai/newsroom
- https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform
- https://www.bolna.ai/newsroom/bolna-ai-raises-funding-from-y-combinator-to-revolutionize-voice-ai-for-indias-next-billion
- https://www.bolna.ai/newsroom/bolna-ai-recognized-among-indias-most-promising-startups-in-yourstorys-tech30-2025
- https://www.bolna.ai/newsroom/bolna-debuts-on-product-hunt-with-voice-ai-agents-for-automated-conversations
- https://www.bolna.ai/symphony
- https://www.bolna.ai/gff-2026
- https://www.bolna.ai/integrations
- https://www.bolna.ai/ai-voice-agent-companies-india
- https://www.bolna.ai/llms.txt
- https://www.bolna.ai/docs/llms.txt
- https://www.bolna.ai/blog/llms.txt
- https://www.bolna.ai/docs/_llms/api-reference.txt

**Bolna docs**
- https://www.bolna.ai/docs/platform-concepts.md
- https://www.bolna.ai/docs/concepts/agent-types.md
- https://www.bolna.ai/docs/concepts/glossary.md
- https://www.bolna.ai/docs/concepts/security.md
- https://www.bolna.ai/docs/get-started/choose-how-to-build.md
- https://www.bolna.ai/docs/get-started/what-it-costs.md
- https://www.bolna.ai/docs/get-started/coming-from-another-platform.md
- https://www.bolna.ai/docs/pricing/call-pricing.md
- https://www.bolna.ai/docs/pricing/preferred-models.md
- https://www.bolna.ai/docs/pricing/outbound-calling-concurrency.md
- https://www.bolna.ai/docs/enterprise/aws-marketplace.md
- https://www.bolna.ai/docs/enterprise/data-residency.md
- https://www.bolna.ai/docs/enterprise/on-premise-deployments.md
- https://www.bolna.ai/docs/telephony-integrations.md
- https://www.bolna.ai/docs/customizations/multilingual-languages-support.md
- https://www.bolna.ai/docs/customizations/supported-languages.md
- https://www.bolna.ai/docs/changelog/self-hosted/september-2025.md

**Bolna changelog**
- https://www.bolna.ai/docs/changelog/october-2026.md
- https://www.bolna.ai/docs/changelog/september-2026.md
- https://www.bolna.ai/docs/changelog/august-2026.md
- https://www.bolna.ai/docs/changelog/july-2026.md
- https://www.bolna.ai/docs/changelog/june-2026.md
- https://www.bolna.ai/docs/changelog/may-2026.md
- https://www.bolna.ai/docs/changelog/april-2026.md
- https://www.bolna.ai/docs/changelog/march-2026.md
- https://www.bolna.ai/docs/changelog/february-2026.md
- https://www.bolna.ai/docs/changelog/january-2026.md
- https://www.bolna.ai/docs/changelog/november-2025.md
- https://www.bolna.ai/docs/changelog/october-2025.md
- https://www.bolna.ai/docs/changelog/september-2025.md

**Bolna blog**
- https://www.bolna.ai/blog/bigquery-to-clickhouse-15m-call-minutes
- https://www.bolna.ai/blog/bolna-launches-openai-realtime-voice-ai-models-india
- https://www.bolna.ai/blog/bolna-turns-one-reflecting-on-a-year-of-growth-and-innovation
- https://www.bolna.ai/blog/bolna-vs-vapi-voice-ai-platform
- https://www.bolna.ai/blog/bolna-vs-retell-voice-ai-platform
- https://www.bolna.ai/blog/bolna-vs-bland-ai
- https://www.bolna.ai/blog/should-your-engineering-team-build-voice-ai-stack
- https://www.bolna.ai/blog/browser-calls-kamailio-freeswitch

**Jobs**
- https://jobs.ashbyhq.com/bolna (via https://api.ashbyhq.com/posting-api/job-board/bolna)
- https://joinsaarthi.com/jobs/bolna/founding-ml-engineer-bengaluru/c24c2677-4dd0-4c72-9843-0e6b510753c2

**YC**
- https://www.ycombinator.com/companies/bolna-ai
- https://www.ycombinator.com/companies/bolna-ai/jobs
- https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india

**Press**
- https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/
- https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/
- https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/
- https://analyticsindiamag.com/ai-news-updates/bengaluru-voice-ai-startup-bolna-grabs-6-3-mn-to-enhance-vernacular-calls
- https://entrackr.com/snippets/voice-ai-startup-bolna-raises-63-mn-in-seed-round-led-by-general-catalyst-11017620
- https://india.entrepreneur.com/news-and-trends/voice-ai-startup-bolna-raises-usd-63-mn-funding-led-by/502062

**Other profiles**
- https://www.linkedin.com/company/bolna-ai/
- https://www.everydev.ai/developers/whismurwave
- https://seedtable.com/companies/bolna-ai/funding-rounds/seed-2026-01

**Product Hunt**
- https://www.producthunt.com/posts/bolna-agent-studio
- https://www.hunted.space/dashboard/bolna-2

**Code**
- https://github.com/bolna-ai/bolna
- https://github.com/bolna-ai/skills
- https://github.com/bolna-ai/n8n-nodes-bolna
- https://pypi.org/pypi/bolna/json

**Competitors**
- https://sacra.com/c/vapi
- https://sacra.com/c/retell-ai
- https://inc42.com/?p=545709
- https://edesy.in/blog/sarvam-ai-competitors-india-2026
- https://edesy.in/blog/gnani-ai-alternatives-2026
- https://smallest.ai/integrations/bolna

**Marketplace and events**
- https://aws.amazon.com/marketplace/pp/prodview-b2zrltwmqdxey
- https://luma.com/f4ge0txz
