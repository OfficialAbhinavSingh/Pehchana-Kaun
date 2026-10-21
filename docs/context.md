# Context: the buildathon, the judges, the sponsors

Condensed from `docs/research/` (researched 2026-10-21; every claim there has a
source link). **Confirmed** = read on an official page. **Likely** = inferred or
second-hand. Re-check anything marked likely before relying on it.

## The buildathon

| | |
|---|---|
| Page | https://www.bolna.ai/symphony/buildathon |
| Theme | "Build anything. Just make it talk." No tracks; voice must be part of it. **Confirmed** |
| Format | Online build. Only the top 3 travel to Bengaluru (travel paid). **Confirmed** |
| Team | 1 to 4 people. We are 3. **Confirmed** |
| Submit | **31 Oct 2026**, time zone not stated (assume IST and submit early). **Confirmed** date |
| Submission form | project name, description of **200 characters max**, a link (repo / live app / demo), a deck or video link (**Google Drive or Luma only**). **Confirmed** in the site's `/submit` route, see `research/04-judges.md` |
| Shortlist | 3 Nov (email). Interviews 5 to 7 Nov. Finalists 8 Nov (top 10 get Symphony tickets). Finale 20 Nov, Abhyas Hall, The Lalit Ashok, Bengaluru. **Confirmed** |
| Prizes | 1st Rs 50,000 + YC interview with Grey Baker (YC General Partner); 2nd Rs 40,000; 3rd Rs 30,000. **Confirmed** |
| Credits | $10 Bolna credit per team plus a credits request form (more Bolna + one or two partners). **Confirmed** |
| Judging rubric | **Not published.** Likely screened by Bolna's founders. |
| Community | Bolna Builders Slack (invite link in `research/01-hackathon.md`) |

## Who is probably judging (none officially named yet)

- **Shortlist & interviews:** Bolna CTO Prateek Sachan, CEO Maitreya Wagh, Head of
  Product Siddharth Batra. Prateek's framing of the buildathon: *"Show your proof of
  work by making something people want."* **Likely**
- **Finale:** founders + Grey Baker (YC) + Bolna's investors who speak at Symphony
  (Akarsh Shrivastava, General Catalyst; Aarthi Ramamurthy, Schema Ventures) + maybe a
  sponsor seat (Kalpa's Prashant Shishodia, Exotel's Sachin Bhatia). **Likely**

What this panel rewards (research/04-judges.md):
1. Real usage numbers from before the deadline, not projections.
2. Hard Indian voice problems: code-switching, numbers, noisy lines, non-Hindi languages.
3. Built on Bolna's stack (API, functions, webhooks, web call). Bolna just shipped
   mid-call language switching (LiD, 21 Oct).
4. Cost per call in rupees; a named buyer; a fit with a YC request for startups
   ("Proving You're Human" is the closest).
5. A demo judges can take part in, plus a recorded backup.

Red flags: generic transactional bots, "multilingual" claims that break on real
Hinglish, unsafe agents (no consent, PII leaks), skipping Bolna.

## Sponsors and why each one is load-bearing for us

| Sponsor | Their hero capability | Our use |
|---|---|---|
| **Kalpa Labs** (YC F25) | Conversation-aware TTS, Hinglish, top realism score; coined the "Turing Clock" | AI arm; we publicly build their proposed metric (credit them) |
| **Cartesia** | Sonic 3.6, Hinglish, voice cloning, emotion | AI arm |
| **Sarvam** | 22-language STT, Indian voices (Bulbul) | AI arm; non-Hindi languages |
| **Deepgram** | Nova-3 multilingual, Flux turn-taking | Turn-taking inside agents; post-call transcription of every call |
| **Plivo** | Bolna's default telephony, cheap India minutes, session recording | Public game number, routing, stereo recording |
| **Exotel** | ~40% of India's voice-AI calls, bot/human handoff | Alternative telephony (trial only calls 10 whitelisted numbers) |

## Competition (as of 21 Oct)

- **No one** in the buildathon or Bolna community is building a human-vs-AI phone game
  (16 buildathon repos + 163 Bolna-related repos scanned; research/11).
- Taken ideas we avoided: scam honeypot (Dadi), supplier bargaining (Bhaav), loan
  collections (Chukta), interpreter, tutors, clinic/legal/farmer helplines.
- Closest prior art (research/10): Kalpa's Turing Clock (proposal only, no product),
  an ICLR 2026 speech Turing test (recorded clips, Chinese/English, no phone), AI21's
  text "Human or Not" (2023), TTS clip arenas. Nobody combines a real phone line, a live
  human control, time-to-detection and Indian languages.
- Re-check rivals around **28 to 30 Oct** (two buildathon repos were still empty).

## Risks we already know

1. Ranking sponsors against each other. Default to `REVEAL_VENDORS=false` and lead
   with *language gaps*, not vendor losers.
2. Indian phone numbers may need DLT / company paperwork. Day 1 blocker; fallback is
   the web-call SDK (AI arms only).
3. Human arm needs volunteers on shift. Schedule "live hours".
4. Consent + India's DPDP Act. See ethics.md.
5. Kalpa, Josh Talks / AI4Bharat or Artificial Analysis could ship something similar.
   Launch publicly by **26 Oct**.
