# product-marketing-context connectors

Every connector is optional. The skill works without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | ICP Definition (win/loss, deal data) | HubSpot |
| `~~revenue intelligence` | pipeline health, forecast and sales-engagement activity | none wired: paste, or connect your own server |
| `~~win/loss` | buyer interviews and research on why deals were won or lost | none wired: paste, or connect your own server |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | Voice and Tone, Proof Points (field feedback, win threads) | Slack |
| `~~email` | customer and stakeholder email threads | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~call recordings` | ICP, Alternatives, Proof Points (buyer language, objections) | Gong, Wispr Flow, Granola, Dovetail |
| `~~video meetings` | meeting recordings, transcripts and summaries from your video tool | Zoom |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | Product Context and Proof Points: decks, pricing, case studies, working docs and sheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~knowledge base` | Product Context, Market Context | Notion, Atlassian |
| `~~data warehouse` | your own product, pipeline and revenue tables | none wired: paste, or connect your own server |

## Customer health

Signals from customers you already have.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~support` | ICP pain points, Voice and Tone | Intercom |
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Mixpanel (US and EU) |
| `~~reviews` | public review themes (G2 and similar) | none wired: paste, or connect your own server |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | Alternatives and Market Context | Semrush, Ahrefs |
| `~~SEO` | keyword and content demand signals | Semrush, Ahrefs |
| `~~competitive intelligence` | competitor cards and win/loss stories your CI team already keeps | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |
| `~~enrichment` | company and contact enrichment for named accounts | none wired: paste, or connect your own server |

## Marketing performance

How campaigns and lifecycle email perform.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |
| `~~email marketing` | lifecycle email performance | Klaviyo |

## Work and delivery

Where launch tasks and design files live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~project tracker` | launch tasks and ticket context | Linear, Asana, monday.com, Productboard |
| `~~design` | design files and assets referenced in PRDs | Figma, Canva |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, google-sheets, google-slides, linear, figma, canva, gmail, google-calendar, klaviyo, supermetrics, amplitude, amplitude-eu, mixpanel, mixpanel-eu, asana, wispr-flow, semrush, crunchbase, exa, ahrefs, monday, productboard, granola, dovetail, zoom.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
