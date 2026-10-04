# Connect your tools

Connectors are optional. Every skill works if you paste your material instead.
Connect a tool when you want skills to pull candidate facts for you to confirm.

## How it works

1. Install a plugin on its own from the marketplace (see the README). Each plugin ships a `.mcp.json` listing the tools it can use.
2. The first time Claude uses a tool, it asks you to sign in. Approve it.
3. Pulled facts arrive as drafts, tagged with category, tool and date. Nothing is saved to your brain until you confirm it.

Installing the whole bundle through the root `pmm-skills` entry may not load the per-plugin connectors. If a tool does not show up, install the plugin on its own.

## Tools

| Tool | Category | Sign-in | Unlocks | If it fails |
|---|---|---|---|---|
| Fireflies | call recordings | Fireflies account | Transcripts for ICP, alternatives, proof points | Check your plan includes API access |
| Gong | call recordings | Gong admin approval usually needed | Same as Fireflies | Ask your Gong admin to enable the MCP integration |
| HubSpot | CRM | HubSpot login | Win/loss and deal data | Needs permission to read deals |
| Notion | knowledge base | Notion login, choose pages to share | Company and product docs | Share the pages with the integration |
| Atlassian | knowledge base | Atlassian login | Confluence docs | Confirm site access |
| SimilarWeb | market data | API key or token required | Competitor traffic and market signals | Needs a SimilarWeb plan with API access |
| Intercom | support | Intercom login | Support themes and pain points | Needs read access to conversations |
| Slack | team chat | Slack login | Launch and field threads | Join the channels you want read |
| Amplitude | product analytics | Amplitude login (EU: separate server) | Usage and adoption metrics | EU workspaces use mcp.eu.amplitude.com |
| Pendo | product analytics | Pendo login | Adoption metrics | Check plan |
| Linear | project tracker | Linear login | Launch tasks | Check workspace access |
| Figma | design | Figma login | Design files for PRDs | Share the file |
| Ahrefs | SEO | Ahrefs API access | Keyword demand | Needs a plan with API access |
| Gmail, Google Calendar, Google Drive | email, calendar, cloud storage | Enable in Claude settings | Mail, calendar, Drive context | These are first-party Claude connectors, not in `.mcp.json` |

G2 and other review sites: no server is wired. Paste an export.

## Privacy

Connectors are read-only by default. Skills ask before writing to any external tool.
