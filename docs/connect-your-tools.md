# Connect your tools

Connectors are optional. Every skill works if you paste your material instead.
Connect a tool when you want skills to pull candidate facts for you to confirm.

## How it works

1. Install a plugin on its own from the marketplace (see the README). Each plugin ships a `.mcp.json` listing the tools it can use.
2. The first time Claude uses a tool, it asks you to sign in. Approve it.
3. Pulled facts arrive as drafts, tagged with category, tool and date. Nothing is saved to your brain until you confirm it.

The `product-marketing-context` plugin wires only the nine connectors it reads from when it builds your brain. Other plugins wire only what their skills read. If you load the repo root as a single plugin instead, the root `.mcp.json` carries the whole catalog. Use one path, not both. If a tool does not show up, install the plugin that wires it on its own.

## Personal setup: nothing is connected for you

This repo lists connectors. It never connects them. Every product marketer who
installs a plugin signs in with their own account, and Claude only sees what
that account can see. No keys, tokens or passwords live in this repo.

- Connect only what you use. A server you do not sign in to is simply not used.
- A different tool in the same category works too (for example Salesforce for CRM). See [make-it-yours.md](make-it-yours.md).
- Run `/mcp` any time to see what is connected.

## Start read-only

1. **Make the first call a read.** After you sign in, ask for one harmless result, such as "list my five most recent calls" or "show one deal's stage". Check it matches what you expect before you run a skill.
2. **Give the least access.** Choose read scopes, one workspace or one test folder first. Widen later.
3. **Skills read; they do not write to your tools.** The few that post, such as a reply in the Slack thread where you tagged Claude, say so in their Outputs section. Anything a skill wants to change in your brain is shown as exact text and waits for your yes.
4. **Check what is connected** with `/mcp`. Remove a server there when you stop using it.

**For your IT or security reviewer:** no credentials live in this repo, every person signs in with their own account, the servers are listed in `connectors.json`, and each plugin wires only what its skills read. See [SECURITY.md](../SECURITY.md).

## What each plugin wires

Skills work without connectors. Connectors load per plugin: install `product-marketing-context` and you get the whole catalog; each other plugin wires only what its skills read.

<!-- generated:plugin-table begin -->
| Plugin | Connectors wired |
|---|---|
| product-marketing-context | Notion, Atlassian, HubSpot, Gong, Intercom, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Linear, Figma, Canva, Gmail, Google Calendar, Klaviyo, Supermetrics, Amplitude (US and EU), Mixpanel (US and EU), Asana, Wispr Flow, Semrush, Crunchbase, Exa, Ahrefs, monday.com, Productboard, Granola, Dovetail, Zoom |
| pmm-positioning | Notion, Atlassian, HubSpot, Gong, Intercom, Slack, Google Drive, Google Docs, Google Slides, Gmail, Google Calendar, Mixpanel (US and EU), Wispr Flow, Semrush, Ahrefs, Granola, Dovetail, Zoom |
| pmm-execution | Notion, Atlassian, Gong, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Linear, Figma, Canva, Gmail, Google Calendar, Asana, Wispr Flow, monday.com, Productboard, Granola |
| pmm-go-to-market | HubSpot, Gong, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Canva, Gmail, Google Calendar, Klaviyo, Supermetrics, Wispr Flow, Semrush, Ahrefs, Granola, Dovetail, Zoom |
| pmm-growth | HubSpot, Gong, Slack, Google Drive, Google Sheets, Gmail, Google Calendar, Klaviyo, Supermetrics, Amplitude (US and EU), Mixpanel (US and EU), Wispr Flow, Semrush, Ahrefs, Granola |
| pmm-intelligence | Slack, Gmail, Google Calendar, Semrush, Crunchbase, Exa, Ahrefs |
| pmm-competitive-intelligence | Notion, Atlassian, HubSpot, Gong, Slack, Google Drive, Google Docs, Gmail, Google Calendar, Wispr Flow, Semrush, Crunchbase, Exa, Ahrefs, Granola, Dovetail, Zoom |
| pmm-toolkit | Notion, Atlassian, Slack, Google Drive, Google Docs, Google Sheets, Google Slides, Canva, Gmail, Google Calendar |
| pmm-sales | Notion, Atlassian, HubSpot, Gong, Intercom, Slack, Google Drive, Google Docs, Gmail, Google Calendar, Amplitude (US and EU), Mixpanel (US and EU), Wispr Flow, Crunchbase, Exa, Granola |
| pmm-meta | None |
<!-- generated:plugin-table end -->

Some connectors need extra access: Semrush needs an API plan,
Gong usually needs an admin to enable it, Crunchbase needs a workspace seat, and Wispr Flow needs
Notetaker and MCP access on your account. Salesforce, GitHub, Zendesk,
Snowflake, Zoom, Salesloft, Clay and other tools with no public endpoint are
connect-your-own or paste-only. The brain plugin (`product-marketing-context`) wires the nine connectors it reads from. Every other plugin wires only the tools its skills read. Install each plugin on its own to load its connectors (see Installation). To add or change a connector, edit `connectors.json` ([how](add-a-connector.md)). Sign-in steps: [docs/connect-your-tools.md](connect-your-tools.md). Competitor answers in a Slack thread: [docs/slack-setup.md](slack-setup.md). Category registry: [CONNECTORS.md](../CONNECTORS.md).

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
| Ahrefs | market data, SEO | Ahrefs login (OAuth) | Competitor backlinks, organic keywords and traffic | Needs a paid Ahrefs plan (Lite or higher). OAuth keys default to a monthly API unit limit that a workspace admin can change |
| monday.com | project tracker | monday.com login (OAuth) | Launch boards, tasks and owners | Ask your monday.com admin to allow the connector for your account |
| Productboard | project tracker | Productboard login (OAuth) | Roadmap items and customer feedback notes | A workspace admin must switch on Settings > Integrations > MCP server and allow your role |
| Granola | call recordings | Granola login (OAuth, no keys to paste) | Meeting notes and transcripts for ICP, alternatives and proof points | Folders and transcripts need a paid Granola plan. On Enterprise an admin chooses which notes members can reach |
| Dovetail | call recordings | Dovetail login (OAuth) | Customer interview transcripts, highlights and insights | Dovetail does not support automatic client registration. If sign-in fails, add it as a custom connector with an API token kept in your environment |
| Zoom | video meetings | Zoom login (OAuth 2.1) | Meeting content and recordings (Zoom Meetings server) | Zoom documents this Meetings address as an example endpoint. Your Zoom admin may need to approve the app |
<!-- generated:tools-table end -->


### Call recorders: any of them works

Skills that read calls (`discovery-call-prep`, `discovery-call-scoring`, `objection-handling`, `deal-review`) need a transcript or AI notes, not a particular vendor. Order: a recorder connector from the table above; the recorder's own transcript saved where Claude can read it (Google Meet transcripts and Gemini notes land in the organiser's Drive, Zoom cloud transcripts and Teams transcripts export as files); a drop folder your owner names; or a paste. Which transcripts exist depends on your plan and on whether people turn recording on. Reading calls is the owner's decision, per source, and only for calls your company already records.

## Connect your own (not wired here)

These tools are in the category list, but this repo does not wire them. Either the vendor gives each customer their own endpoint, the server needs a vendor app or plan first, or no official server exists. If your vendor offers an MCP server, add it as a custom connector in Claude settings (see [make-it-yours.md](make-it-yours.md)) and the skills use it through the category. Otherwise paste an export. The table says what each vendor's own pages said in October 2026. Check yours before relying on it.

<!-- generated:own-table begin -->
| Tool | Category | What the vendor documents | What to do |
|---|---|---|---|
| Salesforce | CRM | Official hosted servers, one per capability: `https://api.salesforce.com/platform/mcp/v1/<SERVER-NAME>` (sandbox: `.../v1/sandbox/<SERVER-NAME>`). Sign-in is OAuth through an External Client App your admin creates in your org | Ask your Salesforce admin for the External Client App consumer key and the server name, then add it as a custom connector |
| Microsoft 365 | cloud storage | Anthropic's Microsoft 365 connector searches SharePoint, OneDrive, Outlook and Teams. It has no public server address and needs a Microsoft Entra Global Administrator to approve it once | Turn it on from the Connectors page in Claude (a Claude organization owner enables it first on Team and Enterprise plans) |
| Box | cloud storage | Official remote server at `https://mcp.box.com`. Your Box admin creates the client ID and secret in the Admin Console | Ask your Box admin, then add it as a custom connector with those credentials kept in your environment |
| GitHub | knowledge base | Reads a brain stored as a file in a repository. This repo wires no GitHub server; use the one your organization approves | Ask your admin which GitHub MCP server is approved, add it as a custom connector, then set brain_source: github in the prospect-research config |
| Zendesk | support | No official hosted server. Community servers use API tokens, which Zendesk is retiring | Paste a ticket export, or use a partner server that signs in with OAuth |
| GitHub | project tracker | GitHub hosts an official remote server at `https://api.githubcopilot.com/mcp/`. Sign-in needs either a personal access token or an OAuth app that your host has been set up with. Whether Claude Code's own OAuth works with it is not confirmed | Add it yourself with your own token kept in your environment, or paste issues and release notes. Never put the token in `.mcp.json`; the structure check blocks it |
| Klue | competitive intelligence | Each customer gets their own endpoint and sign-in | Ask your admin or customer success manager |
| Snowflake | data warehouse | Managed server with one endpoint per database and schema: `https://<account_url>/api/v2/databases/{database}/schemas/{schema}/mcp-servers/{name}`. Snowflake OAuth | Create the server in your account, then add it as a custom connector |
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
