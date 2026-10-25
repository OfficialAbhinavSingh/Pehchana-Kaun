# Launch plan: 300+ real callers, 27 to 29 Oct

Owner: WS3 (#21, run in #27). Judges ask for real usage before the deadline more than
anything else (`docs/context.md`), so launch is a plan with numbers, not a hope.

## The target and the math

- **300 processed calls by the data freeze (29 Oct, evening IST).** That is 100 a day
  over three days, about 12 an hour across 8 busy hours.
- Rough funnel per post (our guesses, not measured): views → link clicks (2 to 5%) → people who actually call
  (30 to 50% of clicks, higher for the browser game). So 300 calls needs roughly
  1,000 to 1,500 clicks, or 30,000+ views across all channels. One post from one of us
  will not do it; forwards in WhatsApp groups and repeat posts with results will.
- Repeat callers help volume but bias the numbers; the leaderboard has a first-call-only
  view for that (`docs/metrics.md`). Ask people to share, not to call ten times.

## Gate: Mahak's go/no-go (#10)

Nothing goes out until #10 says go on 27 Oct morning: number answers, consent plays,
all arms reachable, a test call shows up as `processed`. If the phone number is not
ready, launch with the browser game only (#25) and add the number later with a second
post ("ab phone par bhi").

## Channels

| Channel | Who | Notes |
|---|---|---|
| LinkedIn, personal posts | all three | Biggest reach for the judges' world. Tag Bolna; tag sponsors once, in the results post, not the launch one |
| X | Abhinav | Short clip or screen recording beats text. Tag Bolna |
| College WhatsApp groups | all three | Highest call rate: friends of friends, Hinglish speakers. Hinglish message below |
| Bolna Builders Slack | Abhinav | Builders love testing voice agents. Post in the buildathon/showcase channel only |
| Family WhatsApp groups | all three | Older callers, more Hindi, a different crowd from college: good for the language spread |
| Tamil / Marathi friends | all three | Ask 5 to 10 people each to play in their language. The language gap is the story |
| Dev communities (Discord servers we're already in) | anyone | Only where self-promotion is allowed. Never spam |

No paid promotion. No cold DMs to strangers.

## Schedule (IST)

| When | What | Who |
|---|---|---|
| 26 Oct, night | Final copy check on the live site; post drafts ready; volunteer slots filled for the 27th | all |
| 27 Oct, 10:00 | #10 go/no-go | Mahak |
| 27 Oct, 11:00 | Launch posts: LinkedIn (all three), X, Slack | all |
| 27 Oct, 11:30 | WhatsApp groups (college first, family after lunch) | all |
| 27 Oct, 20:00 | Second WhatsApp nudge in groups that responded ("aaj ke results...") | all |
| 28 Oct, 12:00 | First-results post: calls so far, human false-accusation rate, best AI median. Aggregates only | Abhinav |
| 28 Oct, evening | Language push: ask Tamil/Marathi speakers directly | all |
| 29 Oct, 12:00 | "Language gap" post: where Indian voice AI still breaks | Abhinav |
| 29 Oct, 21:00 | Data freeze (#28). The line stays open; later calls are a bonus, not in the pitch numbers | Abhinav |
| 30 Oct | Thank-you post with final numbers (the same ones the deck uses) | Abhinav |

Each post has the site link, which carries the number and the browser button. Never
post a raw phone number without the context of the game: people would treat it as spam.

## Post drafts

Edit freely; these are starting points. Swap in real numbers before posting and never
post a number we can't trace to the database.

**LinkedIn launch (English):**

> Every voice AI company in India says their agent sounds human. We built a way to check.
>
> Call Pehchana Kaun? and someone picks up: sometimes a real person, sometimes an AI
> voice agent. The moment you think it's a bot, say "tum bot ho!". We time how long
> each AI lasts before real callers catch it, and what gave it away.
>
> Takes two minutes, works from your phone or browser: {SITE_URL}
>
> Built for the Bolna Symphony Buildathon by Pehchaano Labs (me, @Mahak, @Soham).
> Live leaderboard on the site. How long will it fool you?

**WhatsApp (Hinglish):**

> Ek game banaya hai 😄 Call karo, koi uthayega: insaan ya AI. Jaise hi lage bot hai,
> bolo "tum bot ho!". Dekhte hain AI kitne second tak bach paata hai.
> {SITE_URL}
> 2 min lagte hain. Forward kar do please 🙏

**X:**

> Can you tell a human from an AI on a phone call?
> Call, chat, and say "tum bot ho!" when you catch the bot. We time how long Indian
> voice AI survives. {SITE_URL}

**Results post (28 Oct), shape only:**

> Day 1 of Pehchana Kaun?: {N} calls. Real people were called bots {human_rate}% of
> the time. The best AI voice lasted a median {best_median} before getting caught.
> Biggest giveaway: {top_tag}. Still running: {SITE_URL}

Rules for results posts: aggregates only, no individual calls or quotes without
written consent, vendor names only if we decided to reveal them, `n` next to every
number.

## Tracking calls per hour

The leaderboard shows `total_calls` (processed only). For calls coming in, including
ones still processing or unanswered, run this on the prod database (counts only, no
caller data). Enums are stored by name, so the values are upper case:

```sql
SELECT date_trunc('hour', started_at AT TIME ZONE 'Asia/Kolkata') AS hour_ist,
       count(*)                                       AS calls,
       count(*) FILTER (WHERE status = 'PROCESSED')    AS processed,
       count(*) FILTER (WHERE status = 'FAILED')       AS failed,
       count(DISTINCT caller_hash)                     AS unique_callers
FROM calls
WHERE source = 'REAL' AND started_at > now() - interval '24 hours'
GROUP BY 1 ORDER BY 1;
```

Check it every couple of hours on launch day. A rising `failed` share means arms are
not answering (tell Mahak); calls with no `processed` after 15 minutes means the
pipeline is stuck (tell Soham).

Daily, write one line in #27: calls that day, processed, unique callers, which post
drove the spike.

## Volunteers for the human arm

The human arm only takes calls inside live hours or when an admin override is on
(`POST /admin/shift`). No volunteers means no control group, and the false-accusation
baseline is a headline number.

- Need: 2 volunteers per slot so one can miss a call. Slots of 2 hours, 11:00 to 23:00
  IST on 27 to 29 Oct: 18 slots, about 36 volunteer-slots. Ask 15 to 20 friends for 2
  slots each.
- Sign-up: one shared sheet with slot, name, and "number given to Mahak" (yes/no). The
  numbers themselves go only to Mahak, for the dial config, never in the sheet or git.
- Every volunteer gets the persona brief (`bolna/personas/volunteer-brief.md`, WS2),
  knows the call is recorded, and agrees in writing (a message is fine).
- Same safety rules as the AI (`bolna/personas/README.md`): never ask for personal
  details, money or links, keep it under 5 minutes.
- Mahak switches the human arm on and off for the slots (live hours, or the admin
  override; `GET /admin/shift` shows the current state).

## If things go wrong

| Problem | Do |
|---|---|
| Number not ready on 27 Oct | Launch browser-only; phone post when it works |
| Calls fail (arms not answering) | Pause posting, tell Mahak, post again once fixed |
| Few calls by 27 Oct evening | Second wave: ask 10 friends each to forward to 3 groups; post a short screen recording of a call |
| Someone is upset or confused on a call | AI breaks character by design; reply to them publicly and kindly; offer deletion |
| A competitor ships something similar | Note it in #27; our angle is real phone calls, a live human control and Indian languages |

## Competitor re-check (28 to 30 Oct)

Re-run the searches from `docs/research/11-dedup-buildathon-competitors.md`: buildathon
repos (two were empty on 21 Oct), the Bolna builders wall, Bolna Builders Slack, and a
quick search for "voice turing test India". Post what you find in #27.
