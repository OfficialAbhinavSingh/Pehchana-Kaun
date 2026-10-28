# Runbook

For whoever is on call, at any hour. Owner: WS1 (#10). Commands assume
`ADMIN=https://<domain>` and `TOKEN=<ADMIN_TOKEN>`; get both from the team's secret store.

## 60-second triage

1. `curl -s $ADMIN/healthz`. Expect `{"status":"ok",...}`. No answer or an error means the
   backend or its database is down: go to [Backend down](#backend-down).
2. Make one call to the game number. Does it play the notice and ring an arm?
3. Still unclear: read the host's logs for the last 10 minutes (see
   [Where things are](#where-things-are)).

## Pause the game

There is no pause switch in the app. Pausing means sending callers a "busy" message:

1. In the Plivo console, open the Application behind the game number and set its
   **Answer URL** to the hosted copy of `ops/busy.xml` (see [Static busy
   message](#static-busy-message)).
2. To resume, put the Answer URL back to `https://<domain>/telephony/plivo/answer` (POST).

The browser game is separate: it is off when the site is off, or when
`BOLNA_API_KEY` is unset on the backend.

## Humans on or off

The human arm only takes calls inside `live_hours` in `bolna/arms.yaml`, unless an
override says otherwise. The latest unexpired override wins.

```bash
# humans on for 2 hours
curl -s -X POST $ADMIN/admin/shift -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"humans_on_shift": true, "hours": 2, "set_by": "<your name>"}'

# humans off for 6 hours (say a volunteer left)
curl -s -X POST $ADMIN/admin/shift -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"humans_on_shift": false, "hours": 6, "set_by": "<your name>"}'

# what is the state now, and can a human arm take a call?
curl -s $ADMIN/admin/shift -H "Authorization: Bearer $TOKEN"
```

`humans_open_now: true` in the reply is the check. A wrong token gives 401. A call
already ringing a volunteer is not cut off.

## Reprocess a call

`POST $ADMIN/admin/calls/<call_id>/reprocess` exists but is **not implemented yet**: it
returns 501 until WS2 ships `pipeline.py` (#17). Until then there is no way to re-run a
failed call from here; note the call id and tell Soham. Once it ships, fill in this
section.

## Drills

Run each once before launch and write the date and result in the table at the end.

### (a) An arm does not answer

Callers must hear the busy message and the call must end `failed`.

- Without a phone: `pk simulate-call --target $ADMIN --scenario no-answer`. It checks the
  call ends `failed` (and never counts in stats).
- With a phone: ring the number while the only eligible arm's phone is off. Expect the
  Plivo dial to time out (`ring_timeout_s`) and the call to end. What the caller hears
  after a failed dial is **not verified**: the answer XML has nothing after `<Dial>`, so
  check on the real call and fix the XML if the caller just hears silence.

### (b) Backend down

Plivo needs somewhere to send callers when our server cannot answer.

1. Host `ops/busy.xml` at a stable HTTPS URL ([Static busy message](#static-busy-message)).
2. In the Plivo Application, set the **Fallback Answer URL** to it (method GET).
3. Drill: stop the backend (or set the Answer URL to a dead address) and ring the number.
   Expect the busy message, not a ringing line or an error tone.

Whether Plivo uses the fallback on a timeout, a 5xx, or both is **not verified**. Test
both: a stopped container and a broken Answer URL.

### (c) Bolna wallet low

When the balance runs out, Bolna ends executions with status `balance-low` (it is in
`TERMINAL_STATUSES` in `integrations/bolna.py`). The AI arms then stop working while the
human arm still works.

- Prevent it: check the balance before every launch push and daily in the launch week.
- When it happens: top up first. Until then you can keep the game honest by turning
  humans on for the shift, but note the human arm alone makes every call a human call
  and skews the mix, so prefer to [pause the game](#pause-the-game) until topped up.
- What our backend does with a `balance-low` execution is WS2's code (#15) and is not
  built yet: check it when it lands (the call should end `failed`, not `processed`).

### (d) Deepgram error

Intended behaviour: the call keeps its recording, gets `processing_error` set, and can be
re-run. That is WS2's pipeline (#17) and is not built yet, so this drill cannot be run
today. Do it once the pipeline lands: break `DEEPGRAM_API_KEY` on a rehearsal deploy, make
a call, then confirm `processing_error` is set and reprocess works after fixing the key.

## Where things are

| What | Where |
|---|---|
| Backend logs | The host's log view (fill in once the host is chosen, see [deploy.md](deploy.md)) |
| Calls, arms, errors | Postgres, table `calls` (`status`, `arm_id`, `processing_error`, `recording_url`) |
| Plivo call logs and recordings | Plivo console, Logs, Voice |
| Bolna executions | Bolna dashboard, Executions |
| Arms config | `bolna/arms.yaml` (numbers come from env, never in git) |
| Deploy, env vars, rollback | [deploy.md](deploy.md) |
| Rehearsal | `pk simulate-call` ([telephony.md](telephony.md)) |

Logs never contain raw caller numbers (only a hash). Do not paste recordings or numbers
into chat or git ([ethics.md](ethics.md)).

## Balances to watch

| Service | Why it matters | Where |
|---|---|---|
| Bolna | AI arms stop at zero (`balance-low`) | Bolna dashboard |
| Plivo | No credit means no inbound or outbound calls | Plivo console |
| Deepgram | Calls stay unprocessed, no accusation time | Deepgram console |
| Anthropic | Giveaway tags stop | Anthropic console |

Set low-balance alerts in each console where it offers them. Write the threshold you set
in the table below.

## Uptime monitor

Create a monitor (UptimeRobot or similar) for `GET https://<domain>/healthz`, every
1 to 5 minutes, alert to the team chat when it fails twice in a row. `/healthz` also
queries the database, so a pass means the app and Postgres both answer. It does not test
Plivo, Bolna or Deepgram, so keep the [triage](#60-second-triage) test call too.

## Static busy message

`ops/busy.xml` is the Plivo XML used for pausing and for the fallback. Host it somewhere
that serves it over HTTPS with an XML content type and stays up when the backend is down
(the deployed site's static files, or an object-storage bucket). Not the same server as
the backend. Whether `raw.githubusercontent.com` works is **not verified** (it serves
`text/plain`). Fill in the URL once chosen.

## Who to ping

| Area | Who |
|---|---|
| Calls, Plivo, deploy, humans | Mahak |
| Pipeline, Deepgram, Bolna agents | Soham |
| Website, launch, analytics | Abhinav |

## Drill log

| Drill | Date | By | Result |
|---|---|---|---|
| (a) arm does not answer | | | |
| (b) backend down | | | |
| (c) Bolna wallet low | | | |
| (d) Deepgram error | | | |

| Alert | Threshold set | Date |
|---|---|---|
| Bolna balance | | |
| Plivo balance | | |
| Deepgram balance | | |
| Anthropic balance | | |
| `/healthz` monitor | | |
