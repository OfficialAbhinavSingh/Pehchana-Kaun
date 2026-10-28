# Consent, privacy and safety

This is a research game with real people's voices. Get this right before launch;
judges flagged unsafe agents as a red flag, and India's Digital Personal Data
Protection (DPDP) Act applies.

## Consent

- Every call starts with a notice **before** anyone answers: it's a game, you may talk
  to an AI, the call is recorded for research, don't share personal details, stay on the
  line to agree or hang up now. Hindi and English, in a human voice (script in
  [copy.md](copy.md#consent-notice-script-for-mahak-7), how to record it in
  [consent-audio.md](consent-audio.md)). The website repeats it with a link to the
  privacy page.
- Human volunteers sign up explicitly, know they're recorded, and get the same persona
  brief as the AI.
- AI agents reveal honestly when accused and break character immediately if a caller
  seems not to know it's a game, is distressed, or asks to stop
  (`bolna/personas/README.md`).

## Data we keep

| Data | Where | Retention |
|---|---|---|
| Caller number | **never stored**; only `sha256(salt + number)` | n/a |
| Recording | Plivo + our DB URL | delete after the buildathon unless the caller opted in to clip use |
| Word transcript, tags, timings | our DB | anonymized research data |
| Clips in pitch/video | only from teammates or callers who agreed in writing | per consent |

- Anyone can ask for deletion (contact on the privacy page); delete by caller hash.
- No call data in git, issues, screenshots, Slack or the deck except consented clips.

## Agent safety

- Agents never ask for personal data, money, OTPs, addresses or links.
- No medical, legal or financial advice. Keep calls under 5 minutes.
- `accuse_bot` and webhooks are authenticated; prompt injection over the phone can at
  worst change what the agent says, not what our backend does.
