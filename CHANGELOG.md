# Changelog

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
- Removed `VERSIONS.md` — a fourth, stale version ledger superseded by
  this changelog and the `plugin.json` version-sync model.
- Rewrote `README.md`, `QUICK-START.md`, and `AGENTS.md` to remove
  references to a `competitive-battlecard` skill (never built), a
  `buyer-personas` skill (never built), and a "Compounding Loop" system
  (`/foundation/brain.md` auto-updates, `/context/skill-sessions.md`
  logging) that was described as live but was never actually built.
- Corrected `SKILL-SPEC.md`'s example skill lists to only cite skills
  that exist in this repo.
- Added `CLAUDE.md` establishing one version number across the entire
  repo, synced across every manifest.

### product-marketing-context (pmm-foundation)

- Added `.claude-plugin/plugin.json`, `README.md`, and
  `commands/build-brain.md` — this folder is now a proper installable
  plugin, not a bare skill folder.
- Removed the redundant `.skill/skill.json` manifest.
