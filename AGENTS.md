# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository contains **PMM Skills** for AI agents following the [Agent Skills specification](https://agentskills.io/specification.md). Skills install to `.claude/skills/` for Claude Code. This repo also serves as a **Claude Code plugin marketplace** via `.claude-plugin/marketplace.json`.

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

## Build / Lint / Test Commands

**Skills** are content-only (no build step). Verify manually:
- YAML frontmatter is valid
- `name` field matches directory name exactly
- `name` is 1-64 chars, lowercase alphanumeric and hyphens only
- `description` is 1-1024 characters
- All skills read from `/foundation/brain.md` for shared context

## Agent Skills Specification

Skills follow the [Agent Skills spec](https://agentskills.io/specification.md).

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it. Include trigger phrases.
---
```

### Frontmatter Field Constraints

| Field         | Required | Constraints                                                      |
|---------------|----------|------------------------------------------------------------------|
| `name`        | Yes      | 1-64 chars, lowercase `a-z`, numbers, hyphens. Must match dir.   |
| `description` | Yes      | 1-1024 chars. Describe what it does and when to use it.          |
| `license`     | No       | License name (default: MIT)                                      |
| `metadata`    | No       | Key-value pairs (author, version, etc.)                          |

### Name Field Rules

- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- No consecutive hyphens (`--`)
- Must match parent directory name exactly

**Valid**: `go-to-market-strategy`, `positioning-messaging`, `interview-summary`
**Invalid**: `GoToMarketStrategy`, `-positioning`, `positioning--messaging`

### Optional Skill Directories

```
skills/skill-name/
├── SKILL.md        # Required - main instructions (<500 lines)
├── references/     # Optional - detailed docs loaded on demand
├── config/         # Optional - configuration files
└── templates/      # Optional - templates and examples
```

## Writing Style Guidelines

### Structure

- Keep `SKILL.md` under 500 lines (move details to `references/`)
- Use H2 (`##`) for main sections, H3 (`###`) for subsections
- Use bullet points and numbered lists liberally
- Short paragraphs (2-4 sentences max)

### Tone

- Direct and instructional
- Second person ("When you're planning a launch...")
- Professional but approachable
- Focus on the job to be done, not the tool

### Formatting

- Bold (`**text**`) for key terms
- Code blocks for examples and prompts
- Tables for reference data and frameworks
- No excessive emojis

### Clarity Principles

- Clarity over cleverness
- Specific over vague
- Active voice over passive
- One idea per section

### Description Field Best Practices

The `description` is critical for skill discovery. Include:
1. What the skill does
2. When to use it (trigger phrases)
3. Related skills for scope boundaries

```yaml
description: "Assigns launch tier (T1-T4) and generates GTM strategy briefs. Use when planning product launches, features, pricing changes, or market expansion. Chains with positioning-messaging and workflow-orchestrator. Reads brain Section 7 for self-learning."
```

## Brain Integration

**All skills in this repository read from `/foundation/brain.md`** — a shared context layer that stores:

- Section 1: Product context
- Section 2: ICP & personas
- Section 3: Positioning
- Section 4: Competitive landscape
- Section 5: Proof points
- Section 6: Voice & tone
- Section 7: Launch history (self-learning)

**Many skills write back to the brain** (especially Section 7) to capture learnings from launches, retros, and competitive analysis. This creates a compounding intelligence layer — the fifth launch is smarter than the first.

When using these skills, ensure `/foundation/brain.md` exists. If not, run `product-marketing-context` to set it up.

## Workflow Orchestrator

The `workflow-orchestrator` skill chains 15+ other skills for complete GTM programs:

- **Full Product Launch** — positioning → competitive → strategy → campaign → stakeholder
- **Quarterly PMM Cycle** — retro → positioning audit → competitive refresh → OKRs
- **Positioning Refresh** — positioning → value props → update battlecards
- **Competitive Program** — alternatives → battlecards → CI briefing
- **Market Entry** — ICP → personas → positioning → competitive → strategy

When using workflow-orchestrator, it manages context passing, brain updates, and skill routing automatically.

## Claude Code Plugin

This repo serves as a plugin marketplace. The manifest at `.claude-plugin/marketplace.json` lists all skills for installation via:

```bash
claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills
claude plugin install pmm-go-to-market
claude plugin install pmm-positioning
claude plugin install pmm-execution
claude plugin install pmm-toolkit
```

See [Claude Code plugins documentation](https://docs.claude.ai/plugins) for details.

## Git Workflow

### Branch Naming

- New skills: `feature/skill-name`
- Improvements: `fix/skill-name-description`
- Documentation: `docs/description`

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat: add go-to-market-strategy skill`
- `fix: improve clarity in workflow-orchestrator`
- `docs: update README with architecture diagram`

---

### Pull Request Checklist

- [ ] `name` matches directory name exactly
- [ ] `name` follows naming rules (lowercase, hyphens, no `--`)
- [ ] `description` is 1-1024 chars with trigger phrases
- [ ] `SKILL.md` is under 500 lines
- [ ] Skills read from brain where appropriate
- [ ] No sensitive data or credentials
- [ ] Examples match actual skill behavior

---

## Checking for Updates

When using any skill from this repository:

1. **Once per session**, on first skill use, check for updates:
   - Fetch `VERSIONS.md` from GitHub: https://raw.githubusercontent.com/stefanoskarakasis/Product-Marketing-Skills/main/VERSIONS.md
   - Compare versions against local skill files

2. **Only prompt if meaningful**:
   - 2 or more skills have updates, OR
   - Any skill has a major version bump (e.g., 1.x to 2.x)

3. **Non-blocking notification** at end of response:

4. **If user says "update skills"**:
   - Run `git pull` in the Product-Marketing-Skills directory
   - Confirm what was updated

## Skill Categories

See `README.md` for the current list of skills organized by collection. When adding new skills, follow the naming patterns of existing skills in that category.

## Cross-Skill References

Skills reference each other to avoid duplication:

- `workflow-orchestrator` → chains `positioning-messaging`, `go-to-market-strategy`, others
- `go-to-market-strategy` → routes to `positioning-messaging`, `competitive-battlecard`
- `retro` → updates brain Section 7 for self-learning across all skills
- `interview-summary` → feeds insights to `positioning-messaging`, `buyer-personas`

When adding new skills, identify related skills and document cross-references in the `description` field.
