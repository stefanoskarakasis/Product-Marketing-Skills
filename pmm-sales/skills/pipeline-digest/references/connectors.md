# Connectors

All optional. A category is connected only if a tool for it is present and answers. Say which answered and which did not on the "not queried" line.

| Category | Used for | Tools | Without it |
|---|---|---|---|
| `~~CRM` | Open deals, stage and close-date history, last activity, Next Step, contact roles, forecast category, owner | HubSpot wired; Salesforce connect-your-own | Paste rows or a CSV export |
| `~~calendar` | A future-dated meeting on a deal, for "no meeting booked" | Google Calendar | Use meetings logged in the CRM only |
| `~~call recordings` | The date of the latest call as an activity signal | Gong, Granola | Skip |
| `~~email` | The date of the latest thread with the buyer's domain | Gmail | Skip |
| `~~team chat` | The thread you ask in; the weekly delivery; finding a deal owner for a DM | Slack | Reply in chat; DMs stay paste-ready |
| `~~cloud storage`, `~~knowledge base` | A CSV or Sheet to read; the saved digest and `/context/pipeline/` | Google Drive and Docs, Notion | Show in the reply |

Not wired here: support, analytics, company data, enrichment and web research. `customer-context` and `prospect-research` own them. No new category or server is needed.

## Reading guides

- **Salesforce:** names come from the live schema. Usually: `Opportunity` (stage, close date, amount, Next Step, last activity date, forecast category, owner, closed flag), `OpportunityHistory` (stage and close-date changes over time), `OpportunityContactRole` (the role of each contact; read roles only), `Event` and `Task` (dated activity and future meetings). Close date and stage are required fields, so "close date blank" cannot occur: check "close date passed" and "moved twice or more" instead. Ask once if a name is unclear. Salesforce is connect-your-own: no server is wired in this plugin.
- **HubSpot:** read the deal, owner, stage, close-date history, last activity, Next Step and associated contacts' roles by live label.
- **CSV or paste:** columns the skill looks for: deal, account, owner, stage, stage date, close date, amount, last activity, Next Step, contact role, forecast category, segment. Missing columns become questions, not guesses. Label "CSV import" or "pasted". Say how many deals were read.
- **No CRM connected:** say so in one line and say that connecting one gives stage history and activity dates, which make the slow-in-stage check possible. Never skip that line.
- **Drive:** a Doc named `Pipeline digest: [scope], [YYYY-MM-DD]`. Ask before saving; never to a shared drive without saying so.
- **Slack:** the digest goes where it was asked. A DM needs a yes that names it (`rules.md`).

## Where the brain lives

| `brain_source` | Read through |
|---|---|
| `repo` | The repo's file |
| `drive` | `~~cloud storage` |
| `notion` | `~~knowledge base` |
| `local` | File read, Claude Code and Cowork only |
