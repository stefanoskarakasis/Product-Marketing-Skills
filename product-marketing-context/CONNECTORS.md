# product-marketing-context connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~knowledge base` | Product Context, Market Context | Notion, Atlassian |
| `~~CRM` | ICP Definition (win/loss, deal data) | HubSpot |
| `~~call recordings` | ICP, Alternatives, Proof Points (buyer language, objections) | Gong, Wispr Flow |
| `~~market data` | Alternatives and Market Context | Semrush |
| `~~support` | ICP pain points, Voice and Tone | Intercom |
| `~~cloud storage` | Product Context and Proof Points: decks, pricing, case studies, working docs and sheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~team chat` | Voice and Tone, Proof Points (field feedback, win threads) | Slack |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~email` | customer and stakeholder email threads | Gmail |
| `~~design` | design files and assets referenced in PRDs | Figma, Canva |
| `~~marketing analytics` | cross-channel campaign and spend performance | Supermetrics |
| `~~SEO` | keyword and content demand signals | Semrush |
| `~~product analytics` | activation, adoption and retention metrics | Amplitude (US and EU), Mixpanel (US and EU) |
| `~~project tracker` | launch tasks and ticket context | Linear, Asana |
| `~~win/loss` | buyer interviews and research on why deals were won or lost | none wired: paste, or connect your own server |
| `~~reviews` | public review themes (G2 and similar) | none wired: paste, or connect your own server |
| `~~competitive intelligence` | competitor cards and win/loss stories your CI team already keeps | none wired: paste, or connect your own server |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~email marketing` | lifecycle email performance | Klaviyo |
| `~~revenue intelligence` | pipeline health, forecast and sales-engagement activity | none wired: paste, or connect your own server |
| `~~data warehouse` | your own product, pipeline and revenue tables | none wired: paste, or connect your own server |
| `~~video meetings` | meeting recordings, transcripts and summaries from your video tool | none wired: paste, or connect your own server |
| `~~enrichment` | company and contact enrichment for named accounts | none wired: paste, or connect your own server |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, google-sheets, google-slides, linear, figma, canva, gmail, google-calendar, klaviyo, supermetrics, amplitude, amplitude-eu, mixpanel, mixpanel-eu, asana, wispr-flow, semrush, crunchbase, exa.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
