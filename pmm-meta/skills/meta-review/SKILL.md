---
name: meta-review
version: 3.0.0
description: >
  Audits any SKILL.md in this repo against SKILL-SPEC.md, the skill authoring
  standard — checks frontmatter, the seven required sections, tier-appropriate
  sections, and quality-gate structure, then returns a scored checklist with
  prioritized fixes. Trigger on: "review this skill", "audit this SKILL.md",
  "does this skill meet spec", "is this skill done", "quality check this skill",
  or any request to validate a skill file against the repo's authoring standard.
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-08-22
---

# meta-review

Audits a skill's `SKILL.md` against `SKILL-SPEC.md` — the one standard every
skill in this repo is supposed to meet. Runs the same 17-point checklist
`SKILL-SPEC.md` Section 13 defines, returns a pass/fail per check, and
prioritizes fixes so the skill's author knows exactly what to do next.

This is a spec-compliance auditor, not a content-quality judge. It checks
structure — is every required section present, does frontmatter have every
required field, is the file under 500 lines — not whether the skill's actual
domain logic is good. Judging domain logic requires domain expertise this
skill doesn't have; a human or a domain-specific reviewer does that.

## Trigger

- **When:** A skill's `SKILL.md` needs to be checked against the repo's
  authoring standard — before merging a new skill, after editing an existing
  one, or as a periodic health check.

- **Not for:** Checking the correctness of a skill's actual output (a GTM
  brief, a positioning statement, a retro summary) → use `meta-verify`.
  Detecting cross-skill patterns or proposing guardrails → use
  `meta-synthesis`. Extracting learnings from a single completed session →
  use `meta-learn`.

- **Example prompts:**
  - "Review the retro skill"
  - "Audit pmm-okrs against spec"
  - "Does stakeholder-maps meet the authoring standard?"
  - "Check every skill in pmm-execution"

## Inputs

- **Args:** Skill name (required) — the directory name of the skill to audit,
  e.g. `retro` or `positioning-messaging`. If the user names a whole plugin
  instead of one skill, run this skill once per skill in that plugin and
  report all results together.
- **Defaults:** n.v.t. — a skill name is always required.
- **Context keys:** `SKILL-SPEC.md` (the standard being enforced) and the
  target skill's `SKILL.md` file. No brain context needed.

## Pre-flight

- Load `SKILL-SPEC.md` from the repo root. If it's missing, stop — there's
  nothing to audit against.
- Locate the named skill's `SKILL.md`. If the skill directory doesn't exist,
  say so and ask for the correct name rather than guessing.
- This skill is context-agnostic. Do not load `/foundation/brain.md`.

## Steps

### Step 1: Load and Parse

Read the target `SKILL.md` in full. Parse frontmatter separately from body.
Identify which `##` sections are present, in what order, and their approximate
line counts.

### Step 2: Determine Tier

Check `SKILL-SPEC.md` Section 12 (Skill Tiers) for whether this skill is
already listed under a tier. If not listed, ask the user which tier applies
(T1 Strategic / T2 Execution / T3 Utility / T4 Meta) — tier determines which
of the 17 checks apply.

### Step 3: Run the 17-Point Checklist

Work through `SKILL-SPEC.md` Section 13 exactly as written, in order:

**Frontmatter (5 checks)** — all required fields present; `name` matches
directory name; `description` is 300–600 chars with trigger phrases verbatim;
`metadata.context` declared; `version` and `last_updated` present.

**Seven required sections (7 checks)** — `Trigger`, `Inputs`, `Pre-flight`,
`Steps`, `Outputs`, `Verification`, `Do Not Use For` — each present, either
filled in or explicitly marked `n.v.t.`

**Tier-appropriate sections (2 checks, T1/T2 only)** — `Operating Rules`
with ≥6 rules; `Quality Gate` with ≥5 binary checks, only where
`quality_gate: true`.

**Quality (3 checks)** — `SKILL.md` ≤500 lines; any output template is
wrapped in a code fence, not raw `##` headers; an evals file exists with
≥3 test cases including one edge case.

Mark each check pass/fail. A check applying `n.v.t.` correctly (per
`SKILL-SPEC.md` Section 7) counts as pass — an explicit `n.v.t.` is
compliant; an omitted section is not.

### Step 4: Score and Report

```markdown
## Meta-Review — [skill-name]

**Tier:** [T1 / T2 / T3 / T4]
**Score:** [N]/17
**Threshold:** 15/17

### Failed checks
- [Check name] — [what's missing, specifically]

### Passed with n.v.t.
- [Check name] — explicitly marked not applicable

### Recommendation
[PASSES SPEC / NEEDS FIXES] — [one sentence]
```

If the skill scores below 15/17, list every failed check with enough detail
that the author can fix it without re-reading the whole spec. If it passes,
say so plainly — don't manufacture nitpicks to seem thorough.

## Outputs

- **Files written:** n.v.t. — this skill produces a report only, it does not
  edit the audited `SKILL.md`.
- **Chat output format:** The scored checklist template from Step 4.
- **External side effects:** n.v.t.

## Verification

- Every one of the 17 checks from `SKILL-SPEC.md` Section 13 was evaluated,
  not a subset.
- Tier was determined before checks ran (tier changes which checks apply).
- Score and threshold are both stated, not just a pass/fail verdict.
- Every failed check names the specific gap, not just "incomplete."

## Do Not Use For

- **meta-verify** — when the task is checking a skill's *output* (a brief,
  a positioning statement) rather than the skill's own `SKILL.md` structure
- **meta-learn** — when the task is capturing what was learned from a
  completed session, not auditing file structure
- **meta-synthesis** — when the task is detecting a pattern across multiple
  sessions or skills, not a single-file structural audit

## Operating Rules

- **Audit structure, not domain judgment.** This skill checks whether
  required sections exist and are filled in — it does not have the domain
  expertise to judge whether a GTM brief's channel strategy is actually
  good. That's a human call, or a job for the skill that produced the output
  plus `meta-verify`.
- **Score honestly.** A skill that's missing three sections is not "mostly
  there" — report the real count against 17.
- **`n.v.t.` is a pass, silence is a fail.** Per `SKILL-SPEC.md` Section 7,
  an explicit `n.v.t.` on a section that doesn't apply is fully compliant.
  An omitted section is not, even if the reason is obvious.
- **Tier determines scope.** Don't fail a T3 skill for missing a
  Self-Improvement Loop or Changelog — as of `SKILL-SPEC.md` v2.1.0, no
  skill requires either. Don't fail a T3 skill for missing Operating Rules
  or Quality Gate — those are T1/T2 only.
- **Name the fix, not just the gap.** "Missing `## Do Not Use For`" is a
  gap. "Add `## Do Not Use For` listing at minimum the skills this one is
  most often confused with" is a fix.
- **One skill at a time, reported together for a plugin.** If asked to
  review a whole plugin, run the full checklist per skill — don't average
  or summarize across skills in a way that hides which specific skill
  failed which specific check.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Spec loaded | `SKILL-SPEC.md` read before any check ran | Yes |
| Tier determined | Tier confirmed before checks, not assumed | Yes |
| All 17 checks run | No check skipped regardless of early failures | Yes |
| Score stated | Numeric score (N/17) shown, not just pass/fail | Yes |
| Failed checks specific | Each failure names the exact gap | Yes |
| n.v.t. handled correctly | Explicit n.v.t. counted as pass per spec Section 7 | Yes |
