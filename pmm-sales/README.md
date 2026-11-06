# pmm-sales

Sales-facing context for sellers and CSMs, built for Slack first: tag Claude in a thread and get the current state of one customer, or the reason, angle and first question for one prospect, every line sourced.

## Start here

- **You get:** a ~150-word answer in the Slack thread, or a full brief in chat, Cowork or Claude Code: owner, renewal, who has really replied, latest calls, up to five flags, and a check against your brain.
- **First command:** `/pmm-sales:customer-context`
- **Try:** "@Claude catch me up on Northwind before Thursday's renewal call"
- **Before a first touch:** `/pmm-sales:prospect-research`. Try: "@Claude is there a reason to contact Tidewell Foods now?" You get a verdict, a hypothesis, an angle and a first question. EMEA data rules switch on by themselves for European accounts.
- **The brain:** both skills use it for ICP fit, competitors, objections and approved claims. Without one it still runs and says so. Never writes to it.

## Skills (2)

- **customer-context** — Build a dated brief on one existing customer from your CRM, email, calls, docs, chat, support and usage, check it against your brain and show what changed since last time. Read-only.
- **prospect-research** — Build a pre-first-touch brief on one company you do not sell to yet: dated signals mapped to your pains, fit and timing scored separately, a hypothesis with angle, first question and fallback. Checks the CRM first, applies EMEA data defaults, proposes what other skills should learn. Never writes outreach.

## Commands (2)

- `/pmm-sales:customer-context` — Get the current state of one customer.
- `/pmm-sales:prospect-research` — Get the reason, angle and first question for one prospect.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`.

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | customer record, renewal, open opps, contacts | HubSpot |
| `~~team chat` | the thread you ask in; internal escalations | Slack |
| `~~email` | threads with the customer's domain | Gmail |
| `~~calendar` | recent and upcoming meetings | Google Calendar |
| `~~call recordings` | latest call, objections, customer phrases | Gong, Wispr Flow, Granola |
| `~~cloud storage` | account plans; saves the full brief | Google Drive, Google Docs |
| `~~knowledge base` | account plans and notes | Notion, Atlassian |
| `~~support` | escalations by theme | Intercom |
| `~~product analytics` | adoption trend | Amplitude (US and EU), Mixpanel (US and EU) |
| `~~company data` | funding, size, headcount, hiring | Crunchbase |
| `~~web research` | news and pages about the company | Exa |
| `~~enrichment` | company fields (docs only, no server) | none wired: paste, or connect your own server |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
