# Bolna "Symphony Buildathon": research notes

Researched 2026-10-21. Read-only: the apply form was not submitted and nothing was logged into.
Main page: https://www.bolna.ai/symphony/buildathon (B). Some FAQ answers and form details are hidden in the page HTML, so I took them from the page's own JS bundle, https://www.bolna.ai/symphony/buildathon/assets/routes-BiW03H66.js (B-JS). The parent event page is https://www.bolna.ai/symphony (S).

---

## 1. What "Symphony" is

- **Symphony 2026** is Bolna's "India's flagship Voice AI summit". It runs one day: **Fri 20 Nov 2026 at The Lalit Ashok, Bengaluru**. Source: https://www.bolna.ai/symphony
- The page claims 1000+ attendees, 42+ speakers and 3 stages. Source: https://www.bolna.ai/symphony
- The three halls have Hindi/Urdu music names. Source: https://www.bolna.ai/symphony
  - **Sur** (Kalinga Hall) is the main stage for keynotes, product launches and awards.
  - **Abhyas** (Grand Ballroom) is "the build stage of Symphony, home to the buildathon and hackathon". *Abhyas* means practice. **The buildathon finale happens here.**
  - **Mehfil** (Siddhartha Hall) is the expo zone.
- The summit ticket includes "Full access to the summit, plus $100 in Bolna credits, a free 3-month Wispr Flow subscription and 2,500 in Sarvam credits", plus lunch. Source: https://www.bolna.ai/symphony (FAQ)
- Contact email: symphony@bolna.ai. Source: https://www.bolna.ai/symphony
- **The "Buildathon"** is Bolna's online voice-AI build competition, attached to Symphony. Page title: "Buildathon by Bolna: Build with voice at Symphony". OG title: "Bolna Buildathon: Build anything with voice". Source: https://www.bolna.ai/symphony/buildathon
  - The page brands it "Y Combinator × Symphony" and "Path to YC". Source: https://www.bolna.ai/symphony/buildathon
  - Builders on X call it the "Bolna × Y Combinator Buildathon". Source: https://x.com/I_codefullstack/status/2111291682159538455 (search snippet only; X returned HTTP 402)
- **Organizer: Bolna.** Bolna is a voice-AI orchestration platform for Indian enterprises. It is in YC's Fall 2025 batch (YC F25) and raised a $6.3M seed led by General Catalyst. Sources: https://www.ycombinator.com/companies/bolna-ai, https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/
- The page is a Lovable app (`buildathon.bolna-ai.lovable.app`) served under bolna.ai. Its asset timestamps run from 2026-10-13 to 2026-10-14. Source: B-JS
  - [INFERRED] So the page went live around Oct 13–15, 2026.

## 2. Theme, tracks, problem statements

- **Theme:** "Bring any idea. Give it a voice." The page says "Build whatever you like, as long as voice is part of it. A new product, or a voice feature on something you've already built." Source: https://www.bolna.ai/symphony/buildathon
- **There are no tracks.** The page says "Build anything. Just make it talk. No tracks. Bring any idea, as long as it has a voice component." The nav section is labelled "What to Build" (anchor `#tracks`). Sources: https://www.bolna.ai/symphony/buildathon, https://www.bolna.ai/symphony/buildathon/assets/SiteChrome-CBX_uOHj.js
- **Example ideas** (from https://www.bolna.ai/symphony/buildathon):
  1. A voice tutor for kids
  2. A phone helpdesk for a local clinic
  3. A voice layer on an app you already built
  4. A hands-free tool for drivers or field workers
- **Allowed builds (FAQ):** "Anything with voice in it: a new product, a voice feature on an existing one, or something in between." Source: B-JS
- **Required stack / Bolna APIs:** not found. Nothing on the page says you must use Bolna's API or any particular sponsor.
  - [INFERRED] Using Bolna plus the sponsor stack (Plivo/Exotel telephony, Sarvam/Cartesia/Deepgram/Kalpa speech) would probably help with judges, but the page does not require it.
  - Existing projects are explicitly allowed ("a voice feature on something you've already built"), and the form asks "Since when have you been working on this idea?". So pre-existing work looks fine. Source: https://www.bolna.ai/symphony/buildathon

## 3. Eligibility, team size, format, venue

- **Who can apply:** "Students, professionals and indie builders — anyone who wants to build with voice." Source: https://www.bolna.ai/symphony/buildathon (FAQ)
- **Geography or age limits:** none stated.
- **Team size:** "You can apply solo, or as a team of up to 4 people." The form dropdown offers "Just me", 2, 3, 4. Sources: B-JS, https://www.bolna.ai/symphony/buildathon
- **Format:** "No, it's fully virtual. Only the top 3 teams come to Abhyas Hall, The Lalit Ashok, Bengaluru on 20th Nov to present at Symphony, and we cover their travel." The page also says "Build from anywhere". Sources: B-JS (FAQ), https://www.bolna.ai/symphony/buildathon
- **Finale venue:** Abhyas Hall (Grand Ballroom), The Lalit Ashok, Bengaluru, 20 Nov 2026, during Symphony. Sources: https://www.bolna.ai/symphony/buildathon, https://www.bolna.ai/symphony

## 4. Dates (all 2026)

All rows below come from the "How it works" section of https://www.bolna.ai/symphony/buildathon.

| Step | Date | Detail |
|---|---|---|
| 01 Apply & Build | Oct 15 – 31 | "Register and start building your idea." |
| 02 Submit | **Oct 31** | "Deadline to submit your project." |
| 03 Shortlist | Nov 3 | "Selected teams get an interview invite by email." |
| 04 Interview | Nov 5 – 7 | "Interviews with selected teams." |
| 05 Results | Nov 8 | "Finalists announced. Top 10 win free Symphony tickets." |
| 06 Grand Finale | Nov 20 | "Top 3 pitch to the crowd at Abhyas Hall." |

- The hero banner says "Oct 15 – Nov 20, 2026". The "Path to YC" block says "Build something real with voice AI over five weeks". Source: https://www.bolna.ai/symphony/buildathon
  - [INFERRED] "Five weeks" means Oct 15 to Nov 20 overall. The actual build/submit window is **Oct 15–31**.
  - As of today (Oct 21) there are **about 10 days left before the Oct 31 submit deadline**.
- **Separate application deadline vs project submission:** not found. The site only lists "Oct 31 Submit".
  - [INFERRED] The apply form is the registration step. The page does not show how the project itself gets submitted (see section 7).
- **Time zone for the deadline:** not found.

## 5. Prizes, perks, opportunities

- **Total:** "₹1.2 lakh in cash for the top three teams. The winner gets a shot at Y Combinator." Source: https://www.bolna.ai/symphony/buildathon
- **Prizes by place** (from https://www.bolna.ai/symphony/buildathon):
  - **1st:** ₹50,000 + a YC interview. "Interview with Grey Baker, YC Partner. Travel covered, and more."
  - **2nd:** ₹40,000. "Cash, goodies and travel covered. Pitch on the Abhyas stage."
  - **3rd:** ₹30,000. "Cash, goodies and travel covered. Pitch on the Abhyas stage."
- **Path to YC:** "The winning team gets an interview with YC... If you win, you take it straight to a YC interview." Step 03 reads "The winner: Interviews with Grey Baker, YC Partner". Source: https://www.bolna.ai/symphony/buildathon
  - A search-engine snippet words this as "a direct interview with Grey Baker for the next YC Batch". Source: search results citing LinkedIn/X; not verified on a fetched page.
  - **Grey Baker** is a Partner at Y Combinator, previously Director of Product at Figma, and co-founder of Dependabot. He is also a Symphony speaker. Source: https://www.bolna.ai/symphony/speakers
- **Top 10 teams** get free Symphony tickets. The FAQ says "The top 10 teams get free tickets to Symphony." Sources: B-JS, https://www.bolna.ai/symphony/buildathon
- **Travel** is covered for the top 3 teams. FAQ: "Yes. We'll cover travel for the top 3 teams." Source: B-JS
- **Credits for all participants:** NOT on the current page. Search-engine snippets (apparently from LinkedIn posts by Bolna staff) say "Every builder gets credits from the buildathon sponsors Plivo, Exotel, Sarvam, Cartesia, Deepgram and Kalpa Labs (YC F25)". They also mention "cash prizes, free tickets to Symphony, goodies, and lots of credits from the partners". Source: WebSearch snippets pointing at https://www.linkedin.com/in/vaibhav-sharma-9305b7232/ and https://www.linkedin.com/in/siddharthbatra/ (LinkedIn returned HTTP 999, so **UNVERIFIED**)
- **Job/internship offers:** not found.

## 6. Judging criteria and selection

- **Judging rubric:** not found. There is no rubric on the page or in its JS bundle; I searched for "judg", "criteria" and "rule".
- **Selection process (FAQ):** "We review every application and shortlist the strongest builds. Selected teams will hear from us by email." Source: B-JS
- **Stages:** shortlist (Nov 3), then interviews (Nov 5–7), then finalists announced (Nov 8; top 10 get tickets), then the top 3 pitch live (Nov 20). Source: https://www.bolna.ai/symphony/buildathon
- **Who decides the final placing:** not stated.
  - [INFERRED] It is probably Bolna, with Grey Baker or other Symphony speakers as finale judges. This is not confirmed.
- **Named judges/mentors:** not found. Only Grey Baker is named, and only as the YC interviewer.

## 7. Rules and submission requirements

- **Written rules, T&Cs, IP or originality policy:** not found.
- **Submission format** (demo video, repo, deck, live link): not found on the page.
  - [INFERRED] Details will probably come by email or in Slack after you apply.
- **Community:** the "Bolna Builders" Slack, https://join.slack.com/t/bolnabuilders/shared_invite/zt-4dg50suac-narQNDvQ9zKgC7aR2VdS3w. After you apply, the page says "Join the Bolna Builders Slack to meet other teams, find teammates and get updates." Source: B-JS

## 8. Apply form fields (read from the page and B-JS; NOT submitted)

Anchor: https://www.bolna.ai/symphony/buildathon#apply-form. Every field is required unless marked otherwise.

**Your team**
1. **Team size**: dropdown with "Just me", 2, 3, 4.
2. **Team name**: shown only when size > 1. Text, max 100 characters.
3. **Other teammates: name and email, one per line**: shown only when size > 1. Textarea, max 1000 characters, placeholder "Asha Rao, asha@example.com".
   - Helper text: "Add the other N member(s). The team lead is already included above."
   - Validation:
     - every line needs an email
     - line count must equal team size − 1
     - emails must be unique and must not match the lead's email

**About you** (team lead)
4. **Full name**: max 100 characters.
5. **Email**: type email, max 255 characters.
6. **Phone (WhatsApp)**: type tel, max 20 characters, placeholder "+91".
7. **City**: max 100 characters.
8. **College or company**: max 150 characters.
9. **LinkedIn or GitHub**: type URL, max 300 characters.

**Your idea**
10. **Have you decided on your idea?**: toggle with Yes / Not yet. Defaults to Yes.
    - If **Yes**, three more fields appear:
      - 11. **Project name**: max 150 characters.
      - 12. **Since when have you been working on this idea?**: max 150 characters, placeholder "e.g. 2 months, since August 2026, just started".
      - 13. **What are you building, and where does voice AI come in?**: textarea, max 2000 characters, placeholder "Who it's for, what problem it solves, how people will talk to it".
    - If **Not yet**, fields 11–13 are hidden and sent as null.

**Consent**
14. Checkbox (required): "I agree to be contacted by Bolna about the Buildathon and Symphony."

**Behind the scenes**
- A hidden honeypot field named `contact_pref_2`.
- The form POSTs to a server function and sends these keys: name, email, phone, city, org, profile_url, team_size, team_name, teammates, idea_decided, project_name, idea, working_since, consent.
- On success it shows "Application received. Thanks for applying. We'll be in touch by email." and a Slack CTA.

Source for this section: https://www.bolna.ai/symphony/buildathon/assets/routes-BiW03H66.js

Note: the form takes no project link, repo or demo. [INFERRED] It is an application/registration form. The project submission for Oct 31 is a separate step that the page does not describe.

## 9. Sponsors, partners, people

- **Buildathon sponsors** (logos on the page): Plivo, Exotel, Sarvam, Cartesia, Deepgram, Kalpa Labs. Source: https://www.bolna.ai/symphony/buildathon
- **Also shown:** the Y Combinator logo ("Y Combinator × Symphony", "Y Combinator × Bolna"). Source: https://www.bolna.ai/symphony/buildathon
- **Symphony summit partners by tier** (from https://www.bolna.ai/symphony):
  - Diamond: Google Cloud, Truecaller for Business, Exotel, Plivo
  - Gold: Kalpa Labs, Sarvam
  - Silver: Wispr Flow, Simplismart, Cartesia, Deepgram, Vobiz
  - Associates: Smallest.ai, Agnost AI
- **Symphony speakers include** (from https://www.bolna.ai/symphony/speakers):
  - Aarthi Ramamurthy (Schema Ventures)
  - Dr. Manish Gupta (Google DeepMind)
  - Srinivas Narayanan (ex-OpenAI)
  - Grey Baker (YC)
  - Akarsh Shrivastava (General Catalyst)
  - Prasanna Krishnamoorthy (Upekkha)
  - Anuja Dhawan (Dubverse/Exotel)
  - Tanuj Bhojwani (ex-People+AI)
  - Sachin Bhatia (Exotel)
  - Madhav Krishna (Vahan AI)
  - Sudarshan Kamath (Smallest.ai)
  - Prashant Shishodia (Kalpa Labs)
  - Sanjay Jain (Gates Foundation)
  - Shrikant Venkataramani (Pocket FM)
  - others
- **Buildathon judges/mentors:** not found. There is no named list.
- **Organizer contacts:** symphony@bolna.ai and the Bolna Builders Slack. Sources: https://www.bolna.ai/symphony, https://www.bolna.ai/symphony/buildathon

## 10. Past Bolna hackathons and winners

- **Bolna × Cartesia "Voc-a-thon"** (Luma: https://luma.com/ubu85bxv)
  - Format: in-person build sprint in Bengaluru, hosted by Bolna (host listed as Sonam Bala).
  - Timeline: registrations opened May 29, qualification June 5, build June 5–12 with Bolna and Cartesia credits, prototype due June 12, demo day **June 13, 2026**. Luma event data: start 2026-06-13T04:00Z, end 11:00Z (09:30–16:30 IST).
  - Focus: voice agents on Cartesia Sonic 3.5. Prizes: "Standout builds will walk away with exciting prizes" (no amounts given).
  - Luma page data shows `guest_count: 59`. The WebFetch summary said "71 registered", so the count is unclear.
  - Sources: https://luma.com/ubu85bxv plus a WebSearch snippet of the same page.
- **Example Voc-a-thon builds** (participant repos, not official results):
  - "UnHold for Me" (on-hold call agent; team Aryan, Ritika & Nishant): https://github.com/victorvini08/unhold-cartesia-bolna-hackathon
  - "Saheli" (voice shopping Chrome extension): https://github.com/KD-3/saheli-voice-shopping
  - https://github.com/AK1-1/vocathon
- **Voc-a-thon winners:** not found.
- **"Vibes In, Latency Out: A Voice AI Open Mic"** (Bolna, Sep 4, 2026, Bengaluru) was a meetup, not a hackathon. Source: https://www.startupgrantsindia.com/events/vibes-in-latency-out-a-voice-ai-open-mic
- **"Built with Bolna" community wall:** shows community projects such as Chukta (loan collection agent), Dadi (scam-call grandma), Bolna Bhai (Pipecat module), n8n-nodes-bolnaai and BolnaMonitor. It also references a "Bolna.ai-Buildathon" in contributor profiles, with no date. Source: https://www.bolna.ai/builders
- **Current buildathon participant repo:** https://github.com/Thesilentprogramer/Bolna_buildathon (created 2026-10-19, no description).

## 11. Social posts and listings

- **Official Bolna channels** (from https://www.bolna.ai/symphony/buildathon/assets/SiteChrome-CBX_uOHj.js):
  - X: https://x.com/bolna_dev
  - LinkedIn: https://www.linkedin.com/company/bolna-ai/
  - Instagram: https://www.instagram.com/bolna_dev
  - YouTube: https://www.youtube.com/@BolnaVoiceAI
- **Bolna's X announcement:** a search snippet attributes the line "@bolna_dev's Buildathon has officially entered the chat… bring any idea and give it a voice, whether that's a new product or a voice layer on something you've already shipped" to Bolna. I could not fetch X (HTTP 402), so the exact post URL was not found.
- **Team-finding post on X:** "Looking for 2 backend builders for the Bolna × Y Combinator Buildathon! … @ChaiCodeHQ". Source: https://x.com/I_codefullstack/status/2111291682159538455 (search snippet)
  - [INFERRED] ChaiCode's community is promoting or taking part in it.
- **Devfolio / Unstop / Luma / Discord listings for this buildathon:** none found. Registration seems to be only through the bolna.ai form.
  - The Luma "Buildathon 2026" result (https://luma.com/9lsgmkt8) is an unrelated Tech4hack event in Delhi NCR.

## 12. Page FAQs (all answers, verbatim from B-JS)

| Q | A |
|---|---|
| Who can apply? | Students, professionals and indie builders — anyone who wants to build with voice. |
| Is the Buildathon in person? | No, it's fully virtual. Only the top 3 teams come to Abhyas Hall, The Lalit Ashok, Bengaluru on 20th Nov to present at Symphony, and we cover their travel. |
| Can I apply as an individual? | Yes. You can apply solo, or as a team of up to 4 people. |
| What kind of builds are allowed? | Anything with voice in it: a new product, a voice feature on an existing one, or something in between. |
| How does the selection process work? | We review every application and shortlist the strongest builds. Selected teams will hear from us by email. |
| Will travel be covered for the finalists? | Yes. We'll cover travel for the top 3 teams. |
| Will we get tickets to Symphony? | Yes. The top 10 teams get free tickets to Symphony. |

Source: https://www.bolna.ai/symphony/buildathon/assets/routes-BiW03H66.js

## 13. Gaps

These are all not found:
- judging rubric
- written rules / T&Cs / IP policy
- how and where the project is submitted (repo, video, deck), and the deadline time zone
- named judges or mentors
- confirmed credits for all participants (the claim exists only in unverified LinkedIn snippets)
- job or internship offers
- official Voc-a-thon winners
- the exact URL of Bolna's X/LinkedIn announcement

[INFERRED] Asking in the Bolna Builders Slack is the most likely way to fill these gaps.

---

## Sources (visited / used)

- https://www.bolna.ai/symphony/buildathon
- https://www.bolna.ai/symphony/buildathon#apply-form
- https://www.bolna.ai/symphony/buildathon/assets/routes-BiW03H66.js
- https://www.bolna.ai/symphony/buildathon/assets/SiteChrome-CBX_uOHj.js
- https://www.bolna.ai/symphony/buildathon/assets/index-DM3oKn_f.js
- https://www.bolna.ai/symphony
- https://www.bolna.ai/symphony/speakers
- https://www.bolna.ai/builders
- https://join.slack.com/t/bolnabuilders/shared_invite/zt-4dg50suac-narQNDvQ9zKgC7aR2VdS3w (link only, not joined)
- https://luma.com/ubu85bxv
- https://luma.com/9lsgmkt8 (unrelated)
- https://www.startupgrantsindia.com/events/vibes-in-latency-out-a-voice-ai-open-mic
- https://github.com/victorvini08/unhold-cartesia-bolna-hackathon
- https://github.com/KD-3/saheli-voice-shopping
- https://github.com/AK1-1/vocathon
- https://github.com/Thesilentprogramer/Bolna_buildathon
- https://x.com/I_codefullstack/status/2111291682159538455 (snippet only; HTTP 402)
- https://x.com/bolna_dev (snippet only)
- https://www.linkedin.com/in/vaibhav-sharma-9305b7232/ (snippet only; HTTP 999)
- https://www.linkedin.com/in/siddharthbatra/ (snippet only)
- https://www.ycombinator.com/companies/bolna-ai
- https://techcrunch.com/2026/01/20/bolna-nabs-6-3-million-from-general-catalyst-for-its-india-focused-voice-orchestration-platform/
