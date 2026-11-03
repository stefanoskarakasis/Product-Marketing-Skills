# pmm-sales

Customer account context for sellers and CSMs, built for Slack first: tag Claude in a thread and get the current state of one customer, with the risks flagged and every line sourced.

## Start here

- **You get:** a short answer in the Slack thread, or a full brief in chat, Cowork or Claude Code: owner, renewal, who has really replied, the latest calls and threads, up to five flags, and a check against your brain (ICP fit, competitors, objections, claims you may use).
- **First command:** `/pmm-sales:customer-context` (works with pasted notes; no connector needed)
- **Try in Slack:** "@Claude catch me up on Northwind"
- **Try anywhere:** "Customer context for Northwind before Thursday's renewal call."
- **The brain:** sharper with a brain (Sections 2, 3 and 6 especially). With no brain it still builds the brief and says it was built without one. The brain-building skill is a separate plugin, `product-marketing-context`.

## Works wherever you are

| Where | What you get |
|---|---|
| Slack thread | A plain-text reply of about 150 words, answer first, sources in words, a Doc link for the full brief. Nothing internal in a channel with outside members |
| Claude chat | The full brief; offers a Google Doc afterwards |
| Claude Cowork | The full brief, saved to your folder |
| Claude Code | The full brief in markdown, saved to `/context/customers/` |
| Scheduled run | One brief per named customer, saved, one summary line posted to the channel you name |

## Set up Slack (about 10 minutes)

1. Install this plugin and `product-marketing-context`.
2. Add Claude to your Slack workspace and to the channel where your sellers ask (an internal channel, not one shared with customers).
3. Connect your own accounts for the tools you use (`/mcp` shows what is connected). Everything is optional; the CRM and email add the most.
4. In a thread, type: "@Claude catch me up on [a customer you know]".
5. Check the answer against your CRM once. Tell your PMM what was wrong.

Step-by-step sign-ins: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md).

## How it fits with the other plugins

- **This plugin (one customer, current state):** `customer-context`.
- **`pmm-competitive-intelligence`:** when a rival shows up in a customer, this plugin offers `competitive-battlecard` and, once two customers agree, proposes a change to `competitive-profile`.
- **`product-marketing-context`:** the brain this plugin reads. It never writes it. What it learns across customers (objections, customer phrases, stated outcomes) is proposed to the PMM, who confirms.

## Skills (1)

- **customer-context** — Build a dated brief on one existing customer from your CRM, email, calls, docs, chat, support and usage, check it against your brain and show what changed since last time. Slack first. Read-only for your brain, CRM and inbox. Use before a call, a renewal, an escalation or a handover.

## Commands (1)

- `/pmm-sales:customer-context` — Get the current state of one customer.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`. Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

| Category | What it adds | Tools |
|---|---|---|
| `~~CRM` | customer record, renewal and open opps, contacts, activities | HubSpot |
| `~~team chat` | the Slack thread you ask in; internal escalations | Slack |
| `~~email` | threads with the customer's domain | Gmail |
| `~~calendar` | recent and upcoming meetings | Google Calendar |
| `~~call recordings` | latest call, objections, customer phrases | Gong, Wispr Flow, Granola |
| `~~cloud storage` | account plans; saves the full brief as a Google Doc | Google Drive, Google Docs |
| `~~knowledge base` | internal account plans and notes | Notion, Atlassian |
| `~~support` | escalations by theme | Intercom |
| `~~product analytics` | adoption trend | Amplitude (US and EU), Mixpanel (US and EU) |

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
