# Symphony Buildathon: sponsor deep-dive (researched 2026-10-21)

Every fact has an inline source. My opinions and guesses are marked **[INFERRED]**.

---

## 0. The buildathon itself (verified)

- Organiser Bolna. Sponsor logos on the buildathon page: **Cartesia, Deepgram, Exotel, Kalpa Labs, Plivo, Sarvam**, plus Y Combinator ([bolna.ai/symphony/buildathon](https://www.bolna.ai/symphony/buildathon); the logo asset list is in the page bundle `routes-*.js`).
- Prizes total ₹1.2L: 1st ₹50k plus an interview with **Grey Baker (YC Partner)**, 2nd ₹40k, 3rd ₹30k. Top 3 get travel covered and pitch on the Abhyas stage at Symphony on Nov 20. Top 10 get free Symphony tickets ([buildathon page](https://www.bolna.ai/symphony/buildathon)).
- Timeline: build Oct 15–31, **submit Oct 31**, shortlist Nov 3, interviews Nov 5–7, finalists Nov 8, finale Nov 20 (same page).
- There are no tracks: "Anything with voice in it". Example ideas on the page are a kids voice tutor, a clinic helpdesk, a voice layer on an existing app, and a hands-free tool for drivers/field workers. **[INFERRED]** Expect those to be crowded.
- Submission fields: description, a link (GitHub/live app/demo), and a pitch deck or pitch video link (Drive/Luma). The FAQ says sponsor/Bolna credits come through a "credits request form" ([page bundle `submit-*.js`, `routes-*.js`](https://www.bolna.ai/symphony/buildathon)).
- Symphony summit speakers include **Sachin Bhatia (Exotel co-founder)** and Grey Baker (YC). Summit partners also include Google Cloud, NVIDIA Inception, OpenAI, Smallest.ai, Truecaller Business, Vobiz and Wispr Flow. Registration includes $100 Bolna credits and **2,500 Sarvam credits** ([bolna.ai/symphony](https://www.bolna.ai/symphony)).
- **[INFERRED] Bolna judges' lens:** they will reward builds that use Bolna's newest surface area. That means Graph Agents (May 2026), Workflows with WhatsApp follow-ups (Aug 2026), Web Call SDK (Jul 2026), web-search tool (Oct 8 2026), SIP trunks/BYO carrier (Oct 15 2026), MCP/Claude connector (Oct 9 2026), extraction values on graph edges (Oct 8 2026) ([Oct 2026 changelog](https://www.bolna.ai/docs/changelog/october-2026.md), [Bolna blog](https://www.bolna.ai/blog)).

---

## 1. Plivo

### 1.1 Products / 2026 launches
- Voice AI split into two paths. **Audio Streaming** (bidirectional WebSocket, for Pipecat-style stacks) and **SIP trunking** (LiveKit, ElevenLabs, Retell, Vapi). Official Plivo Stream SDKs exist for Python/Node/Java ([plivo docs llms.txt](https://www.plivo.com/docs/llms.txt)).
- **Vibe Agent**, a no-code agent studio. Also Plivo CLI, noise cancellation, VAD, turn detection, and BYO STT/TTS/LLM. Channels are voice, SMS, WhatsApp and chat ([plivo.com/ai-agents](https://www.plivo.com/ai-agents/)).
- India price: domestic ₹0.38/min with a 30s pulse (₹0.19 per 30s). **Audio streaming "Included"** ([plivo.com/voice/pricing/in](https://www.plivo.com/voice/pricing/in/)). Plivo also cut its Voice AI Agent rate to $0.03/min, with telephony billed separately, in the week of Aug 17–24 2026 ([PricingSaaS diff](https://pricingsaas.com/companies/plivo/diffs/2026W35)).
- Compliance tooling for India: TRAI media-anchoring rule (hangup code 4590), India data region, and number KYC. **Vapi is not supported for Indian numbers** ([Calling in India](https://plivo.com/docs/voice-agents/sip-trunking/deploy/calling-in-india)).

### 1.2 Unique capability
- **`<MultiPartyCall>` with participant roles.** These are `Agent`, `Supervisor` (coach mode: the supervisor is heard only by the agent) and **`ai-agent`** (an AI joins the call over WebSocket via `aiAgentStreamServiceUrl`). There is also `recordCoachVoice` ([Multi-party Call XML](https://plivo.com/docs/voice/xml/multiparty-call)). An AI can be a *participant* in a multi-person call with a human coach whispering. **[INFERRED]** Few CPaaS vendors document this.
- Voicemail and answering-machine detection best practices for AI agents ([Audio Streaming best practices](https://plivo.com/docs/voice-agents/audio-streaming/concepts/best-practices)).

### 1.3 Bolna integration
- Bolna calls Plivo "Default for most Bolna deployments" for India + global ([Choosing telephony](https://www.bolna.ai/docs/concepts/choosing-telephony.md)). Supports outbound, inbound and BYO account ([Plivo page](https://www.bolna.ai/docs/plivo.md)). Ambient-noise feature works only on Plivo and Vobiz ([Mar 2026 changelog](https://www.bolna.ai/docs/changelog/march-2026.md)). Plivo is also a carrier preset for Bolna SIP trunks (Oct 15 2026) ([Oct changelog](https://www.bolna.ai/docs/changelog/october-2026.md)).
- Plivo case study: Bolna runs 1M+ calls/month on Plivo. CTO Prateek Sachan says "If today you're building anything in voice AI and you're not using Plivo as a provider, you're probably making a mistake." Verticals: D2C, logistics, e-commerce, recruitment, abandoned carts, delivery confirmations ([plivo.com/customers/bolna](https://www.plivo.com/customers/bolna/)).
- **[INFERRED]** Bolna does not expose Plivo MPC roles. Using `ai-agent`/`Supervisor` roles means calling Plivo directly next to Bolna.

### 1.4 Past hackathons / what devrel wants
- No Plivo-run hackathon with published winners was found (searched). Plivo's docs push Pipecat recipes pairing **Deepgram + Cartesia** and **Sarvam + OpenAI** for Indian languages ([plivo docs llms.txt](https://www.plivo.com/docs/llms.txt)). **[INFERRED]** A Plivo + Deepgram + Cartesia + Sarvam stack is their own preferred showcase.

### 1.5 India GTM
- Use cases they list: lead qualification, e-commerce support, appointment booking, tech support, surveys, multichannel. Logos include Zomato, Razorpay, Uber and Meta ([plivo.com/ai-agents](https://www.plivo.com/ai-agents/)).

### 1.6 Credits
- ₹1,000 free on signup with no card. Startup credits program covers YC/Nexus/Lightspeed/Blume etc. backed startups ([plivo.com/startups](https://www.plivo.com/startups/)).

---

## 2. Exotel

### 2.1 Products / 2026 launches
- **AgentStream** launched Aug 14 2026: full-duplex WebSocket, audio frames under 20 ms, no call-setup lag. Exotel claims **~40% of India's voice AI conversations**, 25B+ interactions/yr and 7,000+ enterprises (Apollo 24/7, HDFC Securities, JSW MG Motor) ([Exotel newsroom](https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/)). Channels are PSTN, WhatsApp, in-app and WebRTC ([Voice&Data](https://www.voicendata.com/news/exotel-launches-agentstream-to-power-ultra-low-latency-ai-voice-experiences-9655590)).
- AgentStream paths: Connect Voice AI API, Flow (App Bazaar with Voicebot + Connect applets for IVR, DTMF and **human handoff**), ExoML Legs (`start_stream` + `start_say` greeting "no dead air" pattern for sales/collections), and StreamKit Cloud (SIP to WSS bridge) ([AgentStream overview](https://developer.exotel.com/docs/agentstream/overview.md), [Legs API](https://developer.exotel.com/docs/agentstream/bot-stream-legs-api.md)).
- VoiceBot Tools Server (Python/OpenAPI/RAG tools via MCP) ([Tools overview](https://developer.exotel.com/docs/voicebot-tools/overview.md)). Other 2026 APIs: ExoVoice Analyze and ExoMind Tasker (Jan 2026). Earlier: **WhatsApp Payments** + Flows (Dec 2025), **ExoVerify missed-call OTP** (Jun 2025), WebRTC SDK (Jul 2025) ([Exotel changelog](https://developer.exotel.com/docs/references/changelog.md)).
- Harmony CX platform, AI Assist (live agent assist, smart replies, auto-disposition), **Call Whisper**, Bot Monitoring ("Monitoring Officer": "let the AI handle the routine while you handle the risks") ([docs.exotel.com llms.txt](https://docs.exotel.com/llms.txt), [Bot Monitoring](https://docs.exotel.com/harmony/bot-monitoring.md)).

### 2.2 Unique capability
- **Supervisory model: one human oversees many bots.** Co-founder Sachin Bhatia: "Models eventually will be like electricity". The pitch moves from "bot-first, human-as-backup" to a human supervising several bots, and conversation intelligence replacing NPS ([Exotel newsroom](https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/)).
- India-native telco primitives: missed-call verification (ExoVerify), DLT compliance built in ([Bolna: Choosing telephony](https://www.bolna.ai/docs/concepts/choosing-telephony.md)), WhatsApp payments, and App Bazaar flows with human Connect.

### 2.3 Bolna integration
- Native Exotel telephony in Bolna since Oct 15 2025 ([Oct 2025 changelog](https://www.bolna.ai/docs/changelog/october-2025.md)). Exotel published the "Bolna Voice AI & Exotel Integration Guide" on 2026-09-15: App Bazaar Voicebot applet points at Bolna, and a Connect applet handles transfer to a human ([Exotel doc](https://docs.exotel.com/exotel-agentstream/bolna-voice-ai-and-exotel-integration-guide.md)). There is also "Connect Exotel SIP trunking to Bolna" ([doc](https://docs.exotel.com/exotel-agentstream/connect-exotel-sip-trunking-to-bolna-voice-ai.md)). Exotel also documents **Cartesia Agents** and **Sarvam Voice Agents** on AgentStream ([docs index](https://docs.exotel.com/llms.txt)).

### 2.4 Past hackathons / devrel
- No Exotel-branded hackathon with winners was found. Exotel ran an AI voicebot workshop at DevConf.IN ([community.exotel.com](https://community.exotel.com/t/ai-voicebot-workshop-at-devconf-in-pune/19)). Exotel has an MCP server repo, `exotel/ExotelMCP` ([GitHub](https://github.com/exotel/ExotelMCP)).

### 2.5 India GTM
- Verticals: CX, sales automation, marketing, debt collection; BFSI, retail, healthcare, logistics, mobility, education ([Exotel newsroom](https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/)). **[INFERRED]** Their buyer is the enterprise contact centre, so they would tweet a "human + AI fleet" ops demo.

### 2.6 Credits
- Trial: free credits, 1 trial ExoPhone, outbound only to **≤10 whitelisted numbers**, no WhatsApp API or campaigns during trial ([Trial account](https://developer.exotel.com/docs/getting-started/trial-account)). **[INFERRED]** Ask Bolna's credits form for a non-trial account if the demo needs real outbound.

---

## 3. Sarvam AI

### 3.1 Products / 2026 launches
- **Saaras v4** STT (GA on Voice Agents Sep 2 2026): 22 Indian languages + English (Global English accents added). Five output modes: `transcribe`, **`translate`** (speech to English text), `verbatim`, `translit`, **`codemix`**. Also language ID with probability, **keyterms (50)**, and diarization on batch ([Saaras model page](https://docs.sarvam.ai/api/getting-started/models/saaras.md), [changelog](https://docs.sarvam.ai/changelog.md)). Epoch claims multi-speaker ASR in one pass and the "lowest average WER of any system tested" ([Epoch summary](https://www.sarvam.ai/epoch/summary)).
- **Bulbul v4 Flash** TTS: 222 persona voices named `<name>_<lang>_<style>` (e.g. `sanchita_hi_kyc`, `sanchita_hi_banking`, `ishita_hi_devotional`, `simran_en_sales`), 13 Hindi-English code-mixed voices, 9 languages ([Bulbul model page](https://docs.sarvam.ai/api/getting-started/models/bulbul.md), [Bolna Sarvam TTS](https://www.bolna.ai/docs/sarvam-voice.md)). Bulbul V4 was shown at Epoch as expressive, with emotion, emphasis, pacing and laughter, as a research preview ([Epoch summary](https://www.sarvam.ai/epoch/summary)). Bulbul v3 reaches EOL on Sarvam Voice Agents Nov 10 2026 ([changelog](https://docs.sarvam.ai/changelog.md)).
- **Instant Voice Cloning (beta)**, **cross-lingual** (an English reference clip can speak Hindi or Tamil), 12 languages, with streaming and WebSocket added Oct 1 2026 and built-in transcribe-back QC ([Voice cloning](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview.md)). **Dubbing API** (Sep 26 2026) ([changelog](https://docs.sarvam.ai/changelog.md)).
- **Sarvam Vision 2.0** document AI (handwriting, KYC, land deeds; 35M+ pages), Sarvam-105B LLM (~$0.80/M blended), Mayura translation, Voice Agents platform (₹3–3.50/min, tests, MCP server, call transfer, number rotation), Kaze glasses and Kivi app ([Epoch summary](https://www.sarvam.ai/epoch/summary), [docs llms.txt](https://docs.sarvam.ai/llms.txt)).

### 3.2 Unique capability
- **Breadth of Indic coverage plus the `translate`/`codemix` STT modes in one model** (22 languages), and **cross-lingual voice cloning**. Persona voices are tuned per *use case* (KYC, banking, devotional, sales). **[INFERRED]** Nobody else sells use-case-specific Indic voice personas.

### 3.3 Bolna integration
- STT `saaras:v4`/`v3` (v4 Aug 2026; keyword biasing Oct 2 2026). Bolna sends **transcribe mode only**: there is no `mode` field, so translate and codemix are not reachable through Bolna. Only 12 of the 23 languages are selectable in Bolna ([Bolna Sarvam STT](https://www.bolna.ai/docs/sarvam-transcriber.md)).
- TTS `bulbul:v4-flash` (Oct 15 2026) and `bulbul:v3` ([Oct changelog](https://www.bolna.ai/docs/changelog/october-2026.md)). **Sarvam is not available as an LLM on Bolna** ([Bolna Sarvam STT](https://www.bolna.ai/docs/sarvam-transcriber.md)). **[INFERRED]** Use Bolna custom LLM to call Sarvam-105B if needed ([custom LLM](https://www.bolna.ai/docs/custom-llm-inference.md)).

### 3.4 Past hackathons / what they reward
- **Sarvam BuildIn' Hours** at Zo House, Bengaluru (₹5L pool; tracks Voice AI, Doc Intelligence, Multilingual, Agents). Winners: (1) **govt tender discovery & application for MSMEs on Sarvam Vision**, (2) Indic storytelling for kids, (3) **Setu, a tool for people who cannot speak to communicate** ([Digital Terminal](https://digitalterminal.in/tech-companies/zo-house-bengaluru-hosts-sarvam-ai-hackathon)).
- **Sarvam Epoch Buildathon** by GrowthX, Jul 26 2026 (₹10L pool; voice agents, document intelligence, multilingual; all participants got 5,000 credits). Winners were not published ([StartupGrantsIndia](https://www.startupgrantsindia.com/sarvam-epoch-buildathon-by-growthx)).
- **[INFERRED]** Sarvam rewards Bharat-scale inclusion (MSMEs, accessibility, vernacular) and builds that combine **voice + Vision/doc AI**.

### 3.5 India GTM
- Conversational agents are ~80% of ARR. Customers in banking, insurance, government and defence (Tata Capital) ([Inc42](https://inc42.com/buzz/sarvam-enters-unicorn-club-with-234-mn-funding-round-led-by-hcltech)). Mahindra Finance has run 1 crore+ calls in 12 languages across sales, collections and employee feedback ([Sarvam story](https://www.sarvam.ai/stories/mahindra-finance-voice-agents)).

### 3.6 Credits
- ₹100 on signup, never expires ([Credits](https://docs.sarvam.ai/api/getting-started/ratelimits.md)). 2,500 credits with a Symphony ticket ([Symphony](https://www.bolna.ai/symphony)). Startup Program gives 6–12 months of credits ([Business Standard](https://www.business-standard.com/companies/start-ups/sarvam-ai-launches-startup-programme-to-back-ai-builders-in-india-details-126030501111_1.html)).

---

## 4. Cartesia

### 4.1 Products / 2026 launches
- **Sonic 3.6** GA Aug 27 2026: 44 languages incl. Odia and Urdu. It adapts emotion and pacing from context, follows **romanized Hindi/Hinglish** transcripts, reads non-English alphanumerics with native letter names, and handles in-transcript disfluencies ("uh"). New `locale` / `accent` / `normalization` fields: e.g. Hindi voice with `normalization: en-IN` reads an OTP digit-by-digit in English ([Cartesia changelog 2026](https://docs.cartesia.ai/changelog/2026.md), [Advanced capabilities](https://docs.cartesia.ai/build-with-cartesia/capability-guides/advanced-capabilities.md)).
- **Emotion controls (beta)** via `generation_config.emotion` or inline `<emotion value="..."/>` SSML. ~60 emotions; best primaries are neutral, calm, angry, content, sad, scared. **English only.** `[laughter]` nonverbal ([Volume/Speed/Emotion](https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion.md)).
- **Voice cloning:** Instant clone from ~10 s ([India page](https://cartesia.ai/regions/india)). On 3.6 it keeps the accent better (up to 60 s input). **A clone can speak several languages natively** (Aug 2026). PVCs carry across models (Sep 2026) ([changelog](https://docs.cartesia.ai/changelog/2026.md)). **Localize Voice** endpoint (a new native-accent voice ID) ([API ref](https://docs.cartesia.ai/api-reference/voices/localize.md)). **Infill** (generate audio bridging two clips) ([API ref](https://docs.cartesia.ai/api-reference/infill/bytes.md)). Pronunciation dictionaries ([changelog](https://docs.cartesia.ai/changelog/2026.md)).
- **Ink-2** STT with built-in turn events (`turn.start/update/eager_end/resume/end`), keyterms, Hindi added Sep 17 2026 ([Ink 2](https://docs.cartesia.ai/build-with-cartesia/stt/latest.md)). **Managed Agents** (Aug 2026; Line SDK hosting ends Dec 1 2026), batch calling of 5,000 per request, dynamic variables, async tools ([changelog](https://docs.cartesia.ai/changelog/2026.md)).

### 4.2 Unique capability
- **Latency plus controllability:** sub-90 ms ([India page](https://cartesia.ai/regions/india)), director-style emotion tags, and one cloned voice speaking many languages with native accent. Sonic 3.6 was preferred ~2:1 over 3.5 in blind tests ([changelog](https://docs.cartesia.ai/changelog/2026.md)).

### 4.3 Bolna integration
- `sonic-3`, `sonic-3.5`, `sonic-3.6` (3.6 recommended, Aug 2026) ([Bolna Cartesia](https://www.bolna.ai/docs/cartesia.md)). Voice cloning for sonic-3 in 10 Indian languages since Nov 2 2025 ([Nov 2025 changelog](https://www.bolna.ai/docs/changelog/november-2025.md)). Clone through the Bolna UI, choosing ElevenLabs or Cartesia ([Clone voices](https://www.bolna.ai/docs/clone-voices.md)).
- Bolna's doc mentions only speaking rate and volume. **[INFERRED]** Emotion `generation_config` is not exposed. Inline `<emotion/>` / `[laughter]` tags in LLM output *might* pass through as text, so test it before relying on it.
- Cartesia's case study on Bolna (Feb 10 2026): 500k+ calls/day, ~40% less engineering time on latency/quality. Quote: "You can't scale voice AI in India with English alone" ([cartesia.ai/customers/bolna](https://cartesia.ai/customers/bolna)).

### 4.4 Past hackathons
- Oct 2024 hackathons: 2,000+ builders, $20k prizes. Winners include **Form Wizard Pro** (voice-guided web forms), Story Narrator, SheBeTalking (speaking styles), **Stella** (voice shopping + try-on), a foul-mouthed robot chef, **SpeakEasy** (language learning that *preserves your voice across languages*), MafiAI (multi-agent voice Mafia), and Hamilton (multi-agent Senate hearing sim) ([cartesia.ai/blog/hacktober](https://cartesia.ai/blog/hacktober)).
- **[INFERRED]** Cartesia rewards personality, emotion range, multi-agent voice casts, and "your voice in another language".

### 4.5 India GTM
- India is Cartesia's 2nd-largest market. Bengaluru office opened Jan 2026 with a $2.5M budget ([StartupWired](https://startupwired.com/2026/01/22/voice-ai-startup-cartesia-enters-india-with-big-plans/)). Named India customers: Raise Financial Services, Bolna, Blue Machines (regulated sectors), Fundamento (lending/insurance), Lorikeet (crisis calls). DPDP-compliant India hosting ([cartesia.ai/regions/india](https://cartesia.ai/regions/india)). Oct 12 2026 blog: "Raise Financial Services x Cartesia: Voice AI for Financial Access in India" ([Cartesia blog](https://cartesia.ai/blog)).

### 4.6 Credits
- Free tier: 20k credits/mo, 1 agent slot, Sonic-3.5 and Ink-2 ([CostBench](https://costbench.com/software/voice-apis/cartesia/free-plan/)). AWS/Google startup offers exist ([AWS](https://aws.amazon.com/startups/offers/cartesia-ai?lang=fr), [Google](https://www.cartesia.ai/google-startups)).

---

## 5. Deepgram

### 5.1 Products / 2026 launches
- **Flux** conversational STT with model-native turn events: `StartOfTurn`, `EagerEndOfTurn` (start the LLM speculatively), `TurnResumed` (cancel it), `EndOfTurn`. Tunable `eot_threshold` / `eager_eot_threshold` / `eot_timeout_ms` ([Bolna Flux doc](https://www.bolna.ai/docs/deepgram-flux.md)). **Flux Multilingual** `flux-general-multi` covers 10 languages **incl. Hindi**, with per-turn language ID and `language_hint`s that can be updated mid-stream ([Flux multilingual](https://developers.deepgram.com/docs/flux/language-prompting.md)). Bring-your-own turn detection and `ForceEndTurn` ([docs index](https://developers.deepgram.com/llms.txt)).
- **Nova-3** covers Assamese, Bengali, Gujarati, Hindi, Kannada, Marathi, Nepali, Punjabi, Tamil, Telugu, Urdu and en-IN, with keyterms updatable mid-stream (Oct 19 2026) ([models overview](https://developers.deepgram.com/docs/models-languages-overview.md), [changelog](https://developers.deepgram.com/changelog/llms.txt)).
- **Flux TTS** (`/v2/speak`, launched Aug 2026): turn-based, **`Interrupt` returns `text_spoken`/`text_remaining`** (exactly what the user heard), and **cross-turn prosody state**. Voices are English-only (`flux-{voice}-en`) ([Flux TTS overview](https://developers.deepgram.com/docs/flux-tts/overview.md), [Interruption](https://developers.deepgram.com/docs/flux-tts/interrupt-handling.md), [voices](https://developers.deepgram.com/docs/flux-tts/voices.md)).
- **India endpoint `api.in.deepgram.com` GA Sep 15 2026** for STT, TTS, Voice Agent and Text Intelligence ([changelog](https://developers.deepgram.com/changelog/2026/9/15.md)). Demand is "concentrated in banking, payments, insurance" ([Deepgram learn](https://deepgram.com/learn/deepgram-india-endpoint-now-generally-available)). Voice Agent API runs STT + LLM + TTS + turn-taking on one WebSocket, with a browser Agent SDK and React UI ([docs index](https://developers.deepgram.com/llms.txt)).

### 5.2 Unique capability
- **Turn-taking inside the model** (eager end-of-turn and resume), and on the TTS side, **knowing exactly what the user heard at barge-in**. This is Deepgram's core brag: "the first conversational speech recognition model built for voice agents" ([Getting started with Flux](https://developers.deepgram.com/llms.txt)).

### 5.3 Bolna integration
- Nova-3/Nova-2 ([Bolna Deepgram STT](https://www.bolna.ai/docs/deepgram-transcriber.md)). **Flux English + Multilingual** since May 2026, exposing eager EOT and language ID ([May changelog](https://www.bolna.ai/docs/changelog/may-2026.md), [blog May 18](https://www.bolna.ai/blog)). Deepgram Indian languages bn/kn/mr/te were added in Bolna Feb 9 2026 ([Feb changelog](https://www.bolna.ai/docs/changelog/february-2026.md)). Bolna TTS supports only `aura`/`aura-2`, not Flux TTS ([Bolna Deepgram TTS](https://www.bolna.ai/docs/deepgram-voice.md)).

### 5.4 Past hackathons / devrel signal
- No 2026 Deepgram hackathon winners list was found. Deepgram DX's newest public demo is **Voice Heist** (pushed 2026-10-21): talk AI gatekeepers into bending a rule, with multi-agent handoffs, function-calling outcomes and a judge LLM scoring each turn. It is "the public version of the game Deepgram runs live" ([github.com/deepgram/voice-heist-demo](https://github.com/deepgram/voice-heist-demo)).
- **[INFERRED]** Deepgram loves playful, multi-agent, interruption-heavy demos where turn-taking quality is visible.

### 5.5 India GTM
- Hiring an India Sales Country Leader ([BuiltIn Bengaluru](https://builtinbengaluru.in/job/sales-country-leader-india/10215793)). APAC HQ in Singapore with +96% YoY APAC API requests (this came from a web-search summary; I did not find or verify the primary URL). BFSI focus (above).

### 5.6 Credits
- $200 free on signup, no expiry ([voice-heist README](https://github.com/deepgram/voice-heist-demo); [agentdeals](https://agentdeals.dev/vendor/deepgram)). Startup Program gives $1k up to $100k for 12 months ([deepgram.com/startup-program](https://deepgram.com/startup-program)).

---

## 6. Kalpa Labs (YC F25)

### 6.1 What they are / products
- SF lab of 3 people. Prashant Shishodia (CEO, ex-Google Assistant ML lead, scaled Gemini variants) and Gautam Jha (CTO, ex-QRT/Squarepoint HFT infra). Building "generalist speech models with LLM-level steerability" that unify STT, TTS, cloning and cross-modal tasks ([YC page](https://www.ycombinator.com/companies/kalpa-labs)).
- **kalpa-tts-1**: English + Hindi + code-switched Hinglish from one model with no language param, ~300 ms TTFA streaming, 11 named voices. Roles include Kiara (radio host, hi+en), Dev (commentator, hi+en), Sana (tutor), Arjun (order updates), Aman (support), Nikhil (clinic line), Wren/Grant/Otis/Tessa/Isla (en) ([kalpalabs.ai](https://kalpalabs.ai/), [voices](https://kalpalabs.ai/voices)).
- **`POST /v1/converse`** ("TTS that has heard the conversation"). You send turns with optional **`audio_wav_b64` spoken history**. If the open turn has only `speaker`, the **model authors and voices the next line**. If it has `text`, you get **contextual TTS** in the voice and rhythm of the conversation so far. A reference clip as the first turn gives in-context voice continuation. There is a stateful WSS with `history_limit` ([Kalpa docs llms-full](https://docs.kalpalabs.ai/llms-full.txt)).
- Report "Towards generalist audio models" (Jul 30 2026): 8B backbone + 300M RVQ decoder, trained from random weights on in-the-wild audio with "no denoising — the room is part of who is speaking". Blind win-rates: 59.3% vs eleven-flash, 55.5% vs **Cartesia sonic-3**, 48.7% vs eleven-v3. The base model (waitlist) does cloning with delivery, scene continuation and style prompts ("speak like sports commentary") ([report](https://kalpalabs.ai/blog/towards-generalist-audio-models)). AudioRealismBench Elo 1364, second only to human recordings (1476) and above Sonic 3.6 (1339) (Design Arena, updated Oct 11 2026) ([kalpalabs.ai](https://kalpalabs.ai/)).
- They proposed **"The Turing Clock"** eval: how long a person can talk to the model before reliably (>50%) deducing it is an AI ([kalpalabs.ai](https://kalpalabs.ai/)).

### 6.2 Unique capability
- **Conversation-conditioned speech.** Spoken history (incl. the *user's* audio) steers tone, so "TTS that isn't tone-deaf" ([report](https://kalpalabs.ai/blog/towards-generalist-audio-models)). Example prompts they list: "talk to elder folks loudly and slowly", "use an empathetic tone when user is in distress", **"Match user's dialect"** (same).

### 6.3 Bolna integration
- Joined Bolna Sep 3 2026. `kalpa-tts-1` became the default Oct 20 2026 (voice Arjun), streamed over a persistent WebSocket, 8 kHz mu-law for telephony ([Bolna Kalpa](https://www.bolna.ai/docs/kalpa.md), [Oct changelog](https://www.bolna.ai/docs/changelog/october-2026.md)).
- **[INFERRED]** Bolna uses the TTS path only, so `/v1/converse` spoken history is not used. To show off converse inside a Bolna call, you would need Bolna's **Custom TTS** (OpenAI-speech-compatible proxy). That path is non-streaming, returns a whole MP3 per request, and has a 20 s timeout ([Custom TTS](https://www.bolna.ai/docs/custom-tts.md)), so there is a latency cost. Or demo converse in a side channel (post-call re-voicing, web demo).
- GitHub: `kalpalabs/stt-bench` benchmarks STT on IndicVoices/Lahaja/Svarah/Vaani across OpenAI, **Deepgram Nova-3, Sarvam**, Gemini. Kalpa also forked `bolna`, `pipecat` and `livekit-agents` (pushed Oct 20–21 2026) ([github.com/kalpalabs](https://github.com/kalpalabs)).

### 6.4 What they ask for
- YC launch asks: **"speech use cases current models fail at"**, production speech practitioners for feedback, and pilot users ([YC page](https://www.ycombinator.com/companies/kalpa-labs)).

### 6.5 GTM
- The homepage demo snippets are a support call, order updates and a Hindi greeting. Voice roles signal support, order updates, radio/podcast, commentary and tutoring ([voices](https://kalpalabs.ai/voices)). After the free tier, pricing is "then a contract" ([kalpalabs.ai](https://kalpalabs.ai/)).

### 6.6 Credits
- **1,000 free minutes for 3 months** on your first org ([Kalpa docs](https://docs.kalpalabs.ai/llms-full.txt)).

---

## 7. Matrix: sponsor × hero capability

| Sponsor | Hero capability (what devrel brags about) | Reachable inside Bolna? | What makes them tweet **[INFERRED]** |
|---|---|---|---|
| **Plivo** | Cheapest India PSTN with streaming included (₹0.38/min); **MultiPartyCall `ai-agent` + `Supervisor` coach roles**; WhatsApp/SMS/Verify on one account | Telephony yes; MPC roles **no** (call Plivo directly) | Real PSTN at scale, AI as a participant in multi-human calls, multichannel follow-up |
| **Exotel** | AgentStream <20 ms frames; App Bazaar Voicebot + **Connect human handoff**; **one human supervising many bots** (Harmony/Monitoring Officer); ExoVerify missed-call; WhatsApp payments | Telephony + Voicebot applet yes; Harmony/AI Assist no | Human+AI hybrid ops for contact centres, Bharat telco primitives (missed call, masking) |
| **Sarvam** | 22-language Saaras v4 with **translate/codemix** modes + diarization; **222 use-case persona voices**; **cross-lingual cloning**; **Sarvam Vision** doc AI | STT (transcribe mode only) + Bulbul yes; Vision/translate/cloning/LLM via direct API | Bharat inclusion (MSME, accessibility, vernacular), voice + documents |
| **Cartesia** | Sonic 3.6 latency + **emotion tags** (en) + **one cloned voice speaking many languages natively** + Hinglish/normalization + localize/infill | Sonic 3.x + cloning yes; emotion params likely no | Personality and emotional range, multi-voice casts, your voice in many languages |
| **Deepgram** | **Flux model-native turn-taking** (eager EOT/resume) + Flux Multilingual per-turn LID (incl. Hindi); Flux TTS `text_spoken` on barge-in; India endpoint | Flux + Nova-3 yes; Flux TTS no | Interruption-heavy, fast back-and-forth, multi-agent, game-like demos |
| **Kalpa** | **Conversation-conditioned TTS** (`/v1/converse` with spoken history; model can author the next turn); Hinglish single model; #1 non-human realism Elo; "Turing Clock" eval | `kalpa-tts-1` TTS yes; converse **no** (custom-TTS proxy or side channel) | Uncanny realism in Hinglish, emotional/contextual adaptation, use cases other models fail at |

---

## 8. Idea seeds where several sponsors' hero capabilities are load-bearing

Taken or rejected ideas are excluded: scam honeypot, bargaining, collections, farmer helplines, legal/grievance, kids tutor, clinic helpdesk, healthcare, two-language interpreter, rental caller. Every seed below is **[INFERRED]**.

### Seed 1. "Turing Clock: Phone Line Edition" (realism arena + regression harness)
People dial a real Indian number and talk in Hinglish or regional languages. They get a human or one of several AI stacks at random (Kalpa / Cartesia / Sarvam voice × Deepgram Flux / Sarvam STT). They press a key the moment they think it's an AI. A public leaderboard shows "seconds to detection" per stack on **8 kHz telephony**, the condition every lab ignores.
- Load-bearing: **Kalpa** (literally their proposed eval, and their YC ask), **Cartesia / Sarvam** (contestants), **Deepgram Flux** (turn-taking is what gives AIs away), **Plivo + Exotel** (real PSTN on two carriers; compare codecs/latency), and **Bolna** (each stack is a Bolna agent; Graph Agent for consent/DTMF; extraction for results).
- Dev-tool angle: the same harness becomes "red-team callers" that simulate accented, noisy, code-switching, interrupting callers against *your* Bolna agent. YC funds voice-agent eval/testing companies.
- Risk: it ranks sponsors against each other. Frame it as "where Indian phone voice is still failing", not winners and losers.

### Seed 2. Contact-centre "Angry Customer Gym" with a live human coach
Trainee agents for BPO, insurance or bank support call a practice line. An AI plays difficult customer personas (furious, confused, crying, code-switching) and escalates or calms based on how the trainee handles it. A senior trainer can **silently join and whisper** to the trainee. A post-call scorecard covers interruptions, dead air, empathy and resolution.
- Load-bearing: **Cartesia emotion** (angry/sad/scared are its strongest primaries) + **Kalpa converse** (persona reacts to the trainee's *actual* tone via spoken history), **Deepgram Flux** turn events (measure talk-over and latency), **Plivo MPC `Supervisor` coach mode** (the whisper), **Exotel** (their buyer is the contact centre; Harmony/AI Assist story), **Sarvam Saaras** (score Hindi/Tamil trainees; codemix).
- Not a "kids tutor": adult workforce, B2B, sold to Exotel/Plivo's own customers.

### Seed 3. "One Supervisor, Twenty Calls" cockpit (Exotel's Monitoring Officer, built)
A live dashboard of N concurrent Bolna calls (demo vertical: motor-insurance claim intake / FNOL, or D2C returns). Each call has live transcript, risk flags (Deepgram/Sarvam keyterms, sentiment) and a one-click action: **whisper an instruction to the bot**, or **take over** (Exotel Connect applet / Bolna transfer). At takeover the human sees exactly what the caller already heard (Flux TTS `text_spoken` pattern).
- Load-bearing: **Exotel** (Voicebot + Connect handoff is their documented Bolna path; Harmony thesis by the co-founder who speaks at Symphony), **Plivo MPC** (`ai-agent` + `Supervisor` roles), **Deepgram Flux** (clean barge-in/turn boundaries), **Sarvam** (Indic keyterms/flags), **Bolna** (transfer tool, extraction on graph edges, Workflows for the follow-up WhatsApp).
- Best fit for the Bolna team (platform ops) and Exotel.

### Seed 4. "Apni Awaaz" shop line: the owner's own voice, in every customer's language
A kirana, D2C or salon owner records 10–60 s once (with consent, disclosed as AI). Customers call or WhatsApp-call and get answered **in the owner's own voice**, in whatever language they speak, with mid-call switching. Orders and bookings land in a sheet, and a WhatsApp confirmation follows.
- Load-bearing: **Cartesia** (Instant clone that keeps the accent, plus the "make your voice multilingual" feature, plus `normalization` for prices/order IDs), **Deepgram Flux Multilingual** (per-turn language ID drives the switch), **Sarvam** (Saaras v4 + cross-lingual clone for languages Flux/Cartesia don't cover, e.g. Odia/Malayalam; side-by-side), **Plivo** (number + WhatsApp + SMS), **Bolna** (multilingual agent with per-language STT/TTS providers, Workflows for WhatsApp follow-up).
- Cartesia's hackathon history (SpeakEasy) shows they reward "your voice across languages". This is a single-party agent, not a two-party interpreter.

### Seed 5. "Cricket Adda" phone-in show with an AI host
Call a number during a live match and an AI radio host/commentator banters with you in Hinglish (or Tamil/Bengali). It pulls live scores via Bolna's web-search tool, reacts to your mood, and handles excited fans who talk over it. Optional: a conference "adda" where several callers share the room.
- Load-bearing: **Kalpa** (they literally ship "Dev — Commentator" and "Kiara — Radio host" Hinglish voices; style prompts like "speak like sports commentary"), **Bolna web search** (Oct 8 2026, built for "scores"), **Deepgram Flux** (constant barge-ins), **Cartesia** (`[laughter]` and `excited`/`triumphant` emotion for English segments), **Sarvam** (regional callers), **Plivo/Exotel** (inbound burst capacity; Plivo MPC for multi-caller rooms).
- Highest "tweetability" and demo-stage energy. Weaker on B2B.

### Seed 6. Missed-call voice classifieds ("OLX for feature phones")
A seller gives a missed call. The AI calls back free and takes a spoken listing ("2 goats, Sitapur, ₹18k") in any of 22 languages, structuring it via Saaras `translate`. Buyers call, browse listings read in their own language, and the AI **bridges buyer and seller on a masked number**. SMS/WhatsApp carries the details.
- Load-bearing: **Exotel** (missed-call + Connect/number-masking bridging is their DNA; DLT), **Sarvam** (22-language STT with translate mode; Bulbul persona voices), **Kalpa** (natural Hinglish callback), **Plivo** (SMS/WhatsApp fallback, cheap callbacks), **Bolna** (Graph Agent for the listing flow, extraction, outbound callbacks).
- Avoid framing it as agriculture or a farmer helpline. Position it as general local commerce.

### Seed 7. "Bolo-for-me" relay calling for deaf and speech-impaired people
The user types or taps (or uses saved phrases) in an app. An AI places a **real PSTN call** to a bank, gas agency or electrician and speaks for them, live. The other side's speech appears as live captions in the user's language. The user can pick a voice, or use a voice banked earlier.
- Load-bearing: **Deepgram Flux / Sarvam Saaras** (live captions; Flux turn events tell the user "your turn now"), **Kalpa / Cartesia** (natural voice; Cartesia clone for voice banking; emotion), **Plivo/Exotel** (real calls to businesses that only answer phones), **Bolna** (Web Call SDK for the user side + outbound to the business).
- Sarvam's past winner "Setu" (communication for people who cannot speak) shows that judges reward this. Risks: it is a call mediator (check it doesn't feel like the rejected interpreter), and it must be clearly disclosed to the callee.

### Seed 8. Voice-first KYC/onboarding with a document handoff mid-call
During an onboarding call for a micro-loan, an insurance policy or a merchant account, the agent says "send me your PAN/Aadhaar photo on WhatsApp now". **Sarvam Vision** extracts the fields while the call continues. The agent reads them back in the caller's language (digits in English inside a Hindi sentence via Cartesia `normalization`) and verifies via missed-call OTP.
- Load-bearing: **Sarvam** (Vision KYC/handwriting, Saaras, `sanchita_hi_kyc` persona voice), **Cartesia** (alphanumeric read-back on 3.6), **Exotel** (ExoVerify missed-call, WhatsApp payments for a ₹1 penny-drop), **Plivo** (WhatsApp media inbound + SMS), **Deepgram** (India endpoint for BFSI data residency, Nova-3 keyterms for names), **Bolna** (Workflows with WhatsApp steps, extraction with allowed_values).
- Hits the BFSI GTM shared by Sarvam, Cartesia, Deepgram and Exotel. It is onboarding, not collections.

---

## 9. Caveats
- I could not read the buildathon's credits-request form link or any judging rubric. The page only says the selection reviews "the strongest builds" ([buildathon page](https://www.bolna.ai/symphony/buildathon)).
- Cartesia's Voice Changer docs were behind a Vercel checkpoint. It shows up only in the 2025 changelog ([2025 changelog](https://docs.cartesia.ai/changelog/2025.md)), so I treated it as unverified.
- Bulbul V4 *expressive* controls (emotion/laughter) were shown at Epoch as a research preview. The shipped `bulbul:v4-flash` documents only persona voices and pace ([Bulbul docs](https://docs.sarvam.ai/api/getting-started/models/bulbul.md)).
- I found no published winners for Plivo, Exotel or Deepgram hackathons in 2026.
