# WS2-01: first-agent browser rehearsal

**Status:** Retell browser rehearsal completed; Bolna phone-path validation remains pending.

## Why this route

The planned Bolna phone-agent check is blocked because the team does not have Bolna
credits or a provisioned number. A temporary Retell single-prompt voice agent was used
in the dashboard's browser test panel to exercise the persona without purchasing a
phone number. Retell web calls use real audio and are billed per minute at the selected
voice/model rate (without telephony charges), so check the trial balance before testing:

- [Retell web call testing](https://docs.retellai.com/test/test-web)
- [Retell testing charges](https://docs.retellai.com/test/testing-pricing)

This is a throwaway evaluation setup. Do not add Retell to the product, its provider
configuration, database, or API contracts. A Retell browser call does not measure the
Bolna/Kalpa phone path or PSTN audio quality. Record the provider and voice used with
every observation.

## Run the rehearsal

1. Create a temporary Retell single-prompt voice agent and use
   [`bolna/personas/priya-pune.md`](../bolna/personas/priya-pune.md) as its prompt.
2. Use the dashboard's **Test Audio** web call only. Do not publish the agent or buy
   or connect a phone number.
3. Keep each call short, use synthetic names and numbers, and stop if the dashboard
   shows that trial credits are unavailable or the expected cost is unclear.
4. Run the five scenarios below. A sixth short Hindi number/date check was added to
   clarify the number readback. Dashboard end-to-end latency is recorded as reported;
   these are exploratory observations, not production latency measurements.
5. Do not commit recordings, raw transcripts, caller details, API keys, screenshots, or
   per-call observations. Use Retell Call History only to review uncertain behavior.
6. Keep any filled copy of
   [`ws2-01-listening-notes.template.json`](ws2-01-listening-notes.template.json)
   private. Do not upload call recordings, transcripts, or filled per-call notes to the
   repository or issue tracker; the project's privacy rules prohibit call data there.
   The PR may state that a browser rehearsal was performed without including call data.

| Run | Scenario | Notes to capture |
|---|---|---|
| 1 | Casual Hinglish opening and conversation | Naturalness, awkward phrasing, response delay |
| 2 | Interrupt the agent while it is speaking | Whether it stops, how quickly it listens, whether it recovers cleanly |
| 3 | Switch between Hindi and English mid-conversation | Whether it follows the switch and keeps the context |
| 4 | Ask it to repeat synthetic numbers and a date in Hindi/Hinglish | Digits spoken, grouping, pronunciation, and corrections |
| 5 | Switch from Hindi to Tamil | Run only if the selected speech and voice configuration supports both; otherwise record “not supported/not tested” and use this run to repeat the weakest earlier scenario |

## Scope and next work

- The Retell browser rehearsal is complete, but it does not satisfy the original
  Bolna phone-specific check or validate Kalpa integration, PSTN audio, or telephony.
- If no Retell trial is available, Kalpa's [public realtime demo](https://kalpalabs.ai/realtime)
  can provide a limited English/Hindi and interruption listening check. Its built-in
  persona does not test Priya, Tamil, or the phone path; the demo page does not state
  usage limits, so check those before repeated calls.
- Once Bolna access and a reachable phone route are available, run those checks
  separately and append the real observations to issue #11.
- Continue Bolna adapter, webhook, and processing work against mocked responses and
  fixtures. This rehearsal does not add a Retell dependency or change those contracts.
