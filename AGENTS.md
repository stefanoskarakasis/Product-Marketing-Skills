# AGENTS.md

Rules for AI agents and contributors working in this repository. Short on purpose: it points to where the detail lives. Claude Code reads it through the one-line `CLAUDE.md`.

## What this repo is

Product marketing skills for B2B SaaS PMMs and GTM operators: 47 skills in 10 plugins, with 55 commands, plus one shared brain (`foundation/brain.md`) that every skill reads. Skills are plain `SKILL.md` files that follow the [Agent Skills specification](https://agentskills.io/specification.md). The repo is also a Claude Code plugin marketplace through `.claude-plugin/marketplace.json`. Creator: Stefanos Karakasis. License: MIT.

## Where things live

| If the task is | Read |
|---|---|
| Writing or changing a skill | `SKILL-SPEC.md` (the canonical standard) |
| Brain sections, field keys, who may write what | `product-marketing-context/references/brain-schema.md` (the brain has 8 sections) |
| Adding or changing a connector | `docs/add-a-connector.md`, then edit `connectors.json` |
| Skill routing and trigger collisions | `docs/routing-checks.md`, `tests/test_triggers.py` |
| The agent map, helper scripts and send guard | `docs/agents-map.md` |
| Installing and using the repo | `README.md`, `QUICK-START.md` |
| Contributing | `CONTRIBUTING.md` |

## Layout

```
.claude-plugin/            marketplace.json and root plugin.json
product-marketing-context/ the brain skill, its schema, template and scripts/
pmm-positioning/           ICP, alternatives, messaging, proof points
pmm-go-to-market/          beachhead, GTM strategy, motions, orchestration
pmm-competitive-intelligence/  profiles, battlecards, briefing, newsletter, media monitoring, hooks/
pmm-intelligence/          signal-monitor
pmm-sales/                 customer-context, prospect-research, deal-review, sales-research-digest (Slack first)
pmm-execution/             OKRs, PRDs, retros, pre-mortems
pmm-growth/                metrics, ideas, value props, customer stories
pmm-toolkit/               writing, briefs, resume, privacy policy
pmm-meta/                  skill quality, learning, verification
context/                   guardrails read by every skill's pre-flight
docs/  examples/  scripts/  tests/  hooks/  .github/
```

## Commands

Skills are content, so there is no build. These checks run on every push:

- `python3 .github/scripts/check_structure.py` — manifests, paths, cross-references, connector files.
- `python3 -m unittest discover -s tests -v` — versions, counts, brain sections, routing, hooks, scripts.
- `python3 scripts/generate_connectors.py --write` — regenerates every `.mcp.json` and connector table from `connectors.json`.
- `python3 scripts/eval_sheet.py --priority` — builds the run sheet for the evals worth running first (`docs/run-the-evals.md`).

## Skill rules

- `name` matches the folder exactly: lowercase letters, digits and single hyphens, 1 to 64 characters.
- `description` is 1 to 1024 characters and keeps the trigger phrases.
- `SKILL.md` stays under 500 lines and 3,000 words (`tests/test_skill_size.py`). Heavy content goes to `references/`, loaded only when needed.
- `.cursor-plugin/` manifests mirror the Claude ones and carry no version. Add a plugin to both marketplaces. Their keys must fit Cursor's plugin schema (`author` takes only `name` and `email`); a test checks it.
- Name another skill or file only after checking that it exists in this repo.
- A skill cites only brain sections that exist in `brain-schema.md`. Sections 1 to 6 are required, 7 and 8 are recommended. Never invent a section and never renumber.
- A skill writes to the brain only where the schema allows, and only after the user confirms the exact before and after.
- Skills are nouns: frameworks Claude loads when a topic matches. Commands are verbs: `/plugin:command`, run by the user.
- Commands need `description`, plus `argument-hint` when they take arguments (`tests/test_command_frontmatter.py`). A command with no arguments goes on that test's `NO_ARGS` list.
- `pmm-positioning` is the exception: its skills and commands carry `name` and `description` only, because the plugin directory refuses other frontmatter keys. Its metadata lives in `pmm-positioning/skills.meta.json` (`tests/test_directory_frontmatter.py`).
- No cross-plugin references in commands. Suggest follow-ups in natural language only, because plugins install independently.

## What shows where

Edit the right text, and keep the ones that must match in sync.

| Text | Where people see it |
|---|---|
| `marketplace.json` description | Marketplace browser and Claude Code |
| `plugin.json` description | Plugin list. Keep it equal to that plugin's `README.md` |
| `SKILL.md` description | Skill list and auto-loading. Carries the trigger phrases |
| Command description and `argument-hint` | Shown when typing `/`. `pmm-positioning` has no hint |
| `README.md` | GitHub only, never loaded at runtime |

## Connectors

- Skills name tools by category with two tildes in backticks, never by vendor.
- Every category used in a skill is listed in that plugin's `CONNECTORS.md`, and every category there exists in the root `CONNECTORS.md`.
- A plugin that ships a `.mcp.json` names each server in its `CONNECTORS.md`. Each server needs `type` and `url`.
- Never commit credentials: no keys, tokens, passwords, `headers`, `env` or authorization values. Each user signs in with their own account.
- Never hand-edit a `.mcp.json` or text between `<!-- generated:... -->` markers. Edit `connectors.json` and run the generator.
- Connectors are read-only by default, pulled facts are drafts until the user confirms, and every skill with a connector block must still work by paste.

## Scripts and hooks

- Scripts that customers run live inside `product-marketing-context/scripts/`, because only skill folders travel with an install. `write_agents_map.py` copies two of them into the customer's `foundation/tools/`.
- The send guard lives in `pmm-competitive-intelligence/hooks/` and again in the root `hooks/`, so both install routes have it. The two copies must stay byte-identical; a test enforces it.
- A script is an accelerator. Every skill must still work by paste when scripts cannot run.

## Releases

- `CHANGELOG.md` is the source of truth. The newest `## vX.Y.Z — YYYY-MM-DD` heading is the released version.
- One version everywhere: `.claude-plugin/marketplace.json`, the root `plugin.json` and every plugin's `plugin.json` (ten files) carry the same number as the newest heading. No per-plugin versions.
- Semver: breaking change is major; new skill, command, hook or changed behavior is minor; fix or docs only is patch.
- Add each user-facing change under `## Unreleased`. To release: rename it to `## vX.Y.Z — YYYY-MM-DD`, set the version in those twelve files (marketplace, root plugin, ten plugins), commit together. Merging to `main` tags and publishes the release.

## Git and pull requests

- Branches: `feature/skill-name`, `fix/skill-name-description`, `docs/description`. Commits follow Conventional Commits: `feat:`, `fix:`, `docs:`.
- Before opening a PR: name matches folder, description has trigger phrases, `SKILL.md` under 500 lines, brain sections are real, no credentials, and every example matches what the skill really does.

## After any change

1. Ask: does this change mention a skill, command, file or number that actually exists? Check the folder, not memory of what was planned. This repo's biggest source of past errors was documentation describing things that were never built, and this file was one of them. The tests now check its counts.
2. Run `python3 .github/scripts/check_structure.py` and `python3 -m unittest discover -s tests`.
3. If you added or removed a skill, command or plugin, update the counts: `README.md` (layer table, "Ten plugins" line, `Available Skills (N Total)` header and table), `QUICK-START.md`, the first paragraph of this file, and each plugin's own `## Skills (N)` and `## Commands (N)` headers. `tests/test_prose_counts.py` fails on a mismatch.
4. If you changed a plugin description, sync its `plugin.json` and `README.md`.
5. Add a bullet under `## Unreleased` in `CHANGELOG.md`.
6. Bump versions only when you release.

When the work is done, offer the follow-ups that apply: run the checks, update counts, sync descriptions, cut a release.
