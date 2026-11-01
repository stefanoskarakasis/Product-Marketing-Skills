# Add or change a connector

Every connector this repo ships is listed in one file: [connectors.json](../connectors.json). You edit that file. A GitHub Action then rewrites everything that depends on it:

- each plugin's `.mcp.json` and the root `.mcp.json` (every server, for people who load the repo root as one plugin)
- the "Wired today" column of every `~~category` row in each `CONNECTORS.md` and plugin README
- the "Servers in this plugin's `.mcp.json`" line in each plugin's `CONNECTORS.md`
- the Google table in the root `CONNECTORS.md`
- the plugin table in the root `README.md`
- the Tools table and the "Connect your own" table in [connect-your-tools.md](connect-your-tools.md)

Never edit those by hand. The text between `<!-- generated:... begin -->` and `<!-- generated:... end -->` is overwritten on the next sync.

## Which plugin gets which server

- `product-marketing-context` (the brain) always gets every server in the file. You do not list it.
- Every other plugin gets a server only if you name it in that server's `"plugins"` list. Add a plugin only when its skills read the server's category, so people sign in to fewer tools and grant fewer permissions.

## Add a server that has a public address

1. Open `connectors.json` on GitHub and click the pencil icon.
2. Copy an existing block from `{` to `},` and paste it at the end of the `"servers"` list, before the closing `]`. Keep the comma between blocks.
3. Change every field:

| Field | What goes in it |
|---|---|
| `name` | Short lowercase id, no spaces. It becomes the key in `.mcp.json` |
| `tool` | Name people recognise, for example `Mixpanel` |
| `category` | A category that already exists in the root `CONNECTORS.md`, without the `~~`. A server can serve two: `"market data, SEO"` |
| `type` | `http` |
| `url` | The vendor's own server address, starting with `https://` |
| `plugins` | The plugins besides the brain that should load it, for example `["pmm-growth"]`, or `[]` for none |
| `signin` | One short phrase: how a person signs in |
| `unlocks` | What it gives the skills |
| `if_fails` | The first thing to try when sign-in fails |

4. Optional fields: `"label"` changes the name shown in the README (`""` hides it, used for regional twins such as `mixpanel-eu`), and `"docs": false` hides the row in the Tools table.
5. Commit directly to `main`. Wait about a minute and open the Actions tab. "Connectors sync" should turn green, and a second commit by `github-actions[bot]` appears with the regenerated files.

If the category is new, add its row to the root `CONNECTORS.md` first. Each plugin that loads the server also needs a row for that category in its own `CONNECTORS.md`. The sync fails with a plain message if either is missing.

## Add a tool that has no public address

Add a block to `"connect_your_own"` with `tool`, `category`, `documents` (what the vendor says, in your words) and `todo` (what a customer should do). Do not put a made-up or per-customer address in `"servers"`.

## Remove or move a server

Delete its block, or change its `"plugins"` list. Commit. The bot does the rest.

## Rules that never change

- No keys, tokens, headers or passwords in `connectors.json` or in any `.mcp.json`. Each person signs in with their own account. The checks block it.
- Read-only by default. Verify the address on the vendor's own page and update `"verified"` at the top when you re-check.
- A server that fails for every user gets removed here, not patched around.

## If the sync goes red

Open the failed run, open the red step and read the one line that explains it. The usual causes are a missing comma or quote in `connectors.json`, a category that is not in the root `CONNECTORS.md`, or a plugin `CONNECTORS.md` that lacks the category row.
