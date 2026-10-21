# Prior-art / dedup check: "Pehchana Kaun?" (phone-call Turing test for Indian voice AI)

Checked 2026-10-21. Sources: WebSearch/WebFetch, arXiv API, gh search (read-only). No logins. X/Twitter pages could not be fetched (402), so X-only announcements may be missed.

Legend for the closeness columns: **Mod** = modality (T = text, V = browser voice, P = real phone/PSTN, Vid = video call). **Live-H** = a live human arm on the other end (judge doesn't know if human or AI). **TTD** = time-to-detection metric. **Indic** = Indian languages. **LB** = public leaderboard.

---

## 0. Summary table (closest first)

| # | Thing | Mod | Live-H | TTD | Indic | LB | Status / date | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | Kalpa Labs "Turing Clock" (proposed metric) | V (concept) | not specified | **YES (the whole idea)** | Hindi/EN (Kalpa models) | no | Proposal only, 30 Jul 2026 blog; no demo/game/LB found | https://kalpalabs.ai/blog/towards-generalist-audio-models |
| 2 | "Human or Machine? A Preliminary Turing Test for S2S Interaction" (STuring, ICLR 2026) | V (recorded dialogues, judged afterwards) | YES (673 human-human dialogues) | no (binary judgement + 18-dim taxonomy) | no (zh/en) | player-accuracy LB on their game platform | arXiv Feb 2026, v3 Sep 2026; code/data released | https://arxiv.org/abs/2602.24080 , https://github.com/Carbohydrate1001/Turing-Test |
| 3 | Tavus Griffin "real-time video Turing test" | Vid (live call) | NO (all AI, participants were told it was a person) | **partial**: "those who did suspect tended to suspect within the first 20 seconds" | no | no (internal study, 54 people) | 1 Oct 2026 | https://www.tavus.io/griffin |
| 4 | AI21 "Human or Not?" | T | YES | no (fixed 2 min) | no (but India was a top-playing country, lowest accuracy 63.5%) | no | 2023 (Apr to Jun), 15M convos, paper arXiv 2305.20010 | https://www.ai21.com/blog/human-or-not-results , https://arxiv.org/abs/2305.20010 |
| 5 | humanornot.so (independent successor) | T | YES | no | no | no (planned) | Live since Dec 2023, ~80k games/day, public PostHog stats | https://humanornot.so/blog/our-launch-story |
| 6 | Artificial Analysis Speech Agent Arena | V (live voice calls) | NO (AI vs AI preference) | no | not mentioned | YES (Elo) | Announced 24 Aug 2026 | https://artificialanalysis.ai/articles/announcing-the-speech-agent-arena |
| 7 | Design Arena AudioRealismBench (the "speech realism leaderboard" Kalpa cites) | clips | human recordings used as anchor ("how often chosen over a real person") | no | no (US English only) | YES (Elo); Kalpa TTS beta #2, Elo 1331 | 2026 | https://designarena.ai/leaderboard/audiorealismbench |
| 8 | Voice Arena (Josh Talks; CEO Shobhit Banga) Hindi TTS leaderboard | clips | no | no | **Hindi** (+6 non-Indic langs) | YES | 2026, 15.5K+ Hindi votes | https://voicearena.com/tts-leaderboard/hindi , https://voicearena.com/tts-methodology |
| 9 | voiceofindia.ai (AI4Bharat IIT-M + Josh Talks) | clips / benchmarks; claims "agents" track | no evidence | no | **YES, 15 langs** | YES | Launched 4 Aug 2026 | https://voiceofindia.ai/press/voice-of-india-launch |
| 10 | Jones & Bergen UCSD Turing tests (GPT-4 2024; GPT-4.5 73% 2025) | T | YES (3-party) | no | no | no (turingtest.live game exists) | 2024-2025 | https://arxiv.org/abs/2503.23674 , https://turingtest.live/ |

Nothing found that combines **real phone number + live human arm + time-to-detection + Indic + public leaderboard**. Details below.

---

## 1. Kalpa Labs "Turing Clock" (the direct inspiration)

- **Exact proposal text** (blog "Towards Generalist Audio Models", 30 Jul 2026, Prashant Shishodia, Gautam Jha & Kalpa team; in the section "Limitations & Future Axes of Improvements"): Turing Clock = *"How long does it take for you to realize you are talking to AI?"*, i.e. *"how long can a person talk with a model before deducing, reliably better than 50% accuracy, that it's an AI?"* They say they *"expect to report this number for all of our new releases."* https://kalpalabs.ai/blog/towards-generalist-audio-models
- **Has Kalpa built it?** No public Turing Clock demo, game, phone line or leaderboard found on kalpalabs.ai (homepage, /realtime, blog), the YC page (https://www.ycombinator.com/companies/kalpa-labs), or the Bolna integration docs (https://www.bolna.ai/docs/kalpa). The /realtime page is a plain "Talk to Kalpa" browser voice call (EN/HI, barge-in), with no guessing element. https://kalpalabs.ai/realtime
- The "Benchmark" section on their homepage is **AudioRealismBench** (Design Arena), not their own. Kalpa TTS Beta v0.1 placed #2 (Elo 1331, behind Bland Speech v3) per Design Arena's post. https://digg.com/tech/z7pnih38
- The blog cites as existing leaderboards: AA TTS (controlled voice), TTS-Arena-V2, and Design Arena audio. None of them measure time-to-detection.
- No GitHub code hits for "turing clock" related to voice (gh search code).
- Kalpa = YC F25, SF, Indian founders, kalpa-tts-1 EN/HI/Hinglish, ~300 ms TTFA, available inside Bolna.
- **Implication [INFERRED]:** Kalpa named the metric and publicly committed to report it, so they are the most likely party to build their own Turing Clock eval, probably internally and for their model only. A neutral, multi-vendor, public, phone-based version is not taken. Using the name "Turing Clock" means using their term; credit it or partner with them instead of looking like you copied it.

## 2. Text Turing games

- **AI21 "Human or Not?"** (Apr to Jun 2023): 2-min chat with a human or a bot (Jurassic-2, GPT-4). 15M+ conversations, 2M+ participants. 68% correct overall; 73% correct when partner was human, 60% when bot. **India had the lowest accuracy of the top-playing countries (63.5%)**; France highest (71.3%). Paper: "Human or Not? A Gamified Approach to the Turing Test", arXiv 2305.20010. Text only. https://www.ai21.com/blog/human-or-not-results , https://arxiv.org/abs/2305.20010
- **humanornot.so** (independent couple Oleg & Kate, Oct to Dec 2023 onwards, still live 2026): text only, ~80k games/day, 41-42% bot success rate, public PostHog dashboard, leaderboards only "planned". https://humanornot.so/blog/our-launch-story , https://humanornot.so/blog/is-human-or-not-playable-2026
- **Clones**: humanornot.io, playturing.com (60 s chat), turingtest.live (3-party, UCSD-style), play.turinggame.ai (could not fetch). All text. https://humanornot.io/ , https://playturing.com/ , https://turingtest.live/
- **"The Turing Game"** (JKU Linz / Ars Electronica Sep 2024, NeurIPS 2024 workshop): 2 humans + 1 AI in group text chat. https://neurips.cc/virtual/2024/104302
- **Jones & Bergen (UCSD)**: GPT-4 at 54% judged human in a 2-party test (arXiv 2405.08007); GPT-4.5 with persona prompt at 73% in a 3-party test (arXiv 2503.23674, Mar 2025). Text. https://arxiv.org/abs/2503.23674
- "The Turing Test Is More Relevant Than Ever" (arXiv 2505.02558): 3-party text interface. https://arxiv.org/abs/2505.02558
- Minor GitHub clones (e.g. Snehajit999/humanornot, 38 stars, a text "human or bot" sentence quiz). Not relevant.

## 3. Voice Turing tests, games and studies

**Interactive and conversational (closest):**
- **STuring: "Human or Machine? A Preliminary Turing Test for Speech-to-Speech Interaction"** (Li et al., CUHK-Shenzhen / Benyou Wang group; arXiv 2602.24080, Feb 2026, ICLR 2026, v3 Sep 2026). 28 participants from 10 countries held 20 to 60 s studio-recorded conversations with 9 S2S systems (GPT-4o, Gemini 2.5 Pro, Qwen3, Kimi, GLM-4.5, Hunyuan, Doubao, Claude Sonnet 4, iFLYTEK Spark) **and with other humans** (1,486 dialogues: 669 H-M, 673 H-H, 144 TTS). **397 third-party judges** gave 2,968 judgements on a **gamified online platform with a public leaderboard of judge accuracy**. Zh + En. Result: *"No existing evaluated S2S system passes the test."* AI gave itself away through paralinguistics (rigid prosody, no disfluencies), emotional expressivity and a "mechanical persona" (sycophancy). 18-dimension human-likeness taxonomy. Code + data released. https://arxiv.org/abs/2602.24080 , https://arxiv.org/html/2602.24080v1 , https://github.com/Carbohydrate1001/Turing-Test
  - Differences from Pehchana Kaun: judges are **not** the person in the conversation (they listen to recordings afterwards); no phone; no time-to-detection; no Indic; leaderboard ranks players, not vendors.
- **Tavus Griffin** (1 Oct 2026): 54 participants had a 1-min **video** call. They were told the partner was a person; it was the AI. 48% believed it was human (the previous model got 2.4%). *"those who did suspect tended to suspect within the first 20 seconds."* Internal study, no human arm, no public game or leaderboard. https://www.tavus.io/griffin , https://cybernews.com/ai-news/tavus-griffin-ai-model/
- **Artificial Analysis Speech Agent Arena** (24 Aug 2026): paid, screened participants do the same task (dental booking, takeout) in **live voice calls** with two hidden S2S models (about 2 to 3 min) and pick a preference. Elo board (Gemini 3.1 Flash Live leads). Models are told "never break role even if asked whether you are an AI". No human arm, no "is it human?" question, no TTD, no Indic mentioned. https://artificialanalysis.ai/speech-to-speech/arena , https://artificialanalysis.ai/speech-to-speech/arena/overview
- **Talk Arena (Stanford SALT, ACL 2025)**: 7,500 interactive large-audio-model interactions from 484 users, pairwise preference. Not a Turing test. https://arxiv.org/abs/2502.15919
- **RealityTest** (Gausen, Summerfield, Kirk et al., arXiv 2606.00168, May 2026): 3,152 real "are you an AI?" probes from about 750 people in 49 countries and 5 languages, run against 17 text and 6 speech models. A single suppression instruction cuts disclosure to below 30%. Disclosure-focused, not detection timing. https://arxiv.org/abs/2606.00168
- **"The Machines Are Calling"** (arXiv 2609.11137, Sep 2026): LLM-persona **voice honeypot on real US phone numbers**, 10,987 inbound calls over 66 days. Synthetic-voice detection on the first 10 s, with blinded listeners. This is the opposite direction (measuring robocallers), but it is the closest **real-PSTN + LLM persona** precedent. https://arxiv.org/abs/2609.11137v2

**Clip-based (listen and guess, not conversational):**
- **Audio Turing Test (ATT)** for Chinese TTS (arXiv 2505.11200, May 2025): human-likeness judgements, ATT-Corpus, Auto-ATT judge model on Hugging Face. https://arxiv.org/abs/2505.11200
- **Lancaster "Bot or Not: Audio Edition"** (Hardaker, Brown, McVean): 15 scripted clips, human or AI. https://www.lancaster.ac.uk/linguistics/news/bot-or-not-audio-edition-can-you-tell-whos-talking
- **Barrington, Cooper & Farid (Sci Rep, arXiv 2410.03791)**: people detect AI voice clones only about 60% of the time. Berkeley quiz: https://farid.berkeley.edu/misc/AIorNotQuiz2 , paper https://arxiv.org/abs/2410.03791
- **WSJ voice-deepfake quiz** (via IOActive): https://www.ioactive.com/article/article-the-wall-street-journal-can-you-tell-the-difference-between-a-human-voice-and-ai-take-our-quiz/
- "Moravec's Paradox: Towards an Auditory Turing Test" (arXiv 2507.23091): auditory perception challenges, not conversation.
- GitHub toys: TalehMalikov/voice-turing-test (Oct 2026, guess your own ElevenLabs clone), MithunShivakoti/AI_VoiceTuringTest (heuristic mic classifier). Trivial.

**Real-world and stunt precedents (unplanned Turing tests, no game):**
- ARN CADA Sydney: an undisclosed AI radio host "Thy" (ElevenLabs) ran for ~6 months before a journalist exposed it (2025). https://www.odditycentral.com/news/radio-station-secretely-uses-ai-host-for-six-months-without-anyone-noticing.html
- Google Duplex (2018): real restaurant calls; callees didn't realise. https://www.cbsnews.com/texas/news/googles-robot-assistant-can-make-your-dinner-reservations/
- Jolly Roger Telephone (bots wasting telemarketers' time). https://forums.theregister.com/forum/all/2023/07/03/jolly_roger_telephone_company/
- Kwindla Kramer (Daily/Pipecat) on X: *"We blew past the Turing test for voice agents about a year ago... people often forget they are talking to a voice agent"* (anecdotal, from deployment data; post not fetchable). https://x.com/kwindla/status/2105715052146033114
- Art: "2147" AI payphone (Sonar), "Turing Test" installation at 38C3 (Conrad Weise, conceptual, mechanics unclear). https://www.designboom.com/design/2147-voice-future-reclaimed-payphone-ai-interface-divina-machina-qs-ventures-sonar-d/ , https://events.ccc.de/congress/2024/hub/en/project/turing-test/

**Phone hotlines:** no "call this number and guess human vs AI" hotline found anywhere. Phone numbers that connect you to AI exist (OpenAI 1-888-GPT-0090, Callanai, the Kalpa/Bolna demo agents), but none have a human arm or a guessing mechanic. https://help.openai.com/en/articles/11391933-1-888-gpt-0090-openai-help-over-phone

## 4. TTS / voice arenas and leaderboards

- **HF TTS Arena V2** (TTS-AGI): blind pairwise TTS clips, mostly English. https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2
- **Artificial Analysis Speech Arena (TTS)** plus the Controlled Voice Arena, which was extended to 9 more languages **including Hindi** (2026). https://artificialanalysis.ai/text-to-speech/arena , https://artificialanalysis.ai/text-to-speech/leaderboard/controlled-voice
- **Design Arena AudioRealismBench**: native-speaker listeners pick "which is more human" from two clips; Bradley-Terry Elo; **a real human recording enters every pool as an anchor**, giving a "% chosen over a real person" figure. Registers: phone agents, conversations, explainers. Explicitly *does not* measure full-duplex interaction or multilingual quality. US English only. https://notes.designarena.ai/audio-realism-benchmark-measuring-realism-in-audio-models/ , https://designarena.ai/leaderboard/audiorealismbench
- **Voice Arena** (Josh Talks; Shobhit Banga is co-founder of Josh Talks and CEO of Voice Arena; methodology advised by Shinji Watanabe, CMU): pairwise "which sounds more like a real person", 100 to 200 native raters per language. Hindi set is 100 sentences (93 with English words, 49 with numbers/IDs). Langs: US EN, **Hindi**, JA, pt-BR, es-MX, Arabic, VI. States it does not evaluate end-to-end voice-agent performance. https://voicearena.com/tts-methodology , https://voicearena.com/tts-leaderboard/hindi
  - Josh Talks also ran the 20k-vote, 11-language blind naturalness study in which Sarvam Bulbul V3 beat ElevenLabs and Cartesia. https://caller.digital/blog/indic-tts-benchmark-bulbul-elevenlabs-sarvam-google-ai4bharat-2026
- **voiceofindia.ai** (AI4Bharat IIT-M + Josh Talks AI, launched 4 Aug 2026): "India's first independent multimodal AI evaluation platform", human-evaluated leaderboards across speech (ASR, TTS, **end-to-end voice agents**, speech translation), LLM, OCR, safety and legal. ASR benchmark covers 15 languages and 1,200+ districts (OI-WER metric, arXiv 2604.19151). I found no Turing-style or phone-call component, but the site is JS-rendered and only partly readable. https://voiceofindia.ai/press/voice-of-india-launch , https://arxiv.org/html/2604.19151
- **Josh Talks "Human-1"** (11 Mar 2026): open full-duplex Hindi conversational model trained on 26k hours of two-person Hindi conversations. Shobhit Banga: *"What it has not yet learned well is how to participate in conversation."* https://www.analyticsinsight.net/press-release/josh-talks-introduces-the-worlds-first-open-full-duplex-conversational-ai-model-in-hindi
- **AI4Bharat Indic LLM-Arena**: text LLMs. https://ai4bharat.iitm.ac.in/blog/indic-llm-arena/
- **Coval public Voice AI benchmarks**: https://benchmarks.coval.ai/overview (JS page, contents not readable). Cekura publishes orchestration benchmarks. Neither appears to include a human-likeness Turing component.
- **Academic full-duplex benchmarks** (automatic, no human-vs-AI guessing): ICASSP 2026 HumDial challenge (arXiv 2601.05564), HumDial-FDBench (2604.21406), FLEXI (2509.22243), Full-Duplex-Bench, S2S-Arena (2503.05085, paralinguistic instruction following).

## 5. Voice-agent eval companies (Hamming, Coval, Cekura, Roark, Bluejay, etc.)

- All of them sell **simulated-caller QA**: AI "voice characters" call your agent at scale, plus LLM judges and production monitoring. Coval is founded by an ex-Waymo lead; Cekura offers accent and noise personas; Hamming runs thousands of concurrent test calls. https://www.coval.ai/blog/hamming-vs-bluejay , https://www.cekura.ai/blogs/hamming-alternative
- There is a 2025 Oxford/UPF paper benchmarking these testing platforms against 21,600 human judgements. https://arxiv.org/abs/2511.04133
- **None found running a public human-vs-AI phone game, and none publishes a human-likeness or time-to-detection score.** Their metrics are task success, latency, interruptions and compliance. [INFERRED] Human-likeness is a gap in their stack, so they could be either buyers or competitors.
- Bolna (YC F25, $6.3M seed, General Catalyst), Smallest.ai ($13M, Jul 2026, explicitly aiming for "indistinguishable from talking to a human"), Sarvam, Gnani and Ringg all claim human-likeness. None runs a public Turing test. https://techcrunch.com/2026/07/31/smallest-ai-raises-13m-to-build-ultra-fast-voice-ai-that-sounds-genuinely-human/

---

## 6. Verdict

**What already exists (do not claim these as novel):**
- Human-or-AI guessing games with a live human arm: done at huge scale in **text** (AI21 2023, humanornot.so, UCSD).
- A voice/S2S Turing test with human-human controls: **STuring (ICLR 2026)** has it, but with recorded dialogues judged by third parties, Zh/En only.
- "% of judges who pick AI over a real human" as a leaderboard: **AudioRealismBench** (clips, English).
- Live-voice-call arenas with Elo: **AA Speech Agent Arena** (preference, no human arm).
- Indian human-eval leaderboards for TTS/ASR (and claimed voice agents): **Voice Arena / voiceofindia.ai (Josh Talks + AI4Bharat)**.
- The metric itself, time until you realise it's AI: **named and proposed by Kalpa ("Turing Clock")**, but not built publicly. Tavus reports an informal "most suspicions within 20 s".

**What appears genuinely novel (no match found):**
1. **A real PSTN phone number** as the interface. Everything else is web, studio or recorded. The phone channel (8 kHz codec, network jitter, Indian telecom conditions) is exactly where Indian voice agents are deployed. [INFERRED]
2. **The judge is the caller, deciding live, with a "you're a bot!" barge-in.** That turns the binary verdict into a **survival-time measure** (Kaplan-Meier style, with right-censoring at 2 min). STuring and AI21 use fixed-length conversations and an after-the-fact binary verdict; Tavus logged detection time only informally.
3. **A live human arm on a voice/phone channel**, so you get a calibrated false-accusation rate against real humans. Nobody has this on voice calls.
4. **Indic and code-switched languages** (Hindi, Hinglish, others) for a conversational Turing test. Zero prior art. Even Design Arena says it does not cover multilingual or full-duplex.
5. **Labelled giveaway cues** captured at the moment of detection (pause, number reading, no laughter, interruption), per language and per stack. STuring has a post-hoc 18-dimension taxonomy; nobody tags cues at the moment of detection.
6. **A public multi-vendor board of time-to-detection** across stacks (Kalpa vs Cartesia vs Sarvam via Bolna).

**Risks and overlaps [INFERRED]:**
- **Kalpa** coined "Turing Clock" and said they'll report it on every release. They might build it themselves (for Kalpa only), or they might welcome a neutral third party. Pitch it as "the first public, multi-vendor Turing Clock" and credit the term, or rename it ("Pehchana Kaun clock"). Don't present the metric as your own invention.
- **Josh Talks (Voice Arena / voiceofindia.ai, Human-1)** is the most capable Indian incumbent: rater networks in 15 languages, an Indian eval brand, and its own full-duplex Hindi model. They could add a "voice agent Turing" track quickly. They also have a conflict of interest, since they score others while building Human-1. That conflict is your neutrality angle.
- **Artificial Analysis** could add an "is it human?" question and a human arm to the Speech Agent Arena with little effort.
- Ethics and legal: the human arm and recorded calls need consent, a disclosure flow and DPDP Act compliance. The "Machines Are Calling" honeypot shows the pattern but in reverse. Keep the human-operator pool paid and screened.

**How to differentiate:**
1. Lead with **time-to-detection on real phone calls with a live human control**: "median seconds until an Indian caller says 'you're a bot', per stack, per language, with a false-accusation rate against real humans." No current leaderboard can produce that number.
2. Make the **cue labels at the moment of detection** the dataset product (the timestamp of the "bot!" call plus its cause), which arenas don't collect. It is directly actionable for vendors ("your number reading in Tamil gets you caught at 23 s").
3. Go **Indic, phone-native and code-switched first**: Hinglish, numbers and amounts, UPI/OTP-style readouts. Voice Arena's Hindi set already shows numbers and code-mix are where models break.
4. Stay a **neutral multi-vendor evaluator**, not a model company (the contrast with Kalpa, Josh Talks and Tavus, which each evaluate their own model).
5. Cite the AI21 hook: Indians were the *least* accurate at spotting bots in 2023 (63.5%). "Pehchana Kaun?" tests whether that still holds by voice, in Indian languages.
