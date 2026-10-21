# Past Bolna + India voice-AI hackathons: what won, what's overdone, where the gaps are

Researched 2026-10-21 for the Bolna Symphony Buildathon (submissions close Oct 31, 2026).
Rules for this file: every fact has an inline source. My own opinions are tagged **[INFERRED]**. "not found" means I searched and found nothing public.

---

## 0. The target event: Bolna Symphony Buildathon (current)

- Build window Oct 15–31, 2026. Submit by Oct 31. Shortlist Nov 3, interviews Nov 5–7, results/top-10 Nov 8, grand finale Nov 20 at Abhyas hall, The Lalit Ashok, Bengaluru (https://www.bolna.ai/symphony/buildathon, https://buildathon.bolna-ai.lovable.app/symphony/buildathon)
- Prizes: 1st ₹50,000 + YC interview with Grey Baker (YC partner); 2nd ₹40,000 + travel; 3rd ₹30,000 + travel; top 10 get free Symphony tickets (same sources)
- Teams of 1–4. Voice must be a core component. Existing projects can add a voice feature. Only the top 3 travel (https://buildathon.bolna-ai.lovable.app/symphony/buildathon)
- No tracks. Example ideas on the page: voice tutor for kids, phone clinic helpdesk, adding voice to an existing app, hands-free tools for drivers/field workers (same source)
- Sponsors: Plivo, Exotel, Sarvam, Cartesia, Deepgram, Kalpa Labs (same source)
- **No published judging criteria.** The organisers say "We review every application and shortlist the strongest builds." The submission form asks for: a description of 200 characters max, a link (repo, live app or demo), and a deck or video link (Google Drive or Luma only). Per a participant's notes: https://github.com/jaygautam-creator/dadi/blob/main/docs/SUBMISSION.md
- Symphony summit, Nov 20, 1000+ attendees. Speakers include Grey Baker (YC), Manish Gupta (Google DeepMind), Srinivas Narayanan (ex-OpenAI), Sanjay Jain (Gates Foundation) and Sachin Bhatia (Exotel co-founder) (https://www.bolna.ai/symphony)

---

## 1. Every Bolna hackathon or buildathon I could find

### 1a. Bolna "Voice AI Agents Hackathon", San Francisco (early, date not shown)
- Organised by the Bolna founders Prateek Sachan and Maitreya Wagh at Zeitgeist, 199 Valencia St, SF. 36 attended. Evening format: hacking 6:00 PM, submissions 7:30 PM, demos by 8:00 PM (https://luma.com/e/evt-Cvl4tYE33XR5PLR)
- Theme: build on Bolna, "an open source infra to build and deploy human-like voice AI agents" (same source)
- Winners, judges, prizes: **not found**

### 1b. Bolna × Cartesia "Voc-a-thon", Bengaluru, June 2026
- In-person build sprint. Registration opened May 29, qualification June 5, build with credits June 5–12, prototype due June 12, demos June 13. 71 participants. Hosted by Sonam Bala (https://luma.com/ubu85bxv). Participant repos give the demo date as June 13, 2026 (https://github.com/victorvini08/unhold-cartesia-bolna-hackathon)
- Prizes listed only as "exciting prizes". **Winners and judges: not found** in Luma, web search, LinkedIn search or GitHub.
- What the submission asked for, per a participant's checklist: a live callable agent link, a problem statement, a target metric with expected improvement, and a backup recording. The checklist says "the rubric penalizes going live with no fallback". Submissions were due 2:00 PM on demo day (https://github.com/KD-3/saheli-voice-shopping/blob/main/SUBMISSION.md)
- The same team noted that judges were "voice AI operators (Bolna + Cartesia teams)" who have "seen every transactional bot (lead qual, support, reminders)", that the form asked for a "novel application or real Indian problem", and that the demo was "live, in-person, 4-ish minutes" (https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md)

| Project | What it does | Stack | Source |
|---|---|---|---|
| **UnHold for Me** (Aryan, Ritika, Nishant) | Consumer agent that calls a company for you, navigates the IVR with DTMF, waits on hold and talks to the human rep. It pings you only for an OTP or consent through an `ask_user` relay, then gives you a summary card. They demoed against an IVR they built themselves ("Acme") that judges could call | Bolna + Cartesia Sonic 3.5, FastAPI, Next.js | https://github.com/victorvini08/unhold-cartesia-bolna-hackathon |
| **Saheli** | Voice companion on a phone call while you browse Amazon.in. A Chrome extension feeds the current page to the agent, which compares products, uses the most critical review to talk you out of bad buys, and adds to cart by voice | Bolna + Cartesia sonic-3-preview, Chrome MV3, FastAPI, 7 function-calling tools | https://github.com/KD-3/saheli-voice-shopping |
| **NestFlow – Family Chief of Staff** | Household manager by phone call in EN/HI/TE/KN: groceries, chores, instructions for domestic help, reminders. Updates appear live on a dashboard. Target metric: ≥90% item capture vs a ~60% baseline | Bolna, Cartesia, Node/Socket.io | https://github.com/AK1-1/vocathon |
| **NyayOS** | Access-to-justice line. A citizen calls, a Hindi/English agent identifies the issue (unpaid salary, FIR refusal, withheld deposit, pension delay), the system generates complaint documents and the case shows up on an NGO paralegal dashboard. Repo created June 10, 2026, matching the Voc-a-thon window **[INFERRED]** | Bolna, Cartesia Sonic-3.5, Deepgram Nova-3, GPT-4.1 mini, Supabase, n8n | https://github.com/YuvrajHajari/NyayOs |

### 1c. Bolna Symphony Buildathon, Oct 2026 (in progress): competitor builds already public
These are what you are up against. Repos found via GitHub search and the Builders wall (https://www.bolna.ai/builders).

| Project | What it does | Source |
|---|---|---|
| **Dadi** | AI grandmother honeypot that answers scam calls in Hinglish, stalls the scammer, captures UPI IDs and bank accounts through live function calls, and drafts a cybercrime complaint plus a fraud-intel feed. Bolna + Sarvam STT + ElevenLabs voice. Live war room at dadi-teal.vercel.app | https://github.com/jaygautam-creator/dadi |
| **Chukta** | Overdue-loan collections agent ("Priya") in Indian languages. Negotiates a plan within lender policy, sends a UPI link on WhatsApp during the call, and checks RBI fair-practice compliance before and after each call | https://github.com/S-tevens/chukta |
| **Bhaav** (repo `bolna.ai-Buildathon`) | Calls a small business's suppliers in Hindi, Kannada or English, collects quotes, and bargains using only real offers. A "lie-catcher" blocks any number the agent can't prove before TTS speaks it. Judges can "Be the supplier" in the browser. Sarvam Saaras/Bulbul, Groq, Cloudflare Workers | https://github.com/Pushkarmondal/bolna.ai-Buildathon |
| **Bolna-Voice-AI-agent** | Hinglish loan pre-check agent with careful language locking and number read-back (LiveKit + Sarvam) | https://github.com/nandy2uy/Bolna-Voice-AI-agent |
| **bolnabuddy** | Bill tracking/reminder app with a voice session (file tree only, no README) | https://github.com/SaiCharanBodigay/bolnabuddy |
| **voice-doctor** | Claude Code skill that diagnoses why a Bolna/Sarvam agent sounds robotic and rewrites its prompt and config | https://github.com/dakshinsiva/voice-doctor |
| **claude-call-me** | Claude Code skill that phones you via Bolna for decisions, task-end updates and a daily standup | https://github.com/MithunSidhaarth/claude-call-me |
| **Call Lab for Bolna** | Reproduces and diagnoses Bolna calls dropping at ~12s using the open-source engine and a fake Twilio caller | https://github.com/rishi-sangare/bolna-call-lab |
| ai_calling_feature | "AI Calling feature with Bolna AI & Pilveo" (stub) | https://github.com/Madhusudan0012/ai_calling_feature |
| Bolna_buildathon, bolna-agent, BolNa, BolnaAI | Empty, a chat app, or a generic Retell/Twilio template | https://github.com/Thesilentprogramer/Bolna_buildathon, https://github.com/opsenes-ai/bolna-agent, https://github.com/Gyanaberia/BolNa, https://github.com/swetha16-7/BolnaAI |

- Side note: ≥6 near-identical "Home Credit Loan Against Property qualification voice agent" repos were created Oct 10–11, 2026. This looks like a Bolna hiring assignment, not the buildathon **[INFERRED]** (e.g. https://github.com/ganeshdwara/home-credit-lap-voice-agent, https://github.com/suryakiranyeddu/home-credit-lap-voice-agent). Loan-qualification bots are therefore very familiar to Bolna staff.

### 1d. "Built with Bolna" wall (https://www.bolna.ai/builders)
- 14 builds, "Bengaluru · est. 2024". It describes itself as covering projects "from gig-worker matching to elder-care check-ins" (https://www.bolna.ai/builders)
- Builders and repos on the wall (from the page's embedded data): @Madhusudan0012 ai_calling_feature, @nandy2uy Bolna-Voice-AI-agent, @api-evangelist bolna (third-party API profile), @Pushkarmondal bolna.ai-Buildathon (Bhaav), @S-tevens chukta, @jaygautam-creator dadi, @anand-therattil Bolna_bhai, @SaiCharanBodigay bolnabuddy, @Thesilentprogramer Bolna_buildathon, @opsenes-ai bolna-agent, @Gyanaberia BolNa, @swetha16-7 BolnaAI, @lazerbeam47 BolnaMonitor, @Harsh-Mer623 n8n-nodes-bolnaai (https://www.bolna.ai/builders)
- **BolnaMonitor** (lazerbeam47 / Dabbu Mothsera): real-time drift detection per ASR+LLM+TTS provider combo, using the latency fields Bolna already emits in `meta_info` (rolling z-score/EWMA, error-rate and 2000ms absolute alerts) (https://github.com/lazerbeam47/BolnaMonitor). Bolna republished its write-up on its own blog: the migration script lists the post "when-one-provider-combo-goes-down…" by Dabbu Mothsera (https://github.com/bolna-ai/blog/blob/main/scripts/migrate-builders.mjs). **[INFERRED]** Bolna visibly rewards infrastructure and observability builds that use its own internals.
- **Bolna Bhai**: WebSocket servers that plug open-source Indic ASR/LLM/TTS (AI4Bharat IndicConformer, Indic Parler-TTS, Qwen via vLLM, etc.) into Pipecat (https://github.com/anand-therattil/Bolna_bhai)
- **n8n-nodes-bolnaai**: n8n integration nodes (https://github.com/Harsh-Mer623/n8n-nodes-bolnaai)
- Other Bolna community work: **Bolna India**, a Telugu voice form-filler for an Aadhaar-style address update using the Bolna Web Call SDK and custom functions (https://github.com/vishalsingh2972/bolna-india)

### 1e. Bolna Campus Builders (ongoing program, not a single event)
- Per-semester campus program: workshops, build nights, "Bolna tracks at existing hackathons", credits, Slack access to engineers, and projects featured on the Builders wall. Example uses it gives: hostel FAQ lines, club registration, placement-cell helplines (https://www.bolna.ai/campus)
- Specific campus-track winners: **not found**

---

## 2. Other India voice-AI hackathons

### Sarvam AI
**Sarvam BuildIn' Hours**, Zo House Bengaluru, Sun Aug 9, 2026
- 12-hour build. 100 selected from 6,272 applicants. Organised with Elevation Capital Basecamp and HackCulture. ₹5L split across the top 3. Tracks: Voice AI, Document Intelligence, Multilingual AI, AI Agents. Judges included Arsh Goyal (https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon, https://digitalterminal.in/tech-companies/zo-house-bengaluru-hosts-sarvam-ai-hackathon)
- Criteria: real-world problem solving, working prototype, presentation (https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon)
- **Winners:**
  1. Government Tender Discovery & Application for MSMEs, built on Sarvam Vision
  2. Storytelling for Kids in Indic Languages
  3. **Setu**, which lets people who cannot speak communicate visually

  (https://digitalterminal.in/tech-companies/zo-house-bengaluru-hosts-sarvam-ai-hackathon)
- Arsh Goyal on the field: participants tackled "genuine Bharat-specific problems" (https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon)
- Related participant repos: **Quotra**, a CPPP/GeM tender GO/NO-GO tool where every reason cites a clause. **[INFERRED]** It is the same idea as winner #1 and may be that team (https://github.com/jenineeuq/quotra-sarvam-lane). **SachhaSaathi** checks forwarded messages, screenshots and voice notes for scams and misinformation (https://github.com/neelabh04/sarvam-hackathon). **NoticePilot** explains GST notices in Malayalam (https://github.com/m6un/sarvam-hackathon)

**Sarvam Epoch Buildathon** (with GrowthX and Lightspeed), Razorpay Arena, Koramangala, Sun Jul 26, 2026
- 8 hours, ~200 curated builders, ₹10L prize pool. The top 10 presented on the Sarvam Epoch stage on Jul 30. Tracks: voice agents, document intelligence, multilingual AI (https://www.startupgrantsindia.com/sarvam-epoch-buildathon-by-growthx, https://x.com/LightspeedIndia/status/2080224074387566813)
- Winners: **not verified.** A search-engine summary said "WireVoice", a voice-first assistant for technicians working with electrical schematics (Hithesh Karanth), took 1st, with stats of 3,000+ applications, 360 attendees and 220 projects. I could not find any source page for this, so treat it as unconfirmed.
- Participant repo: **The Consequence Engine** (Document Intelligence track). It sequences land-record mutation paperwork after a death in the family, refuses unreadable fields and gives a Hindi audio summary (https://github.com/shashank288/the_consequence_engine)

**IndiaMART × Sarvam Voice Hackathon, ~Oct 10–16, 2026** (inferred from repo dates)
- Numbered problem statements from IndiaMART, e.g. "Problem 2: Global Context — Memory Across Channels" and "Problem 6: Seller Enrichment" (https://github.com/chitransh100/Voice-Hackathon-IM, https://github.com/Sagar2001Yadav/Sarvam-Hackathon)
- **Published jury weights:** Business Impact 25%, Solution Completeness 20%, Technical Robustness 20%, Voice Experience 20%, Demo & `skills.md` 15% (https://github.com/chitransh100/Voice-Hackathon-IM/blob/main/impact.md)
- At least one Sarvam hackathon in this period also had an "idea library" of ~49 numbered ideas (e.g. #26 "Heritage Storytelling Agent") (https://github.com/Nitish-Biswas/sarvam_hackathon, https://github.com/Dulari-Bhushan/sarvam-hackathon)
- One participant's README lists "Necessity of Voice", "Hard Voice Problem" and "Stress Case", which looks like a required template **[INFERRED]** (https://github.com/La-pinoz/Sarvam_Hackathon)
- Projects: **VANI**, cross-channel memory for IndiaMART's voice agent. **Seller Enrichment**, which turns voice, card, website or PDF into a pre-filled seller profile. **FasalVachak**, a Hindi crop-disease voice helpline. **Dadi Desk**, one citizen voice agent that routes to grievance, RTI, insurance appeal or scheme application, with a scam shield and an evidence trail. **Aaroh**, heritage storytelling (sources above)
- Winners: **not found**
- An earlier "IndiaMART AI Hackathon" (theme "10X Productivity", 270 participants, 90 teams) is dated 21 May 2026 on IndiaMART's site (https://corporate.indiamart.com/video-category/indiamart-videos-marketing/page/2/). A search summary dated it Dec 31, 2025, so the date is unclear.

**Warpspeed 2025** (Lightspeed + Sarvam + others), Bengaluru, Jun 21–22, 2025
- Theme: Agentic AI. Grand prize **DreamOps**, an AI on-call engineer. 1st runner-up **PragyanAI**, a multilingual interactive learning platform. 2nd runner-up **PlushieOS**, an emotional AI companion in a soft toy (https://devfolio.co/blog/warpspeed-2025-recap/)

### Smallest.ai
- "Let's Build AI Voice Agents with smallest.ai", Bengaluru, Jul 26, 2025. ₹10,000 cash prize. Mentors from Smallest, including CTO Sirsho Chakraborty (https://lu.ma/idu6gzgm, via search summary). Winners: **not found**
- Voice AI HackSprint 2.0, run by "Smallest Events" in San Francisco on Mar 14, 2026, so not India (https://luma.com/ikzcmqld)
- Smallest × AI Grants India: free voice infra for Indian builders, Mar 2026 (https://m.thewire.in/article/ptiprnews/smallest-ai-collaborates-with-ai-grants-india-to-bring-state-of-the-art-voice-ai-to-indias-grassroots-builders)

### Exotel
- A HackerEarth-hosted hackathon on detecting emotion from call audio. Year and winners **not found** (https://www.hackerearth.com/recruit/customers/exotel)
- Exotel AgentStream hackathon: **not found**

### Plivo
- A 2023 Plivo hackathon (SMS/voice API apps) shows up only through participant repos, e.g. an SMS banking app (https://github.com/kasheravaibhav14/plivo_hackathon)
- A "Plivo Hackathon 2026" GitHub org (created May 21, 2026) has one repo, **plivo-mirror**. It checks every sentence a voice agent speaks against ground truth, corrects it before TTS and blocks unauthorised tool calls (https://github.com/plivo-hackathon-26/vijay-echo-codec). Format and winners: **not found**. **[INFERRED]** Possibly a hiring hackathon.

### Deepgram (India)
- **not found.** Only global events (e.g. https://blog.deepgram.com/best-8-deepgram-projects-hack-cambridge)

### Cartesia (India)
- Only the Bolna × Cartesia Voc-a-thon above. Cartesia opened an India office in Jan 2026 (https://startupwired.com/2026/01/22/voice-ai-startup-cartesia-enters-india-with-big-plans/)

### Kalpa Labs
- No hackathon found. CB Insights lists it as a YC-backed speech-model company (https://www.cbinsights.com/company/kalpalabs)
- Note: "Kalpa Impact", a co-organiser of the BHASHINI VYOMA challenge, may be a different entity. Not verified.

### Gnani.ai
- **Great Indian AI Internship Challenge 2026** is open now. Entries Oct 1 – Nov 10, 2026 (11:59 PM IST). Open brief, theme "Build Sovereign AI for India", built on Gnani voice and language models. Prize: up to 100 paid 6-month internships (stipend up to ₹1L/month). 5,000 credits each. Students only, teams of 1–2. Requires a demo video, a write-up and public LinkedIn/X posts (https://www.successcds.net/?p=177105, https://fintechbiznews.com/fintech-technology/great-indian-ai-internship-challenge-by-gnani-ai). **[INFERRED]** A student team's Bolna build could also be re-skinned onto Gnani models and entered here by Nov 10.
- **NVIDIA India Agentic AI Open Hackathon** (NVIDIA + Sarvam + gnani.ai). Finals in Bengaluru on Jul 24–25, 2026, with ~2,293 teams and 14 finalists (https://www.openhackathons.org/s/siteevent/a0CUP00004gn7e32AA/se000496 plus search summary). Winners: **not found**

### Bhashini / AI4Bharat / government
- **VYOMA Innovation Challenge** (BHASHINI, Current AI, Kalpa Impact). Finale at IIIT-Delhi, Sep 16, 2026. Built on Suno Sutra, an open offline/edge multilingual voice reference design. Winners: Team Asha Sahayak, Team Shravan, Team Sangrah ("Apna Saatti"), and Team Sahyak Mitra with **A.V.E.R.A.** (Autonomous Voice-enabled Edge Rural Advisor) (https://fintechbiznews.com/fintech-technology/bhashini-current-ai-and-kalpa-impact-conclude-vyoma-innovation-challenge)
- **Bhasha Techathon 2024** (BHASHINI + Google Cloud + MachineHack), Mar 8 – May 15, 2024 (https://analyticsindiamag.com/google-cloud-bhashini-and-machinehack-come-together-for-bhasha-techathon/). The Favorable Project Award went to a speech-to-text complaint system for CRIS (railways) covering 22 languages (https://cps.iic.du.ac.in/?p=9659). Full winners list: **not found**
- **Bhashini Grand Innovation Challenge**: ₹1L per team to prototype, ₹50L to the winner (https://indiaai.gov.in/article/the-meity-introduced-bhashini-grand-innovation-challenge). Winners: **not found**
- **Rajasthan Language Model Training Hackathon** (BHASHINI, Jul 2026) for Marwari, Mewari and other dialects. Winners: **not found** (https://www.drishtiias.com/state-pcs-current-affairs/bhashini-launches-rajasthan-language-model-training-hackathon)
- **Voice Tech for All** (SYSPIN, IISc), a TTS model challenge across 9 languages. Winner Immverse AI, then LTRC-SPL, then Somya.ai (search summary of https://syspin.iisc.ac.in/voicetechforall; the page itself did not render)

### Google / AWS (large India hackathons with voice-heavy winners)
- **Google Cloud Agentic AI Day 2025**, Bengaluru, Jul 27, 2025 (Guinness record, 57,000+ participants) (https://blog.google/intl/en-in/company-news/seizing-our-moment-in-guinness-world-records/). 1st place **GuruMitra**: offline-first, edge-deployed teaching assistant for multi-grade classrooms in 22+ languages, claiming 70% less lesson-prep time (https://lnmiit.ac.in/congratulations-to-team-gurumitra-clinched-1st-place-at-the-google-cloud-agentic-ai-day-hackathon-2025/). **KrishAI** won Breakthrough Concept with "expert help to farmers on demand" (https://lnmiit.ac.in/congratulations-to-team-krishai-has-won-the-breakthrough-concept-award/)
- **AWS AI for Bharat Hackathon** (Hack2Skill + YourStory, 2026). ~96,000 registrations, 1,400+ prototypes (https://yourstory.com/2026/06/crop-insurance-conversational-analytics-ai-for-bharat-hackathon). Winners included:
  - **SocraticDev**
  - **Content Room**, regional content adaptation
  - A **WhatsApp-first crop-insurance claims** platform in 7 languages with an operator dashboard
  - **RetailAI**, conversational analytics for small retailers
  - **MedhaOS**, an agentic hospital journey across web, WhatsApp and voice
  - **Kisan Mitra AI**, which turns soil reports into advice, grades crops, and works voice-first in dialects

  (same source)

### ElevenLabs
- **ElevenLabs Worldwide Hackathon**, Bangalore leg (Feb 2025, 70 builders). Winners:
  1. **lossfunk**, an AI film generator
  2. **ECHO AI**, an agent that turns messy info into structured data
  3. **Pochinki**, ads woven into podcasts

  The global winner was GibberLink (London) (https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)

### Agora / Vapi / Murf / others (India)
- **EchoSphere** (KNOTiC × Agora Conversational AI). Jul 22 – Aug 21, 2026, finale in Delhi Sep 12 (https://www.startupgrantsindia.com/echosphere-agora-conversational-ai-hackathon). Winners: **not found**
- **Convo AI Hackathon India** (online, Nov 14–15, 2025, Agora-sponsored, with GDG) (https://convoai.world/events/convoai-convo-ai-hackathon-india-online-november/). Winners: **not found**
- **HackBLR 2026** (Geek Room + Vapi Events). Online Apr 18, offline final Apr 26, 2026, ₹35k+ pool, Voice AI focus (https://luma.com/ia0ik7c6). Winners: **not found**
- **The Golden Hour** (E-Cell IIT Kharagpur × CallKaro AI). Sep 12 – Oct 18, 2026. Enterprise voice agents "within strict business guardrails", ₹1L pool (https://www.startupgrantsindia.com/competitions/the-golden-hour-a-voice-ai-hackathon). Winners: **not found**
- **Murf AI "30 Days of AI Voice Agents"** challenge: 400+ developers, 150+ agents, a community challenge with no named winners (https://www.01net.it/murf-ai-concludes-a-first-of-its-kind-30-day-developer-challenge-on-building-ai-voice-agents)
- **ALEXATHON** (Deshpande Startups, Hubballi): winners Shaurya (AquaSafi), TheVoice (IIIT Dharwad), and SRV, a team of 9th-graders from a Gadag village. Year not stated (https://www.deshpandefoundationindia.org/blog/voices-worth-hearing-alexathon/)
- Devfolio/Unstop/HackerEarth "voice tracks" with named voice winners: **not found** beyond the above
- A blog summarising 2026 hackathon winners mentions: a regional-language legal-rights tool for rural women with voice input, a WhatsApp bot for ASHA workers doing local-language triage, a govt-job application agent, and an RTI processor. It says judges reward "a specific problem for a specific user", "AI as a multiplier", and "a demo that works on the first try", and avoid generic chatbots, note-takers and dashboards. Event names are not given (https://blogs.reskilll.com/hackathon-ideas-that-won-2026-judges-actually-pick-examples/)

---

## 3. Pattern analysis

### What the confirmed winners have in common
| Winner | Specific user | Bharat-specific? | Voice role |
|---|---|---|---|
| Govt tenders for MSMEs (Sarvam BuildIn') | MSME owner | yes | secondary (Vision-led) |
| Kids storytelling in Indic (Sarvam BuildIn') | children | yes | primary |
| Setu (Sarvam BuildIn') | people who can't speak | yes | core accessibility |
| GuruMitra (Google) | multi-grade teacher | yes | multimodal, offline |
| Crop-insurance claims, WhatsApp-first (AWS) | farmer at claim time | yes | WhatsApp, operator-assisted |
| A.V.E.R.A. etc. (VYOMA) | rural users, offline | yes | edge voice |
| PragyanAI (Warpspeed) | learners | yes | multilingual |
| ElevenLabs BLR winners | creators/media | no | creative TTS |
| DreamOps (Warpspeed) | on-call engineers | no | none |

1. **Narrow user, exact moment.** Every Bharat-track winner names one person and one situation: an MSME bidding a tender, a farmer filing a claim after crop loss, a teacher with three grades in one room (sources in §2). Broad "assistant for everyone" ideas don't appear among winners.
2. **Voice is load-bearing, not decoration.** **[INFERRED]** from the confirmed winners plus the Sarvam template ("if you remove voice, the product is completely unusable", https://github.com/La-pinoz/Sarvam_Hackathon). Accessibility and low-literacy users make voice necessary rather than nice.
3. **A judge takes part in the demo.** **[INFERRED]** This is the strongest recurring move in Bolna-specific builds:
   - UnHold: judges call the fake IVR.
   - Bhaav: "Be the supplier" and try to make it lie.
   - Dadi: a judge plays the scammer on speaker.
   - Saheli: a phone on speaker plus live browsing, with captions so the back of the room can follow.

   (sources in §1b and §1c)
4. **A metric with a baseline.** The Voc-a-thon form required a target metric and expected improvement (https://github.com/KD-3/saheli-voice-shopping/blob/main/SUBMISSION.md). The IndiaMART×Sarvam jury gives Business Impact the highest weight, 25% (https://github.com/chitransh100/Voice-Hackathon-IM/blob/main/impact.md).
5. **Trust and guardrails as the technical depth.** Voice-infra judges have "seen every transactional bot" (https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md). Strong builds therefore show a hard voice problem solved: a number lie-catcher before TTS (Bhaav, plivo-mirror), RBI compliance checks (Chukta), language locking and number read-back (nandy2uy), refusal-first handling (Consequence Engine).
6. **A backup recording is mandatory.** The Voc-a-thon rubric penalised live demos without a fallback (https://github.com/KD-3/saheli-voice-shopping/blob/main/SUBMISSION.md).
7. **Bolna values infra builders.** BolnaMonitor got a featured spot and a blog re-post (https://github.com/bolna-ai/blog/blob/main/scripts/migrate-builders.mjs). **[INFERRED]** A build that uses deep Bolna features (custom LLM endpoint, graph agents, function calls, Web Call SDK, webhooks, `meta_info` latencies) will read well to Bolna engineers. Bhaav's deck lists exactly these features (https://github.com/Pushkarmondal/bolna.ai-Buildathon/blob/main/docs/SUBMISSION.md).
8. **The winner gets a YC interview.** **[INFERRED]** A startup-shaped story (buyer, market size, real usage during Oct 21–31) matters more here than at a normal hackathon. Dadi plans to show "stats from the real build period" (https://github.com/jaygautam-creator/dadi/blob/main/docs/SUBMISSION.md).

### Overdone: avoid, or only enter with a clear twist
| Category | Evidence of saturation |
|---|---|
| **Farmer advisory / crop-disease helpline** | FasalVachak (https://github.com/La-pinoz/Sarvam_Hackathon), Kisan Mitra AI (AWS), KrishAI (Google), KisanVani (https://dev.to/dharmesh1991/building-kisanvani-kisaan-vaannii-an-ultra-low-latency-multilingual-voice-agent-for-indian-2c3), KisanMitra (https://dev.to/rishabh_dev/-building-kisanmitra-ai-empowering-indian-farmers-with-a-full-stack-voice-agent-15f), kisansetu (https://github.com/Himancer/kisansetu). Sarvam's own docs ship an "Agri & Rural Voice Agents" reference design (https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/agri-rural) |
| **Citizen legal / grievance / RTI / govt form-filling** | NyayOS, Dadi Desk, Bolna India (Aadhaar form), the Rajasthan legal-rights tool, the RTI processor, CivicAssist (sources above) |
| **Loan qualification / collections / BFSI outbound** | Chukta and the Hinglish loan pre-check are already in this buildathon. ≥6 Home Credit LAP clones exist (§1c) |
| **Scam detection / honeypot** | Dadi is already in this buildathon. SachhaSaathi and Dadi Desk's scam shield exist (§1c, §2) |
| **Kids tutoring / storytelling / lesson narration** | A Sarvam winner, Lesson Loom (https://github.com/blank6890/sarvam-hackathon-26), PragyanAI, and Bolna's own example list. **[INFERRED]** Expect many entries |
| **Clinic helpdesk / hospital triage / ASHA bots** | MedhaOS, the ASHA WhatsApp bot, and Bolna's example list |
| **Household / personal reminder / bill assistants** | NestFlow, bolnabuddy |
| **Recruiting / phone-interview bots** | This is Bolna's own flagship use case: its builders page quotes reviews of its "recruitment platform" and its "phone interview" agent (https://www.bolna.ai/builders) |
| **Document → voice summary** | Audit-Duty (https://github.com/Bharathconfig/AutomataForceSarvam), NoticePilot, Consequence Engine, Aaroh |
| **Generic lead-qualification / support / reminder bots** | Judges have "seen every transactional bot" (https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md) |

### Gaps: nothing found in any of the sources above
All **[INFERRED]**: the claim is that I found no public build, not that none exists. Each one uses sponsor products.

1. **Phone relay for deaf and hard-of-hearing Indians.** Live two-way call captioning plus typed-to-speech on a normal PSTN call, in Indian languages. India has no telecom relay service like the US TRS. Setu, a non-speaking communication tool, won Sarvam BuildIn', so judges reward this kind of accessibility (https://digitalterminal.in/tech-companies/zo-house-bengaluru-hosts-sarvam-ai-hackathon). Uses Plivo/Exotel telephony, Deepgram/Sarvam STT and Cartesia TTS. The demo: a judge phones a deaf user and the conversation happens live.
2. **Live cross-language call interpreter.** For example, a Tamil-speaking migrant worker on the phone with a Hindi-speaking doctor, landlord or police station. No repo bridged two Indian languages inside one live call. Every build above is a single caller talking to a bot.
3. **"Calls N places for you" for urgent searches.** Hospital bed or ICU availability, pharmacy stock for a scarce drug, or blood bank units, run as parallel outbound calls with aggregated results. UnHold (one company, customer service) and Bhaav (suppliers, price) prove the mechanics, but nobody applied them to urgent health logistics.
4. **Field and blue-collar workers who can't look at a screen.** Bolna lists "drivers/field workers" as an example, but no repo exists yet. Ideas: truck-driver load confirmation and dispatch, an electrician pulling up wiring specs hands-free (WireVoice reportedly won Sarvam Epoch, unverified), or a factory-floor SOP lookup. Bolna lists this category, so expect some competition.
5. **Testing and eval infrastructure for Indic voice agents.** A synthetic-caller red-team bench with accents, background noise, code-switching, interruptions and number dictation that scores any Bolna agent. Pieces exist (Bhaav's 50-chat bench, Call Lab, voice-doctor, BolnaMonitor), but nobody built a general "CI for Hinglish voice agents". This matches Bolna's demonstrated taste for infra (BolnaMonitor). The weak spot is that it's less "Bharat impact" for the YC story.
6. **Inbound phone ordering for kiranas and small restaurants.** The shop's missed calls turn into orders, written straight to a WhatsApp or khata ledger. Bhaav covers the buy side (shop → suppliers). No build covers the sell side (customers → shop).
7. **Agent-to-agent voice negotiation**, e.g. a buyer agent and a seller agent over a real call. Bhaav lists this as roadmap only (https://github.com/Pushkarmondal/bolna.ai-Buildathon/blob/main/docs/SUBMISSION.md).
8. **Emergency / 108 pre-triage or disaster helpline in dialects.** Not seen in any repo or winner list.

### Demo style that fits this buildathon
**[INFERRED]**, built on the evidence above:
- Submission is async (a ≤200-character description, a link, and a deck or video). Shortlisted teams get interviewed Nov 5–7. The demo video does the work: a 2–3 minute video with a real phone call, a split screen showing the dashboard reacting live, and one "wow" moment (an OTP relay, a blocked lie, a captured UPI ID).
- Give judges a way to call it themselves. A public number or Web Call SDK button plus a passcode let them test it on their own phones.
- Show real numbers from real calls made during Oct 21–31, not projections.
- Name the Bolna features you used (graph agent, custom LLM, functions, webhooks, Web Call SDK) and the sponsor models (Sarvam / Deepgram STT, Cartesia TTS, Plivo / Exotel telephony).
