# Telephony layer: design and decisions

Owner: WS1 (Calls). Code: `backend/src/pehchana/telephony/`, `api/telephony.py`,
`arms.py`, `api/admin.py`.

## Why this exists

The public number may have to move between vendors. Plivo is the first choice, but an
Indian number may not be granted (DLT / company paperwork, see
[architecture.md](architecture.md#day-1-unknowns-verify-with-a-real-call-then-update-this-doc)),
and Exotel is the known alternative. Switching must be a stepwise extension, not a
rewrite. The layer follows the open/closed principle: **open for extension** (add a
vendor) and **closed for modification** (routing, models, pipeline and HTTP routes do
not change when a vendor is added).

## Structure

```
telephony/
  base.py       TelephonyProvider Protocol + vendor-neutral dataclasses
  registry.py   name -> factory; get_provider(name); provider_names()
  plivo.py      PlivoProvider, the only module that imports `plivo`
  call_flow.py  vendor-neutral call lifecycle (arm choice, Call rows, status changes)
api/telephony.py   thin HTTP handlers, generated per registered provider
arms.py            arm registry, eligibility, balanced random choice
```

Dependencies point one way: `api` -> `call_flow` -> `base`. Only `registry.py` knows
which vendors exist. Nothing outside `plivo.py` imports a vendor SDK.

### The provider contract (`base.py`)

| Method | Job |
|---|---|
| `verify(WebhookRequest) -> bool` | Authenticate a webhook. Must fail closed. |
| `parse_incoming(form) -> IncomingCall` | Caller number and the vendor's call id. |
| `answer_response(CallPlan) -> ProviderResponse` | Consent notice, then record from answer, then dial the arm. |
| `busy_response() -> ProviderResponse` | No arm free: apologise, hang up. |
| `parse_dial_status(form) -> DialResult` | Answered or not, and duration. |
| `parse_recording(form) -> RecordingEvent` | Recording URL, which channel is the caller, optional download headers. |

Every method takes or returns plain dataclasses, so `call_flow.py` never sees a vendor
field name.

### Request lifecycle

1. `POST /telephony/<provider>/answer`: verify, parse, hash the caller number, pick an
   arm, insert a `Call` (`status=routed`), return the provider's answer response. If no
   arm is eligible, return the busy response and insert nothing.
2. `POST .../dial-status?call_id=`: mark `ended` with duration, or `failed` if the arm
   never picked up (failed calls never count in stats). A late or duplicate callback on
   a finished call is ignored.
3. `POST .../recording?call_id=`: store `recording_url` and `recording_caller_channel`,
   then queue `pipeline.process_call` unless the call failed. If the pipeline is not
   implemented yet, log a warning and still return 204 so the vendor does not retry.

## Adding a provider

1. Create `telephony/<vendor>.py` with a class that satisfies `TelephonyProvider` and a
   `from_settings(settings)` classmethod. Keep vendor settings in `config.py`.
2. Add one line to `_FACTORIES` in `registry.py`.
3. Set `TELEPHONY_PROVIDER=<vendor>`. Routes `/telephony/<vendor>/*` appear
   automatically.
4. Point the vendor's webhooks at those URLs.

No change to `call_flow.py`, `arms.py`, `models.py`, the pipeline or the routes.
`tests/test_telephony.py` holds the contract checks a new provider should also pass,
and `FakeProvider` in `tests/test_call_flow.py` shows the core flow running on a second
vendor with no core changes.

### What the abstraction cannot hide

- **The Turing Clock needs a two-channel recording that starts when the arm answers**
  ([metrics.md](metrics.md)). A vendor that cannot provide it must raise from
  `parse_recording`. It must not return a recording that would skew timings.
- **The Protocol was designed from one vendor.** Exotel's flow is applet-based, not XML
  `<Dial>` + `<Record>`, so expect the Protocol to need a reshape when the second vendor
  arrives. The goal is that the reshape is confined to `base.py` and the vendor modules,
  not that it never happens.
- **Recording downloads** may need vendor auth. `RecordingEvent.download_headers`
  carries them. They are not persisted, so the pipeline must ask the provider again for
  a re-run (open item for WS2).

## Decisions

| Decision | Why | Cost |
|---|---|---|
| Vendor-neutral DB columns `provider`, `provider_call_id` (unique together) replace `plivo_call_uuid` | Renaming after real calls exist needs a migration; there is no Alembic history yet. | Shared contract change, flagged in the PR. |
| `Call.recording_caller_channel` | The caller's channel is a property of the vendor's recording, not global config. | New column read by WS2. |
| Routes generated from the registry, not a `{provider}` path param | Keeps `/telephony/plivo/*` exactly as the contract test and the Plivo dashboard expect, and still needs no route edits for a new vendor. | Routes are built at import time, so a provider must be registered before the app starts. |
| Small registry (`dict`), no plugin discovery | Switching vendors is likely; plugin machinery is not needed for 2 or 3 vendors. | Adding a vendor touches `registry.py` (one line). |
| Webhook URL for signatures is `PUBLIC_BASE_URL` + path + query | Vendors sign the URL they called; behind a tunnel or proxy `request.url` has the wrong host. | `PUBLIC_BASE_URL` must be exact. |
| Caller number is hashed (`sha256(salt + number)`) before it touches a model or log | [ethics.md](ethics.md): raw numbers are never stored or logged. | Cannot reverse a hash to contact a caller. |
| Human arm with no `live_hours` is closed unless the admin override opens it | Required by the shared spec; no volunteers means no human calls, which fails safe. | A missing config silently disables the control arm. |
| `load_arms` skips an arm with neither dial numbers nor an agent id | An arm whose env vars are unset must never receive traffic. An agent id alone is kept so web calls can use it. | A typo in an env var name drops the arm with no error. |
| `choose_arm` weights by `weight / (1 + recent_count)` over the last 6 hours | Balances sample sizes at around 100 calls while every arm stays possible, so callers cannot predict the next one. | Window length is a guess; tune from real traffic. |
| `caller_id=None` on the dial | Lets the vendor pass the caller's own id through, which helps match the Bolna execution later. | Unverified; Plivo may substitute its own number. |
| `answered_at` = dial end time minus duration | The dial-status callback fires at hang-up, so this is the only answer time available without another event. | An estimate, accurate to about a second; confirm on a real call. |
| `python-multipart` added as a dependency | FastAPI cannot parse the vendors' form-encoded webhooks without it. Found by the first end-to-end test. | None. |

## Security

- Every webhook handler verifies the vendor signature first and answers 403 on failure.
  `PlivoProvider.verify` fails closed on a missing token, header or nonce, and on any
  error from the SDK.
- `/admin/*` requires `Authorization: Bearer <ADMIN_TOKEN>`, compared in constant time.
- No raw caller numbers in the database, logs or tests.

## Not verified against real Plivo

Confirm on the Day-1 test call, then update this section and
[architecture.md](architecture.md#day-1-unknowns-verify-with-a-real-call-then-update-this-doc):

- [ ] Form field names: `From`, `CallUUID`, `DialBLegStatus`, `DialBLegDuration`,
      `RecordUrl`, `RecordingDuration`.
- [ ] The `<`-separated number list inside one `<Number>` rings all volunteers at once.
- [ ] Which stereo channel is the caller (`CALLER_CHANNEL`, default 0).
- [ ] What caller id the Bolna agent sees on the bridged call.
- [ ] Whether `answered_at` from the estimate matches the recording's t = 0.

## Tests

`tests/test_telephony.py` (provider contract, Plivo parsing, signatures with Plivo's own
signing helper), `tests/test_arms.py` (loading, live hours, eligibility, balancing),
`tests/test_call_flow.py` (signed webhooks through the real routes, failure and busy
paths, admin shift, a fake second provider). Run `make check-api`.
