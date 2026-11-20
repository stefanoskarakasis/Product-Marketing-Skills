# pmm-toolkit connectors

Every connector is optional. All 4 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `gaccs-brief` | calendar, email, team chat, cloud storage, knowledge base |
| `pmm-resume` | No connector named in the skill |
| `privacy-policy` | No connector named in the skill |
| `writing-assistant` | No connector named in the skill |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | thread context for briefs | Slack |
| `~~email` | email context for drafts and briefs | Gmail |
| `~~calendar` | project dates and stakeholder meetings | Google Calendar |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | source docs, sheets and decks | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~knowledge base` | source material for briefs and writing | Notion, Atlassian |

## Work and delivery

Where launch tasks and design files live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~design` | creative assets referenced in briefs | Canva |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, slack, google-drive, google-docs, google-sheets, google-slides, canva, gmail, google-calendar.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
