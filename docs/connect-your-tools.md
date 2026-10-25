# Connect your tools

Connectors are optional. Every skill works if you paste your material instead.
Connect a tool when you want skills to pull candidate facts for you to confirm.

## How it works

1. Install a plugin on its own from the marketplace (see the README). Each plugin ships a `.mcp.json` listing the tools it can use.
2. The first time Claude uses a tool, it asks you to sign in. Approve it.
3. Pulled facts arrive as drafts, tagged with category, tool and date. Nothing is saved to your brain until you confirm it.

The `product-marketing-context` plugin wires every connector in the catalog. Other plugins wire only what their skills read. If you load the repo root as a single plugin instead, the root `.mcp.json` carries the whole catalog. Use one path, not both. If a tool does not show up, install the plugin that wires it on its own.

## Personal setup: nothing is connected for you

This repo lists connectors. It never connects them. Every product marketer who
installs a plugin signs in with their own account, and Claude only sees what
that account can see. No keys, tokens or passwords live in this repo.

- Connect only what you use. A server you do not sign in to is simply not used.
- A different tool in the same category works too (for example Salesforce for CRM). See [make-it-yours.md](make-it-yours.md).
- Run `/mcp` any time to see what is connected.

## Tools

<!-- generated:tools-table begin -->
| Tool | Category | Sign-in | Unlocks | If it fails |
|---|---|---|---|---|
| Notion | knowledge base | Notion login, choose pages to share | Company and product docs | Share the pages with the integration |
| Atlassian | knowledge base | Atlassian login | Confluence docs | Confirm site access |
| HubSpot | CRM | HubSpot login | Win/loss and deal data | Needs permission to read deals |
| Gong | call recordings | Gong admin approval usually needed | Transcripts for ICP, alternatives, proof points | Ask your Gong admin to enable the MCP integration |
| Intercom | support | Intercom login | Support themes and pain points | Needs read access to conversations |
| Slack | team chat | Slack login | Launch and field threads; questions, answers and approvals in tagged threads | Join the channels you want read. To tag Claude in a channel, ask your Slack admin to add it (see docs/slack-setup.md) |
| Google Drive | cloud storage | Google login | Find and read files, decks and PDFs | Same: use the built-in Claude connector if the plugin sign-in fails |
| Google Docs | cloud storage | Google login | Read and draft documents | Google lists this server as Developer Preview. If sign-in fails, use Drive or paste the text |
| Google Sheets | cloud storage | Google login | Read metric and planning sheets | Same Developer Preview note. If sign-in fails, export to CSV and paste |
| Google Slides | cloud storage | Google login | Read existing decks | Same Developer Preview note. If sign-in fails, use Drive or paste the text |
| Linear | project tracker | Linear login | Launch tasks | Check workspace access |
| Figma | design | Figma login | Design files for PRDs | Share the file |
| Canva | design | Canva login | Launch assets and designs | Open the design to your account |
| Gmail | email | Google login | Customer and stakeholder email threads | If sign-in fails, enable the built-in Claude Gmail connector in Claude settings instead |
| Google Calendar | calendar | Google login | Meeting cadence, launch dates | Same: use the built-in Claude connector if the plugin sign-in fails |
| Klaviyo | email marketing | Klaviyo login | Lifecycle email performance | Needs access to the Klaviyo account |
| Supermetrics | marketing analytics | Supermetrics login | Cross-channel campaign performance | Needs a Supermetrics plan with the data sources you want |
| Amplitude | product analytics | Amplitude login | Usage and adoption metrics | EU workspaces use the separate `amplitude-eu` server. Ignore the one that does not match your region |
| Mixpanel | product analytics | Mixpanel login | Usage and funnel metrics | US and EU workspaces use separate servers (`mixpanel`, `mixpanel-eu`). Ignore the one that does not match your region. India workspaces: add `https://mcp-in.mixpanel.com/mcp` as a custom connector |
| Asana | project tracker | Asana login | Launch tasks and project context | This repo uses Asana's v2 server. Asana's older SSE address is deprecated |
| Wispr Flow | call recordings | Wispr Flow account, browser sign-in | Meeting transcripts, summaries and notes from Wispr Flow Notetaker | Needs Notetaker and MCP access on your account, and an active HIPAA agreement blocks it. Wispr's docs do not cover Claude Code: if sign-in fails, add it as a connector in Claude settings, or paste transcripts |
| Semrush | market data, SEO | Semrush login (OAuth) | Competitor traffic, keyword demand and organic positioning | Needs a Semrush plan with API units. SEO data comes with Semrush One or SEO Classic plans, traffic and market data with the Trends API |
| Crunchbase | company data | Crunchbase login (OAuth) | Funding, headcount and leadership changes for a named company | Needs a Crunchbase MCP seat assigned by your workspace admin. In Claude Code the connector only loads when you are signed in with a Claude.ai subscription, not an API key |
| Exa | web research | None needed: free and rate-limited | Web search and page fetch for competitor and market signals | Rate-limited without an account. For your own Exa usage, add `https://mcp.exa.ai/mcp?login` as a custom connector |
<!-- generated:tools-table end -->

## Connect your own (not wired here)

These tools are in the category list, but this repo does not wire them. Either the vendor gives each customer their own endpoint, the server needs a vendor app or plan first, or no official server exists. If your vendor offers an MCP server, add it as a custom connector in Claude settings (see [make-it-yours.md](make-it-yours.md)) and the skills use it through the category. Otherwise paste an export. The table says what each vendor's own pages said in October 2026. Check yours before relying on it.

<!-- generated:own-table begin -->
| Tool | Category | What the vendor documents | What to do |
|---|---|---|---|
| Salesforce | CRM | Hosted MCP servers use per-user OAuth 2.0 with PKCE and are aimed at customers with Flex Credits. The docs give no public endpoint | Ask your Salesforce admin for your org's server address |
| GitHub | project tracker | GitHub hosts an official remote server at `https://api.githubcopilot.com/mcp/`. Sign-in needs either a personal access token or an OAuth app that your host has been set up with. Whether Claude Code's own OAuth works with it is not confirmed | Add it yourself with your own token kept in your environment, or paste issues and release notes. Never put the token in `.mcp.json`; the structure check blocks it |
| Klue | competitive intelligence | Each customer gets their own endpoint and sign-in | Ask your admin or customer success manager |
| Zendesk | support | No official general-purpose hosted server was found as of August 2026. Partner and community servers exist. Zendesk is retiring API tokens (none can be created from 27 October 2026), so token-based community servers will stop working | Paste an export, or use a partner server that signs in with OAuth |
| Snowflake | data warehouse | Managed server with one endpoint per database and schema: `https://<account_url>/api/v2/databases/{database}/schemas/{schema}/mcp-servers/{name}`. Snowflake OAuth | Create the server in your account, then add it as a custom connector |
| Zoom | video meetings | Zoom hosts an official server over streamable HTTP. Its docs page does not list the address or sign-in steps | Take the address from Zoom's developer docs, or paste transcripts |
| Salesloft | revenue intelligence | Official read-only server, reported as an admin-enabled add-on for customers with an Agent package | Ask your Salesloft admin. Clari and Outreach: no official server found, paste exports |
| Pardot | email marketing | Only third-party servers found | Paste exports |
| Clay | enrichment | Runs on your machine as a CLI over stdio (`clay mcp`) and signs in with `clay login` or an API key in your environment | Add it as a local server in your own Claude settings. Never put the key in `.mcp.json`; the structure check blocks it |
| LinkedIn | company data | Only unofficial servers found | Paste exports. Avoid servers that scrape the site |
<!-- generated:own-table end -->

Pulled facts from any of these are drafts like any other connector output.

## Privacy

Connectors are read-only by default. Skills ask before writing to any external tool. Gmail in particular: skills only read threads you point them at. The brain plugin loads every Google server. Other plugins load only the Google servers their skills use (see the Google table in `CONNECTORS.md`).

## Adding or changing a connector

Edit `connectors.json`. See [add-a-connector.md](add-a-connector.md).
