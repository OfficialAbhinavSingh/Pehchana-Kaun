# Data freeze (29 Oct) and the pitch numbers

Code only. Call data never goes in this folder or anywhere in git; `pk
export-snapshot` refuses to write inside the repo.

## Freeze

On 29 Oct, 21:00 IST, against the prod database:

```bash
cd backend
DATABASE_URL=<prod url> uv run pk export-snapshot ~/pk-private/freeze-2026-10-29.json
```

It prints the number of calls and a sha256. Post both in #28 so everyone can check
they use the same file. Keep the file in private storage only (team drive with access
limited to the three of us).

The snapshot has every call (real and demo, phone and web, every status) with times,
arm, language, caller hash, accusation times and giveaway tags. It has no recording
URLs, transcripts, accusation phrases or provider ids.

## Numbers sheet

```bash
cd backend
uv run pk numbers ~/pk-private/freeze-2026-10-29.json > ~/pk-private/numbers.md
```

The sheet uses `build_leaderboard` on the snapshot, so every Turing Clock follows the
same rules as the live site (`docs/metrics.md`). Demo rows are always left out. Run it
twice: same file, same sheet.

What it has: calls counted, unique callers, human false-accusation rate, Turing Clock
per voice with CI, a first-call-only check, a check without calls under 10 s that
ended with no accusation (`--short-call-s` to change the cutoff), each language, top
giveaways, repeat callers, calls per day, and browser games on their own.

Vendor names stay hidden unless `REVEAL_VENDORS=true` is set when you run it.

## Before a number goes on a slide

- It is in the sheet, from the frozen file. No hand-edited numbers.
- `n` is next to it.
- The two checks (first call only, no short calls) tell the same story. If they
  don't, say so on the slide or drop the claim.
- Soham has reviewed the sheet (#28).
- Clips: only from teammates or callers who agreed in writing.
