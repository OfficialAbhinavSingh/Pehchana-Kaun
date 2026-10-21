# Global Voice-AI Hackathon Winners (2024-2026): Idea Mining for Bolna Symphony Buildathon

Compiled 2026-10-21. Scope: global, non-India-specific voice hackathons only (Bolna/India-specific events are covered elsewhere).
Convention: every fact carries an inline source URL. Anything marked **[INFERRED]** is my opinion or synthesis, not a sourced fact.

Coverage gaps (stated up front so nothing is overclaimed):
- **Retell, Hume AI (2024-26), HackMIT, TreeHacks voice tracks, LiveKit AIEWF hackathon, Twilio ConversationRelay challenge:** I searched for each and found no published winner list. TreeHacks 2025 and 2026 grand prizes were not voice projects ([2025](https://stanforddaily.com/2025/02/18/treehacks-awards-200000-in-prizes-to-students-from-around-the-world/), [2026](https://stanforddaily.com/2026/02/15/12th-annual-treehacks/)).
- **ElevenLabs Global Hackathon, Dec 11 2025 (30 cities, $200K+):** the AI Tinkerers results pages for London, SF, NYC, Berlin, Bengaluru, Singapore and others still say "Results Coming Soon" ([Berlin results page](https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/results)). The Berlin *showcase* lists projects but not placements ([showcase](https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/showcase)).
- **ElevenHacks 2026 (11 weekly hacks, $240K+):** winners were due June 25 2026, per a search snippet of [hacks.elevenlabs.io](https://hacks.elevenlabs.io/). The page blocks fetching behind a Vercel checkpoint, so I could not confirm the winners.
- **YC x AgentPhone "Call My Agent Hackathon" (May 17 2026):** the overall winner is not published anywhere I could reach. Details are in section 1.

---

## 1. Hackathon-by-hackathon winners

### 1.1 ElevenLabs Worldwide Hackathon (with a16z), Feb 22-23 2025
Source: [ElevenLabs winners blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)
- **Format:** 300+ agents built across 6 in-person cities, 3 community events and an online Discord track, over 40 hours. Partners were a16z, PostHog, Lovable, Clerk, Make, PICA, fal.ai, Vercel and Mistral ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)).
- **Judges:** Mati Staniszewski (ElevenLabs CEO), Guillermo Rauch (Vercel), James Hawkins (PostHog), Anton Osika (Lovable), and Bryan Kim and Justine Moore (a16z) ([search snippet of blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)).

| Placement | Project | One-liner | Why it won / notes |
|---|---|---|---|
| **Global top prize** (London #1) | **GibberLink** (Boris Starkov, Anton Pidkuiko) | Two AI agents on a call detect each other and switch from English to a sound-level data protocol | Judges were unanimous, and the demo video went viral (Forbes covered it) ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)). Demo scenario: a hotel booking call where the "receptionist" notices the caller is an AI and proposes switching modes ([Wikipedia](https://en.wikipedia.org/wiki/Gibberlink)). Repo [PennyroyalTea/gibberlink](https://github.com/PennyroyalTea/gibberlink): 4,918 stars, created 2025-02-23 (gh API, checked 2026-10-21). |
| Online 1st | **Hugo Tour Guide** | Location-aware AI travel companion | "Feature-rich conversational agent" ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Online 2nd | **Pep** | Multimodal voice + vision physical-therapy coach | Healthcare impact ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Online 3rd | **Agent SFX** (Philippines) | Generates voiceovers and SFX for game developers using vision models (Godot) | Practical dev tool ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| London 2/3 | Espresso Labs; Vox Populi | Voice-first personal assistant; 3D sandbox with AI speech | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| NYC 1/2/3 | **Unstuck**; **Procuro**; Show Me How | Voice agent for any website; **supply-chain parts procurement via agent phone calls**; task-learning guide | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| SF 1st | **Dealwise** (Yvonne Li, Jason Fan) | **AI agent that phones businesses for price quotes and availability** (household services) | The team found that adding slight pauses, a mild accent and natural hesitation made the people being called engage with the AI caller ([PostHog recap](https://posthog.com/blog/elevenlabs-hackathon)) |
| SF 2nd | **Roadmate** | Driving copilot / drowsiness monitor with dashcam | Personal story: a teammate's friend had a drowsy-driving accident, and this was in the pitch deck ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)) |
| SF 3rd | **Hippo** | Meeting-quality analyzer (floor-sharing, sentiment, information density) | Unusual domain expertise on the team (lexicologists); the recap's lesson was "weirdness is your weapon" ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)) |
| Warsaw 1/2/3 | **DeepSky**; **Claimsio**; Voyagr | Airspace-safety voice AI; **automated debt-collection compliance**; travel insider | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Seoul 1/2/3 | **Voice Guardian**; AMUSH; PrintMoneyAI | **Home protection via AI voice**; multilingual AI shopping host; conversational PM agent | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Bangalore 1/2/3 (city of the global event) | lossfunk; ECHO AI; Pochinki | AI film generator; thought-organization agent; podcast ad integration | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Partner prizes | Playcade (fal.ai); PostHog Meeting Copilot; Voyagr (Lovable) | | ([blog](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)) |
| Austin (AI Tinkerers community node) 1/2/3 | ARIA; Hello: Earth; Austin culture guide | 3D real-time voice agent; newcomer civic/culture guide | ([AI Tinkerers Austin results](https://austin.aitinkerers.org/hackathons/h_X_WXp4d33gk/results)) |

Notable non-winner: **Badgermole**, a camera-based scene description tool for blind users, did not place. The recap says this was because similar features now ship by default in OpenAI and Apple tools ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)). The same recap notes that teams used Lovable to save about 20 hours of coding and spent that time on user testing ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)).

### 1.2 Project Europe x ElevenLabs hackathon, Warsaw, early Dec 2025
Source: [ShiftMag](https://shiftmag.dev/we-should-all-do-what-elevenlabs-did-with-its-voiceai-hackathon-7326/)
- **Format:** 17 countries, 20 hours, a developer track and a creative track.
- **Grand prize (EUR 10,000):** **qForge**, a voice-driven interactive storytelling engine with a game-builder foundation.
- **Other notable projects:** DevTierUS (molecular design for drug discovery) and HackAvengers (a first-person language-learning game in 17+ languages).
- **CEO quote:** Mati Staniszewski stressed "action produces information" and said that "the more teams build, test, discard, and rebuild, the faster they move toward something meaningful" ([ShiftMag](https://shiftmag.dev/we-should-all-do-what-elevenlabs-did-with-its-voiceai-hackathon-7326/)).

### 1.3 ElevenLabs-supported healthcare hackathons, Spring 2026
Source: [ElevenLabs blog](https://elevenlabs.io/blog/how-hackathon-teams-are-using-elevenlabs-to-make-care-more-accessible)
- **Timbre**, Penn AI Hackathon overall winner (Apr 12 2026): a 60-second voice screening for Parkinson's that uses speech as the *diagnostic input*.
- **Junction**, Penn AI best use of ElevenLabs: a voice triage that hands patients off from an AI chatbot to human clinicians.
- **VOCA**, Babson Generator finalist (Apr 11): a communication layer for nonverbal people, including those with autism or ALS.
- **Health Butler**, Clinical OpenClaw winner (London): answers NHS primary-care patients in their native language.

### 1.4 Vapi Build Challenge 2025 (online, ~1 month, announced June 19 2025)
Source: [Vapi blog](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025). 300+ submissions.

| Category | Project | One-liner | Link |
|---|---|---|---|
| Real-World Apps | **Lavar** | Reading companion that remembers your questions and logs notes in context | [video](https://www.youtube.com/watch?v=x1jdEKQDg0c) |
| Real-World Apps | **Talvin** | AI recruiter **already in production**: voice screening and reference-check calls | [X](https://x.com/NewanV/status/1930342386196197543) |
| Creative | **FROSTai** | Hands-free support agent for field technicians | [LinkedIn](https://www.linkedin.com/posts/danielpgreen_nyc-buildwithvapi-voiceai-activity-7340193398101856256-E9dB) |
| Creative | **Jiffly** | **Consumer concierge that makes outbound calls to find and book local service appointments** | [video](https://www.youtube.com/watch?v=h2QaPD3IQZc) |
| Community picks | Adultin Buddy, JobGenie, **Candling** (emergency-call triage for first responders), Vapinception, **LeadSense** (outbound sales agent for car dealerships) | | [Vapi blog](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025) |

Related: an AI Automation Society community hackathon ($5K top prize) was won by a high-school student with a mental-health web app built on Vapi, n8n and Bolt.new ([Skool post](https://www.skool.com/ai-automation-society/new-video-this-vapi-n8n-voice-agent-won-5000-in-just-21-days)).

### 1.5 AssemblyAI x DEV.to Voice Agents Challenge (winners published Aug 7 2025)
Sources: [AssemblyAI blog](https://www.assemblyai.com/blog/these-7-voice-ai-projects-just-blew-us-away), [DEV challenge page](https://dev.to/challenges/assemblyai-2025-07-16). 60+ submissions using Universal-Streaming.

| Category | Project | One-liner | Links |
|---|---|---|---|
| Real-Time Performance | **Hogwarts Spell Caster** (@axrisi) | Speak spells, which become keyboard actions in a game; showcases sub-300ms latency | [DEV](https://dev.to/axrisi/hogwarts-spell-caster-real-time-voice-magic-with-assemblyai-universal-streaming-e3e), [repo](https://github.com/turazashvili/Hogwards-Legacy-Cast-with-Voice) |
| Domain Expert | **AI✧Debate** (@nadinev) | Real-time AI debate opponent | [DEV](https://dev.to/nadinev/aidebate-1cpa), [repo](https://github.com/nadinev6/AIDebate) |
| Business Automation | **Wynnie** (@neilblaze, @achalbajpai) | Autonomous voice shopping with automatic language detection and multi-agent orchestration, framed as accessible e-commerce for underserved users | [DEV](https://dev.to/neilblaze/wynnie--4po3), [demo](https://wynnie-v1.vercel.app/) |
| Finalists | Voice of Voiceless; Grasp, Articulate & Refine; **CareSetu AI** (health appointments); **Elder Care Companion** | | [AssemblyAI blog](https://www.assemblyai.com/blog/these-7-voice-ai-projects-just-blew-us-away) |

### 1.6 AssemblyAI NYC Hackathon, Dec 6 2024
Source: [AssemblyAI blog](https://www.assemblyai.com/blog/top-speech-ai-projects-and-winners-at-2024-assemblyai-hackathon)
- **1st: Dealty.** Transcribes real-estate deal calls live and **fills application forms with the extracted fields in real time**. Team quote: "enabling us to populate application forms on the fly."
- **2nd: Muse.** Mental-health journaling assistant.
- **Special mention: Say What.** Audio-clip guessing game.

### 1.7 SF Voice Agent Hackathon (AssemblyAI + LiveKit + Rime + Accel), Sep 19 2025
Source: [AssemblyAI recap](https://assemblyai.com/blog/voice-agent-hackathon-sept-19)
- **Grand prize: Voxy.** Zero-code voice-agent builder with memory and multi-voice switching. Judges: "The platform just works. You can see how this could make voice agents accessible to any business."
- **Technical complexity: Podweaver.** Dynamic podcast ad insertion with voice cloning, keeping timing within 250ms.
- **Most Fun (3 winners):** Deep Fried Learning (voice cooking assistant), Hands-Free Podcast, Work Daddy (ADHD productivity).
- **Notable non-winners:** Civic Voice (routes citizen complaints to government departments), **Scam Fighters** (deepfake detection plus engaging scammers), **Check on Loved Ones** (elderly medication compliance), AI Minder, Pathfinder, True Voice, Smooth Life.

### 1.8 OpenAI Realtime Voice x Reasoning Hackathon (AI Tinkerers NYC, 2025)
Source: [results](https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/results). The original listing dated it Feb 15-16 2025 ([voting page](https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/voting)); a Betaworks listing later showed it as postponed ([Betaworks](https://www.betaworks.com/event/openai-realtime-voice-x-reasoning-hackathon)).
- **1st: Bitter Lessons.** "Rubber ducking" voice partner for SRE incident investigations.
- **2nd: Bellhop.** Voice tools for luxury-resort staff.
- **3rd: Ensure.** **A voice agent that calls your insurer, verifies codes, and appeals denials with peer-reviewed medical evidence.**
- **Prizes:** 25K OpenAI credits plus Meta Ray-Bans for 1st; 7 finalists gave 5-minute live demos on the main stage ([voting page](https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/voting)).

### 1.9 OpenAI "Voice Hack Night" (with Cerebral Valley), finalists May 30 2026, winners ~Jun 1-2 2026
Sources: [OpenAIDevs finalists post](https://x.com/OpenAIDevs/status/2060768476386689253), as mirrored by [traeai](https://www.traeai.com/en/entities/voice-hack-night) and [traeai entity page](https://www.traeai.com/en/entities/agentic-os-for-a-phone). The event was 6 hours long, and 4 finalists went to a public vote.
- **1st / People's Choice: Agentic OS for a Phone** (@isausmanov). A voice-first mobile OS where agents act across apps; won $50K in API credits.
- **2nd: Wagner.** Multi-agent virtual meeting room for infrastructure planning.
- **3rd: Surgical Triage.** Built by hand surgeons; handles emergency referral calls, reviews images, checks standards, and generates referral packages.
- **Special award: Curo.** Socratic physics tutor for kids.
- Source for the descriptions: [traeai](https://www.traeai.com/en/entities/voice-hack-night) and its linked entity pages.

### 1.10 Daily / Pipecat Open Source Realtime AI Hackathon, Oct 19-20 2024
Sources: [Daily blog](https://www.daily.co/blog/building-the-future-highlights-from-our-open-source-realtime-ai-hackathon/), [Cartesia recap](https://cartesia.ai/blog/hacktober). Sponsors included Cartesia, Google Cloud, Tavus, Vapi and Coval.
- **SF 1st: Cruzy.** Road-trip companion with real-time video and voice plus Mapbox navigation.
- **SF 2nd: Instant Voice.** Turns any website into a voice assistant (Vapi).
- **Remote 1st: Stella.** Voice stylist with guided browsing and **virtual try-on**.
- **Remote 2nd: Yes Chef! / "Foul-mouthed Robot Chef."** Robotic arm with attitude. Cartesia's recap: "ambitious hardware integration captured audience imagination."
- **3rd (tie):** VoiceUI (live visuals during voice conversation) and SuperstarAI.

### 1.11 Cartesia "Hacktober" 2024 (AGI House SF, Oct 13 2024; Cal Hacks 11.0)
Source: [Cartesia blog](https://cartesia.ai/blog/hacktober). Cartesia reported 2,000+ builders and $20K in prizes across its October events.
- **AGI House 1st: Form Wizard Pro.** **Turns any web form into a voice-guided experience.**
- **AGI House 2nd and 3rd:** Story Narrator AI (kids' interactive narration) and **SheBeTalking** (speaking styles and tones; praised for "cultural sensitivity").
- **AGI House notable mention:** Roasted.lol (vision analysis plus voice roasts).
- **Cal Hacks 11.0 Cartesia winner: SpeakEasy.** Language learning that keeps your own voice across languages. Notables: Hamilton (multi-agent Senate hearing simulation) and MafiAI (voice Mafia game).

### 1.12 AI Tinkerers: Gemini x Pipecat Virtual Hackathon (2025)
Source: [results](https://virtual-events.aitinkerers.org/hackathons/h_n6aQtoaNlUo/results). Prizes were $100K Gemini credits and $100K Pipecat Cloud credits.
- **Best Gemini Live + Pipecat: Boba Bot.** Judge quotes: "I like the character a lot", "…the interface seemed snappy and responsive."
- **Gemini credits prize:** Light to the Noodles.
- **Pipecat Cloud prize: Happyverse VC Pitch Playground.** Practise pitching to AI investors. Judge: "Cool integration of document upload."
- **Finalists:** Lanturn (head-mounted ESP32-CAM voice and vision assistant) and BridgeSpeak.

### 1.13 Google Gemini Live Agent Challenge (Devpost-style, results May 16 2026)
Source: [Google Cloud blog](https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge). 11,878 participants, 1,536 projects, 151 countries.
- **Grand prize: ORION.** Voice-directed surgical co-pilot so surgeons "without breaking scrub" get answers, live data and visuals.
- **Live Agent winner: drone-copilot.** Talk to a drone to navigate it and run visual inspections.
- **Creative Storyteller winner: Sankofa.** An AI "griot" that turns family histories into narrated multimodal stories.
- **UI Navigator winner: Moonwalk.** Hands-free voice desktop control.
- **Special awards:** Wand (voice plus pointing gestures for browsing), JohnKeats.AI (reads vocal cues for an empathetic companion), Rayan Memory.
- **Honorable mentions with direct India transfer value:**
  - **NagarDrishti:** hands-free pothole and waterlogging reporting while driving, feeding a dashboard for city officials.
  - **Ekaette:** **replaces hold queues across phone calls and WhatsApp.**
  - **Call My Parts:** **autonomously searches vendors, calls suppliers, and ranks used-vehicle-part options.**
  - VibeCat and Relay.

### 1.14 Cal Hacks 12.0 (Oct 24-26 2025, 695 projects, 3,000+ hackers)
Source: [winner's blog](https://blog.dylanlu.com/cal-hacks-12/)
- **Grand prize: FaceTimeOS.** You FaceTime your Mac and talk to it; a computer-use agent (Agent S) does the task while a parallel voice reply streams back.
- Repo: [dylanelu/FaceTimeOS](https://github.com/dylanelu/FaceTimeOS) ("CalHacks 12.0 1st Overall Winner"; gh API).
- Demo tactics are in section 3.

### 1.15 AI Hackathon @ Berkeley 2026: Deepgram track (June 2026)
Source: [Deepgram DevRel recap](https://blog.nhcarrigan.com/post/ai-hackathon-berkeley-2026). 141 of 398 projects (35%) built voice-first for the track.
- **Deepgram track winner: aside.ai.** A clip-on Raspberry Pi camera wearable that narrates your surroundings live in a chosen persona ("hype man, goth therapist, epic quest narrator"). It won because the team kept the sponsor judge in the loop for 24 hours: "By the time I submitted the winner, I had watched them build the project."
- **Standouts named in the recap:**
  - **voxaid:** fine-tuned wav2vec2 on dysarthric speech (TORGO) for ALS, CP and stroke patients, then Claude, then Deepgram Aura TTS.
  - **aintercept:** **listens to a call and alerts as soon as it detects scam patterns.** The builder's grandmother had fallen for a fake-police scam.
  - **crisisroom:** voice incident command, built by a Navy veteran.
  - **moggie** and **séance:** "argue with your water bottle."

### 1.16 YC-hosted / YC-adjacent voice hackathons
- **YC x Medplum Hackathon (Aug 1 2026).** 2nd place: **CareLoop, a pre-visit voice AI agent for chronic care.** People's Choice: MedTrace AI. 1st place (Lamina) was not voice ([Medplum recap](https://www.medplum.com/blog/yc-medplum-hackathon-2026-recap)).
- **"Call My Agent Hackathon" at YC, May 17 2026.**
  - Hosted by AgentPhone (YC P26) as a 14-hour sprint. The brief was agents that act in the real world via calls, SMS and iMessage; the promo said "No more sandbox demos."
  - **1st place prize was a guaranteed YC interview** ([David Lieb on X](https://x.com/dflieb/status/2052146123079639398); [Internshala listing](https://internshala.com/competitions/call-my-agent-hackathon/)). Sponsors: Google DeepMind, Moss, Browser Use, AgentMail.
  - The overall winner is not public. One team placed 3rd in the Browser Use track with an international-student admissions helper ([Regis](https://regisinnovationchallenge.com/stories-details/hackathon-and-beyond.html)).
  - **This is the closest analogue to Symphony's YC-interview prize.** [INFERRED]
- **"YC Voice Agent Hackathon": FireSight (self-reported win, video published May 2026).** A 100% offline, hands-free multimodal voice agent for firefighter building inspections, running Gemma on Cactus (YC S25) with Meta glasses ([YouTube](https://www.youtube.com/watch?v=KuzUJNjJvAs)). I could not independently verify the placement.
- **Google DeepMind x Cactus Compute global hackathon (on-device FunctionGemma).** 1st CactusRoute, 2nd cloudNein (private on-device finance AI for CFOs), 3rd WarriorsPersonalAssistant. The search snippet named the [SF results page](https://sf.aitinkerers.org/hackathons/h_DRGnrtIWaG8/results) and an [iTWire report](https://itwire.com/business-it-news/security/global-hackathon-%E2%80%98unites-london,-boston-and-san-francisco-to-build-the-future-of-personal-ai-on-the-edge%E2%80%99.html).
- **AWS x MiniMax MCP Agents Hackathon (SF, May 30 2025).** 1st **95 Voice Root**, a voice assistant with personal context; 3rd **Nurse Nora**, a healthcare voice assistant ([MiniMax news](https://www.minimax.io/news/aws-x-minimax-mcp-agents-hackathon)).

### 1.17 Other 2025-26 voice winners worth knowing
- **Big Berlin Hack (~May 2026, 1,500 applicants, 158 projects).** 1st overall plus the telli & ai-coustics track: **Smoothy, a "dual-brain" voice companion that makes daily check-in calls to elderly people living alone, tracks medication and flags concerns to family in real time** ([LinkedIn post](https://pt.linkedin.com/in/netoo-edson)).
- **AURORA 2026 (Sri Lanka, Jul 2026).** Won by the PeraCom team with **AI-powered voice-phishing defense** ([Univ. of Peradeniya CE news](https://www.ce.pdn.ac.lk/news/2026-07-20-AURORA-2026-champions.html)).
- **Vyrothon 2026 (GDG).** Top position and $2,000 for an AI voice agent that instantly calls leads 24/7 (search snippet of the [GDG event page](https://gdg.community.dev/events/details/google-gdg-on-campus-comsats-university-abbottabad-pakistan-presents-hack-to-hero-meet-the-vyrothon-champions/)).
- **Berlin ElevenLabs Dec-2025 showcase (projects, not placements):**
  - **Lifeline:** a 112/911 dispatcher agent on LiveKit, Groq Whisper, Kimi K2 and ElevenLabs. It triages calls, coaches CPR, and dispatches units with live ETA maps; the team claims it cuts coordination from "30-90 seconds to under 2 seconds."
  - **Wayfinder:** voice browser agent for blind users.
  - **Echo:** a voice exit-interview agent that captures departing employees' knowledge.
  - Source: [showcase](https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/showcase).

---

## 2. Recurring winning archetypes (ranked by how often they placed)

1. **"The agent makes the phone calls for you" (outbound, real-world action).** This is the most repeated winning pattern.
   - Winners: Dealwise (SF 1st, [PostHog](https://posthog.com/blog/elevenlabs-hackathon)); Procuro (NYC 2nd, [ElevenLabs](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)); Jiffly (Vapi winner, [Vapi](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025)); Ensure (insurance appeals, NYC 3rd, [results](https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/results)); Call My Parts (Gemini HM, [Google](https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge)); Talvin reference-check calls ([Vapi](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025)).
   - Even GibberLink is a booking call ([Wikipedia](https://en.wikipedia.org/wiki/Gibberlink)), and YC's own hackathon brief was "agents that actually touch the real world" ([X](https://x.com/dflieb/status/2052146123079639398)).
2. **Healthcare and care workflows.**
   - Winners: Pep, Timbre, Junction, Health Butler, ORION, Surgical Triage, CareLoop, Smoothy, CareSetu, Elder Care Companion (sources above).
   - Context: a16z found ~18% of YC voice-agent founders target healthcare ([a16z](https://a16z.com/ai-voice-agents-2025-update/)).
3. **Elderly, accessibility and "the voiceless."** Smoothy, Check on Loved Ones, VOCA, voxaid, Voice of Voiceless, Wayfinder, Form Wizard Pro (sources above).
4. **Fraud and scam defense.** Voice Guardian (Seoul 1st), aintercept, Scam Fighters, PeraCom AURORA 2026 (sources above).
5. **Hands-free voice for physical or field work, often with vision or hardware.** FROSTai, FireSight, drone-copilot, ORION, Lanturn, Relay, aside.ai, Robot Chef, Roadmate (sources above).
   - [INFERRED] Hardware plus voice reliably gets "audience imagination" points ([Cartesia](https://cartesia.ai/blog/hacktober)).
6. **Voice that controls a computer or phone (voice as the OS).** FaceTimeOS (Cal Hacks 1st), Agentic OS for a Phone (OpenAI 1st), Moonwalk, Wand, Unstuck, Instant Voice (sources above).
7. **Voice turned into structured data or forms.** Dealty (AssemblyAI 1st), Form Wizard Pro (AGI House 1st), NagarDrishti dashboard (sources above).
8. **Compliance and collections in BFSI.** Claimsio (Warsaw 2nd), Ensure ([ElevenLabs](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon), [NYC](https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/results)). a16z reports fintech is the top B2B sub-industry for YC voice agents at 16.9% ([a16z](https://a16z.com/ai-voice-agents-2025-update/)).
9. **Delight and personality.** Games and novelty (Hogwarts Spell Caster, aside.ai personas, séance, MafiAI, Boba Bot's "character") win "most fun", real-time and people's-choice categories (sources above).
   - [INFERRED] These rarely win a YC-oriented grand prize on their own unless the novelty is a protocol-level idea like GibberLink.

## 3. Demo tactics that won (evidence first, then my read)

- **Make it go viral, or at least make it a 60-second clip.**
  - Evidence: GibberLink's recorded demo went viral and was picked up by Forbes; judges were unanimous ([ElevenLabs](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon)). The repo got 4.9K stars ([GitHub](https://github.com/PennyroyalTea/gibberlink)).
  - [INFERRED] Symphony is an online, video-judged event, so the submission video is the demo.
- **Show the "two agents on a call" or "agent calls a real business" moment.**
  - Evidence: GibberLink staged a hotel-booking call ([Wikipedia](https://en.wikipedia.org/wiki/Gibberlink)), and Dealwise placed real calls to service providers ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)).
  - [INFERRED] A live outbound call that a judge can *hear succeed* is more convincing than a web chat widget.
- **Humanize the voice and measure it.**
  - Evidence: Dealwise found that pauses, a mild accent and hesitation made callees engage ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)).
  - [INFERRED] Report a before/after metric (pick-up or completion rate, robotic vs. humanized voice). That is an engineering insight, not a feature list.
- **Lead with a personal "why."**
  - Evidence: Roadmate's teammate's friend's accident ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)); aintercept's grandmother's scam ([Deepgram recap](https://blog.nhcarrigan.com/post/ai-hackathon-berkeley-2026)); crisisroom's Navy damage-control story (same source).
- **Cut whatever is flaky and polish what judges see.**
  - Evidence: FaceTimeOS removed clicking from the demo because the agent struggled with it, and dedicated someone to UI. The author advises "craft ideas cooler than previous winners" and notes "not many people care about making things look pretty" ([blog](https://blog.dylanlu.com/cal-hacks-12/)).
- **Latency is a visible feature.**
  - Evidence: Boba Bot judges said "snappy and responsive" ([results](https://virtual-events.aitinkerers.org/hackathons/h_n6aQtoaNlUo/results)), and Hogwarts won the "Real-Time Performance" category ([AssemblyAI](https://www.assemblyai.com/blog/these-7-voice-ai-projects-just-blew-us-away)).
  - [INFERRED] Put a latency counter on screen.
- **Quantify the operational win.**
  - Evidence: Lifeline claimed coordination drops from "30-90 seconds to under 2 seconds" ([showcase](https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/showcase)). Talvin cites 488 resumes cut to 15 finalists in 7 days, "hiring time by 67%" ([getlatka](https://getlatka.com/companies/talvin.ai), via search snippet).
- **Show real users or production use if you have any.**
  - Evidence: Talvin was "already in production" when it won ([Vapi](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025)), and Voxy's judges said "The platform just works" ([AssemblyAI](https://assemblyai.com/blog/voice-agent-hackathon-sept-19)).
- **Engage sponsor judges throughout the event.**
  - Evidence: aside.ai won the Deepgram track because "they had been in conversation with me for the entire event" ([recap](https://blog.nhcarrigan.com/post/ai-hackathon-berkeley-2026)).
  - [INFERRED] For Symphony, post build updates in the sponsors' Discord channels and tag Sarvam/Plivo/Exotel/Cartesia/Deepgram DevRel with progress clips.
- **Make the audience-vote format work for you.**
  - Evidence: OpenAI Voice Hack Night's winner was a public-vote People's Choice ([traeai mirror of @OpenAIDevs](https://www.traeai.com/en/entities/agentic-os-for-a-phone)).
  - [INFERRED] If Symphony has any community vote, a consumer-legible demo matters.
- **Use builders like Lovable/Bolt for the UI and spend the saved time on testing.** Evidence: "We built the app itself in Lovable, it saved us 20 hours of coding" ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)).

## 4. Overdone ideas judges are likely tired of [INFERRED, with frequency evidence]

I count each of these 4+ times across the lists above. Some still placed, but usually with a twist.
- **Travel and city guides:** Hugo, Voyagr, Cruzy, Roadmate, Austin culture guide ([ElevenLabs](https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon), [Daily](https://www.daily.co/blog/building-the-future-highlights-from-our-open-source-realtime-ai-hackathon/), [Austin](https://austin.aitinkerers.org/hackathons/h_X_WXp4d33gk/results)).
- **Meeting copilots and knowledge bots:** PostHog Meeting Copilot, Hippo, Wagner, the Berlin "Live meeting expert agents" ([showcase](https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/showcase)).
- **Language-learning and translation apps:** SpeakEasy, HackAvengers, BridgeSpeak, "Talk to my agent."
- **Generic personal assistant / to-do / daily planner:** Espresso Labs, Adultin Buddy, AI Minder, Smooth Life.
- **Mental-health journaling or AI therapist:** Muse, the AAS winner, JohnKeats.AI.
- **AI podcast generators:** AI Podcaster, Morning Brief, Pochinki, Podweaver.
- **Generic "screen reader / scene describer for the blind":** explicitly lost because OpenAI and Apple ship it by default ([PostHog](https://posthog.com/blog/elevenlabs-hackathon)).
- **No-code voice-agent builders and "voice widget for any website":** Voxy, Instant Voice, Unstuck, Vapinception.
  - For a Bolna event this competes directly with the host's own product. [INFERRED] Avoid it.
- **Plain inbound appointment-booking bots for clinics or restaurants.**
  - The space is crowded with funded YC companies, e.g. Certus AI for restaurant phone lines ([YC](https://www.ycombinator.com/companies/certus-ai)) and LunaBill for healthcare billing calls ([YC](https://www.ycombinator.com/companies/lunabill)).
  - [INFERRED] A YC partner will ask "why you vs. these?"

## 5. Hackathon projects that became companies / YC

- **April (YC S25).**
  - Built at a weekend hackathon in May 2025 as a 12-hour prototype that read emails aloud and handled "reply to Sarah", "delete all promos" and meeting moves by voice ([search summary of Forbes/HN coverage](https://hn.svelte.dev/item/45015230)). YC then invited the team to the batch, and it is listed as YC S25 ([YC page](https://ycombinator.com/companies/april)).
  - The Forbes article reports that a Y Combinator hackathon led to April and that YC invited the founders after they won ([Forbes, via search snippet](https://www.forbes.com/sites/digital-assets/2025/09/19/could-a-y-combinator-ai-startups-voice-agent-transform-productivity/)).
  - **This is the clearest "voice hackathon to YC" precedent.**
- **Talvin.** Won the Vapi Build Challenge while already in production ([Vapi](https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025)). A third-party estimate puts it at $330K revenue with no VC as of 2026 ([getlatka](https://getlatka.com/companies/talvin.ai); unverified estimate).
- **Happyverse.** An existing startup used the Gemini x Pipecat hackathon to ship a feature and won Pipecat credits ([results](https://virtual-events.aitinkerers.org/hackathons/h_n6aQtoaNlUo/results)).
  - [INFERRED] Hackathon wins are also used by early startups as distribution and credits.
- **GibberLink.** Huge attention (Forbes, 4.9K-star repo), but I found no evidence of a company ([Wikipedia](https://en.wikipedia.org/wiki/Gibberlink), [GitHub](https://github.com/PennyroyalTea/gibberlink)).
  - [INFERRED] Virality alone does not equal a startup, and a YC interview needs a market story too.
- **Market context for a YC judge:**
  - Companies building with voice were 22% of a recent YC class. YC voice founders are ~69% B2B, ~18% healthcare, ~13% consumer, and fintech is the largest B2B sub-industry at 16.9% ([a16z 2025 voice update](https://a16z.com/ai-voice-agents-2025-update/)).
  - AgentPhone (YC P26) exists to give agents phone numbers for calls and SMS ([Internshala](https://internshala.com/competitions/call-my-agent-hackathon/)).
  - Vocera (YC, IIT Bombay founders) does automated testing of voice agents ([Daily Pioneer](https://www.dailypioneer.com/2024/state-editions/innovators-get-y-combinator-funding-to-perfect-voice-ai-systems.html)).
  - [INFERRED] Voice infra and evals are investable but compete with the sponsors. An application-layer agent with a clear buyer is safer for this event.

## 6. Idea seeds that transfer to India (phone-first, Indic, UPI, BFSI, schemes)

India context facts:
- ~350M people in India use feature phones (IDC via [TechCrunch, Jul 2024](https://techcrunch.com/?p=2806846)).
- NPCI's UPI 123PAY lets feature-phone users pay via an IVR number, missed call, or sound-based proximity ([NPCI](https://npci.org.in/what-we-do/upi-123pay/product-overview)).
- Hello! UPI enables conversational voice payments in Hindi and English via apps, telecom calls and IoT devices ([NPCI](https://npci.org.in/what-we-do/hello-upi/product-overview)).
- "Digital arrest" scam cases grew from 39,925 (₹91.14 cr lost) in 2022 to 123,672 (₹1,935.51 cr) in 2024 (NCRP data cited in Parliament, via [Manorama Yearbook](https://www.manoramayearbook.in/current-affairs/india/2025/03/13/digital-arrests-explained.html)).

Each seed: the global precedent, the India twist, the Symphony-sponsor fit, and the demo. Seeds, twists and demos are **[INFERRED]** proposals; the precedents are sourced above.

1. **"Bhav-Taol": an agent that calls N vendors in parallel and returns ranked quotes.**
   - Precedent: Dealwise (SF 1st), Procuro (NYC 2nd), Jiffly (Vapi), Call My Parts (Gemini HM). This is the strongest archetype in section 2.
   - India twist: a kirana owner or small fabricator speaks the need ("50 kg Fortune oil, Thursday delivery"). The agent calls 5 distributors, transporters or used-part dealers in Hindi, Marathi or Tamil, negotiates, and returns a ranked WhatsApp summary with a UPI payment link.
   - Sponsor fit: Plivo or Exotel outbound in parallel; Sarvam Indic STT/TTS; Cartesia/Deepgram for latency.
   - Demo: 3-5 simultaneous live calls answered by teammates playing vendors with different dialects, and a live-updating price table. Metric: "45 min of calls became 3 min."
2. **"Kavach": a digital-arrest and UPI-fraud shield for parents.**
   - Precedent: Voice Guardian (Seoul 1st), aintercept (Berkeley), Scam Fighters (SF), PeraCom voice-phishing defense (AURORA 2026).
   - India twist: call screening or conference-in for elderly users. It detects "CBI/customs/police" or "stay on video call" scripts in Indic languages, warns in the user's language, alerts the child, and pre-fills a 1930 / cybercrime.gov.in report.
   - Optional honeypot mode: wastes the scammer's time and captures mule UPI IDs. Legal and ethics framing is needed.
   - Demo: a scripted fake-officer call in Hindi with the shield interrupting live. Cite the NCRP numbers above for scale.
3. **"Amma Daily": a mother-tongue check-in caller for elderly parents on feature phones.**
   - Precedent: Smoothy (Big Berlin Hack 1st), Check on Loved Ones, Elder Care Companion, CareCall.
   - India twist: an outbound daily call (no app, works on a ₹1,000 feature phone) covering medicines, BP or sugar readings spoken aloud, mood, and "did you eat." Escalates to the NRI or working child on WhatsApp and books a follow-up. Pairs with seed 2 as one product.
   - Demo: the judge receives the call on their own phone and hears the WhatsApp summary arrive.
4. **"Claim Saathi": health-insurance claim and denial fighter, or compliant collections.**
   - Precedent: Ensure (NYC 3rd: calls insurers and appeals denials with evidence), Claimsio (Warsaw 2nd: debt-collection compliance), LunaBill (YC: healthcare billing callers).
   - India twist A: a cashless-claim follow-up agent that calls the TPA, hospital desk and insurer, tracks query letters, and drafts a grievance.
   - India twist B: a BFSI collections agent with built-in conduct guardrails (call windows, no coercive language, consent, a full audit trail) and promise-to-pay capture plus a UPI collect link.
   - Both map to the fintech/B2B segment YC over-indexes on ([a16z](https://a16z.com/ai-voice-agents-2025-update/)).
   - Demo: a compliance score per call, plus a side-by-side of a human script vs. the agent.
5. **"Missed-Call Sarkar": scheme and civic grievance agent via missed call.**
   - Precedent: NagarDrishti (Gemini HM: voice pothole reporting to an officials' dashboard), Civic Voice (SF), Form Wizard Pro (AGI House 1st: voice-filled forms), Dealty (voice to structured form).
   - India twist: give a missed call and the agent calls back for free in the caller's dialect. It checks eligibility for schemes or files a municipal complaint, reads back the reference number, and proactively calls back when the status changes.
   - Demo: a feature-phone call, then a filled form or ticket appearing on a dashboard.
6. **"Bolo Khata": voice ledger and udhaar collection for kirana.**
   - Precedent: Dealty (voice to structured data), Wynnie (voice commerce for underserved users with automatic language detection), Hello! UPI (NPCI voice payments).
   - India twist: the shopkeeper says "Ramesh ko 240 udhaar, Shukravar tak" during a call or voice note. The agent logs it, and on the due date politely calls Ramesh in his language and sends a UPI link.
   - Demo: 3 voice entries become a ledger, and an auto reminder call ends in a "paid" webhook.
7. **"Haath-Free": a field-worker voice copilot (ASHA, agri extension, technicians).**
   - Precedent: FROSTai (Vapi winner), FireSight (offline, on-device), drone-copilot (Gemini winner), Lanturn, Relay.
   - India twist: an ASHA worker or electrician speaks observations in dialect over a normal call. The agent fills the register or service form, flags high-risk cases, and reads back the protocol (cf. Lifeline's live CPR coaching).
   - Demo: a messy dialect monologue becomes a clean structured record in real time, with field accuracy shown.
8. **"Press-1 Killer": a drop-in replacement for SMB IVRs.**
   - Precedent: Ekaette (Gemini HM: replaces hold queues across phone and WhatsApp), Talvin (in production).
   - India twist: an Exotel/Plivo-native agent for coaching centres, diagnostic labs and two-wheeler service centres in Hinglish. It handles the top 5 intents end to end (booking, report status, fees via UPI) and hands off to WhatsApp.
   - Caveat: this is crowded (see section 4). Only pick it with a real pilot customer.

**My top picks for a YC-partner judge:** [INFERRED]
- **#1 Bhav-Taol, #2 Kavach + Amma Daily combined, #4 Claim Saathi.**
- Reasons:
  - Each repeats the single most-rewarded archetype: an agent that places real phone calls and completes a real-world task.
  - Each has an obvious Indian buyer or wedge.
  - Each makes a 2-minute demo where the judge can hear the call succeed.
  - Each stays clear of the host's own builder product.

---

### Source index (primary)
- https://elevenlabs.io/blog/announcing-the-winners-of-the-elevenlabs-worldwide-hackathon
- https://posthog.com/blog/elevenlabs-hackathon
- https://shiftmag.dev/we-should-all-do-what-elevenlabs-did-with-its-voiceai-hackathon-7326/
- https://elevenlabs.io/blog/how-hackathon-teams-are-using-elevenlabs-to-make-care-more-accessible
- https://vapi.ai/blog/meet-the-winners-of-the-vapi-build-challenge-2025
- https://www.assemblyai.com/blog/these-7-voice-ai-projects-just-blew-us-away
- https://www.assemblyai.com/blog/top-speech-ai-projects-and-winners-at-2024-assemblyai-hackathon
- https://assemblyai.com/blog/voice-agent-hackathon-sept-19
- https://nyc.aitinkerers.org/hackathons/h_q2ugc3T5gts/results
- https://www.traeai.com/en/entities/voice-hack-night
- https://www.daily.co/blog/building-the-future-highlights-from-our-open-source-realtime-ai-hackathon/
- https://cartesia.ai/blog/hacktober
- https://virtual-events.aitinkerers.org/hackathons/h_n6aQtoaNlUo/results
- https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge
- https://blog.dylanlu.com/cal-hacks-12/
- https://blog.nhcarrigan.com/post/ai-hackathon-berkeley-2026
- https://www.medplum.com/blog/yc-medplum-hackathon-2026-recap
- https://internshala.com/competitions/call-my-agent-hackathon/
- https://berlin.aitinkerers.org/hackathons/h_AUrIIiOrRa8/showcase
- https://a16z.com/ai-voice-agents-2025-update/
- https://en.wikipedia.org/wiki/Gibberlink
