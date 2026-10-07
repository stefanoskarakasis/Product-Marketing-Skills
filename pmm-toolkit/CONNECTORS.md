# pmm-toolkit connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~knowledge base` | source material for briefs and writing | Notion, Atlassian |
| `~~team chat` | thread context for briefs | Slack |
| `~~email` | email context for drafts and briefs | Gmail |
| `~~calendar` | project dates and stakeholder meetings | Google Calendar |
| `~~cloud storage` | source docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~design` | creative assets referenced in briefs | Canva |

Servers in this plugin's `.mcp.json`: notion, atlassian, slack, gmail, google-calendar, google-drive, canva, google-docs, google-sheets, google-slides.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
