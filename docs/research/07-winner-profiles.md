# Serial Hackathon Winners: profile teardown for the Bolna Symphony Buildathon

Compiled 2026-10-21. Every fact has an inline source. Opinions are tagged **[INFERRED]**. Where a claim exists only as a self-report (personal site or profile) and I couldn't independently verify it, it's marked *(self-reported)*. Full non-fork repo tables are in the appendix at the bottom.

Context: Bolna Symphony Buildathon. Online, build anything with voice AI (adding voice to an existing project is allowed). Submissions due 31 Oct 2026. Prize ₹1.2L plus a YC interview for the winner. Sponsors: Plivo, Exotel, Sarvam, Cartesia, Deepgram, Kalpa Labs. Judges are probably the Bolna team plus a YC partner.

> **Ethics note:** Submitting someone else's project as your own is not OK, and a judge pool steeped in Indian voice AI is likely to recognise recent winners (for example Sadak, which won a Sarvam buildathon three months ago). Everything below is **inspiration**, or a **fork with visible credit**, and only where the license allows it. A repo with no license file is "all rights reserved" by default, so you can take inspiration from it but you can't fork it.

---

## 1. Kuber Mehta (@Kuberwastaken)

### Who
- Kuber Mehta, New Delhi, India. GitHub bio: "I build (& break) stuff". Company field: PolyThink. 899 followers, 294 public repos. Source: https://api.github.com/users/Kuberwastaken
- Age 19. Studying BSc CS at BITS Pilani and BTech AI & DS at GGSIPU (both current). https://kuber.studio/llms.txt
- AI Initiatives at Razorpay (YC W15) since Jun 2026, in a 5-person central AI lab that reports to CEO Harshil Mathur. Earlier: Perplexity Business Fellow (Mar–Aug 2025), AI Summer Resident at Nas Daily (Dubai), HTMX intern. https://kuber.studio/llms.txt and https://github.com/Kuberwastaken/Kuberwastaken
- Personal site https://kuber.studio/. Blog "MindDump", which he says gets 50–100k readers a month (https://kuber.studio/llms.txt). LinkedIn 14k+ followers (self-reported, same source). X: @kuberwastaken.
- He pitched world-model caching at YC Startup School Bangalore 2026. YC partner Jared Friedman reportedly called it "the obvious future of the video games industry", and the clip got about 300k views on Instagram *(self-reported)*. https://kuber.studio/llms.txt

### Top ~10 repos (stars from the GitHub API, 2026-10-21)
| Repo | ★ | Lang | Created | License | What |
|---|---|---|---|---|---|
| [claurst](https://github.com/Kuberwastaken/claurst) | 10,324 | Rust | 2026-03-31 | GPL-3.0 | Claude Code reimplemented in Rust after the npm sourcemap leak. "7k stars in its first week", #1 on GitHub trending *(self-reported)* ([llms.txt](https://kuber.studio/llms.txt)) |
| [backdooms](https://github.com/Kuberwastaken/backdooms) | 642 | HTML | 2025-02-12 | MIT | A DOOM/Backrooms game that fits inside a QR code. "Top HN post of 2025" *(self-reported)*, and cited in arXiv:2506.11008 ([llms.txt](https://kuber.studio/llms.txt)) |
| [cookie](https://github.com/Kuberwastaken/cookie) | 324 | TS | 2026-08-05 | Modified MIT (credit required if deployed) | "I didn't set a cookie": a live fingerprinting demo that narrates back to you what the site learned ([README](https://github.com/Kuberwastaken/cookie)) |
| [hp-laser-1008a-macos](https://github.com/Kuberwastaken/hp-laser-1008a-macos) | 176 | C | 2026-08-17 | NOASSERTION | macOS driver written with Claude. Covered by [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-uses-claude-ai-to-create-native-macos-driver-for-obscure-windows-only-printer-linux-container-hack-enables-system-wide-cmd-p-printing-driver-now-available-on-github) and [The Register](https://www.theregister.com/ai-and-ml/2026/08/19/dev-taps-claude-code-to-craft-custom-printer-driver-for-macos/5289875) |
| [megaphone](https://github.com/Kuberwastaken/megaphone) | 172 | Swift | 2026-07-13 | MIT | **Voice.** On-device Mac dictation using Apple SpeechAnalyzer and Foundation Models. Built for the OpenAI Build Week hackathon ([README](https://github.com/Kuberwastaken/megaphone)). Result not stated. Also on [Devpost](https://devpost.com/software/megaphone-qp6i5f) |
| [meow](https://github.com/Kuberwastaken/meow) | 165 | Python | 2025-06-11 | Apache-2.0 | An image file format for AI workflows |
| [picogpt](https://github.com/Kuberwastaken/picogpt) | 134 | HTML | 2026-02-12 | none | GPT that fits in a QR code |
| [sweeta](https://github.com/Kuberwastaken/sweeta) | 120 | Python | 2025-10-03 | Apache-2.0 | Sora 2 watermark removal ("research use only") |
| [litmus](https://github.com/Kuberwastaken/litmus) | 72 | HTML | 2026-03-28 | MIT | A parallel autonomous ML-research org running on OpenClaw |
| [DoomMe](https://github.com/Kuberwastaken/DoomMe) | 63 | Python | 2026-01-02 | MIT | DOOM playable inside a GitHub README |
| [math-gambling](https://github.com/Kuberwastaken/math-gambling) | 9 | Python | 2026-09-10 | GPL-2.0 | Volunteer distributed compute to search for x³+y³+z³=114. It's framed as "gamble your compute", with a live leaderboard and a working paper ([README](https://github.com/Kuberwastaken/math-gambling), [site](https://kuber.studio/math-gambling/)) |

### Hackathon wins (from his own llms.txt, https://kuber.studio/llms.txt)
| Hackathon | Date | Result | Project | Proof |
|---|---|---|---|---|
| Nothing Essential Lab S1 Hackathon | 2026 | **Winner**, prize was a Nothing Phone 3 | HN-Digest | https://x.com/essential/status/2026712093018263847, https://playground.nothing.tech/detail/app/pDCVJNrJVYHj5PxM |
| Hack Club SiteJam | 2025 | **1st place** | [CottagOS](https://github.com/Kuberwastaken/CottagOS) (http://cottagos.kuber.studio) | *(self-reported)* https://kuber.studio/llms.txt |
| Unsloth x AMD RL Hackathon, IIT Delhi | 2026 | 4th place | not named (probably [minesweeper-llm](https://github.com/Kuberwastaken/minesweeper-llm), "RL Agent to solve Minesweeper with Qwen 2.5 14B" **[INFERRED]**) | *(self-reported)* |
| Google x Kaggle Long Context AI Hackathon | 2025 | Top 10 | Books Re-imagined | *(self-reported)* |

- He says he has done "20+ hackathons" ([llms.txt](https://kuber.studio/llms.txt)). Devpost lists only two projects, neither marked as a winner: https://devpost.com/Kuberwastaken. His Devfolio profile (https://devfolio.co/@kubermehta) shows no winner entries.
- **[INFERRED]** Kuber is a *virality* winner more than a *hackathon* winner. His leverage is HN/X/press reach and stars (10k on Claurst), not podium finishes. He's the best of the three to study for "make the YC partner remember you".

### Why his stuff wins attention [INFERRED, based on the READMEs and llms.txt above]
- **An absurd, constraint-driven hook you can say in one line.** "DOOM in a QR code", "GPT in a QR code", "DOOM in a README", "Gamble your compute to solve x³+y³+z³=114". The title is the pitch.
- **Humour plus a culture-specific persona.** AsianMOM ("Aiyah! You still staring at screen?", [README](https://github.com/Kuberwastaken/AsianMOM)), Rocky TTS, nogreeting, hinge-mcp ("your clanker can finally swipe for you now").
- **Always live on a custom subdomain** (`*.kuber.studio`), plus a blog write-up for most projects ([llms.txt](https://kuber.studio/llms.txt) lists one per project).
- **Riding the news cycle**: the Claude Code leak became Claurst, Sora 2 became sweeta/spica, the Hail Mary film became rocky-tts.
- **Careful README craft**: hero image, badges, a "how it works" section, honest limitations (math-gambling's README spells out what the search *doesn't* cover).

### Voice/audio/agent projects
- [megaphone](https://github.com/Kuberwastaken/megaphone) (MIT): on-device dictation, plus "Hey Megaphone, make that formal" voice commands.
- [ATHENA](https://github.com/Kuberwastaken/ATHENA) (MIT): an open-source, privacy-first smart speaker on Raspberry Pi.
- [rocky-tts](https://github.com/Kuberwastaken/rocky-tts) (NOASSERTION): a cloned character voice, with a rule-based rewrite into Rocky's speech patterns before synthesis.
- [Training-Voice-Extractor](https://github.com/Kuberwastaken/Training-Voice-Extractor) (none): pulls vocals out of YouTube for training data.
- Agent work: [reference](https://github.com/Kuberwastaken/reference), [subagentmaxxing](https://github.com/Kuberwastaken/subagentmaxxing), [agent-notifications](https://github.com/Kuberwastaken/agent-notifications), [hinge-mcp](https://github.com/Kuberwastaken/hinge-mcp) (MIT).

### Voice-extension candidates
| Project (license) | Voice version | Why judges would care [INFERRED] | Legal |
|---|---|---|---|
| [AsianMOM](https://github.com/Kuberwastaken/AsianMOM) (**Apache-2.0**) | **"Desi Mom Calls You"**: a Bolna outbound agent rings you at 7am and at deadlines. It nags in Hindi, Tamil or Bengali (Sarvam or Cartesia voices), asks what you did today, and roasts you if you lie (it checks GitHub commits, screen time, etc.). The webcam roast becomes a phone-call roast | Viral, funny, very India-specific, and it shows Indic TTS persona quality. Demo clips spread on X | You can fork with attribution (keep LICENSE and NOTICE, credit Kuber visibly). Better to rebuild the concept, since the original is WebGPU vision, not telephony |
| [megaphone](https://github.com/Kuberwastaken/megaphone) (**MIT**) | Hinglish/Indic dictation plus voice edit commands using Sarvam STT, or "call a number and dictate a WhatsApp note" | Practical, but [INFERRED] it's desktop-only, so it doesn't show off Bolna's phone agents | Fork with credit is OK |
| [math-gambling](https://github.com/Kuberwastaken/math-gambling) (GPL-2.0) | Weak fit. At most a "call the leaderboard" hotline | [INFERRED] Not a good voice story | GPL-2.0: a fork must stay GPL |
| [ATHENA](https://github.com/Kuberwastaken/ATHENA) (**MIT**) | Indic privacy-first home speaker that hands off to a Bolna phone agent when you're away from home | Hardware demos land well, but it's risky in 10 days | Fork with credit is OK |

---

## 2. Ayaan Gazali (@ayaangazali)

### Who
- Ayaan Gazali, San Jose, California. GitHub bio "I like to build". GitHub account created 2025-09-10. 85 followers, 122 public repos. https://api.github.com/users/ayaangazali
- Freshman in Computer Software Engineering at San José State University. Described as an "eleven-time hackathon winner" with events "affiliated with Y Combinator, NVIDIA, Microsoft, and AWS", and as a LinkedIn creator with "over 2 million views". Source: [SJSU Engineering blog, 2026-02-23](https://blogs.sjsu.edu/engineering/2026/02/23/spartan-engineers-where-innovation-lives-ai-super-bowl-lx-the-chip-comeback/)
- Portfolio claims: "10x Hackathon Winner at Microsoft, NVIDIA, AWS, and more", SWE intern at Kamco Invest (AML/KYC), Stanford Code-in-Place section leader. https://github.com/ayaangazali/ayaan-portfolio, https://ayaan-portfolio-puce.vercel.app
- LinkedIn headline "cs + math @ sjsu" (https://www.linkedin.com/in/ayaangazali/). The page couldn't be fetched (HTTP 999). According to search-engine snippets of it, he has done "44 hackathons and won 17" *(unverified snippet)*. X: [@Ayaan_Gazali](https://x.com/Ayaan_Gazali). He builds with a group called "42nights" ([jelly README](https://github.com/ayaangazali/jelly)).

### Top ~10 repos (he's low on stars; ranked by relevance) [INFERRED ranking]
| Repo | ★ | Created | License | What |
|---|---|---|---|---|
| [graph-engineering](https://github.com/ayaangazali/graph-engineering) | 3 | 2026-07-21 | MIT | `/graph` for Claude Code: turns a goal into a DAG of specialist subagents |
| [eyes](https://github.com/ayaangazali/eyes) | 1 | 2026-10-17 | **Apache-2.0** | An MCP server that lets agents pay a nearby human about $3 to look at something in the real world. Built for YC's "Make Something Agents Want" hackathon, Oct 17–18 2026 ([README](https://github.com/ayaangazali/eyes)); live at https://eyes.pictures |
| [ratchet](https://github.com/ayaangazali/ratchet) | 1 | 2026-08-29 | MIT | A coding agent where "the tests decide" when it's done. Includes a red-team eval of the verifier |
| [jelly / GRADUATE](https://github.com/ayaangazali/jelly) | 0 | 2026-09-27 | none | Routes repeated, verified agent work to a small model you own. Built at Own Your Intelligence Hackathon (YC, 2026-09-27) |
| [founder-mode / SF SPEEDRUN](https://github.com/ayaangazali/founder-mode) | 0 | 2026-07-11 | none | A one-file canvas game, "how fast can your startup IPO?". It has VC coffee-chat dialogue minigames and an accelerator-interview room. https://sfspeedrun.com |
| [mycpa / Diligent](https://github.com/ayaangazali/mycpa) | 0 | 2025-10-13 | none | **Voice/video** AI CFO avatar over a 10-K dataroom (Gemini plus Pipecat). Built for the Google AI Agents Hackathon, with a [58s demo](https://youtu.be/sa8UMgLPKnk) |
| [callyala](https://github.com/ayaangazali/callyala) | 0 | 2025-12-28 | none | **Voice.** Outbound AI calling for car dealerships in English and Arabic (ElevenLabs, Claude analysis) |
| [iSPY](https://github.com/ayaangazali/iSPY) | 0 | 2025-11-29 | none | Gemini VLM CCTV theft and incident detection. The README opens with "The $125 Billion Problem" |
| [jobbot](https://github.com/ayaangazali/jobbot) | 0 | 2026-09-08 | MIT | Autonomous job-application agent. Built for the Multi-App AI Agent Hackathon (Lemma and Comma Capital), with a [Loom demo](https://www.loom.com/share/ba249f7a6ef44f8299da296888ea533e) |
| [cactus-voice-control / Wooly](https://github.com/ayaangazali/cactus-voice-control) | 0 | 2026-04-19 | MIT | **Voice.** iPhone Action Button, then on-device Whisper and Qwen, then a Mac drives the iOS Simulator |
| [fly-around-sf](https://github.com/ayaangazali/fly-around-sf) | 0 | 2026-10-19 | none | 3D SF built from 172k real building footprints, multiplayer drone. https://ayaangazali.github.io/fly-around-sf/ |

### Hackathon wins
**Verified on Devpost** (https://devpost.com/ayaangazali-work):
| Hackathon | Date | Prize(s) | Project | Proof |
|---|---|---|---|---|
| [Production Agents Hackathon](https://production-agents-hackathon.devpost.com/) | ~Nov 2025 **[INFERRED from team repo created 2025-11-22]** | **Top Overall Winners**, **Best Use of Parallel**, **Best use of LightningAI** | Urban: a privacy-first AI agent that triages citizen issues for cities | https://devpost.com/software/urban (team repo https://github.com/Steve-Dusty/urban) |
| [Hack with MLH and DigitalOcean: SF](https://mlhaihackathonsf.devpost.com/) | ~Dec 2025 **[INFERRED]** | **[2nd] Best Use of DigitalOcean GradientAI** | Learning Assistant ("Your class, amplified by AI"), built on **LiveKit voice** | https://devpost.com/software/learning-assistant-shkxn7 |
| [UC Berkeley AI Hackathon 2026](https://ai-hackathon-2026.devpost.com/) | 2026 | **Best Use of the Agentverse by Fetch AI** | Fireflai, a multi-agent tool for firefighters (uses **Deepgram**) | https://devpost.com/software/fireflai |

**Claimed but not independently verified:**
- Search snippets of his LinkedIn mention 1st place at an AWS Agentic AI Hackathon (Networking Copilot), 1st at SCE Hacks (M&A Due Diligence Assistant), and 2nd in a YC "Nivara" track. I couldn't open the page (HTTP 999). Treat these as *unverified*. https://www.linkedin.com/in/ayaangazali/
- Wins "at Microsoft, NVIDIA, AWS": [portfolio README](https://github.com/ayaangazali/ayaan-portfolio). "Eleven-time winner": [SJSU blog](https://blogs.sjsu.edu/engineering/2026/02/23/spartan-engineers-where-innovation-lives-ai-super-bowl-lx-the-chip-comeback/).
- Projects entered without a listed win: Telly at [MHacks 2026](https://devpost.com/software/telly), MOCHA at [HackHayward 2026](https://devpost.com/software/mocha-q9xnfd), GuideMe at [Hack for Social Impact 2025](https://devpost.com/software/guideme-964oxh), CadXR at [SensAI Hack 2025](https://devpost.com/software/cadxr).

### Why he wins [INFERRED]
- **Volume plus sponsor-prize targeting.** All three verified wins include *sponsor tracks* (Parallel, LightningAI, DigitalOcean, Fetch.ai). He stacks several sponsor APIs into one project to qualify for several tracks (Urban won 3 prizes at once). Source for the tags: [Urban](https://devpost.com/software/urban), [Fireflai](https://devpost.com/software/fireflai).
- **Every project has a demo video** (YouTube, Vimeo or Loom on every Devpost page above).
- **A big-number problem statement up front** ("$125 Billion Problem", "60+ hours per deal") plus a one-line tagline ("Talk to your dataroom").
- **YC-flavoured, agent-native themes** in 2026 (Eyes, GRADUATE, VitalLink MCP for ChatGPT): he builds for whatever the judges are currently obsessed with.
- **Voice shows up often.** Callyala (ElevenLabs), Diligent (Pipecat), Learning Assistant (LiveKit), GuideMe (Vapi), Telly and MOCHA (ElevenLabs), Fireflai (Deepgram): https://devpost.com/ayaangazali-work

### Voice/audio projects
callyala, mycpa/Diligent, vorag (Voice RAG), cactus-voice-control/Wooly, Learning Assistant (LiveKit), Telly (voice care assistant, team repo [42nights/telly](https://github.com/42nights/telly), no license), GuideMe (Vapi), MOCHA (ElevenLabs).

### Voice-extension candidates
| Project (license) | Voice version | Why judges would care [INFERRED] | Legal |
|---|---|---|---|
| [eyes](https://github.com/ayaangazali/eyes) (**Apache-2.0**) | **"Kaan" (ears) for Bharat**: an MCP tool that lets an AI agent *phone* the offline world. A Bolna outbound call goes to a kirana, pharmacy, clinic or mechanic and asks in Kannada, Hindi or Tamil ("Is Dolo 650 in stock? What time do you close?"). It gets a structured answer back to the agent, with Plivo or Exotel telephony and Sarvam STT/TTS. Voice replaces the "pay a human to walk over" step | India's long tail has phones, not APIs, so voice is the API. It fits YC's "Make Something Agents Want" thesis exactly, and it's a natural Bolna showcase (outbound calls, Indic, structured extraction) | Apache-2.0 allows a fork with attribution and NOTICE. The clean approach is a fresh build that credits Eyes as inspiration |
| [Telly](https://github.com/42nights/telly) (no license) | **A daily check-in call to elderly parents** in their own language: medicine reminders, mood and fall check, and escalation to children over WhatsApp | Emotional, India-relevant (parents living apart from kids), good retention story for a YC partner | No license, so **inspiration only** |
| [callyala](https://github.com/ayaangazali/callyala) (no license) | Indic outbound calls for 2-wheeler service centres | [INFERRED] Too close to Bolna's own core use case, so low novelty for Bolna judges | Inspiration only |
| [founder-mode](https://github.com/ayaangazali/founder-mode) (no license) | **"YC Interview Simulator" voice agent**: a 10-minute rapid-fire mock YC interview over a phone call that grades your answers | Flatters the prize (the winner gets a YC interview) and the YC judge. Viral among founders | Inspiration only |

---

## 3. Parth Mittal (@mittal-parth)

### Who
- Parth Mittal. GitHub bio: "MTS @Oracle | 15x Hackathon Winner | ex-Tech Lead @IRIS-NITK | @Polkadot-Blockchain-Academy Alumnus | NITK'24". 197 followers. https://api.github.com/users/mittal-parth
- Member of Technical Staff at Oracle (Exadata DBaaS control plane) since Oct 2025. Earlier: Averlon intern, Tech Lead of IRIS at NITK (24K+ users). B.Tech ECE at NITK Surathkal (2020–24). Polkadot Blockchain Academy, with distinction. https://mittalparth.dev/
- "Participated in 35+, won 15 ... and judged 3." https://mittalparth.dev/. The profile README says "30+" ([README](https://github.com/mittal-parth/mittal-parth)).
- Site https://mittalparth.dev/, X [@mittalparth_](https://x.com/mittalparth_), Devfolio https://devfolio.co/@parthmittal (short bio there: "13x Hackathon Winner | ETHIndia'22, 24 Winner").
- He has a regular teammate: [ahmedfahim21](https://github.com/ahmedfahim21) is the top contributor on Sadak (168 commits vs Parth's 29, [contributors API](https://api.github.com/repos/mittal-parth/sadak/contributors)).

### Top ~10 repos
| Repo | ★ | Created | License | What |
|---|---|---|---|---|
| [personal-portfolio](https://github.com/mittal-parth/personal-portfolio) | 180 | 2022-09-17 | none | A portfolio template that imports from LinkedIn |
| [Cluboard](https://github.com/mittal-parth/Cluboard) | 20 | 2021-05-17 | none | A resource-sharing app for college clubs |
| [claude-clan / Claude City](https://github.com/mittal-parth/claude-clan) | 19 | 2026-08-08 | none | A codebase shown as an isometric city where Claude Agent SDK crews build and review PRs live. https://playclaude.vercel.app/, [demo](https://youtu.be/-WVMaU1-sHE) |
| [Khoj](https://github.com/mittal-parth/Khoj) | 17 | 2024-12-06 | **GPL-3.0** | A geo-location treasure hunt that onboards people to Web3. https://playkhoj.com, [demo](https://www.youtube.com/watch?v=98OJuvBur6s) |
| [hackathon-curation-agent](https://github.com/mittal-parth/hackathon-curation-agent) | 14 | 2025-08-17 | AGPL-3.0 | Curates hackathons from Gmail newsletters with Gemini and posts them to Twitter |
| [polkadot-dev-cli](https://github.com/mittal-parth/polkadot-dev-cli) | 10 | 2024-11-06 | none | A Rust CLI for Polkadot developers |
| [sadak](https://github.com/mittal-parth/sadak) | 4 | 2026-07-26 | none | **Voice-first.** A 3D Indic language-learning game: 10 Indian cities, 10 languages, all voice on Sarvam (Bulbul v3 TTS, Saaras v4 STT, sarvam-105b LLM). https://playsadak.vercel.app ([README](https://github.com/mittal-parth/sadak)) |
| [ai-call-screening](https://github.com/mittal-parth/ai-call-screening) | 1 | 2026-07-11 | none | **Voice.** A live scam-call detector: Wear OS mic, then phone, then Gemini Live API, then a watch vibration on a scam verdict ([README](https://github.com/mittal-parth/ai-call-screening)) |
| [kosh-sdk](https://github.com/mittal-parth/kosh-sdk) | 1 | 2025-03-20 | none | No-code remote MCP servers in TEEs (Marlin, nilRAG). ETHGlobal Trifecta, TEE track ([README](https://github.com/mittal-parth/kosh-sdk)) |
| [agentic-commerce](https://github.com/mittal-parth/agentic-commerce) | 0 | 2026-02-15 | **Apache-2.0** | India-first agentic commerce on Google UCP, with UPI and "voice-first and multilingual" in 11+ Indian languages ([README](https://github.com/mittal-parth/agentic-commerce)) |
| [Kahani](https://github.com/harshagw/kahani) (teammate's repo) | 9 | 2026-07-11 | none | Type one sentence and walk into a generated isometric RPG. Nano Banana 2 Lite, Gemini, and **Sarvam Bulbul v3** voiced NPCs. https://kahani-phi.vercel.app |

### Hackathon wins
**Recent, as listed on his site** (https://mittalparth.dev/):
| Hackathon | Date | Result | Project | Proof |
|---|---|---|---|---|
| Anthropic **Push to Prod** (Basecamp Bengaluru) | 2026-08-08 ([event listing](https://allai.events/event/push-to-prod-hackathon-building-at-the-frontier)) | **1st Runner Up**, "2nd among 5K+ applications" | Claude City | https://mittalparth.dev/, https://github.com/mittal-parth/claude-clan, https://youtu.be/-WVMaU1-sHE |
| **Google DeepMind** Bangalore Hackathon | ~Jul 2026 (Kahani repo created 2026-07-11) | **Winner**, "1st place among 4K applications" | Kahani | https://mittalparth.dev/, https://x.com/mittalparth_/status/2076292927882682602, https://github.com/harshagw/kahani |
| **Sarvam Epoch Buildathon** (GrowthX x Sarvam, ₹10L pool, 26 Jul 2026, [details](https://www.startupgrantsindia.com/sarvam-epoch-buildathon-by-growthx)) | 2026-07-26 | **2nd Runner Up**, "among 3K applications" | **Sadak** (voice-first Indic) | https://mittalparth.dev/, https://github.com/mittal-parth/sadak |
| **ETHIndia'24** | Dec 2024 | **Top 10 winners**, "$5000 in grants" | Khoj | https://mittalparth.dev/, https://github.com/mittal-parth/Khoj |

**Older, from Devfolio/Devpost project pages:**
| Hackathon | Prize(s) | Project | Proof |
|---|---|---|---|
| ETHIndia 2022 | **Top 12 Winners** ($500 per builder), **Polygon Best Public Goods**, **Biconomy Best New Module using the SDK** | ChargeSwap (blockchain EV battery swap) | https://devfolio.co/projects/chargeswap-3527 |
| Warpspeed: GenAI Hackathon by Lightspeed (2023) | **First Runners Up** ($1,500), **Replit** $500 cycles | Comicify.ai | https://devfolio.co/projects/comicifyai-97a6, https://mittalparth.dev/ |
| ETHforAll | Superfluid prize pool, Polywrap prize pool | Green Trust | https://devfolio.co/projects/green-trust-ed14 |
| ICON HYPERBUILD (Devpost) | Honorable Mention | Green Trust | https://devpost.com/software/green-trust-xj2w6g |
| Ideathon 2k22 | The Most Innovative Idea (INR 3000), Top 12 | Huntly | https://devfolio.co/projects/huntly-b5a9 |

That's about 9 verified results against the claimed 15. The rest aren't public on Devfolio or Devpost.

### Why he wins [INFERRED]
- **Games and play as the wrapper for a serious capability**: a treasure hunt (Khoj), an RPG (Kahani), a language game (Sadak), an agent city (Claude City). His site literally says "building Claude Code as a game" (https://mittalparth.dev/).
- **The sponsor's tech is load-bearing, and the README says so.** Kahani's README has a section titled "Why this needs NB2 Lite (generation is load-bearing)". Sadak runs "every voice, in both directions" on Sarvam. He wins *sponsor-hosted* events (DeepMind, Sarvam, Anthropic, ETHIndia/Polygon) by putting the host's newest model at the centre.
- **An Indian cultural layer**: Hindi names (Khoj, Kahani, Sadak) and real Indian cities from OpenStreetMap. Judges in Bangalore relate to it immediately.
- **Polish**: a `play<name>.vercel.app` live link, a cinematic OG image, screenshots, a YouTube demo, and a credits section.
- **A repeat team of strong builders** (ahmedfahim21 and others) and a high hackathon cadence (35+).

### Voice/audio projects
Sadak (Sarvam STT/TTS/LLM, plus a LiveKit voice-agent worker in [docs/VOICE_AGENT.md](https://github.com/mittal-parth/sadak)), Kahani (Bulbul NPC voices), ai-call-screening (Gemini Live), Echo ("proactive AI assistant that's always listening", [Devpost, Gemini 3 Hackathon](https://devpost.com/software/echo-35brtd)), agentic-commerce (voice-first multilingual), and To-Do-App-2.0 (speech-to-text, 2021).

### Voice-extension candidates
| Project (license) | Voice version | Why judges would care [INFERRED] | Legal |
|---|---|---|---|
| [ai-call-screening](https://github.com/mittal-parth/ai-call-screening) (no license) | **Scam-call shield for India.** A Bolna/Exotel agent answers suspected "digital arrest", KYC or courier scam calls for an elderly user, screens them in Hindi or Tamil, and alerts family. Alternatively a honeypot that keeps the scammer busy (like O2's "Daisy" AI granny). Use a *simulated* scammer for the demo, to stay clear of recording and consent issues | A huge, current Indian pain point, a clear telephony showcase for Plivo or Exotel, a strong emotional demo, and an obvious B2C or bank/telco B2B path for the YC partner | No license, so **inspiration only** (rebuild from scratch) |
| [agentic-commerce](https://github.com/mittal-parth/agentic-commerce) (**Apache-2.0**) | **Order by phone call in your language**: the user calls a number, a Bolna agent browses UCP merchants, and checkout goes through a UPI link by SMS | India-first, voice is the native interface for the next 500M users, and it's a real commerce flow | Fork with attribution is OK |
| [sadak](https://github.com/mittal-parth/sadak) (no license) | Phone-call language tutor | **[INFERRED] Avoid.** It already won Sarvam's buildathon in Jul 2026, and the judge and sponsor overlap (Sarvam) is high | Inspiration only |
| [Khoj](https://github.com/mittal-parth/Khoj) (GPL-3.0) | Voice clues by phone during a city hunt | Fun, but a weak case for voice | A GPL fork stays GPL |

---

## 4. Cross-cutting winning playbook [INFERRED, distilled from the three profiles above]

1. **Lead with a one-line hook that's absurd or emotional.** "DOOM in a QR code", "Talk your way through ten Indian cities", "Agents pay a human $3 to look". If the title needs explaining, change it.
2. **Make the host's or sponsor's tech load-bearing, and write that down explicitly.** Copy Parth's "Why this needs X" section. For Bolna that means Bolna orchestration, plus Sarvam (Indic STT/TTS), plus Plivo or Exotel (real PSTN calls), plus Deepgram or Cartesia as a fallback. Stacking sponsor APIs makes you eligible for several tracks or prizes (Ayaan's Urban won 3 prizes).
3. **Give India its own flavour.** Hindi project names, real Indian cities and languages, Indian pain points (scam calls, kirana stores, elderly parents). The two Bangalore-host wins (DeepMind, Sarvam) both leaned into this.
4. **Play or theatre beats a dashboard.** Two of the three people wrap capability in a game or persona (Parth's games, Kuber's AsianMOM and Rocky).
5. **Show a live, real artifact.** A live URL on a custom domain, and for voice, **a real phone number judges can call during judging.** That's the single strongest move for a voice buildathon.
6. **Make a demo video of 60–120 seconds.** Every one of Ayaan's Devpost entries has one, as do Parth's Khoj and Claude City and Kuber's blog posts.
7. **Write the README like a landing page**: hero image or GIF, tagline, "how it works" diagram (Mermaid), honest limitations, credits to libraries and people.
8. **Distribution is part of the product.** Kuber's wins come from X/HN virality. Post the demo clip on X and LinkedIn before judging closes and tag the sponsors.
9. **Aim at what the judges want right now.** The YC partner cares about a big market, a clear user, and whether anyone would pay. Ayaan builds to YC's current themes (agents, MCP). Have a one-slide "who pays, how big" answer ready.
10. **Use a repeat team with clear roles.** Parth's core group recurs across wins.

## 5. Top 3 voice-extension candidates for the Bolna buildathon [INFERRED]
1. **Scam-call shield or honeypot for Indian families.** Inspired by Parth's [ai-call-screening](https://github.com/mittal-parth/ai-call-screening) (no license, so rebuild from scratch). Bolna inbound and outbound calls plus Exotel or Plivo plus Sarvam Indic. Strongest mix of social impact, telephony showcase and YC-market story.
2. **"Kaan": agents that phone the offline Indian world.** Inspired by Ayaan's [eyes](https://github.com/ayaangazali/eyes) (Apache-2.0, so a fork with credit is allowed, though a fresh build is better). The agent calls a kirana, pharmacy or clinic in the local language and returns structured data. Pitches as "voice is India's API".
3. **"Desi Mom Calls You": an accountability or roast call agent.** Inspired by Kuber's [AsianMOM](https://github.com/Kuberwastaken/AsianMOM) (Apache-2.0, credit required if forked). Highest virality, and it shows off Indic TTS personas.

Honourable mentions: the YC Interview Simulator call (from [founder-mode](https://github.com/ayaangazali/founder-mode)), an elder-care check-in call (from [Telly](https://github.com/42nights/telly)), and voice ordering on UCP and UPI (from [agentic-commerce](https://github.com/mittal-parth/agentic-commerce), Apache-2.0).

**Source caveats:** An LLM summary of mittalparth.dev gave some wrong years. The years above come from the site's raw text, repo creation dates and event pages. I couldn't fetch the LinkedIn and X pages directly, so wins sourced only from them are marked unverified.

---

## Appendix: full non-fork repo lists

### Appendix: Kuberwastaken, all non-fork repos (source: https://api.github.com/users/Kuberwastaken/repos, fetched 2026-10-21)

| Repo | Stars | Lang | Created | License | Description |
|---|---|---|---|---|---|
| [claurst](https://github.com/Kuberwastaken/claurst) | 10324 | Rust | 2026-03-31 | GPL-3.0 | Agentic Coding for Builders who Ship |
| [backdooms](https://github.com/Kuberwastaken/backdooms) | 642 | HTML | 2025-02-12 | MIT | A self-contained game that fits inside a QR code inspired by DOOM 1993 and The Backrooms |
| [cookie](https://github.com/Kuberwastaken/cookie) | 324 | TypeScript | 2026-08-05 | NOASSERTION | Modern Browsers Don't Really Need The Cookie to Track You Anymore |
| [hp-laser-1008a-macos](https://github.com/Kuberwastaken/hp-laser-1008a-macos) | 176 | C | 2026-08-17 | NOASSERTION | Native macOS (Apple Silicon) driver for the HP Laser 1003-1008 |
| [megaphone](https://github.com/Kuberwastaken/megaphone) | 172 | Swift | 2026-07-13 | MIT | Free, private, on-device dictation for Mac, powered by Apple's SpeechAnalyzer and Foundati |
| [meow](https://github.com/Kuberwastaken/meow) | 165 | Python | 2025-06-11 | Apache-2.0 | The most Purr-fect Image File Format for your AI workflows |
| [picogpt](https://github.com/Kuberwastaken/picogpt) | 134 | HTML | 2026-02-12 | none | GPT in a QR Code ; The actual most atomic way to train and inference a GPT in pure, depend |
| [sweeta](https://github.com/Kuberwastaken/sweeta) | 120 | Python | 2025-10-03 | Apache-2.0 | Remove Watermarks from SORA 2 Video Generations with LaMA inpainting. (RESEARCH AND EDUCAT |
| [litmus](https://github.com/Kuberwastaken/litmus) | 72 | HTML | 2026-03-28 | MIT | Run a Parallel Autonomous ML Research Organization on your OpenClaw instance.  |
| [awesome-idea-of-the-day-archive](https://github.com/Kuberwastaken/awesome-idea-of-the-day-archive) | 70 | JavaScript | 2025-07-14 | MIT | Takes a screenshot of ideabrowser.com everyday |
| [DoomMe](https://github.com/Kuberwastaken/DoomMe) | 63 | Python | 2026-01-02 | MIT | DOOM running inside a README |
| [awesome-fucking-websites](https://github.com/Kuberwastaken/awesome-fucking-websites) | 31 | HTML | 2025-12-20 | MIT | A curated list of websites that tell you to just use the fucking tool. |
| [reference](https://github.com/Kuberwastaken/reference) | 22 | Python | 2026-06-29 | MIT | Let your AI agents search each other's past sessions. |
| [ATHENA](https://github.com/Kuberwastaken/ATHENA) | 19 | Python | 2025-05-21 | MIT | An Open Source, Customizable Smart Speaker that Actually Respects Privacy |
| [caffeineOSS](https://github.com/Kuberwastaken/caffeineOSS) | 17 | Swift | 2026-06-25 | MIT | ☕ Caffeinate your Mac — a tiny menu-bar app that keeps macOS awake. ~120 lines of Swift, z |
| [rocky-tts](https://github.com/Kuberwastaken/rocky-tts) | 17 | Python | 2026-04-07 | NOASSERTION | A plug-and-play TTS voice of Rocky, from Andy Weir's Project Hail Mary, voiced by James Or |
| [blog](https://github.com/Kuberwastaken/blog) | 16 | TypeScript | 2025-01-03 | CC-BY-SA-4.0 | ᨒ MindDump - The Best Terminal-Inspired Blog Website on The Internet™ |
| [Huawhoop](https://github.com/Kuberwastaken/Huawhoop) | 16 | Java | 2026-05-11 | none | Reverse Engineering Huawei Band 10 to get better stats |
| [VPSmaxxing](https://github.com/Kuberwastaken/VPSmaxxing) | 16 | Shell | 2026-06-30 | MIT | A skill to get Claude to set up your Claude Code and Codex AI workflows on a remote VPS wi |
| [AsianMOM](https://github.com/Kuberwastaken/AsianMOM) | 13 | HTML | 2025-05-15 | Apache-2.0 | A WebML based Vision-Language App that Roasts you like an Asian Mom |
| [MiniLMs](https://github.com/Kuberwastaken/MiniLMs) | 12 | Jupyter Notebook | 2025-04-19 | Apache-2.0 | A research project focused on studying and implementing minimalist language model architec |
| [subagentmaxxing](https://github.com/Kuberwastaken/subagentmaxxing) | 12 | Python | 2026-07-09 | MIT | Drive OpenAI Codex & Cursor CLI coding agents as subagents with the same ergonomics as nat |
| [kindle-ai-usage](https://github.com/Kuberwastaken/kindle-ai-usage) | 11 | JavaScript | 2026-08-28 | none | Turn a compatible old Kindle into a low-power, multi-device AI usage dashboard. |
| [flm](https://github.com/Kuberwastaken/flm) | 10 | Python | 2026-09-09 | NOASSERTION | A language model trained from scratch through fly-connectome recurrence. ChatFLM: local co |
| [free-deep-research](https://github.com/Kuberwastaken/free-deep-research) | 10 | TypeScript | 2025-02-06 | Apache-2.0 | My free implementation of @dzhng's implementation of OpenAI's new Deep Research agent. Get |
| [hinge-mcp](https://github.com/Kuberwastaken/hinge-mcp) | 10 | TypeScript | 2026-09-28 | MIT | your clanker can finally swipe for you now |
| [math-gambling](https://github.com/Kuberwastaken/math-gambling) | 9 | Python | 2026-09-10 | GPL-2.0 | Gamble your compute to solve x³+y³+z³=114 |
| [spica](https://github.com/Kuberwastaken/spica) | 9 | TypeScript | 2025-10-08 | Apache-2.0 | Endlessly Extend OpenAI's Sora 2 Outputs |
| [Github-Art](https://github.com/Kuberwastaken/Github-Art) | 8 | Python | 2024-11-05 | Apache-2.0 | Turn your GitHub Commit History into a Pixel Art Canvas |
| [agent-notifications](https://github.com/Kuberwastaken/agent-notifications) | 7 | Python | 2026-04-12 | MIT | Allow your OpenClaw / Hermes agent to get notifications |
| [Dynamic-Readme-Images](https://github.com/Kuberwastaken/Dynamic-Readme-Images) | 7 | JavaScript | 2025-02-19 | MIT | A Template Repository to get "Dynamically Updating" Pictures in Readme |
| [Kuberwastaken.github.io](https://github.com/Kuberwastaken/Kuberwastaken.github.io) | 7 | JavaScript | 2024-12-21 | LGPL-2.1 | The Best Terminal-Inspired Portfolio Website on The Internet™ |
| [fuzzy-redirect](https://github.com/Kuberwastaken/fuzzy-redirect) | 6 | TypeScript | 2025-11-23 | MIT | Autocorrect for your website URLs - Fuzzy URL matching and redirection for React and Next. |
| [Kuberwastaken](https://github.com/Kuberwastaken/Kuberwastaken) | 6 | - | 2024-10-24 | none |  |
| [engram](https://github.com/Kuberwastaken/engram) | 5 | TypeScript | 2025-05-31 | NOASSERTION | The Biggest, Centralized, No BS Open-Source pSEO Content Aggregator for IP University Note |
| [localdrop](https://github.com/Kuberwastaken/localdrop) | 5 | Dart | 2026-10-09 | Apache-2.0 | LocalSend-based file sharing with experimental Linux AirDrop compatibility via omdrop. |
| [clawdbot-skills](https://github.com/Kuberwastaken/clawdbot-skills) | 4 | Python | 2026-01-25 | MIT | A collection of sharp, witty, and functional skills for Clawdbot. Maintained by Valerie (✨ |
| [LifeMap](https://github.com/Kuberwastaken/LifeMap) | 4 | JavaScript | 2025-02-25 | MIT | Create and Visualize your Personal Networks to Navigate Life's Complexities |
| [nogreeting](https://github.com/Kuberwastaken/nogreeting) | 4 | TypeScript | 2025-10-27 | Apache-2.0 | Imagine calling someone on the phone, going [GREETING]! then putting them on hold, if you  |
| [ORCUS](https://github.com/Kuberwastaken/ORCUS) | 4 | Python | 2025-01-06 | Apache-2.0 | A Dual Model AI Based Comment-Analyzer and Flag-Generator for Social Media |
| [Resume](https://github.com/Kuberwastaken/Resume) | 4 | TeX | 2025-01-01 | none | Kuber Mehta's Resume |
| [awesome-claude-mcp-servers](https://github.com/Kuberwastaken/awesome-claude-mcp-servers) | 3 | JavaScript | 2026-07-01 | NOASSERTION | A curated, searchable catalog of Model Context Protocol (MCP) servers for Claude — Desktop |
| [awesome-codex-mcp-servers](https://github.com/Kuberwastaken/awesome-codex-mcp-servers) | 3 | JavaScript | 2026-07-01 | NOASSERTION | A curated, searchable catalog of Model Context Protocol (MCP) servers for OpenAI Codex — C |
| [kubeats](https://github.com/Kuberwastaken/kubeats) | 3 | Kotlin | 2026-04-22 | none | A probably broken but cool modification of pauwma/GlyphBeat for Nothing Phone 3 |
| [one-of-the-top-open-source-ai-tools](https://github.com/Kuberwastaken/one-of-the-top-open-source-ai-tools) | 3 | - | 2025-10-04 | WTFPL | Saving Open Source, All contributions accepted. Just add your name to Readme.md if you wan |
| [riemann](https://github.com/Kuberwastaken/riemann) | 3 | Python | 2026-07-23 | Apache-2.0 | Research archive and the collective progress of humanity to the Riemann Hypothesis and pot |
| [TREAT](https://github.com/Kuberwastaken/TREAT) | 3 | Python | 2024-12-29 | Apache-2.0 | An Open-Source AI Web App to Detect Triggering Content in Movies and Shows |
| [TREAT-CS50](https://github.com/Kuberwastaken/TREAT-CS50) | 3 | CSS | 2024-12-31 | none | An Early (Flan T-5) version of An Open-Source AI Web App to Detect Triggering Content in M |
| [Berghain](https://github.com/Kuberwastaken/Berghain) | 2 | Python | 2025-09-21 | none | (Most) Code I used for the ListenLabs Berghain Challenge + Blog and Technical breakdown |
| [goldbach](https://github.com/Kuberwastaken/goldbach) | 2 | Python | 2026-07-23 | Apache-2.0 | Research archive and the collective progress of humanity to Goldbach's Conjecture and pote |
| [JumpCut](https://github.com/Kuberwastaken/JumpCut) | 2 | Python | 2025-01-20 | none | A Music Streaming App for Gen Z's Attention Span |
| [minicraft](https://github.com/Kuberwastaken/minicraft) | 2 | HTML | 2026-04-14 | none | A playable copy of Minecraft Classic hidden inside a single X thread that's self-decoding, |
| [planethunt](https://github.com/Kuberwastaken/planethunt) | 2 | HTML | 2026-10-10 | NOASSERTION | TESS planet-hunt evidence and write-up |
| [Portfolio-UI](https://github.com/Kuberwastaken/Portfolio-UI) | 2 | TypeScript | 2025-04-25 | none |  |
| [TREAT-R1](https://github.com/Kuberwastaken/TREAT-R1) | 2 | Python | 2025-01-25 | none | A DeepSeek R1 version of TREAT: An Open-Source AI Web App to Detect Triggering Content in  |
| [BrainAI](https://github.com/Kuberwastaken/BrainAI) | 1 | HTML | 2025-03-13 | none | Beyond Artificial, This is Real Intelligence. |
| [c5-k4](https://github.com/Kuberwastaken/c5-k4) | 1 | Python | 2026-08-12 | none | building a counterexample-discovery program stemming from a 20-vertex graph and actual pat |
| [CottagOS](https://github.com/Kuberwastaken/CottagOS) | 1 | JavaScript | 2025-05-06 | none |  |
| [Hello-World](https://github.com/Kuberwastaken/Hello-World) | 1 | - | 2026-01-31 | none |  |
| [HOBOEM](https://github.com/Kuberwastaken/HOBOEM) | 1 | HTML | 2026-01-09 | NOASSERTION |  |
| [Law-and-Disorder](https://github.com/Kuberwastaken/Law-and-Disorder) | 1 | JavaScript | 2025-02-10 | Apache-2.0 | A Repo for team Future Layoffs' Hackathon project for Code Genesis |
| [MindDump-Preview-Update](https://github.com/Kuberwastaken/MindDump-Preview-Update) | 1 | JavaScript | 2025-02-19 | none | Automatically takes a screenshot to capture updates on my Blog Website - MindDump everyday |
| [pokeclaw](https://github.com/Kuberwastaken/pokeclaw) | 1 | JavaScript | 2026-05-06 | none | An MCP bridge and skill to give poke persistent hardware to run on |
| [ROOP-AI-Deepfakes](https://github.com/Kuberwastaken/ROOP-AI-Deepfakes) | 1 | Jupyter Notebook | 2024-04-25 | MIT | This tool will help you to use AI to deepfake any photo/video with the help of Google Coll |
| [sacredsteps-landing](https://github.com/Kuberwastaken/sacredsteps-landing) | 1 | TypeScript | 2025-07-22 | none |  |
| [Sprig-Music-Maker](https://github.com/Kuberwastaken/Sprig-Music-Maker) | 1 | Python | 2025-05-06 | none |  |
| [strongy](https://github.com/Kuberwastaken/strongy) | 1 | Java | 2026-02-21 | GPL-3.0 | [WIP] A prettier, faster Minecraft stronghold calculator — built on top of Ninjabrain-Bot  |
| [the-archon](https://github.com/Kuberwastaken/the-archon) | 1 | JavaScript | 2026-04-25 | none |  |
| [Training-Voice-Extractor](https://github.com/Kuberwastaken/Training-Voice-Extractor) | 1 | Python | 2026-02-11 | none | A few python scripts to get raw vocals/ conversations from youtube videos |
| [TREAT-Classic](https://github.com/Kuberwastaken/TREAT-Classic) | 1 | Python | 2025-02-11 | Apache-2.0 | A Flan T-5 Large Version of An AI web application Built with Flask and Python to Analyze M |
| [TREAT-EXAONE](https://github.com/Kuberwastaken/TREAT-EXAONE) | 1 | Python | 2025-03-18 | none | A LGAI EXAONE Version of An AI web application to Analyze Movie and Show scripts for Poten |
| [trytreat](https://github.com/Kuberwastaken/trytreat) | 1 | HTML | 2025-01-09 | Unlicense | A Web Version for TREAT- An AI Web App to Detect Triggering Content in Movies and Shows |
| [vyyra](https://github.com/Kuberwastaken/vyyra) | 1 | TypeScript | 2025-07-02 | none |  |
| [algorithm-design-sga-1](https://github.com/Kuberwastaken/algorithm-design-sga-1) | 0 | C | 2025-10-23 | none |  |
| [badluck](https://github.com/Kuberwastaken/badluck) | 0 | TypeScript | 2025-08-17 | MIT |  |
| [bda-sga2](https://github.com/Kuberwastaken/bda-sga2) | 0 | Java | 2026-05-02 | none | Building a Library Manager App from Scratch with Spring Boot |
| [better-ranklist](https://github.com/Kuberwastaken/better-ranklist) | 0 | JavaScript | 2025-06-04 | none | studying ipu-ranklist and mayhaps making a better one idk |
| [brag-sheet](https://github.com/Kuberwastaken/brag-sheet) | 0 | HTML | 2025-01-24 | none | A Brag Sheet for Recommendation Letters for Kuber Mehta |
| [conway99-c3-orbit-restriction](https://github.com/Kuberwastaken/conway99-c3-orbit-restriction) | 0 | Lean | 2026-07-23 | Apache-2.0 | Lean 4 formalization of the Conway 99-graph free-C3 triangular-orbit restriction |
| [dreambooth](https://github.com/Kuberwastaken/dreambooth) | 0 | - | 2025-03-27 | none | Realistic AI recreations trained from picture data |
| [ECP](https://github.com/Kuberwastaken/ECP) | 0 | HTML | 2025-03-16 | none | Github Repo for Ecommerce Photoshoot |
| [engram-backend](https://github.com/Kuberwastaken/engram-backend) | 0 | JavaScript | 2025-06-06 | none |  |
| [engram-dn](https://github.com/Kuberwastaken/engram-dn) | 0 | JavaScript | 2025-06-01 | none |  |
| [engram-exp-v2](https://github.com/Kuberwastaken/engram-exp-v2) | 0 | JavaScript | 2025-06-01 | none |  |
| [engram-files](https://github.com/Kuberwastaken/engram-files) | 0 | - | 2025-06-01 | NOASSERTION |  |
| [engram-material](https://github.com/Kuberwastaken/engram-material) | 0 | JavaScript | 2025-06-01 | none |  |
| [formal-conjectures-counterexamples](https://github.com/Kuberwastaken/formal-conjectures-counterexamples) | 0 | Lean | 2026-07-24 | none |  |
| [gemsy](https://github.com/Kuberwastaken/gemsy) | 0 | TypeScript | 2025-07-08 | none |  |
| [Hacktober-Fest](https://github.com/Kuberwastaken/Hacktober-Fest) | 0 | HTML | 2024-10-26 | none | A youtube clone made for Hacktoberfest 2024 |
| [HF-Agents-Course](https://github.com/Kuberwastaken/HF-Agents-Course) | 0 | Python | 2025-02-15 | none | All the stuff I make for Hugging Face's Agents Course goes here |
| [hob-revamped](https://github.com/Kuberwastaken/hob-revamped) | 0 | HTML | 2026-06-10 | none |  |
| [ijti-resume-template](https://github.com/Kuberwastaken/ijti-resume-template) | 0 | - | 2026-01-11 | MIT | ATS friendly custom hand-made resume template. |
| [Jekyll-terminal](https://github.com/Kuberwastaken/Jekyll-terminal) | 0 | Ruby | 2025-05-05 | none |  |
| [leanshot](https://github.com/Kuberwastaken/leanshot) | 0 | AppleScript | 2026-07-01 | MIT |  |
| [linkedin-forensics](https://github.com/Kuberwastaken/linkedin-forensics) | 0 | Python | 2026-08-09 | MIT | Agent skill: evidence-led OSINT forensics on public LinkedIn posts, profiles & media — dec |
| [LLMpdf](https://github.com/Kuberwastaken/LLMpdf) | 0 | JavaScript | 2025-05-20 | GPL-2.0 | Trying to run a LLM inside a PDF lol |
| [minesweeper-llm](https://github.com/Kuberwastaken/minesweeper-llm) | 0 | Python | 2026-02-15 | none | RL Agent to solve Minesweeper with Qwen 2.5 14B Instruct |
| [Nothing-DOOM-Essential-Backend](https://github.com/Kuberwastaken/Nothing-DOOM-Essential-Backend) | 0 | C | 2026-02-28 | GPL-2.0 | Running DOOM inside an Essential Space |
| [ORCUS-Web](https://github.com/Kuberwastaken/ORCUS-Web) | 0 | Python | 2025-01-12 | none | Web Version of a Dual Model AI Based Comment-Analyzer and Flag-Generator for Social Media |
| [pdf-inspector](https://github.com/Kuberwastaken/pdf-inspector) | 0 | Python | 2026-08-03 | NOASSERTION | Agent skill: local PDF → Markdown for Claude Code/Codex/Cursor, powered by Firecrawl's pdf |
| [PolyThink-Alpha-Spaces](https://github.com/Kuberwastaken/PolyThink-Alpha-Spaces) | 0 | Python | 2025-03-27 | none |  |
| [real-disease-real-kid-hackathon](https://github.com/Kuberwastaken/real-disease-real-kid-hackathon) | 0 | Python | 2026-08-26 | NOASSERTION |  |
| [Retro](https://github.com/Kuberwastaken/Retro) | 0 | JavaScript | 2025-05-14 | none |  |
| [roblox-irc-chat](https://github.com/Kuberwastaken/roblox-irc-chat) | 0 | - | 2026-01-16 | none | Better chat for boblox |
| [sacredsteps](https://github.com/Kuberwastaken/sacredsteps) | 0 | TypeScript | 2025-07-20 | none | Learn Religions like Never Before |
| [silverilla-rebooted](https://github.com/Kuberwastaken/silverilla-rebooted) | 0 | - | 2025-06-05 | none |  |
| [Singapore-Plan](https://github.com/Kuberwastaken/Singapore-Plan) | 0 | HTML | 2025-04-06 | none | A rough itenary for the singapore trip |
| [thiswebsiteisnotonline](https://github.com/Kuberwastaken/thiswebsiteisnotonline) | 0 | JavaScript | 2025-08-24 | Apache-2.0 |  |
| [TREAT-3B](https://github.com/Kuberwastaken/TREAT-3B) | 0 | Python | 2025-01-05 | Apache-2.0 | A Llama 3.2 3B version of An Open-Source AI Web App to Detect Triggering Content in Movies |
| [TREAT-Chocosyrup-Spaces](https://github.com/Kuberwastaken/TREAT-Chocosyrup-Spaces) | 0 | Python | 2025-06-07 | none |  |
| [TREAT-Classic-Spaces](https://github.com/Kuberwastaken/TREAT-Classic-Spaces) | 0 | Python | 2025-02-19 | none | TREAT Classic for Hugging Face Spaces. Check out the normal version at https://github.com/ |
| [TREAT-EXAONE-SPACES](https://github.com/Kuberwastaken/TREAT-EXAONE-SPACES) | 0 | Python | 2025-03-21 | none | A Backup GitHub Repo for the Hugging Face Spaces Port of TREAT-EXAONE |
| [TREAT-Gemini](https://github.com/Kuberwastaken/TREAT-Gemini) | 0 | Python | 2025-01-03 | Apache-2.0 | A Google Gemini Version of An Open-Source AI Web App to Detect Triggering Content in Movie |
| [TREAT-R1-API](https://github.com/Kuberwastaken/TREAT-R1-API) | 0 | Python | 2025-01-26 | none | A version of TREAT R1 that uses hugging Face's Inference API |
| [valerie-dashboard](https://github.com/Kuberwastaken/valerie-dashboard) | 0 | Python | 2026-01-25 | MIT | A monochrome, pixel-art inspired system dashboard for Valerie. |
| [video-dump](https://github.com/Kuberwastaken/video-dump) | 0 | - | 2026-01-01 | none |  |
| [wowii-63-85-counterexample](https://github.com/Kuberwastaken/wowii-63-85-counterexample) | 0 | Lean | 2026-07-23 | Apache-2.0 | Lean 4 certificates for C5[K4] counterexamples to WOWII Graph Conjectures 63 and 85 |
| [YT-Transcripts-API](https://github.com/Kuberwastaken/YT-Transcripts-API) | 0 | Python | 2025-07-04 | none |  |

### Appendix: ayaangazali, all non-fork repos (source: https://api.github.com/users/ayaangazali/repos, fetched 2026-10-21)

| Repo | Stars | Lang | Created | License | Description |
|---|---|---|---|---|---|
| [graph-engineering](https://github.com/ayaangazali/graph-engineering) | 3 | JavaScript | 2026-07-21 | MIT | Graph engineering for Claude Code: /graph turns any goal into a DAG of specialist subagent |
| [eyes](https://github.com/ayaangazali/eyes) | 1 | TypeScript | 2026-10-17 | Apache-2.0 | Eyes: agents pay a nearby human a few dollars to check something in the physical world |
| [GazaliEdge](https://github.com/ayaangazali/GazaliEdge) | 1 | HTML | 2024-10-26 | none | GazaliEdge is a personalized finance and stock analysis tool designed for comprehensive ma |
| [ratchet](https://github.com/ayaangazali/ratchet) | 1 | Python | 2026-08-29 | MIT |  |
| [ShieldNet](https://github.com/ayaangazali/ShieldNet) | 1 | Python | 2025-11-15 | none |  |
| [Adaptive-ATS](https://github.com/ayaangazali/Adaptive-ATS) | 0 | Python | 2025-09-23 | none |  |
| [ai-crypto-trader-backtest](https://github.com/ayaangazali/ai-crypto-trader-backtest) | 0 | Python | 2026-06-15 | none |  |
| [ai-stock-trader-backtest](https://github.com/ayaangazali/ai-stock-trader-backtest) | 0 | Python | 2026-06-15 | none |  |
| [alibaba-stationery-store](https://github.com/ayaangazali/alibaba-stationery-store) | 0 | HTML | 2026-06-15 | none |  |
| [amplo-site](https://github.com/ayaangazali/amplo-site) | 0 | TypeScript | 2026-04-27 | none | Amplo — operating system for the agentic enterprise (Next.js 16, Vercel) |
| [aya](https://github.com/ayaangazali/aya) | 0 | JavaScript | 2026-03-27 | none |  |
| [ayaan-portfolio](https://github.com/ayaangazali/ayaan-portfolio) | 0 | TypeScript | 2026-02-02 | none |  |
| [ayaangazali](https://github.com/ayaangazali/ayaangazali) | 0 | - | 2026-06-11 | none |  |
| [BibBackSpartans](https://github.com/ayaangazali/BibBackSpartans) | 0 | - | 2025-09-08 | none | We are the BigBackSpartans |
| [bill-splitter](https://github.com/ayaangazali/bill-splitter) | 0 | JavaScript | 2026-06-15 | none |  |
| [bridgeai-rapid-aid](https://github.com/ayaangazali/bridgeai-rapid-aid) | 0 | TypeScript | 2025-11-08 | none |  |
| [cactus-voice-control](https://github.com/ayaangazali/cactus-voice-control) | 0 | Swift | 2026-04-19 | MIT | iPhone Action Button + on-device Whisper/Qwen/Gemma + Mac runs mobile-use against iOS Simu |
| [callyala](https://github.com/ayaangazali/callyala) | 0 | TypeScript | 2025-12-28 | none |  |
| [cbse-test-paper-generator](https://github.com/ayaangazali/cbse-test-paper-generator) | 0 | Python | 2026-06-15 | none |  |
| [coffee-shop](https://github.com/ayaangazali/coffee-shop) | 0 | HTML | 2026-06-15 | none |  |
| [Daja](https://github.com/ayaangazali/Daja) | 0 | TypeScript | 2026-06-11 | none | NexusHub — Electron + React desktop AI super app (Finance War Room, Sports, PDF, Health, A |
| [deep-environment](https://github.com/ayaangazali/deep-environment) | 0 | - | 2026-02-16 | none | Improving changes |
| [dropshipping-store](https://github.com/ayaangazali/dropshipping-store) | 0 | JavaScript | 2026-06-15 | none |  |
| [fanta](https://github.com/ayaangazali/fanta) | 0 | Python | 2026-02-28 | NOASSERTION |  |
| [fidget-spinner-shop](https://github.com/ayaangazali/fidget-spinner-shop) | 0 | HTML | 2026-06-15 | none |  |
| [fly-around-sf](https://github.com/ayaangazali/fly-around-sf) | 0 | TypeScript | 2026-10-19 | none | Fly a drone around all 172,000 buildings of a 3D San Francisco. Collect landmarks, solve c |
| [founder-mode](https://github.com/ayaangazali/founder-mode) | 0 | HTML | 2026-07-11 | none |  |
| [fraud-detect](https://github.com/ayaangazali/fraud-detect) | 0 | Python | 2026-01-04 | MIT |  |
| [Fuyu](https://github.com/ayaangazali/Fuyu) | 0 | TypeScript | 2025-11-22 | none |  |
| [fuyu_ayaan](https://github.com/ayaangazali/fuyu_ayaan) | 0 | - | 2025-12-06 | none |  |
| [global-tour-guide](https://github.com/ayaangazali/global-tour-guide) | 0 | JavaScript | 2026-03-29 | none | Premium interactive travel showcase with Three.js 3D globe, GSAP ScrollTrigger, and mouse  |
| [hack-hayward](https://github.com/ayaangazali/hack-hayward) | 0 | TypeScript | 2026-03-21 | none |  |
| [hackday](https://github.com/ayaangazali/hackday) | 0 | TypeScript | 2026-01-27 | none |  |
| [homebrew-ratchet](https://github.com/ayaangazali/homebrew-ratchet) | 0 | Ruby | 2026-08-29 | none |  |
| [Homeless](https://github.com/ayaangazali/Homeless) | 0 | - | 2025-11-08 | none |  |
| [indian-restaurant-menu](https://github.com/ayaangazali/indian-restaurant-menu) | 0 | HTML | 2026-06-15 | none |  |
| [iSPY](https://github.com/ayaangazali/iSPY) | 0 | TypeScript | 2025-11-29 | none |  |
| [jelly](https://github.com/ayaangazali/jelly) | 0 | Python | 2026-09-27 | none | GRADUATE — route repeated, test-verified agent work to a small model you own. Own Your Int |
| [jobbot](https://github.com/ayaangazali/jobbot) | 0 | Python | 2026-09-08 | MIT | Autonomous job-application agent. Finds roles, tailors a one-page resume, fills and verifi |
| [kuwaiti-restaurant-menu](https://github.com/ayaangazali/kuwaiti-restaurant-menu) | 0 | HTML | 2026-06-15 | none |  |
| [lab12](https://github.com/ayaangazali/lab12) | 0 | Java | 2026-04-24 | none |  |
| [Live-Financial-Dashboard](https://github.com/ayaangazali/Live-Financial-Dashboard) | 0 | HTML | 2025-09-10 | none | GazaliEdge |
| [maywood](https://github.com/ayaangazali/maywood) | 0 | TypeScript | 2026-02-12 | none |  |
| [mun-lab](https://github.com/ayaangazali/mun-lab) | 0 | Python | 2026-08-10 | none | Self-hosted deep-research desk for Model UN prep and research-paper work |
| [MyCFA](https://github.com/ayaangazali/MyCFA) | 0 | TypeScript | 2025-10-02 | none |  |
| [mycpa](https://github.com/ayaangazali/mycpa) | 0 | TypeScript | 2025-10-13 | none |  |
| [Networking-Copilot](https://github.com/ayaangazali/Networking-Copilot) | 0 | Python | 2025-10-02 | none | A personalized, authentic and contextual version of linkedin |
| [Obidient](https://github.com/ayaangazali/Obidient) | 0 | TypeScript | 2025-11-03 | MIT |  |
| [openclaw-site](https://github.com/ayaangazali/openclaw-site) | 0 | TypeScript | 2026-04-27 | none | OpenClaw — soul-forged AI agent platform landing site (Next.js 16, Vercel-ready) |
| [Portfolio](https://github.com/ayaangazali/Portfolio) | 0 | HTML | 2025-06-28 | none | Portfolio Website |
| [pr-assets](https://github.com/ayaangazali/pr-assets) | 0 | - | 2026-09-13 | none | Screenshots referenced from pull request descriptions |
| [prox-animation](https://github.com/ayaangazali/prox-animation) | 0 | JavaScript | 2026-08-06 | none | Self-contained 9:16 web animation: product scan, live research run, competitor table, verd |
| [pybacktest](https://github.com/ayaangazali/pybacktest) | 0 | Python | 2026-07-08 | none |  |
| [rag-system](https://github.com/ayaangazali/rag-system) | 0 | Python | 2026-06-15 | none |  |
| [restaurant-menu-qna](https://github.com/ayaangazali/restaurant-menu-qna) | 0 | HTML | 2026-06-15 | none |  |
| [sat-chatbot](https://github.com/ayaangazali/sat-chatbot) | 0 | Python | 2026-06-15 | none |  |
| [savewithmoi](https://github.com/ayaangazali/savewithmoi) | 0 | TypeScript | 2025-11-16 | none |  |
| [study-chatbot](https://github.com/ayaangazali/study-chatbot) | 0 | Python | 2026-06-15 | none |  |
| [TheGreenGuide](https://github.com/ayaangazali/TheGreenGuide) | 0 | HTML | 2023-08-11 | none |  |
| [TheShortFund](https://github.com/ayaangazali/TheShortFund) | 0 | Python | 2025-11-02 | none |  |
| [Trexcart](https://github.com/ayaangazali/Trexcart) | 0 | HTML | 2019-08-23 | none |  |
| [vorag](https://github.com/ayaangazali/vorag) | 0 | Python | 2025-12-28 | none |  |
| [weather-app](https://github.com/ayaangazali/weather-app) | 0 | JavaScript | 2026-06-15 | none |  |
| [workshop](https://github.com/ayaangazali/workshop) | 0 | - | 2026-03-10 | none |  |
| [yc-mcp-chatgpt](https://github.com/ayaangazali/yc-mcp-chatgpt) | 0 | HTML | 2026-02-25 | none |  |
| [yolo](https://github.com/ayaangazali/yolo) | 0 | CSS | 2026-02-03 | none |  |

### Appendix: mittal-parth, all non-fork repos (source: https://api.github.com/users/mittal-parth/repos, fetched 2026-10-21)

| Repo | Stars | Lang | Created | License | Description |
|---|---|---|---|---|---|
| [personal-portfolio](https://github.com/mittal-parth/personal-portfolio) | 180 | JavaScript | 2022-09-17 | none | The only developer portfolio template you'll ever need with modern UI/UX. Import data stra |
| [Cluboard](https://github.com/mittal-parth/Cluboard) | 20 | HTML | 2021-05-17 | none | A full-stack web application to facilitate sharing resources in college clubs with email n |
| [claude-clan](https://github.com/mittal-parth/claude-clan) | 19 | TypeScript | 2026-08-08 | none | Turn your codebase and GitHub PRs into a live isometric city where AI agents visibly build |
| [Khoj](https://github.com/mittal-parth/Khoj) | 17 | TypeScript | 2024-12-06 | GPL-3.0 | A geo-location treasure hunt app that turns Web3 onboarding into an adventure. |
| [hackathon-curation-agent](https://github.com/mittal-parth/hackathon-curation-agent) | 14 | Python | 2025-08-17 | AGPL-3.0 | An intelligent agent that automatically curates hackathons from your email newsletters, ev |
| [polkadot-dev-cli](https://github.com/mittal-parth/polkadot-dev-cli) | 10 | Rust | 2024-11-06 | none | CLI tool for Polkadot developers bundling linting, formatting, and version management. |
| [Cash-Flow-Minmiser](https://github.com/mittal-parth/Cash-Flow-Minmiser) | 5 | JavaScript | 2021-12-19 | none | A React application to help users visualise and minimise cash flow among multiple transact |
| [GreenTrust](https://github.com/mittal-parth/GreenTrust) | 5 | JavaScript | 2023-02-28 | none |  |
| [sadak](https://github.com/mittal-parth/sadak) | 4 | TypeScript | 2026-07-26 | none | An interactive, voice-first game where users learn new languages through everyday conversa |
| [jev-experiments](https://github.com/mittal-parth/jev-experiments) | 2 | Python | 2026-09-17 | none |  |
| [Say-No-To-Sign-In-Articles](https://github.com/mittal-parth/Say-No-To-Sign-In-Articles) | 2 | Python | 2021-09-13 | none |  |
| [ai-call-screening](https://github.com/mittal-parth/ai-call-screening) | 1 | Kotlin | 2026-07-11 | none |  |
| [Freadom](https://github.com/mittal-parth/Freadom) | 1 | Python | 2021-11-17 | none | A simple tool to scrape articles. Works even on websites that dont allow users to read the |
| [GSDC-NITK-CRUD-API](https://github.com/mittal-parth/GSDC-NITK-CRUD-API) | 1 | Python | 2021-11-18 | none | A Django based CRUD API using GraphQL to manage employees in an organization.  |
| [issue-curation-agent](https://github.com/mittal-parth/issue-curation-agent) | 1 | - | 2026-04-29 | Apache-2.0 | Find issues to work on, across open source repos using the Cursor CLI |
| [kosh-sdk](https://github.com/mittal-parth/kosh-sdk) | 1 | TypeScript | 2025-03-20 | none | ETHGlobal Trifecta hack for the TEE track  |
| [To-Do-App-2.0](https://github.com/mittal-parth/To-Do-App-2.0) | 1 | HTML | 2021-05-13 | none | A Progressive Web Application with OAuth 2.0. It supports media and Speech to text input f |
| [TRINIT_HackOverflowSquad_Dev02](https://github.com/mittal-parth/TRINIT_HackOverflowSquad_Dev02) | 1 | JavaScript | 2022-01-29 | none |  |
| [agentic-commerce](https://github.com/mittal-parth/agentic-commerce) | 0 | TypeScript | 2026-02-15 | Apache-2.0 |  |
| [anasaijaz](https://github.com/mittal-parth/anasaijaz) | 0 | - | 2022-01-31 | none | Config files for my GitHub profile. |
| [bank-landing-page-react](https://github.com/mittal-parth/bank-landing-page-react) | 0 | JavaScript | 2022-09-14 | none | A landing page for a bank with modern UI/UX using React and Tailwind. |
| [bindu](https://github.com/mittal-parth/bindu) | 0 | TypeScript | 2026-10-04 | none | Fast open source alternative to Grok Bot / Muse / Dots (WIP) |
| [Django-Ecommerce-Website](https://github.com/mittal-parth/Django-Ecommerce-Website) | 0 | - | 2021-04-28 | none | My first website using Django |
| [docs](https://github.com/mittal-parth/docs) | 0 | - | 2023-06-04 | none |  |
| [experiments](https://github.com/mittal-parth/experiments) | 0 | TypeScript | 2026-09-22 | none | Fun random stuff I work on :) |
| [it301-project](https://github.com/mittal-parth/it301-project) | 0 | C | 2023-04-12 | none |  |
| [mittal-parth](https://github.com/mittal-parth/mittal-parth) | 0 | - | 2021-11-29 | none |  |
| [notes](https://github.com/mittal-parth/notes) | 0 | - | 2026-08-24 | none |  |
| [pba-group-13-activity-2](https://github.com/mittal-parth/pba-group-13-activity-2) | 0 | Rust | 2024-05-21 | none |  |
| [rails-todo-scaffold](https://github.com/mittal-parth/rails-todo-scaffold) | 0 | Ruby | 2024-02-18 | none | Testing Rails Application |
| [Ruby-On-Rails-CRUD](https://github.com/mittal-parth/Ruby-On-Rails-CRUD) | 0 | Ruby | 2021-06-05 | none | Simple project to understand basic CURD in Ruby On Rails  |
| [SkyNet](https://github.com/mittal-parth/SkyNet) | 0 | Solidity | 2023-12-08 | none |  |
| [To-Do-WebApp-Django](https://github.com/mittal-parth/To-Do-WebApp-Django) | 0 | - | 2021-05-04 | none |  |
| [vyan](https://github.com/mittal-parth/vyan) | 0 | TypeScript | 2025-08-09 | none | An EV Battery Swapping De-PIN ecosystem on the Sei Blockchain with AI powered stock manage |
| [zku-bg](https://github.com/mittal-parth/zku-bg) | 0 | Solidity | 2022-06-08 | none | Background Assignment for ZKU's July-August Cohort. |
