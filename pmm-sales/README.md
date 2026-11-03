# pmm-sales

Sales-facing context for sellers and CSMs, built for Slack first: tag Claude in a thread and get the current state of one customer, with risks flagged and every line sourced.

## Start here

- **You get:** a ~150-word answer in the Slack thread, or a full brief in chat, Cowork or Claude Code: owner, renewal, who has really replied, latest calls, up to five flags, and a check against your brain.
- **First command:** `/pmm-sales:customer-context`
- **Try:** "@Claude catch me up on Northwind before Thursday's renewal call"
- **The brain:** `customer-context` uses it for ICP fit, competitors, objections and approved claims. Without one it still runs and says so. Never writes to it.

## Skills (1)

- **customer-context** — Build a dated brief on one existing customer from your CRM, email, calls, docs, chat, support and usage, check it against your brain and show what changed since last time. Read-only.

## Commands (1)

- `/pmm-sales:customer-context` — Get the current state of one customer.

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
| `~~product analytics` | adoption trend | Amplitude, Mixpanel |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
