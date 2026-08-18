# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository contains **PMM Skills** for AI agents following the
[Agent Skills specification](https://agentskills.io/specification.md).
This repo also serves as a **Claude Code plugin marketplace** via
`.claude-plugin/marketplace.json`.

- **Name**: Product Marketing Skills
- **GitHub**: [stefanoskarakasis/Product-Marketing-Skills](https://github.com/stefanoskarakasis/Product-Marketing-Skills)
- **Creator**: Stefanos Karakasis
- **License**: MIT

## Repository Structure

```
Product-Marketing-Skills/
├── .claude-plugin/
│   └── marketplace.json        # Claude Code plugin marketplace manifest
├── pmm-go-to-market/           # Go-to-market strategy + workflow orchestration
├── pmm-positioning/            # Positioning & messaging
├── pmm-execution/              # Day-to-day PMM execution
├── pmm-toolkit/                # PMM utilities
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── AGENTS.md                   # AI agent guidelines
└── VERSIONS.md                 # Skill version tracking
```

Product-Marketing-Skills/ 
├── .claude-plugin/ │ 
├── marketplace.json # Claude Code plugin marketplace manifest 
│ └── plugin.json # Root plugin manifest 
├── product-marketing-context/ # The brain — pmm-foundation plugin 
├── pmm-go-to-market/ # Go-to-market strategy + workflow orchestration 
├── pmm-positioning/ # Positioning & messaging ├── pmm-execution/ # Day-to-day PMM execution 
├── pmm-toolkit/ # PMM utilities 
├── pmm-meta/ # Meta skills (skill quality, learning, verification) 
├── context/ # Shared guardrail/pattern files (scaffolding, not yet populated) 
├── sessions/ # Shared session-learning files (scaffolding, not yet populated) 
├── CONTRIBUTING.md ├── SKILL-SPEC.md # Skill authoring standard 
├── LICENSE 
├── README.md 
├── QUICK-START.md 
└── AGENTS.md


## Build / Lint / Test Commands

Skills are content-only (no build step). Verify manually:
- YAML frontmatter is valid
- `name` field matches directory name exactly
- `name` is 1-64 chars, lowercase alphanumeric and hyphens only
- `description` is 1-1024 characters
- Brain-dependent skills read from `/foundation/brain.md` for shared context

## Agent Skills Specification

Skills follow the [Agent Skills spec](https://agentskills.io/specification.md)
and this repo's own [SKILL-SPEC.md](SKILL-SPEC.md), which is the canonical
authoring standard for this repo specifically.

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it. Include trigger phrases.
---
```

### Name Field Rules

- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- No consecutive hyphens (`--`)
- Must match parent directory name exactly

**Known exceptions in this repo today, being corrected:** several skill
folders (`retro`, `positioning-messaging`, `pmm-resume`, `privacy-policy`,
`writing-assistant`, `experiment-doc`) currently have a `name:` field in
their frontmatter that doesn't match their folder name. This is a tracked
issue, not an intentional pattern — new skills must match exactly.

## Brain Integration

Brain-dependent skills read from `/foundation/brain.md` — a shared context
layer built by the `product-marketing-context` skill. It has 6 core
sections (Product Context, ICP, Alternatives & Positioning, Voice & Tone,
Market Context, Proof Points) plus an optional Section 7 (Strategy Layer:
advantages, perceptions, revenue levers).

**Status:** not every skill's brain-read/write claims have been verified
against this schema yet — see `product-marketing-context/ROADMAP.md` for
the correction plan in progress. Don't assume a skill's stated brain
section references are accurate until that work is marked done there.

When using brain-dependent skills, ensure `/foundation/brain.md` exists.
If not, run `product-marketing-context` to build it.

## Claude Code Plugin

This repo serves as a plugin marketplace via
`.claude-plugin/marketplace.json`, listing six plugins:

```bash
claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
claude plugin install pmm-foundation
claude plugin install pmm-go-to-market
claude plugin install pmm-positioning
claude plugin install pmm-execution
claude plugin install pmm-toolkit
claude plugin install pmm-meta
```

See [Claude Code plugins documentation](https://docs.claude.ai/plugins)
for details.

## Git Workflow

### Branch Naming

- New skills: `feature/skill-name`
- Improvements: `fix/skill-name-description`
- Documentation: `docs/description`

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/)
specification: `feat: ...`, `fix: ...`, `docs: ...`.

### Pull Request Checklist

- [ ] `name` matches directory name exactly
- [ ] `description` is 1-1024 chars with trigger phrases
- [ ] `SKILL.md` is under 500 lines
- [ ] Brain-dependent skills correctly cite real brain sections (see
      `SKILL-SPEC.md` Section 8-9)
- [ ] No sensitive data or credentials
- [ ] Examples match actual skill behavior — don't reference a skill,
      command, or file that doesn't exist in this repo

## Versioning

This repo uses one version number across the entire repo, not independent
per-plugin versions. `marketplace.json`, every `plugin.json`, and the
newest `CHANGELOG.md` heading always carry the same version. See
`CLAUDE.md` for the full rule and release procedure.

## Cross-Skill References

When adding new skills, only reference other skills by name if they
actually exist in this repo — verify the folder and frontmatter `name:`
field before citing a skill in your own `description` or routing text.
