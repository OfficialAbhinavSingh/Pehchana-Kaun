# Metrics

## The Turing Clock

Kalpa Labs proposed the Turing Clock as "how long can a person talk with a model
before deducing, reliably better than 50% accuracy, that it's an AI?"
([source](https://kalpalabs.ai/blog/towards-generalist-audio-models)). Our phone-game
version:

- **t = 0** when the arm answers (start of the Plivo session recording).
- **Event** = the caller's first accusation ("tum bot ho", "you're a bot", ...) found in
  the caller channel of the recording.
- **Censored** = the call ended with no accusation; we only know the arm survived at
  least that long.
- **Turing Clock of an arm** = median of its Kaplan-Meier survival curve: the first time
  t with S(t) <= 0.5. If the curve never drops to 0.5, the clock is longer than the
  longest call we saw (`max_observed_s`). That is a real pass only when those calls were
  long: five calls dropped at 5 s say nothing, so such an arm is ranked and shown by
  that lower bound ("more than 0:05"), never as a winner. (lifelines needs S < 0.5, so
  it can differ when S sits on exactly 0.5; `test_scoring.py` pins our rule.)

Why survival analysis: most short calls end without a verdict. Averaging only the
accused calls would reward arms that bore people into hanging up.

## Reported per arm (and per arm x language)

| Metric | Meaning |
|---|---|
| `n_calls` | processed real calls (no demo rows, no unanswered dials) |
| `accusation_rate` | share of calls with an accusation |
| `median_turing_clock_s` | KM median; `null` = not reached within `max_observed_s` |
| `max_observed_s` | longest observed call time (accusation or hang-up) |
| `median_ci_low_s`, `median_ci_high_s` | 95% CI for the median, from the pointwise band; `null` = not reached yet |
| `fooled_at_60s` | KM survival at 60 s; `null` when no call lasted 60 s (and S had not reached 0) |
| `top_giveaways` | most frequent giveaway tags before the accusation |

For the **human control arm**, `accusation_rate` is the **false-accusation rate**: how
often people call a real person a bot. This is the baseline every AI arm is judged
against, and is itself a headline number.

## Honesty rules

- Show `n_calls` next to every number; hide rankings below `MIN_CALLS_FOR_RANKING`.
- Report confidence intervals once n allows (Greenwood's formula for KM, on the
  log(-log S) scale so the band stays in [0, 1]; matches lifelines' default).
- Callers who call repeatedly learn the voices: report first-call-only numbers as a
  check (caller hash makes this possible without storing numbers).
- Never mix demo data into public numbers; the API must say if it did.
- Vendor names are hidden by default (`REVEAL_VENDORS=false`): we compare language and
  failure modes, not sponsors.
