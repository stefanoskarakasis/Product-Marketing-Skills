---
name: meta-review
version: 1.0.0
description: >
  Audits any SKILL.md against SKILL-SPEC v2.0.0 and produces a scored gap list
  with prioritised fixes. The CI pipeline for the skill repo — run before shipping
  any new or updated skill. Trigger on: "review this skill", "audit this skill
  against spec", "is this skill to spec", "what's missing from this skill", "score
  this skill", "check this skill", or any request to evaluate a SKILL.md file
  against the authoring standard.

metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-06-06
---

# meta-review

The CI pipeline for the skill repo. Reads any `SKILL.md`, scores it against
SKILL-SPEC v2.0.0, and produces a prioritised gap list with exact fixes.

Not a style guide. Not suggestions. A pass/fail checklist that tells you precisely
what is missing, why it matters, and what to write to fix it — before the skill
ships.

---

## Trigger

- **When:** Any new skill is being prepared for commit, any existing skill is being
  upgraded, or you want to know the current spec-compliance score of a skill.
- **Not for:** Reviewing skill *output quality* (a skill's output on a real task) →
  that is `meta-verify`. Reviewing brain file health → use `product-marketing-context`
  audit mode. Reviewing skill *behaviour over multiple sessions* → that is `meta-audit`
  (future skill).
- **Example prompts:**
  - "Review `pre-mortem` against spec"
  - "Is `go-to-market-strategy` to spec?"
  - "What's missing from `beachhead-segment`?"
  - "Score all skills in `pmm-execution`"
  - `/meta-review pmm-go-to-market/skills/go-to-market-strategy/SKILL.md`

---

## Inputs

- **Args:** Path to a `SKILL.md` file, skill name, or plugin folder name.
  Free format — skill name alone is sufficient if unambiguous in the repo.
- **Defaults:** If no target named, ask before proceeding. Never assume.
- **Context keys:**
  - `SKILL-SPEC.md` at repo root — required. This is the scoring standard.
    Load it before reading the target skill.
  - Target `SKILL.md` — required. Read in full before scoring.
  - n.v.t. — no brain file, no MCP sources, no external context needed.
    This skill is intentionally context-agnostic.

---

## Pre-flight

- Load `SKILL-SPEC.md` from repo root before reading the target skill.
  If not found: block and surface:
  > "SKILL-SPEC.md not found at repo root. Ensure it exists before running review."
- Read the target `SKILL.md` in full. Do not score from a partial read.
- Identify the skill's declared tier (T1/T2/T3/T4) from frontmatter or body.
  Tier determines which sections are required vs optional.
- n.v.t. — no other pre-flight conditions.

---

## Steps

### Step 1: Load and Parse

Load `SKILL-SPEC.md` silently. Load target `SKILL.md` silently.

Extract: `name`, `version`, `description` char count, `metadata.context`,
`metadata.quality_gate`, `last_updated`, all `##` section headers, line count.

Note: evals folder cannot be verified from SKILL.md alone — flag for manual check.

Identify and state the skill tier before scoring.

---

### Step 2: Run the 19-Point Checklist

Score each check as ✅ Pass, ❌ Fail, or ⚠️ Partial.

**Frontmatter — 5 checks:**

| # | Check | Pass condition |
|---|---|---|
| F1 | All required frontmatter fields present | `name`, `version`, `description`, `metadata.author`, `metadata.context`, `metadata.quality_gate`, `last_updated` all present |
| F2 | `name` matches directory name | Exact match, lowercase, hyphens only |
| F3 | `description` is 300–600 chars with trigger phrases | Count chars, trigger phrases verbatim |
| F4 | `metadata.context` declared correctly | Exactly `brain-dependent` or `context-agnostic` |
| F5 | `version` and `last_updated` present | Both fields exist with valid values |

**Seven required sections — 7 checks:**

| # | Check | Pass condition |
|---|---|---|
| S1 | `## Trigger` present | When, Not for, Example prompts — all three sub-fields |
| S2 | `## Inputs` present | Args, Defaults, Context keys (or explicit `n.v.t.`) |
| S3 | `## Pre-flight` present | Present with content or explicit `n.v.t.` |
| S4 | `## Steps` present | Named steps in imperative form, minimum 2 |
| S5 | `## Outputs` present | Files written, Chat output format, Side effects (or `n.v.t.`) |
| S6 | `## Verification` present | Concrete and checkable, or explicit `n.v.t.` |
| S7 | `## Do Not Use For` present | Named routing to other skills, or explicit `n.v.t.` |

**Tier-appropriate sections — 4 checks:**

| # | Check | Applies to | Pass condition |
|---|---|---|---|
| T1 | `## Operating Rules` present | T1, T2 | ≥6 rules stated |
| T2 | `## Quality Gate` present | T1, T2 where `quality_gate: true` | ≥5 binary checks in table |
| T3 | `## Self-Improvement Loop` present | T1 | Before/after session structure + trigger format |
| T4 | `## Changelog` present | All tiers | ≥1 entry with version and date |

**Quality — 3 checks:**

| # | Check | Pass condition |
|---|---|---|
| Q1 | SKILL.md is ≤500 lines | Line count confirmed |
| Q2 | Output template in code fence | Templates use ` ```markdown ``` ` not raw headers |
| Q3 | Evals file exists | Cannot verify from SKILL.md — flag for manual repo check |

---

### Step 3: Produce Scored Report

```markdown
## Review Report — [skill-name]
**Spec version:** SKILL-SPEC v2.0.0
**Skill version:** [version]
**Identified tier:** [T1 / T2 / T3 / T4]
**Reviewed:** [date]

### Score: [X]/19
Pass threshold: 17/19. Status: [PASS / FAIL]

### Failures (fix before shipping)
**[Check ID] — [Check name]**
What's missing: [exact description]
Fix: [exact text to add — not a direction, the actual content]

### Partials (improve before next version)
**[Check ID] — [Check name]**
What's incomplete: [specific gap]
Fix: [specific addition]

### Passing checks
[All ✅ checks in one line each]

### Recommended fix order
1. [Highest-impact failure]
2. [Second failure]
Estimated time to spec: [S: <15 min / M: 15–45 min / L: 45+ min]
```

---

### Step 4: Offer Batch Mode

After single-skill review, offer:
> "Want me to run this across all skills in `[plugin folder]` or the full repo?
> Use `/meta-review-all [folder]` to batch."

---

## Outputs

- **Files written:** n.v.t. — review is read-only. No writes ever.
- **Chat output format:** Scored report in the structure above. Markdown formatted
  for copy-paste into a GitHub issue, Notion task, or commit message.
- **External side effects:** n.v.t.

---

## Verification

- Report shows score as X/19 with pass/fail status against 17/19 threshold.
- Every ❌ includes a specific fix, not a vague direction.
- Recommended fix order is present.
- Skill tier identified and stated before scoring begins.
- n.v.t. — no writes to verify.

---

## Do Not Use For

- **meta-verify** — for checking whether a skill's *output* on a real task was
  correct. `meta-review` checks the skill definition file. `meta-verify` checks
  runtime output.
- **product-marketing-context** — for checking brain file health and section quality.
- **Any skill's built-in `/audit` command** — those check a prior decision made by
  that skill. `meta-review` checks the skill file itself.

---

## Commands

### /meta-review [skill-name or path]
Run the full 19-point review on a single skill.

```
/meta-review pre-mortem
/meta-review pmm-go-to-market/skills/go-to-market-strategy/SKILL.md
/meta-review beachhead-segment
```

---

### /meta-review-all [folder or "repo"]
Batch review all SKILL.md files in a folder or the entire repo.

```
/meta-review-all pmm-execution
/meta-review-all repo
```

Output:
```markdown
## Repo Review Summary — SKILL-SPEC v2.0.0

| Skill | Score | Status | Top failure |
|---|---|---|---|
| pre-mortem | 19/19 | ✅ PASS | — |
| go-to-market-strategy | 18/19 | ✅ PASS | Q3: Evals unverified |
| writing-assistant | 14/19 | ❌ FAIL | S1, S2, S7 missing |

Skills passing: [N] | Failing: [N]
Recommended first fix: [skill-name] — [reason]
```

---

### /meta-diff [skill-name] [before-version] [after-version]
Compare two versions and confirm which spec checks improved.

```
/meta-diff go-to-market-strategy v1.0.0 v2.0.0
```

---

### /meta-fix [skill-name] [check-id]
Generate exact copy-paste content to fix a specific failing check.

```
/meta-fix go-to-market-strategy S3
/meta-fix writing-assistant S1
```

Output:
```
Fix for [skill-name] — Check [ID]: [Check name]
Paste this into [exact location in SKILL.md]:
[exact markdown content]
After adding: re-run /meta-review [skill-name] to confirm pass.
```

---

## Operating Rules

- **Load SKILL-SPEC before the skill.** Reading the skill first risks anchoring on
  what's there rather than what's required.
- **Read the full SKILL.md before scoring.** Partial reads produce false failures.
- **Identify tier before applying tier checks.** Wrong tier = wrong checklist.
- **Every failure gets a specific fix.** "Add a Trigger section" is not a fix.
  Exact sub-fields, format, and content type required must be stated.
- **No partial credit on binary checks.** Partial only applies when a section
  exists but is structurally incomplete.
- **Review is read-only.** Never writes to any file under any circumstance.
- **Q3 cannot be verified from SKILL.md alone.** Always flag as "cannot verify —
  confirm evals/ folder exists in repo."
- **Fix order matters.** Frontmatter failures first, then missing required sections,
  then tier-appropriate sections, then quality checks.
- **`n.v.t.` is a valid answer.** Explicit n.v.t. passes the check. Empty section fails it.
- **Batch mode surfaces lowest score first.** Not alphabetical.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| SKILL-SPEC loaded | Spec read before target skill | Yes |
| Target skill read in full | No partial read | Yes |
| Tier identified | Stated before scoring begins | Yes |
| All 19 checks evaluated | No check skipped | Yes |
| Every ❌ has specific fix | No vague directions | Yes |
| Score stated as X/19 | Numerical score with pass/fail | Yes |
| Fix order present | Prioritised, not alphabetical | Yes |
| Q3 flagged correctly | Noted as unverifiable from file | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load `SKILL-SPEC.md` — note any version changes since last session.
2. Check `knowledge/meta/rules.md` — apply confirmed patterns silently.
3. Check `knowledge/meta/hypotheses.md` — note any pattern testable today.

### After every session:
1. Note which check most commonly failed across skills reviewed.
2. Log to `knowledge/meta/hypotheses.md`.
3. If same check fails across 3+ skills → propose promotion to `knowledge/meta/rules.md`.

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v1.0.0 — 2026-06-06
Initial build. Meta skill in `pmm-meta` plugin.
- Context-agnostic: no brain, no MCP. Review must be objective.
- 19-point checklist mirrors SKILL-SPEC v2.0.0 Section 13.
- Tier detection before scoring.
- Commands: /meta-review, /meta-review-all, /meta-diff, /meta-fix.
- Q3 permanently flagged as unverifiable from file content.
- Read-only by design.
- Renamed from `review` to `meta-review` for consistent meta- naming convention.
