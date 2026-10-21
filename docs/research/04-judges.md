# Bolna Symphony Buildathon: who will judge it, and what each judge rewards

Researched 2026-10-21. Read-only throughout: I logged into nothing, posted nothing and submitted no forms. LinkedIn and X mostly blocked automated fetches (HTTP 999/402/451). The exceptions were LinkedIn's public company page, a few public post pages, and Prateek Sachan's public profile. Those were read with curl.

Labels used below:
- **CONFIRMED JUDGE**: named by Bolna as a judge or juror.
- **CONFIRMED ROLE**: named in an official role that involves evaluating teams, but not called a "judge".
- **PROBABLE**: strong circumstantial case.
- **POSSIBLE**: plausible, with weak evidence.
- **[INFERRED]**: my reasoning, not something a source states.

---

## 0. Summary

- **No judge, jury or mentor list has been published (as of 2026-10-21).** I checked:
  - every bolna.ai Symphony page (`/symphony`, `/symphony/speakers`, `/symphony/buildathon`)
  - the newest JS bundles, including the new `/submit` route
  - Bolna's LinkedIn company page and its buildathon posts with their comments
  - Prateek Sachan's public LinkedIn activity
  - Luma, and web/X search snippets

  None of them names a judge.
- **Only one person is officially tied to evaluation: Grey Baker (YC General Partner).** He interviews the winner for YC: "1st place: ₹50,000 + an interview with Grey Baker, YC Partner" ([Bolna LinkedIn post](https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU)). He is also a Symphony speaker ([speakers](https://www.bolna.ai/symphony/speakers)). So he is a **CONFIRMED ROLE** (post-win interviewer), **not** a confirmed buildathon judge.
- **A "jury" exists but is unnamed.** A search snippet attributed to a Bolna staffer's LinkedIn reads: "the top 10 teams will be presenting their pitch in front of a jury and 500+ attendees on Nov 20 in Bangalore". Source: WebSearch snippet pointing at https://www.linkedin.com/in/vaibhav-sharma-9305b7232/ and https://www.linkedin.com/in/siddharthbatra/. Both returned HTTP 999, so this is **UNVERIFIED**.
  - It conflicts with the official copy, which says "top 3 will also pitch live on the Abhyas stage" ([Bolna post](https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU); [buildathon page](https://www.bolna.ai/symphony/buildathon)).
- **Who decides which stage** [INFERRED]:
  - **Shortlist (Nov 3) and interviews (Nov 5–7):** almost certainly the Bolna team, i.e. the founders plus product, devrel and community staff. The FAQ says "We review every application and shortlist the strongest builds" ([buildathon JS](https://www.bolna.ai/symphony/buildathon/assets/routes-fUN6ZzhH.js)).
  - **Ranking the top 3 on Nov 20:** a jury drawn from people already at Symphony. That means Bolna founders, sponsor leads (Exotel, Kalpa, Plivo, Sarvam, Cartesia, Deepgram, Smallest) and investor speakers (General Catalyst, Schema, Upekkha). Grey Baker would be a natural headline juror, because the prize is his interview.
- **How Bolna frames it:** CTO Prateek Sachan wrote "Show your proof of work by making something people want" ([Prateek's post](https://www.linkedin.com/posts/bolna-ai_activity-7516864461119467520-uNZa)). That is YC's motto almost word for word. **Optimise for real users and real usage, not for polish.**

---

## 1. Search log: where I looked for a named judge list

| Where | Result | Source |
|---|---|---|
| `/symphony/speakers` (Next.js RSC payload + HTML) | 15 speakers + "Mr. Bolna" AI host. No judge/jury section | https://www.bolna.ai/symphony/speakers |
| `/symphony` | Says Abhyas is "home to the buildathon **and hackathon**". Also an "awards" close on Sur. No jury named | https://www.bolna.ai/symphony |
| `/symphony/agenda` | 404 | https://www.bolna.ai/symphony/agenda |
| Buildathon bundle (new build, `routes-fUN6ZzhH.js`) | Only change from the Oct 14 build: a "Can I get credits for my project?" FAQ plus a credits request form. "judg", "jury" and "mentor" don't appear | https://www.bolna.ai/symphony/buildathon/assets/routes-fUN6ZzhH.js |
| Submit route bundle (`submit-CKZ-Kgk0.js`) | Fields only: project name, ≤200-char description, http(s) link, Drive/Luma deck or video. No criteria | https://www.bolna.ai/symphony/buildathon/assets/submit-CKZ-Kgk0.js |
| Bolna LinkedIn company page and posts | Prize/credits copy. Tagged staff: **Prateek, Maitreya, Tanisha** on the launch post; **Maitreya, Sharath, Tanisha** on Prateek's post. No judges | https://www.linkedin.com/company/bolna-ai/ , https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU , https://www.linkedin.com/posts/bolna-ai_activity-7516864461119467520-uNZa |
| Bolna's "one month away" post | Describes Symphony as "speaker panels, fireside chats, **a Buildathon for learners**, live demonstrations, product experiences, an awards night…" | https://www.linkedin.com/posts/bolna-ai_we-are-officially-only-a-month-away-from-activity-7518621798473863169-Pkh5 |
| Prateek Sachan public profile | Buildathon post plus 3 product posts (quoted in §3). No judges | https://www.linkedin.com/in/prateek-sachan |
| Voc-a-thon Luma (Bolna × Cartesia, Jun 13 2026) | Host Sonam Bala. No judges listed | https://luma.com/ubu85bxv |
| X (@bolna_dev, @xan_ps, @maitreya_wagh, @greybaker) | Blocked (402/451). Snippets show no judge names | https://x.com/bolna_dev |
| WebSearch: "Bolna buildathon judges / jury / mentors" | Nothing | n/a |
| Participant repos for this buildathon (gh code search) | Dadi's kit confirms "No published judging criteria" | https://github.com/jaygautam-creator/dadi/blob/main/docs/SUBMISSION.md |

**Precedent from Bolna's last hackathon:** a Voc-a-thon participant planned around "Judges are voice AI operators (Bolna + Cartesia teams)… They've seen every transactional bot (lead qual, support, reminders)". This is a participant's own belief, **not** an official statement ([Saheli spec](https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md)). The same team noted "the rubric penalizes going live with no fallback" ([Saheli SUBMISSION.md](https://github.com/KD-3/saheli-voice-shopping/blob/main/SUBMISSION.md)), and the form asked for a "novel application or real Indian problem" ([Saheli spec](https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md)).

---

## 2. Grey Baker: CONFIRMED ROLE (YC interviewer for the winner); PROBABLE finale juror [INFERRED]

**Role and background**
- General Partner at YC since **June 16, 2026**, after serving as a Visiting Partner ([YC blog](https://www.ycombinator.com/blog/chris-golda-and-grey-baker-general-partners)). He was announced as a Visiting Partner on Oct 14, 2025 (mirror of the YC post: https://startup-kit-arabic.lovable.app/news/meet-ycs-newest-visiting-partners-zbqfjf).
- Career ([YC profile](https://www.ycombinator.com/people/grey-baker); [YC blog](https://www.ycombinator.com/blog/chris-golda-and-grey-baker-general-partners)):
  - Co-founded **Dependabot**, a dev tool used by over a million people, acquired by GitHub in 2019.
  - Co-founded **Pincites** (YC S23), AI contract redlining inside Microsoft Word, acquired by Filevine.
  - Early employee at **GoCardless** (joined at 6 people, led product and engineering to 100+).
  - Cycled about 29,000 km around the world, then built Dependabot "as a side project".
  - MPhil in Economics from Cambridge, top of his year.
- Bolna's page calls him "previously … Director of Product at Figma" ([speakers](https://www.bolna.ai/symphony/speakers)). YC's bio leaves Figma out. His own June 2025 Hacker News comment says "PM at Figma here (for dev tools, not slides)" ([HN](https://news.ycombinator.com/item?id=44152221)), so a Figma dev-tools product role is consistent.
- Earlier he was a GitHub PM for secret scanning and push protection ([HN](https://news.ycombinator.com/item?id=35897726), [HN](https://news.ycombinator.com/item?id=34010158)). A podcast says he started at McKinsey and taught himself to code in 6 months ([IndieBites ep. 60](https://indiebites.com/60)).

**What he says publicly (themes)**
- **Bootstrapping, revenue, doing things that don't scale.** Dependabot grew to $14k MRR before the GitHub sale. The inflection point was distribution through the GitHub Marketplace ([IndieBites](https://indiebites.com/60)).
- **Side projects and learning by building.** "I've made big leaps forward in my skills by building (relatively large) side projects" ([HN, Dec 2024](https://news.ycombinator.com/item?id=42290253)).
- **Shipping small and honest.** In 2025 he built mentions.us solo, and said: "I don't think it will ever be a money spinner"; "I'd rather they use the service for free than not at all - I get valuable feedback… and the validation of having built something other people use" ([HN](https://news.ycombinator.com/item?id=43527768), [HN](https://news.ycombinator.com/item?id=43529860)).
- **Security and trust are reflexive for him.**
  - On MCP auth RCEs: "pretty surprised the MCP server auth process could pop a calculator on widely adopted clients… totally unnecessary unsafe" ([HN, Sep 2025](https://news.ycombinator.com/item?id=45349627)).
  - He praised the Next.js CVE disclosure process ([HN](https://news.ycombinator.com/item?id=43450165)).
  - On AI spam: "There are structural differences between spammy accounts and real ones, because their incentives are different" ([HN](https://news.ycombinator.com/item?id=35869397)).
- **Platform distribution and dev tools** run through his whole career: Dependabot, GitHub Advanced Security, Figma dev tools.
- **Vertical AI inside an existing workflow.** Pincites lived *inside* Word, and its acquirer had been its customer first ([LegalTech Monitor](https://www.legaltechmonitor.com/2025/12/exclusive-filevine-acquires-pincites-ai-powered-contract-redlining-company-strengthening-its-positioning-for-corporate-legal-and-enhancing-its-ai/)).
- **Gaps:**
  - I found no Lightcone episode or essay by Grey on voice AI. X was blocked.
  - No India-specific statements found.
  - He wrote none of the Fall 2026 RFS items ([YC RFS](https://www.ycombinator.com/rfs)).

**YC's current Requests for Startups that touch voice** ([YC RFS](https://www.ycombinator.com/rfs)):
- **"AI for the Aging Population"** (Max Kolysh): "Voice interfaces that can hold real conversations, monitoring that helps older adults stay safe and independent."
- **"Proving You're Human"** (Max Kolysh): "Voice clones and fake video calls are getting cheap and ultra-realistic, and fraud like this is exploding."
- **"The Primer"** (Andrew Miklas): adaptive tutoring for young children "at the quality of a devoted private tutor and at consumer scale". This matches Bolna's own example idea, "A voice tutor for kids" ([buildathon](https://www.bolna.ai/symphony/buildathon)).
- **"AI-Powered Consumer Products for 1 Billion People"** (Raphael Schaad).
- **"Self-Maintaining APIs"** (Harsha Gaddipati), and **"Multiplayer AI"** (Aaron Epstein) for agent sessions.

**YC on Bolna specifically**
- YC rejected Bolna several times. The feedback was "Indian enterprises are not going to pay, and you are not going to make money out of this" (Maitreya, [TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)).
- On the buildathon post Maitreya joked: "if this had existed earlier, we may have not needed 6 attempts" ([comment](https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU)).
- [INFERRED] So the YC objection to answer in an India voice pitch is **willingness to pay**.

**What would impress Grey [INFERRED]**
- Real users and money in the build window: calls handled, retention, a paying pilot, a letter of intent.
- A crisp "who pays and why now". Distribution through an existing channel: phone numbers, WhatsApp, an existing app's users.
- A solo or small team that ships fast, plus evidence the founders will keep going after the hackathon. It is a YC interview, so founder–market fit matters.
- Security and abuse thinking: consent, spoofing, prompt injection over voice, PII.

**Pet peeves [INFERRED from his record]**
- Unsafe defaults.
- Spammy growth.
- Hand-wavy TAM with no users.

---

## 3. Bolna founders: PROBABLE judges at every stage [INFERRED]

### Prateek Sachan, co-founder and CTO
- YC bio: "Building the Voice API infrastructure platform for India. Previously built and scaled Zomato, Tata 1MG, BrowserStack & Atlassian" ([YC](https://www.ycombinator.com/companies/bolna-ai)). LinkedIn headline: "Building Bolna (YC F25) | Ex-Zomato, BrowserStack | IIT Delhi"; 31K followers ([profile](https://www.linkedin.com/in/prateek-sachan)).
- Top contributor and PyPI author of the open-source `bolna` engine ([GitHub](https://github.com/bolna-ai/bolna/graphs/contributors)).
- **He personally posted the buildathon:** "Show your proof of work by making something people want" ([post](https://www.linkedin.com/posts/bolna-ai_activity-7516864461119467520-uNZa)). He also answered applicants' comments himself, e.g. fixing the expired Slack link ([same](https://www.linkedin.com/in/prateek-sachan)).

**Recent themes, all from https://www.linkedin.com/in/prateek-sachan, Oct 2026:**
- **"APIs are the product."** "The dashboard shouldn't be more powerful than the public APIs… if someone wants to build an entirely different product on top of your APIs and infrastructure, your abstractions cannot become their limitation."
- **Agents as the new builders.** "Everyone is a 'builder' now… these builders may never even interact with your amazing dashboards… But their AI agents definitely will… we're already seeing this with our MCP integrations and Ask Bolna."
- **"Developer experience is product design, and over time, product design eventually becomes your brand."** He wants platforms that "give builders, human or AI, the primitives to create things we never imagined."
- **Ask Bolna:** a chat interface that builds workflows. "The idea came out of our first internal demo day last month and went to production within the same week."
- **On-prem / self-hosted Bolna** with Docker/K8s on AWS, GCP, Azure or private servers.
- **His thesis:** "We don't believe a single foundational model can meet enterprise Voice AI needs. Our orchestration layer routes every call to the best-fit model" ([Bolna PR](https://www.bolna.ai/newsroom/bolna-bags-63-million-seed-funding-led-by-general-catalyst-to-build-indias-voice-ai-platform)).

**What would impress him [INFERRED]**
- Builds that use Bolna **programmatically**: API, MCP, webhooks, custom functions, the Web Call SDK, custom LLM endpoints.
- Builds that compose new products on Bolna's primitives, or build things for agents to drive Bolna.
- Infra-flavoured community work already gets featured. BolnaMonitor (provider-combo drift detection from `meta_info` latencies) was put on the Builders wall and re-published as a Bolna blog post ([blog](https://www.bolna.ai/blog/when-one-provider-combo-goes-down); [migration script](https://github.com/bolna-ai/blog/blob/main/scripts/migrate-builders.mjs)).

### Maitreya Wagh, co-founder and CEO
- IIT Delhi, ex-Bain, ex-Probo Founder's Office ([Bolna PR](https://www.bolna.ai/newsroom/bolna-ai-recognized-among-indias-most-promising-startups-in-yourstorys-tech30-2025)). LinkedIn headline: "Building Bolna | Forbes 30U30 | Bain | IIT Delhi" ([post](https://www.linkedin.com/posts/bolna-ai_activity-7518658155262865408-9dOx)). The Forbes listing is self-claimed; I didn't verify it against Forbes.

**Today's post (Oct 21) on LiD, Bolna's real-time language ID** ([post](https://www.linkedin.com/posts/bolna-ai_activity-7518658155262865408-9dOx)):
- "ASR Models have different Word Error Rates for each language, and even within a language… there is a model great at handling short utterances, another for medical terms, and a third when the conversation has a lot of numbers involved."
- "TTS models are trained on voice actors, who are fluent in 1, 2, maybe 3 languages."
- The v1 "was too expensive, kept ping-ponging between languages, and often sounded clunky". The fix came from fine-tuning on "50M minutes of call data".

**Other statements**
- Bolna's companion post says: "We're at home in English on calls with colleagues, immediately switch to Kannada… Tamil on a call back home… sometimes all of them on the same call" ([post](https://www.linkedin.com/posts/bolna-ai_india-loves-to-talk-and-even-more-so-in-activity-7518647097676427264-481p)).
- "What is still stopping them from going from pure demo to POC to pilot to live is the quality of the voice AI calling itself" ([Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)).
- He flags hard spots: Bangla, Assamese and other languages where "low-latency, enterprise-grade models remain scarce"; noise cancellation; "long addresses, location names and pin codes" ([Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)).
- Cost sensitivity: "In India, every rupee matters. Voice AI must be engineered for efficiency" ([Launch YC](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india)).
- "90%+ of business–customer conversations can already be handled by Voice AI today" ([GC story](https://www.generalcatalyst.com/stories/seeding-the-future-with-bolna)).
- Recruiting is an early wedge. A podcast covered Bolna saving recruiters "up to 80% of their time" on screening calls ([Future-Proofed](https://www.youtube.com/watch?v=s4WgH5Y5tfg)).

**What would impress him [INFERRED]**
- Builds that are good at the *Indian* hard parts: code-switching mid-call, numbers and addresses, dialects beyond Hindi, noisy lines.
- Cost per call stated in rupees.
- A clear path from demo to pilot to live, plus the YC angle: proof someone will pay.

### Other Bolna staff likely on the shortlist and interview panel: POSSIBLE [INFERRED]
- **Siddharth Batra, Head of Product.** Headline "Head of Product at Bolna (YC F25)" ([LinkedIn](https://in.linkedin.com/in/siddharthbatra)). Bolna's LiD post calls him "our Head of Product" ([post](https://www.linkedin.com/posts/bolna-ai_india-loves-to-talk-and-even-more-so-in-activity-7518647097676427264-481p)). One search snippet attributes the "jury and 500+ attendees" line to his or Vaibhav Sharma's LinkedIn (unverified). [INFERRED] He'll care about product thinking: the end-user flow, failure handling, and the reason it has to be voice.
- **Tanisha Sharma** and **Sharath (Kuntanahal)** are tagged on both buildathon launch posts ([Bolna post](https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU); [Prateek post](https://www.linkedin.com/in/prateek-sachan)). [INFERRED] They are likely running buildathon operations or marketing. I couldn't fetch their roles (LinkedIn 999).
- **Sonam Bala** was the host of the Bolna × Cartesia Voc-a-thon ([Luma](https://luma.com/ubu85bxv)). She is also tagged on the LiD post. [INFERRED] Likely community/events.
- **Vaibhav Sharma** (Bolna YC F25) posted the buildathon and sponsor-credit details, per search snippets ([LinkedIn](https://www.linkedin.com/in/vaibhav-sharma-9305b7232/), unverified). His role is unknown.
- **Rohit Sai** (Bolna YC F25) appears in search results next to the Voc-a-thon ([LinkedIn](https://www.linkedin.com/in/iamrohitsai/), unverified). Role unknown.
- Engineers repeatedly tagged on product launches: Prabal (built Ask Bolna), Sanket, Puneet, Rishav, Swarakesh, Tanishq ([LiD post](https://www.linkedin.com/posts/bolna-ai_activity-7518658155262865408-9dOx)). [INFERRED] They may do technical screening.

---

## 4. Investor speakers: PROBABLE to POSSIBLE finale jurors [INFERRED]

### Akarsh Shrivastava, Partner, General Catalyst: PROBABLE
- Speaker ([speakers](https://www.bolna.ai/symphony/speakers)). IIT Delhi civil engineering and IIM-A. Previously ran the SaaS/AI/B2B practice at Elevation Capital and spent 3 years at McKinsey ([GC bio](https://www.generalcatalyst.com/team/akarsh-shrivastava)).
- **He is on Bolna's lead investor's deal team.** He co-authored GC's "Seeding the Future with Bolna" ([GC](https://www.generalcatalyst.com/stories/seeding-the-future-with-bolna)).
- What he said about Bolna: "Bolna allows you the freedom to choose any model and has a stack behind it to mold it according to your requirement… for people who want to own some part of the stack, want flexibility in model picking" ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)).
- [INFERRED] He'll look for a B2B buyer, a wedge into enterprise, and a defensible workflow. GC also lists defence and government as his areas.

### Aarthi Ramamurthy, founder and GP, Schema Ventures: PROBABLE (she is a Bolna angel)
- She was an angel in Bolna's seed round ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/); [Inc42](https://inc42.com/buzz/voice-ai-startup-bolna-raises-inr-57-cr-to-deepen-tech-stack/)). Symphony speaker; ex-Meta, Microsoft and Netflix; built and exited YC-backed startups; co-host of the Aarthi and Sriram Show ([speakers](https://www.bolna.ai/symphony/speakers)).
- Schema's thesis is to back "exceptional outsider founders" building from **lived experience** rather than "pedigree or proximity". She funds contrarian founders "because they're actually doing something that's a personal problem for them" ([Fortune](https://www.fortune.com/2025/05/20/aarthi-ramamurthy-schema-ventures-20-million-fund)).
- Sectors: industrial software, robotics, factories, construction, logistics, workflow intelligence, dev tools ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/aarthi-ramamurthy-launches-usd-20-mn-schema-ventures-to/492043)).
- [INFERRED] She will reward a founder's personal story with the problem, and unglamorous industrial or logistics uses of voice.

### Prasanna Krishnamoorthy, Managing Partner, Upekkha: POSSIBLE
- Upekkha is an accelerator for "Indian B2B and vertical AI startups building for global markets". He is a founding volunteer at AIBoomi (ex-SaaSBoomi) and spent "more than a decade helping founders build sustainable, revenue-led businesses" ([speakers](https://www.bolna.ai/symphony/speakers)).
- Upekkha believes "India will become the use case capital of the world in AI" and has done 50+ pre-seed AI deals in 18 months ([CXOToday](https://cxotoday.com/corner-office/from-vanilla-saas-to-vertical-ai-how-upekkha-is-shaping-the-future-of-b2b-startups-1/)).
- [INFERRED] He wants a vertical, a paying customer, and global potential, with revenue discipline over vanity metrics.

### Tanuj Bhojwani, ex-Head of People+AI, now at South Park Commons: POSSIBLE
- Ex-head of People+AI (EkStep), iSPIRT policy, and co-author of *The Art of Bitfulness* with Nandan Nilekani ([speakers](https://www.bolna.ai/symphony/speakers)).
- People+AI looks for "population-scale applications of AI that are relevant to large problems in India" ([search summary of Forbes India / People+AI coverage](https://el.player.fm/series/forbes-india-the-startup-fridays-podcast/startup-fridays-s5-ep5-ai-for-india-how-peopleai-was-born)).
- [INFERRED] He rewards public-good, population-scale and open-protocol thinking.

### Sanjay Jain, Director of DPI, Gates Foundation: POSSIBLE (lower)
- Helped build India Stack, ex-Chief Product Manager at UIDAI (Aadhaar), led Google Map Maker ([speakers](https://www.bolna.ai/symphony/speakers)).
- At Symphony he will speak about the Gates coalition of 60 organisations working to help "3.4 billion people use AI in their own language and voice" ([Bolna post](https://www.linkedin.com/posts/bolna-ai_gates-foundation-joins-the-symphony-stage-activity-7517926268659757057--suL); [YourStory](https://yourstory.com/ai-story/gates-foundation-ai-push-google-microsoft-anthropic)).
- [INFERRED] He'll favour low-resource languages, inclusion and DPI-style interoperability.

---

## 5. Sponsor-side people: POSSIBLE jurors; their stated wants shape scoring [INFERRED]

The buildathon sponsors are Plivo, Exotel, Sarvam, Cartesia, Deepgram and Kalpa Labs ([Bolna post](https://www.linkedin.com/posts/bolna-ai_this-could-be-your-best-shot-at-a-direct-activity-7516469372245331968-TVjU)).

Summit tiers ([Symphony](https://www.bolna.ai/symphony)):
- Diamond: Google Cloud, Truecaller for Business, Exotel, Plivo
- Gold: Kalpa, Sarvam
- Silver: Wispr Flow, Simplismart, Cartesia, Deepgram, Vobiz
- Associates: Smallest.ai, Agnost AI

### Sachin Bhatia, co-founder and Chief Growth Officer, Exotel: POSSIBLE
- Symphony speaker. Previously co-founded Ameyo (merged into Exotel); IIT Guwahati ([speakers](https://www.bolna.ai/symphony/speakers)).
- His views:
  - Models are commoditising: "Models eventually will be like electricity… It doesn't matter if you're buying it from company A or company B."
  - India needs "frontier-minus-one" models for the unit economics.
  - The bot-first, human-as-backup model is "fundamentally flawed". Exotel's "Harmony" has one human supervising many bots.
  - "When you listen, you don't need to ask": conversation intelligence over NPS.
  - Exotel's AgentStream is a full-duplex websocket platform delivering audio in frames under 20 ms.
  - Source for all of the above: search summary of his "Front Page" interview, via [Exotel newsroom](https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/). I read it as a search summary only, not the full transcript.
- [INFERRED] He rewards a human-in-the-loop design, real telephony, and analytics on the conversation.

### Anuja Dhawan, AI Products & Growth at Exotel; co-founder of Dubverse: POSSIBLE
- Symphony speaker ([speakers](https://www.bolna.ai/symphony/speakers)). Exotel acqui-hired Dubverse in April 2026. She leads **Conversation Quality Analytics (CQA)** ([Business Today](https://www.businesstoday.in/amp/technology/story/exotel-acqui-hires-dubverse-to-boost-ai-led-customer-experience-play-524631-2026-04-08); [Exotel](https://exotel.com/newsroom/exotel-acqui-hires-dubverse-voice-ai-team/)).
- [INFERRED] She'll reward measurable call-quality and evaluation work, and multilingual or dubbing expertise.

### Prashant Shishodia, co-founder and CEO, Kalpa Labs (YC F25): POSSIBLE
- Symphony speaker. Previously led full-stack ML for Google Assistant NL; IIT Kharagpur ([speakers](https://www.bolna.ai/symphony/speakers)).
- Kalpa is building one "generalist speech model" covering STT, TTS, cloning and speech reasoning, "steerable via system prompts and audio examples".
- Kalpa's public asks: "**speech use cases current models fail at**", feedback from production speech systems, and early-access pilots ([YC](https://www.ycombinator.com/companies/kalpa-labs)).
- [INFERRED] He'll favour builds that show *why* today's pipelines fail: emotion, context, cross-task. Using Kalpa's API for something a cascaded STT→LLM→TTS stack can't do would stand out.

### Sarvam (Gold sponsor; no Sarvam person on the speaker list): POSSIBLE for a juror slot
- Recent Sarvam hackathon signal: at Sarvam BuildIn' Hours (Aug 9 2026, 100 picked from 6,272 applicants), the judge Arsh Goyal said "ideas… were solving real problems of Bharat" ([substack](https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon)).
- Winners there: MSME tender discovery, Indic storytelling for kids, and **Setu**, a communication tool for non-verbal people ([same](https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon)).
- [INFERRED] Sarvam rewards Bharat-first, Indic-language, accessibility and education ideas.

### Plivo (Diamond sponsor): POSSIBLE
- Likely face: **Ayush Anand, Head of Product – Voice AI**, who speaks on "building Voice AI that works in production" ([search result](https://in.linkedin.com/in/ayanand)).
- Plivo's India push: lower domestic call rates (₹0.19 per 30 s from Aug 15 2026), a no-code "Vibe Agent" builder, and powering Amul's **Sarlaben** agent for 36 lakh Gujarati farmers (search summary; [Plivo](https://plivo.com/campaigns/vapi-vs-plivo)).
- [INFERRED] Plivo rewards real PSTN numbers, production reliability and scale.

### Cartesia and Deepgram (Silver sponsors): POSSIBLE but less likely to sit on the jury
- Cartesia markets Hinglish-native Sonic voices, time-to-first-audio "as low as 40ms", and India data centres ([Cartesia India](https://www.cartesia.ai/india)).
- Cartesia co-ran the June Voc-a-thon with Bolna ([Luma](https://luma.com/ubu85bxv)).
- Deepgram has added Hindi to Nova-3 variants ([Deepgram changelog](https://developers.deepgram.com/changelog/2026/4/30.md)).
- [INFERRED] For both: expressive, low-latency voice that matters to the product, and good speech recognition on Indian accents.

### Sudarshan Kamath, co-founder and CEO, Smallest.ai (Associate sponsor): POSSIBLE
- Builds real-time voice models and agents; IIT Guwahati ([speakers](https://www.bolna.ai/symphony/speakers)).
- [INFERRED] Cares about latency and speed.

---

## 6. Operator and tech speakers: POSSIBLE (lower)

- **Madhav Krishna, CEO, Vahan.ai.** Runs a voice-first AI recruiter for blue-collar workers ([speakers](https://www.bolna.ai/symphony/speakers)). Vahan reports about 40k placements a month and "80-90% of the recruitment process is handled by AI" ([NITI Frontier Tech](https://frontiertech.niti.gov.in/story/voice-ai-at-scale-powering-half-a-million-jobs-a-year-in-india/), via search summary). [INFERRED] He'll favour blue-collar or field-worker voice use cases, which match Bolna's "drivers or field workers" example.
- **Srinivas Narayanan, ex-CTO B2B Applications, OpenAI.** Scaled ChatGPT and the API; advised AI startups at GC ([speakers](https://www.bolna.ai/symphony/speakers)). [INFERRED] He'll look for engineering depth and scale.
- **Dr. Manish Gupta, Senior Director, Google DeepMind** (India and Japan research) ([speakers](https://www.bolna.ai/symphony/speakers)). [INFERRED] He'll care about research novelty and Indic language AI.
- **Shrikant Venkataramani, AI Research, Pocket FM.** Works on SAGA, an agentic script-to-audio pipeline; ex-Murf and Amazon ([speakers](https://www.bolna.ai/symphony/speakers)). [INFERRED] He'll favour generative audio and speech enhancement.

---

## 7. Likelihood table [INFERRED unless a source is cited]

| Person | Shortlist + interview (Nov 3–7) | Finale jury (Nov 20) | Basis |
|---|---|---|---|
| Prateek Sachan (CTO) | **Very likely** | **Very likely** | Posted and answers buildathon comments himself ([profile](https://www.linkedin.com/in/prateek-sachan)) |
| Maitreya Wagh (CEO) | Likely | **Very likely** | Tagged on all buildathon posts; YC-story owner ("6 attempts") |
| Siddharth Batra (Head of Product) | Likely | Possible | Head of Product; jury quote attributed to his/Vaibhav's LinkedIn (unverified) |
| Tanisha / Sharath / Sonam / Vaibhav (Bolna) | Likely (screening, ops) | Unlikely | Tagged on posts; Sonam hosted the Voc-a-thon |
| **Grey Baker (YC)** | Unlikely | **Probable** headline juror | Prize is his interview; Symphony speaker. Not named as judge |
| Akarsh Shrivastava (GC) | No | Probable | Bolna's lead-investor deal team; speaker |
| Aarthi Ramamurthy (Schema) | No | Probable | Bolna angel; speaker |
| Prashant Shishodia (Kalpa) | No | Possible | Sponsor CEO; speaker |
| Sachin Bhatia / Anuja Dhawan (Exotel) | No | Possible | Diamond sponsor; speakers |
| Prasanna Krishnamoorthy (Upekkha) | No | Possible | Accelerator MP; speaker |
| Sarvam / Plivo / Cartesia / Deepgram reps | No | Possible (one sponsor seat) | Sponsors; no named speaker except Plivo's likely product lead |
| Tanuj Bhojwani, Sanjay Jain, Madhav Krishna, Sudarshan Kamath | No | Lower | Speakers |

---

## 8. What attracts this panel: themes they reward

### Themes they repeatedly reward
1. **"Make something people want" with proof of work.** This is Prateek's framing of the buildathon, and YC's motto. Show real calls, real users, retention, or a paying pilot from the Oct 15–31 window. That also answers the "Indian enterprises won't pay" objection YC gave Bolna ([TechCrunch](https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/)). It matters most to Grey, Maitreya and Prasanna.
2. **Solving the hard Indian voice problems instead of avoiding them.** Bolna's founders talk about these constantly ([LiD post](https://www.linkedin.com/posts/bolna-ai_activity-7518658155262865408-9dOx); [Inc42](https://inc42.com/startups/how-bolna-ai-is-helping-enterprises-to-win-the-voice-ai-race/)):
   - mid-call code-switching
   - numbers, addresses and pin codes
   - noisy lines
   - languages beyond Hindi, such as Bangla or Assamese

   Bolna shipped LiD on Oct 21. [INFERRED] Using it visibly, and showing where it helps, is a direct compliment to the team.
3. **API-first composition on Bolna's primitives.** For example API, MCP, custom functions, webhooks, the Web Call SDK, and building for *agents* as users. Prateek: "APIs are the product" ([profile](https://www.linkedin.com/in/prateek-sachan)). BolnaMonitor-style infra builds get featured ([blog](https://www.bolna.ai/blog/when-one-provider-combo-goes-down)).
4. **Unit economics in rupees.** "Every rupee matters" ([Launch YC](https://www.ycombinator.com/launches/OVc-bolna-voice-ai-for-india)). Exotel's "frontier-minus-one" view points the same way. Show cost per call or minute, and route cheaper models where quality allows.
5. **Bharat or population-scale impact, plus a buyer.**
   - Sarvam, People+AI and the Gates DPI speakers reward real problems of Bharat, accessibility and Indic languages ([Sarvam BuildIn'](https://blrxzo.substack.com/p/1-in-62-made-it-in-sarvam-ais-hackathon)).
   - GC and Upekkha want a B2B buyer.
   - [INFERRED] Winning pitches pair the two: an impact story *and* a named payer such as a bank, telco, logistics firm, hospital or school chain.
6. **Things YC is asking for right now** ([YC RFS](https://www.ycombinator.com/rfs)):
   - voice companions and monitoring for older adults
   - anti-voice-clone or anti-fraud tools ("Proving You're Human")
   - kids' tutors (The Primer)
   - consumer AI for a billion people
7. **A human in the loop and conversation intelligence.** Exotel's Harmony and CQA work ([search summary via Exotel](https://exotel.com/newsroom/exotel-launches-indias-first-agent-streaming-platform-for-voice-ai/); [Business Today](https://www.businesstoday.in/amp/technology/story/exotel-acqui-hires-dubverse-to-boost-ai-led-customer-experience-play-524631-2026-04-08)) show that escalation design and call analytics score with telephony sponsors.
8. **Lived-experience founders.** Aarthi's Schema thesis ([Fortune](https://www.fortune.com/2025/05/20/aarthi-ramamurthy-schema-ventures-20-million-fund)), plus YC's founder–market-fit lens. Say why *you* are the person to build this.
9. **A demo the judge can join** [INFERRED from past Bolna-adjacent builds]. Let a juror phone the agent, play the adversary, or watch a live dashboard. Always keep a recorded backup: the earlier rubric "penalizes going live with no fallback" ([Saheli](https://github.com/KD-3/saheli-voice-shopping/blob/main/SUBMISSION.md)).

### Red flags to avoid
- **A generic transactional bot** (lead qualification, support FAQ, reminders) with no twist. Voice-infra judges have "seen every transactional bot" ([Saheli spec](https://github.com/KD-3/saheli-voice-shopping/blob/main/SAHELI_SPEC.md), participant view).
- **Saturated categories without a sharp angle:** farmer advisory, government form-filling, loan collections. Several of these are already in this buildathon (prior research: `ideas_india_hackathons.md` in this scratchpad).
- **"Multilingual" that falls apart on real code-switching.** Bolna's founders call this out explicitly ([LiD post](https://www.linkedin.com/posts/bolna-ai_activity-7518658155262865408-9dOx)).
- **Fake or unclear metrics.** Projections with no real calls behind them. YC and Grey's track record both value honest early numbers ([HN](https://news.ycombinator.com/item?id=43527768)).
- **Unsafe voice agents** [INFERRED, Grey's security background]: no consent, no anti-spoofing, PII leaks, prompt injection over the phone line, cloned voices without safeguards.
- **A UI-only product where voice is bolted on**, when the brief is "give it a voice". Bolna asks "where does voice AI come in?" on the form ([buildathon JS](https://www.bolna.ai/symphony/buildathon/assets/routes-BiW03H66.js)).
- **Ignoring Bolna.** The rules don't require Bolna, but its CTO and CEO are the near-certain screeners [INFERRED]. A build that skips Bolna for a competitor's stack gives up the easiest points.
- **A pitch that is all tech and no buyer.** That fails the YC and investor half of the panel. All business and no live working call fails the Bolna and sponsor half.

---

## 9. Gaps and caveats
- **No judge names exist publicly** as of 2026-10-21. Every judge assignment above is inference.
- **Watch for an announcement** in the Bolna Builders Slack, on @bolna_dev, and on the Bolna LinkedIn company page closer to Nov 3 or Nov 8.
- **"Jury + top 10 pitch"** comes only from an unverified search snippet and conflicts with the official "top 3 pitch" copy.
- **Symphony "hackathon"**: the summit page lists a separate in-person "hackathon" at Abhyas alongside the buildathon ([Symphony](https://www.bolna.ai/symphony)). Its format and judges are unknown.
- **Unverified pages:** I couldn't read Maitreya's, Siddharth's, Tanisha's, Sharath's, Vaibhav's or Grey's LinkedIn/X timelines (blocked). Quotes from them come only from public post pages or press.
- **Exotel quotes** (Sachin Bhatia) are taken from a search-engine summary of the interview, not a transcript.
- **Figma title:** Bolna says Grey was "Director of Product at Figma". His HN comment confirms a Figma PM role for dev tools; I didn't confirm the exact title.
