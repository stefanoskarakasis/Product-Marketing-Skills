# pmm-sales connectors

Every connector is optional. All seven skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `customer-context` | CRM, calendar, call recordings, cloud storage, email, knowledge base, product analytics, revenue intelligence, support, team chat |
| `deal-review` | CRM, calendar, call recordings, cloud storage, email, knowledge base, team chat |
| `discovery-call-prep` | CRM, calendar, call recordings, cloud storage, company data, email, enrichment, knowledge base, revenue intelligence, team chat, web research |
| `discovery-call-scoring` | CRM, calendar, call recordings, knowledge base |
| `objection-handling` | CRM, call recordings, cloud storage, email, knowledge base, team chat |
| `prospect-research` | CRM, calendar, call recordings, cloud storage, company data, email, enrichment, knowledge base, team chat, web research |
| `sales-research-digest` | CRM, cloud storage, team chat |

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | customer or prospect record, renewal and open opps, contacts, activities, owner; deal outcome and loss reason, read-only, for `objection-handling`, only after the objection owner approves | HubSpot |
| `~~revenue intelligence` | engagement and pipeline health for the customer (paste only today) | none wired: paste, or connect your own server |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | the Slack thread you ask in; internal escalations and deal desk threads | Slack |
| `~~email` | threads with the customer's domain | Gmail |
| `~~calendar` | recent and upcoming meetings, attendees | Google Calendar |
| `~~call recordings` | latest call, objections and customer phrases as said; `objection-handling` reads recent calls to build the objection library, only after the objection owner approves | Gong, Wispr Flow, Granola |

## Documents and knowledge

Where plans, notes and your brain are stored, and where full briefs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | account plan, success plan, contract docs; saves the full brief as a Google Doc | Google Drive, Google Docs |
| `~~knowledge base` | internal account plans and notes; where your brain lives if it is in Notion | Notion, Atlassian |

## Customer health

Signals from customers you already have.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~support` | open and recent escalations by theme | Intercom |
| `~~product analytics` | adoption trend and which teams use the product | Amplitude (US and EU), Mixpanel (US and EU) |

## Prospect signals

Facts about a company you do not sell to yet.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~company data` | funding, size, headcount and hiring for a prospect (`prospect-research`) | Crunchbase |
| `~~web research` | open-web news and pages about a prospect (`prospect-research`) | Exa |
| `~~enrichment` | company fields for a prospect; contact fields withheld in EMEA mode (docs only today) | none wired: paste, or connect your own server |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, gmail, google-calendar, amplitude, amplitude-eu, mixpanel, mixpanel-eu, wispr-flow, crunchbase, exa, granola.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **This plugin never writes to a CRM** or any other external tool.
