# Make it yours

The skills in this repo ask for a **category** (call recordings, CRM, knowledge
base and so on), not a vendor. That is what lets each product marketer use their
own stack. Nothing here is connected for you and nothing needs to be edited for
the defaults to work.

## 1. Use the defaults you already have

Install the plugin, run `/mcp`, and sign in to the tools you use. Skip the rest.

## 2. Use a different tool in the same category

You use Salesforce, not HubSpot? Semrush, not Ahrefs? Connect your tool as a
server and the skills use it for that category.

**Claude Code:**

1. Find your tool's MCP server address in its documentation.
2. Run `claude mcp add --transport http <name> <address>`, for example a name like `salesforce`.
3. Run `/mcp` and sign in.

**Claude (web, desktop or Cowork):** go to Settings, then Connectors, then add a custom connector with the server address, and sign in.

Then ask a skill for the category as usual, for example "build my ICP from our CRM deals".

## 3. Change what a plugin ships with

If you maintain your own copy (a fork), edit the plugin's `.mcp.json` and
`CONNECTORS.md` together:

1. Add or remove the server in `.mcp.json` (each server needs `type` and `url`).
2. Name the server in that plugin's `CONNECTORS.md`.
3. Push. The structure check tells you if the two disagree.

The root `CONNECTORS.md` lists other tools that work per category.

## 4. Rules that keep it safe

- Never put an API key, token, password or authorization header in a `.mcp.json`. The structure check fails if you do. Sign in through OAuth instead.
- Connectors are read-only by default. Skills ask before writing to any tool.
- Pulled facts are drafts until you confirm them.
