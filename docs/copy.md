# Site copy, consent script and leaderboard wireframe

Owner: WS3 (#21). The website (#24) takes its words from here, so change them here
first. The visual design is still being picked; this file fixes *what* the pages say
and show, not how they look.

Rules for every line on the site:

- Short. A caller arrives from a WhatsApp forward on a phone and decides in five
  seconds. If a line can go, it goes.
- Hinglish first, English underneath or on toggle. Hinglish in Roman script, the way
  people actually text.
- Never promise what the system does not do. We do not tell a caller afterwards whether
  they talked to a human, so the copy does not say we will.
- No vendor names unless `REVEAL_VENDORS=true` (`Voice A/B/C` otherwise).

`{NUMBER}` is the public game number (#1, not decided yet). Until it exists, the
primary button is "Play in browser" (#25) and the phone block is hidden.

## Landing page

### Hero

| | Hinglish | English |
|---|---|---|
| Title | Pehchana Kaun? | Pehchana Kaun? |
| Line | Call karo. Koi uthayega: insaan ya AI. Bot lage toh bolo "tum bot ho!" | Call. Someone picks up: a person or an AI. Think it's a bot? Say "you're a bot!" |
| Primary button | Call {NUMBER} | Call {NUMBER} |
| Secondary button | Browser mein khelo | Play in your browser |
| Third link | Leaderboard dekho | See the leaderboard |
| Under the buttons | Call record hoti hai, research ke liye. [Privacy](/privacy) | Calls are recorded for research. [Privacy](/privacy) |

On desktop the primary button becomes a QR code for `tel:{NUMBER}` plus the number in
text. On a phone it is a `tel:` link.

Browser play reaches AI voices only, so a person on the browser can never be talking to
a human. The browser button says so in small text: "Browser par sirf AI voices" /
"Browser games are AI only".

### How to play (3 steps)

1. **Call karo.** Phone ya browser se. / **Call.** From your phone or the browser.
2. **Baat karo.** Jo mann kare. Koi insaan ho sakta hai, koi AI. / **Talk.** About
   anything. It might be a person, it might be an AI.
3. **Pakdo.** Jaise hi lage bot hai, bolo "tum bot ho!" / **Catch it.** The moment you
   think it's a bot, say "you're a bot!"

One line under the steps: "Hum ginte hain kitne second mein log AI ko pakad lete hain."
/ "We time how many seconds it takes people to catch the AI."

### Live number strip

`{total_calls} calls so far · the best AI voice lasted {best_median} before getting
caught · updated {generated_at}`

`{best_median}` is the first ranked AI arm's median. Hidden until at least one AI arm
is ranked (`ranked: true`). Before that: "Abhi shuru hua hai. Pehle callers mein
se ek bano." / "Just started. Be one of the first callers."

### FAQ

**Kya call record hoti hai? / Is the call recorded?**
Haan. Call shuru hone se pehle bataya jaata hai. Recording sirf research ke liye hai
aur buildathon ke baad delete ho jaati hai (jab tak aap likh kar clip use karne ki permission
na do). / Yes, and the call tells you before anyone picks up. Recordings are for research
only and are deleted after the buildathon, unless you agree in writing to let us use a clip.

**Yeh scam call toh nahi? / Is this a scam?**
Hum aapko kabhi call nahi karte, aap humein karte ho. Koi aapse OTP, paisa, address ya
link nahi maangega. Koi maange toh phone kaat do aur humein batao. / We never call you;
you call us. Nobody will ask for an OTP, money, your address or a link. If anyone does,
hang up and tell us.

**Mera number save hota hai? / Do you keep my number?**
Nahi. Hum sirf ek one-way hash rakhte hain taaki pata chale kaun dobara call kar raha
hai. Number khud kahin save nahi hota. / No. We keep a one-way hash so we can tell
repeat callers apart. The number itself is never stored.

**Call ka kharcha? / What does it cost?**
Aapke normal call rate jitna. Browser game free hai. / Your normal call rate. The
browser game is free.

**Mujhe pata chalega ki insaan tha ya AI? / Will I find out who it was?**
AI ko pakdoge toh woh maan lega. Results leaderboard par sab ke liye hain. / If you
catch an AI, it admits it. Overall results are on the leaderboard for everyone.

**Kisne banaya? / Who made this?**
Pehchaano Labs, teen logon ki team, Bolna Symphony Buildathon ke liye. / Pehchaano
Labs, a team of three, for the Bolna Symphony Buildathon.

**Apni call delete karwani hai? / Want your call deleted?**
{CONTACT_EMAIL} par likho, jis number se call kiya tha woh batao. Hum hash se dhoondh
kar delete kar denge. / Email {CONTACT_EMAIL} with the number you called from. We find
the call by its hash and delete it.

## Privacy page

From `docs/ethics.md`, in plain words, one screen on a phone:

- What we record: the call audio, the transcript, when an accusation happened.
- What we never keep: your phone number (only a one-way hash).
- Who hears it: the three of us, for research. Clips are used in our pitch only from
  people who agreed in writing.
- How long: recordings are deleted after the buildathon (Nov 2026).
- Deletion: email {CONTACT_EMAIL} with the number you called from.
- The AI never asks for personal data, money, OTPs, addresses or links.

## Consent notice script (for Mahak, #7)

Played before anyone answers. Keep it under 15 seconds per language; long notices
make people hang up before the game starts. Hindi first, then English, recorded by a
teammate in a normal speaking voice (not a robotic IVR voice: the notice must not
sound like one of the arms).

**Hindi (Roman script for the reader):**
> Namaste! Yeh Pehchana Kaun game hai. Aapse koi insaan baat karega ya AI. Call
> research ke liye record hogi. Apni personal details mat batana. Line par bane rahe
> toh aap sahmat hain; nahi khelna toh abhi phone rakh dijiye.

**Hindi (Devanagari, same text):**
> नमस्ते! यह पहचाना कौन गेम है। आपसे कोई इंसान बात करेगा या AI। कॉल रिसर्च के लिए
> रिकॉर्ड होगी। अपनी पर्सनल डिटेल्स मत बताना। लाइन पर बने रहे तो आप सहमत हैं; नहीं
> खेलना तो अभी फ़ोन रख दीजिए।

**English:**
> This is Pehchana Kaun, a game. You'll talk to a person or an AI. The call is
> recorded for research. Please don't share personal details. Stay on the line to
> agree, or hang up now.

The spoken `<Speak>` fallback in `telephony/plivo.py` says the same words, in both
languages. How to record, export, host and check the audio: [consent-audio.md](consent-audio.md).

## Leaderboard wireframe

Content and order only, mapped to `GET /leaderboard` (`web/src/lib/api.ts`). Phone
width first; desktop puts the curve beside the cards.

```
┌───────────────────────────────────────────────┐
│ [demo data banner]   only if includes_demo_data│
│                                                │
│ Leaderboard                                    │
│ {total_calls} calls · updated {generated_at}   │
│ [All calls | First call only]  first_call_only │
│                                                │
│ ┌─ Insaan (control) ─────────────────────────┐ │
│ │ Called a bot by mistake: {accusation_rate} │ │
│ │ n = {n_calls}                              │ │
│ └────────────────────────────────────────────┘ │
│   "Even real people get called bots this often:│
│    every AI number below is read against it."  │
│                                                │
│ ┌─ #1 Voice B ───────────────────────────────┐ │
│ │ Survived  0:48   (95% CI 0:31 to 1:10)     │ │
│ │ Still fooling people at 60 s: 38%          │ │
│ │ n = 112   ·   caught in 61%                │ │
│ │ Gave itself away by: too-fast reply, ...   │ │
│ └────────────────────────────────────────────┘ │
│ ┌─ #2 Voice A ... ───────────────────────────┐ │
│ ┌─ Voice C · needs 7 more calls ─────────────┐ │
│                                                │
│ Survival curve (all arms, one line each)       │
│  100% ┤━━━━╮                                   │
│       │    ╰━━╮___  human stays flat at top    │
│   50% ┤.......╰━━╮..... median line            │
│       │          ╰━━━                          │
│     0 ┼────────────────── seconds              │
│                                                │
│ By language  [Hindi | Tamil | ...]             │
│  same cards, only arms with calls in it        │
│                                                │
│ How we measure (link to docs/metrics.md)       │
└───────────────────────────────────────────────┘
```

| On screen | Field | Rule |
|---|---|---|
| Card order | `arms` | API already sorts: human, ranked AI, unranked AI |
| "Survived 0:48" | `median_turing_clock_s` | `null` with `max_observed_s`: show "more than 0:{max}" and no rank badge |
| CI | `median_ci_low_s`, `median_ci_high_s` | hide when either is `null` |
| "at 60 s" | `fooled_at_60s` | `null`: hide the line |
| Human line | `accusation_rate` of the `kind: "human"` arm | this is the false-accusation rate |
| "needs N more calls" | `ranked: false` | N = `min_calls_for_ranking - n_calls` |
| Giveaways | `top_giveaways` | at most 3 on the card, tag names made human-readable |
| Curve | `curve[].t`, `curve[].survival` | step line; band from `ci_low`/`ci_high` on hover or tap |
| Language tabs | `by_language` | keys are language codes (`hi`, `ta`); show names. `unknown` goes last |
| Empty state | `total_calls == 0` | "No calls yet. Be the first." plus the call button |

Never show: vendor names (unless revealed), individual calls, transcripts, caller
hashes, anything per caller.
