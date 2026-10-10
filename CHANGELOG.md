# Changelog

## Unreleased

### Writing assistant

- `writing-assistant` v2.4.0 drafts marketing content: blog posts, landing pages,
  press releases, case studies, newsletters, and social posts. It takes audience,
  key messages, voice, and proof from the brain and asks once for what is missing,
  or lists its assumptions when told to just draft it.
- Added an Audit mode that names AI patterns and quotes the lines without rewriting.
- Added a routing step so Slack, email, and memo rewrites keep their zero-question
  behavior, with explicit rules for email vs newsletter and post vs blog post.
- Never invents stats, quotes, customer names, results, or search volume. Gaps become
  placeholders, and press release and case study quotes are always placeholders.
- Added `references/` format guides for the six formats plus an SEO checklist.
- Added `/pmm-toolkit:marketing-content` (and the in-skill `marketing-content`
  command). `homepage` now follows the landing-page guide.
- The skill now reads `/foundation/brain.md`. The old
  `.agents/product-marketing-context.md` file still works as a fallback.
- Rewrote the evals to the SPEC format: the original 3 tests plus 12 new ones.

### Connectors

- Added Google Docs, Google Sheets and Google Slides servers. Each plugin wires only
  the Google servers its skills use: Gmail and Calendar in execution,
  go-to-market and toolkit; Drive, Docs, Sheets and Slides in the brain; Drive,
  Docs and Slides in positioning; Drive and Sheets in growth. `pmm-meta` has none.
- Added `~~cloud storage` to the pmm-metrics and experiment-ideas connector blocks.

## v1.1.0 — 2026-10-04

### Connectors

- Added per-plugin `.mcp.json` and `CONNECTORS.md` for six plugins, a root
  `CONNECTORS.md` category registry, and `docs/connect-your-tools.md`.
- Added optional Connectors blocks and evals to the brain and fifteen skills.
- Added structure Check 5 for connector files.
- Wired Canva, Klaviyo, Supermetrics, Amplitude EU, Gmail, Google Calendar and
  Google Drive, and added Slack, Ahrefs and Notion to more plugins. Added
  `~~email marketing` and `~~marketing analytics` categories.
- Added the Slack OAuth client settings that Slack's MCP server needs.
- Added structure Check 6 that blocks credentials in `.mcp.json`, a
  "personal setup" section in the connect guide, `docs/make-it-yours.md`, and
  an "other tools that work" column in `CONNECTORS.md`.
- Added consistent display names for all plugins in the marketplace listing.
- Added a Connectors section to `CLAUDE.md` and `CONTRIBUTING.md`, a connect
  step in `QUICK-START.md`, and an access-requirements note in the README.
- Fixed the dead `hs-proof-points-claims` reference in message-house and
  reset the pmm-positioning version to match the CHANGELOG.

## v1.0.0 — 2026-08-25

### Repo-wide

- Fixed broken JSON syntax in `.claude-plugin/marketplace.json` (unclosed
  array and object).
- Registered `pmm-foundation` (the `product-marketing-context` folder) as
  an installable plugin in `marketplace.json` and root `plugin.json` for
  the first time.
- Fixed the root `plugin.json`'s `skills` field from a single unparseable
  comma-joined string to a proper array; corrected the `pmm-meta` path.
- Fixed `pmm-meta/.claude-plugin/plugin.json`'s `skills` path, which
  pointed at a nonexistent `skills/` subfolder.
- Corrected `SKILL-SPEC.md`'s example skill lists to only cite skills
  that exist in this repo.
- Added `CLAUDE.md` establishing one version number across the entire
  repo, synced across every manifest.

### product-marketing-context (pmm-foundation)

- Added `.claude-plugin/plugin.json`, `README.md`, and
  `commands/build-brain.md` — this folder is now a proper installable
  plugin, not a bare skill folder.
- Removed the redundant `.skill/skill.json` manifest.
