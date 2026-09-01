# CLAUDE.md

Repo-wide rules for AI agents and contributors working in this repository.
See also [AGENTS.md](AGENTS.md) for skill-authoring conventions and
[SKILL-SPEC.md](SKILL-SPEC.md) for the skill quality standard.

## Versioning & Releases

- **`CHANGELOG.md` is the source of truth.** The newest
  `## vX.Y.Z — YYYY-MM-DD` heading is the released version.
- **Keep every version in sync.** `.claude-plugin/marketplace.json`, every
  plugin's `.claude-plugin/plugin.json`, and the newest `CHANGELOG.md`
  heading always carry the same version number. There is no independent
  per-plugin versioning — a change to any one plugin bumps the version
  everywhere.
- **Semver:** breaking change = major. New skill, new command, or changed
  behavior = minor. Fix or docs-only change = patch.
- Every user-facing change gets a bullet in `CHANGELOG.md` under
  `## Unreleased` before it becomes part of a numbered release.

## Release Procedure (manual, until CI enforcement exists)

1. Rename `## Unreleased` in `CHANGELOG.md` to `## vX.Y.Z — YYYY-MM-DD`.
2. Set that same version number in `.claude-plugin/marketplace.json` and
   every `plugin.json` file in the repo (currently seven: root,
   `product-marketing-context`, `pmm-positioning`, `pmm-go-to-market`,
   `pmm-execution`, `pmm-toolkit`, `pmm-growth`, `pmm-meta`).
3. Commit all of the above together in one commit.

## After Any Repo Change

Before committing, ask: does this change reference a skill, command, or
file that actually exists? Check the folder, not just memory of what was
planned. This repo's biggest source of past errors was documentation
describing features that were never built.
