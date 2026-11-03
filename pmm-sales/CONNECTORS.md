# pmm-sales connectors

Optional. `customer-context` works without them: paste what you have and the
output has the same shape. Category definitions live in the root
`CONNECTORS.md`. Sign-in steps are in `docs/connect-your-tools.md`.

| Placeholder | What it adds here | Wired today |
|---|---|---|
| `~~CRM` | customer record, renewal and open opps, contacts, activities, owner | HubSpot |
| `~~team chat` | the Slack thread you ask in; internal escalations and deal desk threads | Slack |
| `~~email` | threads with the customer's domain | Gmail |
| `~~calendar` | recent and upcoming meetings, attendees | Google Calendar |
| `~~call recordings` | latest call, objections and customer phrases as said | Gong, Wispr Flow, Granola |
| `~~cloud storage` | account plan, success plan, contract docs; saves the full brief as a Google Doc | Google Drive, Google Docs |
| `~~knowledge base` | internal account plans and notes | Notion, Atlassian |
| `~~support` | open and recent escalations by theme | Intercom |
| `~~product analytics` | adoption trend and which teams use the product | Amplitude (US and EU), Mixpanel (US and EU) |
| `~~revenue intelligence` | engagement and pipeline health for the customer (paste only today) | none wired: paste, or connect your own server |

<!-- generated:servers begin -->
Servers in this plugin's `.mcp.json`: notion, atlassian, hubspot, gong, intercom, slack, google-drive, google-docs, gmail, google-calendar, amplitude, amplitude-eu, mixpanel, mixpanel-eu, wispr-flow, granola.
<!-- generated:servers end -->

Rules: read-only by default, ask before writing, tag every pulled fact with
category, tool and date, and treat pulled facts as drafts until confirmed.
This plugin never writes to a CRM or any other external tool.
