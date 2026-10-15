# pmm-positioning connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~call recordings` | buyer language, objections, alternatives named on calls | Gong, Wispr Flow |
| `~~CRM` | win/loss reasons and segment data | HubSpot |
| `~~market data` | competitor and market signals | Semrush |
| `~~support` | pain points and churn language | Intercom |
| `~~knowledge base` | internal positioning and market notes | Notion, Atlassian |
| `~~SEO` | keyword demand and competitor organic positioning | Semrush |
| `~~team chat` | win threads and field feedback | Slack |
| `~~cloud storage` | existing decks, case studies and docs | Google Drive, Google Docs, Google Slides |
| `~~reviews` | public review themes (paste only today) | none wired: paste, or connect your own server |
| `~~product analytics` | usage evidence for proof points | Mixpanel (US and EU) |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, google-slides, gmail, google-calendar, mixpanel, mixpanel-eu, wispr-flow, semrush.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
