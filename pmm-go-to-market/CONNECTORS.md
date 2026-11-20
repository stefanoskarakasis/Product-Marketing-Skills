# pmm-go-to-market connectors

Every connector is optional. All 4 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `beachhead-segment` | CRM, call recordings, market data |
| `go-to-market-strategy` | CRM, calendar, call recordings, email, market data, email marketing, marketing analytics |
| `gtm-motions` | CRM, email, email marketing, marketing analytics |
| `workflow-orchestrator` | No connector named in the skill |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | segment performance and pipeline context | HubSpot |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | launch coordination context | Slack |
| `~~email` | stakeholder and customer email threads | Gmail |
| `~~calendar` | launch dates and milestones | Google Calendar |
| `~~call recordings` | buyer language for beachhead and motion choices | Gong, Wispr Flow, Granola, Dovetail |
| `~~video meetings` | meeting recordings and summaries from calls with buyers | Zoom |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | launch docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | segment sizing and competitor signals | Semrush, Ahrefs |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush, Ahrefs |

## Marketing performance

How campaigns and lifecycle email perform.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~marketing analytics` | cross-channel performance | Supermetrics |
| `~~email marketing` | lifecycle and campaign performance | Klaviyo |

## Work and delivery

Where launch tasks and design files live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~design` | launch assets | Canva |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: hubspot, gong, slack, google-drive, google-docs, google-sheets, google-slides, canva, gmail, google-calendar, klaviyo, supermetrics, wispr-flow, semrush, ahrefs, granola, dovetail, zoom.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
