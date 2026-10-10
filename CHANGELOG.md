# Changelog

## v1.4.0 — 2026-10-10

### Works without a brain

- `alternatives-map`, `ideal-customer-profile` and `proof-points` no longer stop when
  there is no brain. They work from the material you paste and, after you confirm,
  start `/foundation/brain.md` with their own section only. If files cannot be
  written, they show the block to save and never claim it was saved.
- `product-messaging-playbook` asks five Quick-Brain questions when there is no brain
  and nothing pasted, builds the playbook from the answers and labels it as such.
  It still never writes to the brain.
- `message-house` now offers two paths that work inside the plugin when there is no
  positioning: paste it, or run `positioning-messaging`.
- `SKILL-SPEC.md` v2.4.0: new missing-brain rule for brain-dependent skills.

### Try it first

- New `examples/example-brain.md`: a finished brain for a fictional company, with
  `examples/README.md` listing five prompts to try before building your own.
- The `brain-template.md` reference example no longer attributes invented numbers and
  quotes to a real company; it points to the fictional example instead.
- Each plugin README opens with a "Start here" block: the outcome, the first command,
  a prompt to try, and whether it needs the brain.

### Evidence

- New `docs/eval-results.md` records which evals have been run. Nothing is marked as
  passed yet.

## v1.3.0 — 2026-10-10

### Customer stories

- New skill `customer-stories` in `pmm-growth`: runs a story from kickoff to customer
  approval. Kickoff questions and an internal brief, interview questions, a draft in
  one fixed seven-block structure (before, decision, rollout, results, people, limit,
  next), the customer review pack, and an audit of a finished story. You choose the
  depth (short, standard, deep) and the angle before drafting.
- Asks for the names and departments of everyone involved and never assumes them. A
  stage and next action are tracked per story. Permission is recorded per use, and a
  cannot-say list is binding on every draft.
- Every stat needs a baseline, period, denominator, source and status; every quote
  needs a named speaker, title and job. Gaps become placeholders; nothing is invented.
  "Up to" claims need the typical value. Runs an 8-point gate on its own draft before handover.
- Keeps a story ledger at `/context/customer-stories.md` and logs each session to
  `/context/skill-sessions.md`. Confirmed claims are handed to `proof-points`.
- Added `/pmm-growth:customer-stories`, a `~~call recordings` connector category
  (Fireflies, Gong) to `pmm-growth`, and a next-skill-map entry.
- `writing-assistant` v2.4.1 points case-study requests to the ledger and to
  `customer-stories` when a verified story is needed.
- `SKILL-SPEC.md` v2.3.1: the Learning Close template now includes `type: execution`
  and the five-field shape, matching `skill-sessions-format.md`.

### Cleanup

- Reworded "four-field" session-log language to the five-field shape (`type`, `skill`,
  `session_date`, `pattern`, `source`) in 5 skills' Verification and Quality Gate lines
  and in 18 eval files. The skills already wrote `type: execution`; only the wording and
  eval checks were stale.
- Removed the `google-prune-upload/` staging folder. Every file in it was identical to,
  or older than, the live copy.

## v1.2.0 — 2026-10-10

### pmm-positioning

- Removed the hard `dependencies: ["product-marketing-context"]` entry from
  `pmm-positioning`'s `plugin.json` and `marketplace.json` entry. That
  dependency lived in a different marketplace than the one `pmm-positioning`
  is submitted to, which Claude Code can't auto-resolve across marketplaces —
  the result was a silent `dependency-unsatisfied` disable: the whole plugin
  loaded with zero skills and zero commands, with no visible error. All
  eight skills already handle a missing brain gracefully (hard-block and
  redirect, or soft-warn and continue); this fix lets that logic actually
  run. Fixes #1.

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
