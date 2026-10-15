# pmm-go-to-market connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | segment performance and pipeline context | HubSpot |
| `~~market data` | segment sizing and competitor signals | Semrush |
| `~~call recordings` | buyer language for beachhead and motion choices | Gong, Wispr Flow |
| `~~team chat` | launch coordination context | Slack |
| `~~email marketing` | lifecycle and campaign performance | Klaviyo |
| `~~marketing analytics` | cross-channel performance | Supermetrics |
| `~~design` | launch assets | Canva |
| `~~email` | stakeholder and customer email threads | Gmail |
| `~~calendar` | launch dates and milestones | Google Calendar |
| `~~cloud storage` | launch docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: hubspot, gong, slack, google-drive, google-docs, google-sheets, google-slides, canva, gmail, google-calendar, klaviyo, supermetrics, wispr-flow, semrush.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
