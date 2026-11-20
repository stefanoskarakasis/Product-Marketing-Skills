# pmm-execution connectors

Every connector is optional. All 8 skills work without them: paste what you have and the output keeps its shape.

- **Category definitions:** the root `CONNECTORS.md`.
- **Sign-in steps:** `docs/connect-your-tools.md`.
- **Install this plugin on its own** to load its `.mcp.json`.

## Which skill reads what

| Skill | Reads |
|---|---|
| `experiment-doc` | No connector named in the skill |
| `interview-summary` | call recordings, email |
| `pmm-okrs` | No connector named in the skill |
| `prd` | cloud storage, knowledge base, design, project tracker |
| `pre-mortem` | team chat, knowledge base, project tracker |
| `prioritization-frameworks` | No connector named in the skill |
| `retro` | calendar, team chat, knowledge base, project tracker |
| `stakeholder-maps` | calendar, email, team chat |

Derived from the connector placeholders each skill names. A placeholder that is not in the root registry is not listed.

## Conversations

Where the buyer and your team talk: threads, calls and meetings.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~team chat` | stakeholder and launch threads | Slack |
| `~~email` | customer and stakeholder email threads | Gmail |
| `~~calendar` | meeting cadence and attendees | Google Calendar |
| `~~call recordings` | interview and call transcripts for summaries | Gong, Wispr Flow, Granola |

## Documents and knowledge

Where plans, notes, data and your brain are stored, and where full outputs are saved.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~cloud storage` | specs, decks, docs and spreadsheets | Google Drive, Google Docs, Google Sheets, Google Slides |
| `~~knowledge base` | retro, PRD and OKR source docs | Notion, Atlassian |

## Work and delivery

Where launch tasks and design files live.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~project tracker` | launch tasks and ticket context | Linear, Asana, monday.com, Productboard |
| `~~design` | design files and assets referenced in PRDs | Figma, Canva |

## Servers

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, gong, slack, google-drive, google-docs, google-sheets, google-slides, linear, figma, canva, gmail, google-calendar, asana, wispr-flow, monday, productboard, granola.
<!-- generated:servers end -->

## Rules

- **Read-only by default.** Ask before writing.
- **Tag every pulled fact** with category, tool and date.
- **Treat pulled facts as drafts** until you confirm them.
- **Treat pulled proof points and quotes as unverified.**
