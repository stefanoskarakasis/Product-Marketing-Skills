# pmm-sales connectors

Every connector is optional. All 9 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `customer-context` | CRM, revenue intelligence, calendar, call recordings, email, team chat, cloud storage, knowledge base, product analytics, support |
| `deal-review` | CRM, calendar, call recordings, email, team chat, cloud storage, knowledge base |
| `discovery-call-prep` | CRM, revenue intelligence, calendar, call recordings, email, team chat, cloud storage, knowledge base, company data, enrichment, web research |
| `discovery-call-scoring` | CRM, calendar, call recordings, knowledge base |
| `objection-handling` | CRM, call recordings, email, team chat, cloud storage, knowledge base |
| `prospect-research` | CRM, calendar, call recordings, email, team chat, cloud storage, knowledge base, company data, enrichment, web research |
| `pipeline-digest` | CRM, calendar, call recordings, email, team chat, cloud storage, knowledge base |
| `sales-collateral` | CRM, call recordings, win/loss, calendar, team chat, cloud storage, knowledge base |
| `sales-research-digest` | CRM, team chat, cloud storage |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | customer or prospect record, renewal and open opps, contacts, activities, owner; deal outcome and loss reason, read-only, for `objection-handling` and `sales-collateral` win-loss, only after the owner approves; open deals with stage history, contact roles and activity, read-only, for `pipeline-digest` | HubSpot |
| `~~win/loss` | structured buyer interviews and win-loss reports, read-only, for `sales-collateral` win-loss | none wired: paste, or connect your own server |
| `~~revenue intelligence` | engagement and pipeline health for the customer (paste only today) | none wired: paste, or connect your own server |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | the Slack thread you ask in; internal escalations and deal desk threads; the weekly digest, and a DM per deal owner only after a yes that names it, for `pipeline-digest` | Slack |
| `~~email` | threads with the customer's domain | Gmail |
| `~~calendar` | recent and upcoming meetings, attendees | Google Calendar |
| `~~call recordings` | latest call, objections and customer phrases as said; `objection-handling` reads recent calls to build the objection library, and `sales-collateral` reads them for win-loss, only after the owner approves | Gong, Wispr Flow, Granola |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

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

## Market and company data

Facts about competitors, markets and named companies.

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
