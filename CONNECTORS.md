# Connectors

Skills in this repo refer to tools by **category**, written with two tildes
before the category name, never by vendor. Each plugin ships its own
`.mcp.json` that wires the vendors its skills use (the brain plugin wires every one), and its own `CONNECTORS.md`
that lists which categories it uses. This file is the master list of
categories. Every category used in a plugin must exist here.

Connectors are optional. Every skill works without them: paste what you
have and the output has the same shape.

## Rules

1. Read-only by default. Ask before writing to any external tool.
2. Every pulled fact is tagged with category, tool and date.
3. Pulled facts are drafts until you confirm them.
4. Pulled proof points and quotes enter the registry unverified.
5. No connectors? Paste the material and continue.

## Categories

| Placeholder | What it provides | Wired today | Other tools that work |
|---|---|---|---|
| `~~knowledge base` | Company overview, product docs, pricing, positioning docs | Notion, Atlassian | Confluence, Guru, Google Drive |
| `~~CRM` | Win/loss reasons, deal data, segment performance | HubSpot | Salesforce (hosted MCP uses per-user OAuth but has no public endpoint: connect your own org's server), Pipedrive, Attio |
| `~~call recordings` | Sales and customer call transcripts, objections, buyer language | Gong, Wispr Flow | Chorus, Grain, Otter, Avoma |
| `~~market data` | Competitor traffic, audience and market-size signals | Semrush | Sensor Tower, Crunchbase |
| `~~support` | Support conversations, recurring pain points, churn language | Intercom | Zendesk (no official hosted server found: paste or connect a partner server), Front, Help Scout |
| `~~reviews` | Public reviews and win/loss themes (G2 etc.) | Docs-only today: paste exports | G2, Capterra, TrustRadius (export and paste) |
| `~~competitive intelligence` | Competitor cards, win/loss stories and profiles your CI team already curates | Docs-only today: connect your vendor's MCP server, or paste | Klue, Crayon, Kompyte, Contify |
| `~~win/loss` | Structured buyer interviews and win/loss reports: why deals were won or lost | Docs-only today: paste exports | Clozd, Primary Intelligence, Anecdote, Dovetail |
| `~~company data` | Funding, headcount, hiring and leadership changes for a named company | Crunchbase | PitchBook, LinkedIn (no official server: paste exports) |
| `~~SEO` | Keyword demand, competitor organic positioning | Semrush | Moz |
| `~~product analytics` | Usage, activation and adoption metrics | Amplitude (US and EU), Mixpanel (US and EU) | Heap, Google Analytics |
| `~~marketing analytics` | Cross-channel campaign and spend performance | Supermetrics | Google Analytics, Funnel, Windsor |
| `~~email marketing` | Lifecycle email and campaign performance | Klaviyo | Pardot (only third-party servers found: paste exports), Mailchimp, Customer.io |
| `~~team chat` | Team threads, launch coordination, field feedback | Slack | Microsoft Teams |
| `~~project tracker` | Launch tasks, roadmap items, ticket context | Linear, Asana | Jira, ClickUp, monday |
| `~~design` | Design files, prototypes and launch assets | Figma, Canva | Adobe Creative Cloud |
| `~~email` | Customer and stakeholder email context | Gmail | Outlook |
| `~~calendar` | Meeting cadence, launch dates and attendees | Google Calendar | Outlook Calendar |
| `~~cloud storage` | Decks, docs and spreadsheets in Drive | Google Drive, Google Docs, Google Sheets, Google Slides | OneDrive, SharePoint, Dropbox, Box |
| `~~revenue intelligence` | Pipeline health, forecast and sales-engagement activity | Docs-only today: Salesloft's server is an admin-enabled add-on, so ask your admin for the endpoint | Clari, Outreach |
| `~~data warehouse` | Your own product, pipeline and revenue tables | Docs-only today: Snowflake's endpoint is per account | BigQuery, Databricks |
| `~~video meetings` | Meeting recordings, transcripts and summaries from your video tool | Docs-only today: Zoom publishes an official server, take the address from Zoom | Google Meet, Microsoft Teams |
| `~~enrichment` | Company and contact enrichment for named accounts | Docs-only today: Clay runs locally as a CLI over stdio, so it cannot sit in `.mcp.json` | Apollo |
| `~~web research` | Open-web search and page fetch for competitor moves, launches and market signals | Exa | Any web-search MCP server |

Gmail, Google Calendar, Google Drive, Docs, Sheets and Slides can also be enabled as built-in
Claude connectors in Claude settings. If sign-in through a plugin fails,
use the built-in connector instead.

### Google connectors by plugin

The brain plugin (`product-marketing-context`) wires every Google server. Every other plugin wires only the Google servers its skills use, Calendar included: fewer sign-ins, fewer permissions. This table is generated from `connectors.json`. Do not edit it by hand.

<!-- generated:google-table begin -->
| Plugin | Gmail | Calendar | Drive | Docs | Sheets | Slides |
|---|---|---|---|---|---|---|
| product-marketing-context | yes | yes | yes | yes | yes | yes |
| pmm-positioning | yes | yes | yes | yes |  | yes |
| pmm-execution | yes | yes | yes | yes | yes | yes |
| pmm-go-to-market | yes | yes | yes | yes | yes | yes |
| pmm-growth | yes | yes | yes |  | yes |  |
| pmm-intelligence | yes | yes |  |  |  |  |
| pmm-competitive-intelligence | yes | yes | yes |  |  |  |
| pmm-toolkit | yes | yes | yes | yes | yes | yes |
| pmm-meta |  |  |  |  |  |  |
<!-- generated:google-table end -->

**Your own tool is not listed?** Skills ask for a category, not a vendor. Connect
any server in that category and the skill uses it. See `docs/make-it-yours.md`.

See `docs/connect-your-tools.md` for sign-in steps per tool.
