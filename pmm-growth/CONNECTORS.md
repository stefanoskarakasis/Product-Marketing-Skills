# pmm-growth connectors

Every connector is optional. All 5 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `customer-stories` | No connector named in the skill |
| `experiment-ideas` | email, cloud storage, product analytics, SEO, email marketing, marketing analytics |
| `pmm-metrics` | CRM, email, cloud storage, product analytics, email marketing, marketing analytics |
| `positioning-ideas` | No connector named in the skill |
| `value-prop-statements` | No connector named in the skill |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Customer and deal record

Where the account, the opportunity and the pipeline numbers live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | funnel and conversion data | HubSpot |

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | team threads, launch coordination, field feedback | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~call recordings` | customer calls and quotes to build stories from | Gong, Wispr Flow, Granola |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | metric sheets, past reports and experiment logs | Google Drive, Google Sheets |

## Customer health

Signals from customers you already have.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Mixpanel (US and EU) |

## Market and company data

Facts about competitors, markets and named companies.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~market data` | traffic and market benchmarks | Semrush, Ahrefs |
| `~~SEO` | keyword and content demand signals | Semrush, Ahrefs |

## Marketing performance

How campaigns and lifecycle email perform.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |
| `~~email marketing` | lifecycle email performance | Klaviyo |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: hubspot, gong, slack, google-drive, google-sheets, gmail, google-calendar, klaviyo, supermetrics, amplitude, amplitude-eu, mixpanel, mixpanel-eu, wispr-flow, semrush, ahrefs, granola.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
