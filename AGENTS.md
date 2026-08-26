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
│   ├── marketplace.json        # Claude Code plugin marketplace manifest
│   └── plugin.json             # Root plugin manifest
├── product-marketing-context/  # The brain — product-marketing-context plugin
├── pmm-go-to-market/           # Go-to-market strategy + workflow orchestration
├── pmm-positioning/            # Positioning & messaging
├── pmm-execution/              # Day-to-day PMM execution
├── pmm-toolkit/                # PMM utilities
├── pmm-meta/                   # Meta skills (skill quality, learning, verification)
├── context/                    # Guardrails: meta-patterns.md, read by every skill's pre-flight
├── CONTRIBUTING.md
├── SKILL-SPEC.md                # Skill authoring standard
├── LICENSE
├── README.md
├── QUICK-START.md
├── CHANGELOG.md                 # Repo-wide release log — see Versioning below
└── AGENTS.md                    # AI agent guidelines
```

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

**No known exceptions as of 2026-08-24.** Every skill's frontmatter
`name:` field matches its directory name exactly. `experiment-doc` was
the last remaining mismatch (its frontmatter previously said
`experiment-doc-builder`) — fixed in the structural-compliance sweep
that also added missing required sections to several skills.

## Brain Integration

Brain-dependent skills read from `/foundation/brain.md` — a shared context
layer built by the `product-marketing-context` skill. It has exactly 6
sections: Product Context, ICP Definition, Alternatives & Positioning,
Voice & Tone, Market Context, and Proof Points Registry. There is no
Section 7 — earlier drafts of several skills invented one (variously
called "Strategy Layer," "Launch History," or "Meta-Learnings") and every
instance found has been removed. If you see a skill reference a brain
Section 7, that's a bug — file it or fix it, don't treat it as real.

**Status:** every skill's brain-read/write claims have been verified
against this 6-section schema as of Workstream 4b. If a skill you're
touching cites a section number that doesn't match this list, treat that
as a bug in the skill, not in this document.

When using brain-dependent skills, ensure `/foundation/brain.md` exists.
If not, run `product-marketing-context` to build it.

## Claude Code Plugin

This repo serves as a plugin marketplace via
`.claude-plugin/marketplace.json`, listing six plugins:

```bash
claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
claude plugin install product-marketing-context
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
