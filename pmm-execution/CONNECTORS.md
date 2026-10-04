# pmm-execution connectors

Optional. Every skill in this plugin works without them: paste what you have
and the output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~call recordings` | interview and call transcripts for summaries | Fireflies, Gong |
| `~~knowledge base` | retro, PRD and OKR source docs | Notion, Atlassian |
| `~~project tracker` | launch tasks and ticket context | Linear |
| `~~design` | design files referenced in PRDs | Figma |

Servers in this plugin's `.mcp.json`: fireflies, gong, notion, atlassian, linear, figma.

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, treat pulled facts as drafts until confirmed, and
treat pulled proof points and quotes as unverified.
