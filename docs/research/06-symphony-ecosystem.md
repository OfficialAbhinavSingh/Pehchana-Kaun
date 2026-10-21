# Symphony 2026 (Bolna) — Ecosystem Map for Buildathon Idea Selection

Researched 2026-10-21. Scope: non-sponsor partners + speaker companies. The 6 buildathon sponsors (Plivo, Exotel, Sarvam, Cartesia, Deepgram, Kalpa Labs) are only touched where a *speaker* belongs to them.
Convention: every fact carries an inline source URL. Anything marked **[INFERRED]** is my opinion/synthesis, not a sourced fact.

---

## 0. Event facts (from bolna.ai, scraped from server-rendered HTML)

- Date/venue: Fri 20 Nov 2026, The Lalit Ashok, Bengaluru; "1000+ attendees, 42+ speakers, 03 stages" — https://www.bolna.ai/symphony
- Stages: **Sur** (Kalinga Hall, main: keynotes, firesides, product launches, awards), **Abhyas** (Grand Ballroom, buildathon/hackathon), **Mehfil** (Siddhartha Hall, expo booths/live demos) — https://www.bolna.ai/symphony
- Registration includes $100 Bolna credits, 3-month Wispr Flow subscription, 2,500 Sarvam credits — https://www.bolna.ai/symphony (FAQ)
- **No agenda / session list / talk titles are published.** `/symphony/agenda` returns the generic shell; the only agenda-related string in the JS bundles is a T&C line reserving the right to change "agenda, speakers or sessions without notice" (layout chunk) — https://www.bolna.ai/symphony
- Partner logos on page (file names in HTML): google-cloud, truecaller-business, exotel, plivo, kalpa-labs, sarvam, wispr-flow, simplismart, cartesia, deepgram, vobiz, smallest, agnost-ai, openai, nvidia-inception — https://www.bolna.ai/symphony
- Buildathon: virtual Oct 15–31 build, submit Oct 31, shortlist Nov 3, interviews Nov 5–7, results Nov 8 (top 10 get Symphony tickets), top 3 pitch at Abhyas on Nov 20; prizes ₹50k + YC interview with Grey Baker / ₹40k / ₹30k; "No tracks… as long as it has a voice component"; their own examples: voice tutor for kids, phone helpdesk for a local clinic, **"a voice layer on an app you already built"**, **"a hands-free tool for drivers or field workers"** — https://www.bolna.ai/symphony/buildathon
- AI host "Mr. Bolna" is callable at +91 22 6953 9260 — https://www.bolna.ai/symphony/speakers

### 0.1 Full published speaker list (14 + AI host)

Only 14 humans are published despite the "42+" claim (speaker thumbnails in HTML = exactly these 15 incl. mr-bolna). No talk titles are listed. Source for every row: https://www.bolna.ai/symphony/speakers

| # | Name | Title (as listed) | Org | Bio notes from page |
|---|---|---|---|---|
| 1 | Aarthi Ramamurthy | Founder | Schema Ventures | Founder & GP; ex-Meta/Microsoft/Netflix; Aarthi & Sriram Show |
| 2 | Dr. Manish Gupta | Senior Director | Google DeepMind | Leads research teams in India & Japan; ex-VideoKen, IBM, Xerox |
| 3 | Srinivas Narayanan | Former CTO B2B Applications | OpenAI | Scaled ChatGPT + API; 10+ yrs Meta; advised AI startups at General Catalyst |
| 4 | Grey Baker | Partner | Y Combinator | GP at YC; ex-Figma Director of Product; co-founded Dependabot; **judges buildathon winner's YC interview** |
| 5 | Akarsh Shrivastava | Partner | General Catalyst | Invests AI, consumer, defence, government; ex-Elevation SaaS/AI lead |
| 6 | Prasanna Krishnamoorthy | Managing Partner | Upekkha | Accelerator for Indian B2B / vertical AI going global; AIBoomi founding volunteer |
| 7 | Anuja Dhawan | Founder | Dubverse (now Exotel) | Leads AI Products & Growth at Exotel; Dubverse dubbing in 30+ languages |
| 8 | Tanuj Bhojwani | Former Head | People+AI | Now South Park Commons; ex-iSPIRT; co-author *The Art of Bitfulness* with Nandan Nilekani |
| 9 | Sachin Bhatia | Co-founder | Exotel | Co-founder & CGO; co-founded Ameyo |
| 10 | Madhav Krishna | Founder & CEO | Vahan AI | Recruitment platform for blue/grey-collar workers |
| 11 | Sudarshan Kamath | Founder & CEO | Smallest.ai | Real-time voice models & agents for enterprise |
| 12 | Prashant Shishodia | Co-founder | Kalpa Labs (sponsor) | YC-backed generalist speech models; ex-Google Assistant NLU |
| 13 | Sanjay Jain | Director of DPI | Gates Foundation | Key India Stack contributor; ex-UIDAI Chief PM; led Google Map Maker |
| 14 | Shrikant Venkataramani | AI Research | Pocket FM | Contributed to **SAGA**, Pocket FM's agentic framework turning scripts into produced audio episodes; ex-Murf, Amazon |
| — | Mr. Bolna | AI host | Bolna | "Previously a customer care expert, recruiter, salesperson, receptionist and professional reminder-giver" |

---

## 1. Non-sponsor partners

### Google Cloud (Diamond)
- Gemini Live now supports 25 Indian languages/dialects incl. Sanskrit, Bhojpuri, Maithili (Google I/O Connect India, 15 Jul 2026) — https://india.entrepreneur.com/technology/google-i-o-connect-india-2026-agentic-ai-enterprise-and-other-key-announcements
- Gemini on Google Distributed Cloud inside Indian data centres for regulated/public sector; CAPSEM agent-sandboxing open-sourced — same source
- Quote, Preeti Lobana (Country Manager, Google India): "India's builders are already deploying AI faster than almost anywhere else…our focus is on providing infrastructure and guardrails" — same source
- "Over 40% of Gemini's Indian language users already rely on voice interactions" — https://blog.google/intl/en-in/company-news/outreach-initiatives/google-for-india-2024-bringing-ai-to-every-indian-across-our-products/
- **Beckn + Gemini:** Google Cloud India MD Bikram Bedi unveiled an open-source Gemini agent framework for Beckn-enabled open networks so users can discover and transact (seeds, electronics, jobs, courses) "using their voice on any network-compliant app in the language of their choice" — https://www.afaqs.com/news/digital/google-google-for-india-2024-gemini-live-7239517
- 2026 agentic partnerships highlighted: boAt, Cropin, Pine Labs (consumer hardware, agri, commerce) — https://yourstory.com/2026/09/google-cloud-brings-gemini-deeper-into-india-businesses (search snippet; page 403 to fetch)

### Truecaller for Business (Diamond)
- Verified Business Caller ID: brand name, logo, green highlight, verified badge and optional **call reason** shown before pickup; case studies cite 30–83% higher answer rates; ~$20/month per number — https://support.myoperator.com/portal/en/kb/articles/what-should-i-do-if-i-need-to-change-my-name-displayed-in-truecaller-20-9-2025
- Bolna already exposes Truecaller verification for its agents; call reasons include "Customer Support, Delivery Confirmation, Front Desk, Recruitment, Prospect Check"; verification takes 1–3 business days — https://www.bolna.ai/docs/truecaller-verification
- **Secure Calls** (Jun 2025): anti-spoofing "automated call signing process that performs a secure backend handshake with Truecaller to verify the caller's identity on a call-by-call basis"; first customer NoBroker — https://mobileidworld.com/truecaller-launches-secure-calls-anti-spoofing-feature-for-business-users-in-india/
- **AI Call Scanner**: detects AI-synthesized vs human voice; English first, Hindi in progress — https://www.cxodigitalpulse.com/introducing-the-worlds-first-ai-call-scanner-by-truecaller-the-fastest-most-accurate-ai-voice-scam-detection-system
- Truecaller Assistant (consumer AI call screener) supports English, Hindi, Hinglish — https://www.voicendata.com/truecaller-introduces-truecaller-assistant-in-india-to-curb-spam-fraud-calls
- Use-case verticals: service/support, ride-hailing, logistics/delivery, sales, fraud management; Swiggy/Urban Company early clients — https://www.medianews4u.com/truecaller-crosses-the-500-customer-milestone-for-its-business-offering/
- **[INFERRED]** Truecaller's tension point for 2026: it simultaneously flags AI voices as risky (Call Scanner) and sells verification to businesses running AI agents. Anything that makes *legitimate AI-agent calls* provably trustworthy lands squarely on their roadmap.

### Wispr Flow (Silver)
- India = 14% of installs but ~2% of IAP revenue (Oct 2025–Apr 2026); Hinglish model in beta, Android launch; India usage ~50:50 desktop/mobile vs 80:20 in US; India price ₹320/mo with target ₹10–20/mo; 2 linguistics PhDs; plan to expand beyond Hindi in 12 months — https://techcrunch.com/2026/05/09/voice-ai-in-india-is-hard-wispr-flow-is-betting-on-it-anyway/
- CEO Tanay Kothari: "The biggest thing is people are starting to use it more in personal apps" (messaging/social, Hindi-English mix) — same source
- Counterpoint's Neil Shah: "India is the ultimate stress test for voice AI" — same source

### Simplismart (Silver)
- Inference/deployment platform, 150+ open models incl. speech (Whisper), dedicated/VPC/on-prem — https://aiagentstore.ai/ai-agent/simplismart
- Reported (May 2026) NVIDIA in talks to lead ~$20M round at ~$100M valuation — https://www.newskart.com/nvidia-in-talks-to-lead-simplismarts-20m-round-what-it-could-mean-for-indias-ai-infra-race/
- LiveKit plugin; sub-400ms voice agent pipeline (Whisper + Gemma 3 4B + Orpheus TTS) — https://docs.simplismart.ai/guides/livekit
- **[INFERRED]** They want buildathon projects that run open/fine-tuned speech models on their infra, i.e. anything where cost-per-minute or a custom small model is the punchline.

### Vobiz (Silver)
- Founded 2025 (Suman Gandham, Vikash Srivastava), Bengaluru; AI-native telephony: DIDs, SIP trunking, bidirectional WebSocket audio in 20ms frames, <80ms P95 telephony latency; scaled from ~100k calls/month to 10M+/day; customers Sarvam, Bolna, Razorpay, RevRag, Smallest.ai, Navana — https://inc42.com/startups/how-vobiz-ai-is-building-the-backbone-of-indias-voice-ai-boom/
- Problem statement: legacy telephony "built for human-to-human calls… not built for AI-to-human conversations"; with AI, dropped audio means the model "may interpret it incorrectly and respond with something completely different" — same source
- Roadmap: WhatsApp, SMS, RCS; AMD/transcription value-adds — same source

### Smallest.ai (Associate; speaker Sudarshan Kamath)
- Lightning TTS, Pulse STT, Electron SLM for voice agents; Voice 4.0 + **Hydra** asynchronous architecture; $21M total funding — https://indiacsr.in/smallest-ai-21-million-next-gen-enterprise-voice-ai/
- Kamath: "The industry has focused on making models larger when the real challenge is architectural" — same source; "While I'm speaking to you, you're already thinking, and you might interrupt me…" (full-duplex thinking) — https://techcrunch.com/?p=3148682
- Kamath (seed announcement): "enterprises are stuck with outdated tools that frustrate customers and overburden agents" — https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/smallest.ai-raises-8m-seed-to-redefine-enterprise-voice-ai-1084349

### Agnost AI (Associate) — what it is
- YC **S26**, San Francisco; founders Shubham Palriwala (CEO, ex-Cisco, first hire at Formbricks) and Parth Ajmera (CTO, IIT Madras) — https://www.ycombinator.com/companies/agnost-ai
- Product: analytics for chat **and voice** agents — finds silent failures, drift, hallucinations, frustration, hidden feature requests, churn signals; clusters them and turns them into evals/fixes; OTel-native, "three lines of code"; >1M messages/day analyzed; Product Hunt #3 on 25 Aug 2026 — https://www.hunted.space/product/agnost-ai
- Newer positioning: turn production traces into training data for workload-specific models ("22.9% higher task success, 90.2% lower median latency, 94.5% lower cost" vs frontier in one case study) — https://www.ycombinator.com/companies/agnost-ai

### OpenAI (logo; speaker Srinivas Narayanan is ex-OpenAI)
- GPT-Live-1.1 (16 Oct 2026) added two native Hindi voices (Neer, Leher); India priorities listed: Hindi-English code-mixing, Android-first, intermittent connectivity, native pronunciation — https://letsdatascience.com/news/openai-expands-chatgpt-voice-features-for-india-ec6a9572
- Narayanan previously relayed Indian-founder feedback on high developer cost and weak Indian-language performance (Global IndiaAI Summit 2024) — https://indiaai.gov.in/article/openai-s-srinivas-narayanan-praises-bhashini-and-expresses-support-for-india-s-ai-mission (cert expired at fetch; via search snippet)
- He left OpenAI (Apr 2026) to return to India to be with his aging parents — https://www.businesstoday.in/amp/technology/news/story/who-is-srinivas-narayanan-the-iit-madras-alumnus-behind-chatgpt-growth-leaving-openai-526317-2026-04-18

### NVIDIA Inception (logo)
- Nemotron family used by Indian firms for voice assistants/agents across 22 languages; Gnani building 14B speech-to-speech on Nemotron Speech (15x inference-cost cut, 10M+ calls/day); CoRover deployment Feb 2026 — https://blogs.nvidia.com/blog/india-ai-mission-infrastructure-models/
- Vahan fine-tuned Nemotron 3 Nano for a faster/cheaper voice recruiter — https://yourstory.com/ai-story/vahanai-uses-nvidia-ai-to-speed-up-blue-collar-hiring (search snippet)

---

## 2. Speaker organisations

### Google DeepMind India — Dr. Manish Gupta
- Mumbai Tech Week (May 2026): language- and voice-led solutions as principal adoption path; "culturally rooted AI responses matter", English-then-translate is insufficient; dataset creation is a bottleneck; multimodal voice+visual+text is next frontier — https://letsdatascience.com/news/deepmind-discusses-india-first-ai-and-project-vaani-f09d8b50
- Dec 2025: 22 Gemma models on AIKosh; Project Vaani speech data for 110 Indian languages; $2M to IIT Bombay Indic language hub — https://letsdatascience.com/news/google-rolls-out-india-built-ai-models-globally-e8f58383
- Project Vaani (Google + IISc + ARTPARK): goal 154,000 hrs from all 773 districts; ~31,270 hrs audio + ~2,067 hrs transcribed open-sourced across 109 languages — https://www.gktoday.in/google-deepmind-launches-ai-project-for-125-indian-languages/ (via search snippet); Project Morni targets 125 Indian languages — https://businessworld.in/article/google-deepminds-project-morni-to-digitise-preserve-125-indian-languages-531232

### Gates Foundation — Sanjay Jain (Director, DPI)
- Listed in Gates' 2026 Goalkeepers expert guide under **"AI Voice + Language Equity"** — https://www.gatesfoundation.org/ideas/media-center/gk-2026-press-kit/experts
- 21 Sep 2026: 60-org coalition (Anthropic, Google, Amazon, Microsoft, NVIDIA, OpenAI Foundation…) to make AI work in underrepresented languages and voices; 5-year goal of 3.4B people; four workstreams: open language-data infra, benchmarks, tools for builders, privacy/consent/data sovereignty; **voice named a particular priority** (education, health, agri, financial and public services) — https://www.local10.com/business/2026/09/21/gates-foundation-launches-coalition-to-build-more-representative-language-data-sets-for-ai/ and https://letsdatascience.com/news/gates-foundation-coalition-targets-ais-language-data-gap-8d851904
- Coalition stresses "concrete resources with clear provenance, permissions and benchmarks" over broad language-support claims — https://letsdatascience.com/news/gates-foundation-coalition-targets-ais-language-data-gap-8d851904
- No direct 2026 quote from Jain on voice found. **[INFERRED]** His lens = India Stack design: open protocols, consent, interoperability, cost at population scale. Pitch anything as "a reusable rail", not an app.

### People+AI / EkStep — Tanuj Bhojwani (former head)
- People+AI = EkStep initiative for population-scale AI; also runs Open Cloud Compute (micro data-centre network) — https://siliconcanals.com/?p=48471
- EkStep Voice AI program: **VoicERA**, open-source end-to-end voice stack hosted on BHASHINI, vendor-neutral across telephony/ASR/TTS/LLM, benchmark "less than ₹1 per minute"; Listen At Scale (Jan–Feb 2026): 20 orgs, 5 lakh minutes each, ~5M citizens, 7.4M minutes; Impact At Scale (100 days, 50+ use cases); production examples MahaVISTAAR, Amul's Sarlaben (3.6M dairy farmers), **BlueDots voice job-matching** (10,000+ local openings surfaced in Ghaziabad vs <100 on national platforms) — https://voiceai.ekstep.org/
- VoicERA launched on BHASHINI at India AI Impact Summit 2026 with MeitY/DIBD, EkStep, COSS, IIIT-B, AI4Bharat — https://www.digitalindia.gov.in/press_release/voicera-launched-on-bhashini-national-infrastructure-at-india-ai-impact-summit-2026/
- Listen at Scale shifted outreach from "rigid, one-way channels like SMS blasts and IVR" to two-way voice that turns speech into structured data — https://www.callmissed.com/en/blog/listen-at-scale-how-sarvam-ekstep-and-ai4bharat-are-revolutionizing-multilingual
- Bhojwani bio: "storyteller who codes"; co-author with Nilekani — https://el.player.fm/series/forbes-india-the-startup-fridays-podcast/startup-fridays-s5-ep5-ai-for-india-how-peopleai-was-born

### Vahan AI — Madhav Krishna
- Voice-first AI recruiter for blue/grey-collar; 500k+ hires/yr; 80–90% of recruitment workflow automated; recruiters handle 3x candidates; challenges = STT/TTS integration, latency at volume, per-interaction cost; **next: adjacent services for low-income workers incl. micro-investment** — https://frontiertech.niti.gov.in/story/voice-ai-at-scale-powering-half-a-million-jobs-a-year-in-india/
- $10M Series B (Khosla, YC); 8 Indian languages planned — https://india.entrepreneur.com/news-and-trends/blue-collar-recruitment-platform-vahanai-raises-10/480091

### Pocket FM — Shrikant Venkataramani
- AI powers 93% of catalog, 99% of new content; 80x cheaper production; $500M ARR run-rate; Pocket Saga microdramas fully AI-produced (TechCrunch via) — https://aiunderstanding.org/news/pocket-fm-doubles-revenue-to-500m-as-ai-produces-93-of-audio-content
- OpenAI API partnership for 300k+ creators — https://letsdatascience.com/news/pocket-fm-integrates-openai-apis-for-storytelling-0b41eedf
- Speaker page: SAGA = agentic script→produced-audio framework — https://www.bolna.ai/symphony/speakers

### Dubverse → Exotel — Anuja Dhawan
- Apr 2026 acqui-hire; Dhawan leads **Conversation Quality Analytics (CQA)**: analyze 100% of interactions in real time instead of sample QA; Exotel CEO: "Most enterprises today lack visibility into the majority of their customer conversations." — https://exotel.com/newsroom/exotel-acqui-hires-dubverse-voice-ai-team/
- Exotel's Sachin Bhatia (Aug 2026): "Models eventually will be like electricity"; India needs "frontier-minus-one" models; "bot-first, human-as-backup" is flawed; Harmony = one human supervises many bots; conversation intelligence should replace NPS; ~40% of India's voice AI conversations run on Exotel — https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/

### Y Combinator — Grey Baker (Fall 2026 RFS, relevant items) — https://www.ycombinator.com/rfs
- **Proving You're Human**: deepfake CFO call ($25M); voice clones cheap → rebuild trust for calls, messages, transactions
- **AI for the Aging Population**: conversational voice interfaces; Alexa frustrates seniors; coordinate family caregivers
- **New Operating Systems for the Physical World**: "80% of the global workforce doesn't sit at a desk"; coordinate AI agents + field workers
- **AI-Powered Consumer Products for 1 Billion People**
- Also The Primer (kids tutor — excluded by brief), Multiplayer AI, AI-Native Compliance

### General Catalyst — Akarsh Shrivastava
- Led Bolna's $6.3M seed; Akarsh: "Bolna allows you the freedom to choose any model and has a stack behind it…" — https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/
- GC $5B India commitment (Feb 2026): "India's greatest AI opportunity is diffusion, deploying AI at population scale"; founders solve "billion-person complexity first" — https://pulse2.com/general-catalyst-commits-5-billion-to-india-over-five-years/amp/

### Schema Ventures — Aarthi Ramamurthy
- $20M solo-GP fund; industrial software, robotics, factories, construction, logistics, workflow intelligence, dev tools; backs "exceptional outsider founders"; four portfolio cos in voice agents/infra incl. Bolna — https://www.fortune.com/2025/05/20/aarthi-ramamurthy-schema-ventures-20-million-fund (and search snippet)
- Angel in Bolna's seed — https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform

### Upekkha — Prasanna Krishnamoorthy
- 50+ pre-seed AI investments in 18 months; "India becoming the use case capital of the world in AI"; wants "vertical workflows, not horizontal platforms"; winners are "system integrators" — https://cxotoday.com/corner-office/from-vanilla-saas-to-vertical-ai-how-upekkha-is-shaping-the-future-of-b2b-startups-1/

### Bolna itself (host)
- 200k+ calls/day; 60–70% of volume English/Hindi; mostly SMB self-serve (Spinny, Snabbit); Maitreya Wagh quoting investors early on: "…Indian enterprises are not going to pay" — https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/

### DPI rails relevant to the room (context, not a partner)
- NPCI preparing agentic payments on UPI ("Unified Agent Protocol" expected at GFF Sep 2026), built on **UPI Circle** (delegate payment authority) + **Reserve Pay** (block funds, ₹10k / 90 days cap today); spending limits, audit trails, identity checks — https://www.thestar.com.my/tech/tech-news/2026/09/01/india-preparing-rollout-of-agentic-payments-on-upi-sources-say
- Hello UPI: voice UPI payments via apps, telecom calls, IoT, built on Bhashini — https://www.dtnext.in/lifestyle/technology/npci-launches-new-products-users-can-make-voice-enabled-upi-payments-734695

---

## 3. Intersections (problems 3+ orgs in the room care about)

| Theme | Who cares (evidence above) | Why it lights up the room [INFERRED] |
|---|---|---|
| **A. Trust in AI-agent calls** (is this caller legit, is it AI, why is it calling) | Truecaller (Verified ID, call reason, Secure Calls, AI Call Scanner), YC RFS "Proving You're Human" (Grey Baker judges), Bolna (Truecaller integration), Exotel/Vobiz/Plivo (carriers), Gates/Jain (safe DPI) | Every agent vendor's pickup rate depends on it; Truecaller is a Diamond sponsor and has no public "AI agent disclosure" standard yet |
| **B. Voice as the front door to DPI rails** (UPI agentic payments, Beckn/ONDC discovery) | Google Cloud (Beckn+Gemini voice agent), Sanjay Jain (India Stack), Tanuj/EkStep (VoicERA, Beckn lineage), GC "diffusion" thesis, NPCI agentic UPI | Brand-new rails (UPI Circle/Reserve Pay for agents) with almost no voice demos yet |
| **C. Non-desk / blue-collar workforce** | Vahan (voice recruiter, next = financial services for workers), EkStep BlueDots, YC "OS for the physical world", Truecaller call reason "Recruitment", Bolna's own "hands-free tool for drivers or field workers" example, Schema (logistics/construction) | Biggest real call volume in India; Bolna explicitly listed it |
| **D. Quality/eval of Indic code-mixed voice agents in production** | Agnost (failure analytics), Exotel CQA (Anuja), Simplismart/Smallest/NVIDIA (custom small models), DeepMind (datasets bottleneck), Gates coalition (benchmarks), OpenAI (code-mixing eval) | Infra-heavy room; every vendor needs this, nobody owns Indic-specific evals |
| **E. Family delegation / aging parents** | YC RFS aging, Srinivas Narayanan (left OpenAI for parents), UPI Circle (delegation), Truecaller (scam protection for elders), Gemini Live (40% voice) | Emotional + technical; ties A and B together |
| **F. Voice-native consumer content** | Pocket FM (AI audio), Wispr Flow (personal apps, Hinglish), Gemini Live, YC "1B consumer", OpenAI Hindi voices | Consumer flavor in an enterprise-heavy room |

---

## 4. Idea seeds (avoiding the excluded list)

Each seed lists who in the room it hits. All framing is **[INFERRED]**.

1. **"Signed Agent Calls": a disclosure + verification layer for AI voice agents.**
   The agent says it's an AI at the start of the call, sends a signed call-reason token (Truecaller-style call reason + Secure-Calls-style per-call signature), and the callee can say "verify" mid-call. That triggers an out-of-band check (SMS/WhatsApp link, or a call back to a registered number) confirming the brand, the purpose and a one-time phrase. Ships as a Bolna/Pipecat middleware plus a public registry.
   *Hits:* Truecaller, YC "Proving You're Human" (Grey Baker), Exotel/Vobiz/Plivo, Bolna, Gates/DPI trust. Different from a scam honeypot because it equips **legit** callers rather than baiting fraudsters.

2. **Parent Line: a family-delegated voice concierge for elderly parents.**
   The parent calls one number and speaks a request in their language (mobile recharge, electricity bill, cab, reorder groceries). The agent carries it out on UPI Circle-style delegated limits set by the child and sends the child a WhatsApp summary. Callbacks come from a Truecaller-verified ID. No health features.
   *Hits:* YC aging RFS, Srinivas Narayanan's personal story, NPCI agentic UPI, Truecaller, Google Gemini Live, General Catalyst "diffusion". Strongest seed for an emotional on-stage pitch.

3. **Voice-to-Beckn: a "call to discover and book" agent for open networks.**
   A feature-phone user calls and asks for something like "a plumber near Whitefield tomorrow" or "a skilling course in Kannada". The agent issues Beckn search/select/confirm calls and closes with a UPI Reserve Pay mandate, read back aloud. This is essentially Google Cloud's 2024 Beckn+Gemini promise rebuilt on today's telephony.
   *Hits:* Google Cloud, Sanjay Jain, Tanuj/People+AI, EkStep, Vobiz/Exotel. Stay away from farmer inputs and rentals to keep clear of the exclusions.

4. **Shift-Talk: hands-free voice logging for field and gig workers.**
   A delivery rider, technician or site worker talks during or after a shift ("drop 14 failed, gate locked", "used 3 bags cement"). The agent asks structured follow-ups, writes the result into the employer's system or a sheet, and flags anomalies to the supervisor. This matches Bolna's own buildathon example word for word.
   *Hits:* Bolna example list, YC "OS for the physical world", Schema Ventures (logistics/construction), Vahan, Wispr Flow (voice instead of typing), Upekkha (vertical workflow).

5. **Voice Work-Passport: a portable, verified work history built over calls.**
   A worker builds a skills and experience profile by talking. The agent then calls past employers or supervisors for voice reference checks (from a Truecaller-verified "Recruitment" caller ID) and issues a shareable credential, DigiLocker/verifiable-credential style. Vahan's next step into worker financial services needs exactly this kind of trust signal.
   *Hits:* Vahan, EkStep BlueDots, Sanjay Jain (credentials/DPI), Truecaller, YC physical-world RFS. It is not a recruiter bot; it is the trust layer under one.

6. **Indic Call-Replay Lab: regression testing for code-mixed voice agents.**
   Feed in real or sample call recordings. It clusters failures (Hinglish/Tanglish switches, numbers, addresses, barge-ins, noisy lines), synthesizes adversarial test calls with different accents, noise and code-mix ratios using sponsor TTS, replays them against any agent endpoint, and scores the results. Output is an eval report plus a regression suite.
   *Hits:* Agnost, Exotel CQA (Anuja), Simplismart/Smallest/NVIDIA (fine-tuning loop), DeepMind (datasets bottleneck), Gates coalition (benchmarks), OpenAI (code-mixing eval). Best for an infra-heavy judging panel; weakest stage demo.

7. **Talk-back Audio Series: interactive audio drama over a phone call.**
   A Pocket FM-style serialized story where the listener speaks to characters or picks branches by voice, playable over a plain phone call or WhatsApp voice. Kept to entertainment, no tutoring.
   *Hits:* Pocket FM (SAGA), Wispr Flow (consumer voice), OpenAI Hindi voices, Gemini Live, YC "1B consumer". The only consumer-entertainment option, so it stands out among B2B demos.

8. **App-to-Phone Bridge: turn any app's API or MCP server into a multilingual phone number.**
   Point it at an OpenAPI spec or MCP server and get a callable number where users without smartphones can do the app's core actions by voice in 10+ languages, with Truecaller-verified outbound confirmations. This literally answers Bolna's "voice layer on an app you already built".
   *Hits:* Bolna, Vobiz/Exotel/Plivo, Google (A2A/ADK), Smallest/Simplismart, Upekkha. Risk: reads as a horizontal tool, which Upekkha says it doesn't want.

**Top 3 for this room [INFERRED]:** #2 Parent Line (emotional, mixes DPI + trust, YC RFS match), #1 Signed Agent Calls (Diamond sponsor Truecaller + YC RFS + every telephony vendor), #4 Shift-Talk (matches Bolna's own example, and blue-collar is the biggest real call volume in the room).

---

## 5. Gaps / caveats
- Only 14 of the "42+" speakers are public; no agenda or talk titles. Re-check https://www.bolna.ai/symphony/speakers before finalizing, because more names (likely from Sarvam, Plivo, Truecaller, Google Cloud) will probably appear.
- No direct 2026 voice quotes found for Sanjay Jain, Tanuj Bhojwani, Aarthi Ramamurthy or Grey Baker. Their angles above are inferred from org programs and RFS text.
- The Google Cloud Beckn+Gemini agent framework is from Oct 2024. I found no 2026 follow-up on its status.
- VoicERA launch date: the gov page's event is India AI Impact Summit 2026, which voiceai.ekstep.org lists as Feb 15–20, 2026. A summarizer said "Oct 14, 2026", which looks wrong.
- Firecrawl was out of credits. Research used WebSearch/WebFetch, and some pages (YourStory, exchange4media) returned 403, so those points rest on search snippets.
