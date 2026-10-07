# pmm-positioning connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~call recordings` | buyer language, objections, alternatives named on calls | Fireflies, Gong |
| `~~CRM` | win/loss reasons and segment data | HubSpot |
| `~~market data` | competitor and market signals | SimilarWeb |
| `~~support` | pain points and churn language | Intercom |
| `~~knowledge base` | internal positioning and market notes | Notion, Atlassian |
| `~~SEO` | keyword demand and competitor organic positioning | Ahrefs |
| `~~team chat` | win threads and field feedback | Slack |
| `~~cloud storage` | existing decks, case studies, docs and sheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~email` | customer and stakeholder email language for positioning | Gmail |
| `~~calendar` | stakeholder meetings and customer call dates | Google Calendar |
| `~~reviews` | public review themes (paste only today) | none wired |
| `~~product analytics` | usage evidence for proof points (paste only today) | none wired |

Servers in this plugin's `.mcp.json`: fireflies, gong, hubspot, similarweb, intercom, notion, atlassian, ahrefs, slack, google-drive, gmail, google-calendar, google-docs, google-sheets, google-slides.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
