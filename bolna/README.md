# bolna/

Everything we configure on the Bolna side lives here as files, so agents are
reproducible and reviewable in PRs instead of clicked together in the dashboard.

| Path | What |
|---|---|
| `arms.yaml` | Who can pick up a call: human control + one entry per AI voice stack |
| `agents/_template.json` | Bolna agent body template (filled per arm by `pk sync-agents`) |
| `functions/accuse_bot.json` | Custom function the agent calls when accused of being a bot |
| `personas/` | The persona every arm plays (same for all, so only the voice differs) |

`${VAR}` placeholders are substituted from the environment at sync time.
