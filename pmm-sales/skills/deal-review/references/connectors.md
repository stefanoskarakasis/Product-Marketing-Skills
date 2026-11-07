# Connectors

All optional. A category is connected only if a tool for it is present and answers. Say which answered and which did not on the "not queried" line.

| Category | Used for | Tools | Without it |
|---|---|---|---|
| `~~CRM` | Stage, close-date history, amount band, contacts, next step, owner, opt-out | HubSpot wired; Salesforce connect-your-own | Paste the deal row |
| `~~call recordings` | Transcripts, objections, who spoke | Gong, Granola | Paste a transcript |
| `~~email` | Threads with the buyer's domain | Gmail | Skip |
| `~~calendar` | Meetings held and booked, attendee roles | Google Calendar | Skip |
| `~~team chat` | The thread you ask in; the weekly queue | Slack | Reply in chat |
| `~~cloud storage`, `~~knowledge base` | The saved review and `/context/deals/` | Google Drive and Docs, Notion | Show in the reply |

Not wired here: support, analytics, company data, enrichment and web research. `customer-context` and `prospect-research` own them.

## Reading guides

- **HubSpot:** read the deal, owner, stage, close-date history, last activity and contacts' roles by live label. Never amounts in Slack for deals the asker does not own.
- **Salesforce:** take names from the live schema. The Opportunity holds stage and close date; the owner is the Opportunity owner; roles come from Opportunity Contact Roles. Ask once if unclear.
- **Drive:** a Doc named `Deal review: [Deal], [YYYY-MM-DD]`. Ask before saving; never to a shared drive without saying so.

## Where the brain lives

| `brain_source` | Read through |
|---|---|
| `repo` | The repo's file |
| `drive` | `~~cloud storage` |
| `notion` | `~~knowledge base` |
| `local` | File read, Claude Code and Cowork only |
