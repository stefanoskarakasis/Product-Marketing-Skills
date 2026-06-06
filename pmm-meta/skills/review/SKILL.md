---
name: review
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

# Review

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
  that is `verify`. Reviewing brain file health → use `product-marketing-context`
  audit mode. Reviewing skill *behaviour over multiple sessions* → that is future
  `audit` meta skill.
- **Example prompts:**
  - "Review `pre-mortem` against spec"
  - "Is `go-to-market-strategy` to spec?"
  - "What's missing from `beachhead-segment`?"
  - "Score all skills in `pmm-execution`"
  - `/review pmm-go-to-market/skills/go-to-market-strategy/SKILL.md`

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
  If SKILL-SPEC.md is not found: block and surface:
  > "SKILL-SPEC.md not found at repo root. The review skill requires it as the
  > scoring standard. Ensure it exists before running review."
- Read the target `SKILL.md` in full. Do not score from a partial read.
- Identify the skill's declared tier (T1/T2/T3/T4) from its frontmatter
  `metadata` or body content. Tier determines which sections are required vs optional.
- n.v.t. — no other pre-flight conditions.

---

## Steps

### Step 1: Load and Parse

Load `SKILL-SPEC.md` silently. Load target `SKILL.md` silently.

Extract from the target skill:
- `name` field
- `version` field
- `description` character count
- `metadata.context` value
- `metadata.quality_gate` value
- `last_updated` value
- All section headers present (## level)
- Line count
- Whether an `evals/` file exists (note: cannot verify from SKILL.md alone —
  flag as "cannot verify from file content, check repo structure")

Identify the skill tier from any of: explicit tier label in body, position in
SKILL-SPEC tier table (Section 12), or inference from sections present.
State the identified tier before scoring.

---

### Step 2: Run the 19-Point Checklist

Score each check as ✅ Pass, ❌ Fail, or ⚠️ Partial. No partial credit on
binary checks — Partial only applies where a section exists but is incomplete.

**Frontmatter — 5 checks:**

| # | Check | Pass condition |
|---|---|---|
| F1 | All required frontmatter fields present | `name`, `version`, `description`, `metadata.author`, `metadata.context`, `metadata.quality_gate`, `last_updated` all present |
| F2 | `name` matches directory name | Exact match, lowercase, hyphens only — verify against path if provided |
| F3 | `description` is 300–600 chars with trigger phrases | Count chars, confirm trigger phrases present verbatim |
| F4 | `metadata.context` declared correctly | Value is exactly `brain-dependent` or `context-agnostic` |
| F5 | `version` and `last_updated` present | Both fields exist with valid values |

**Seven required sections — 7 checks:**

| # | Check | Pass condition |
|---|---|---|
| S1 | `## Trigger` present | Includes When, Not for, Example prompts — all three sub-fields |
| S2 | `## Inputs` present | Args, Defaults, Context keys — all three sub-fields (or explicit `n.v.t.`) |
| S3 | `## Pre-flight` present | Present with content or explicit `n.v.t.` |
| S4 | `## Steps` present | Named steps in imperative form, minimum 2 steps |
| S5 | `## Outputs` present | Files written, Chat output format, External side effects (or `n.v.t.`) |
| S6 | `## Verification` present | Concrete and checkable, or explicit `n.v.t.` |
| S7 | `## Do Not Use For` present | Named routing to other skills, or explicit `n.v.t.` |

**Tier-appropriate sections — 4 checks:**

| # | Check | Applies to | Pass condition |
|---|---|---|---|
| T1 | `## Operating Rules` present | T1, T2 | ≥6 rules stated |
| T2 | `## Quality Gate` present | T1, T2 where `quality_gate: true` | ≥5 binary checks in table format |
| T3 | `## Self-Improvement Loop` present | T1 | Before/after session structure + trigger format |
| T4 | `## Changelog` present | All tiers | ≥1 entry with version and date |

**Quality — 3 checks:**

| # | Check | Pass condition |
|---|---|---|
| Q1 | SKILL.md is ≤500 lines | Line count confirmed |
| Q2 | Output template in code fence | Any output template uses ` ```markdown ``` ` not raw headers |
| Q3 | Evals file exists | Cannot verify from SKILL.md — flag for manual repo check |

---

### Step 3: Produce Scored Report

```markdown
## Review Report — [skill-name]
**Spec version:** SKILL-SPEC v2.0.0
**Skill version:** [version from frontmatter]
**Identified tier:** [T1 / T2 / T3 / T4]
**Reviewed:** [date]

---

### Score: [X]/19

✅ Passing: [N]
❌ Failing: [N]
⚠️ Partial: [N]

Pass threshold: 17/19. Status: [PASS / FAIL — N checks below threshold]

---

### Failures (fix before shipping)

**[Check ID] — [Check name]**
What's missing: [exact description of the gap]
Fix: [exact text or section to add — not "add a trigger section", but the
     actual content or format required]

[Repeat for each ❌]

---

### Partials (improve before next version)

**[Check ID] — [Check name]**
What's incomplete: [specific gap within the existing section]
Fix: [specific addition needed]

[Repeat for each ⚠️]

---

### Passing checks
[List all ✅ checks in one line each — confirm what's correct]

---

### Recommended fix order
1. [Highest-impact failure — typically a missing required section]
2. [Second failure]
3. [Partials, lowest priority]

Estimated time to bring to spec: [S: <15 min / M: 15–45 min / L: 45+ min]
```

---

### Step 4: Offer Batch Mode

After single-skill review, offer:
> "Want me to run this across all skills in `[plugin folder]` or the full repo?
> Use `/review-all [folder]` to batch."

---

## Outputs

- **Files written:** n.v.t. — review is read-only. It produces no writes.
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

- **verify** — for checking whether a skill's *output* on a real task was correct.
  `review` checks the skill definition. `verify` checks the skill's runtime behaviour.
- **product-marketing-context** — for checking brain file health and section quality.
- **Any skill's built-in `/audit` command** — those check a prior *decision* made
  by that skill (e.g. beachhead segment scored 6 months ago). `review` checks the
  skill file itself.

---

## Commands

### /review [skill-name or path]
Run the full 19-point review on a single skill. Produces the scored report.

```
/review pre-mortem
/review pmm-go-to-market/skills/go-to-market-strategy/SKILL.md
/review beachhead-segment
```

---

### /review-all [folder or "repo"]
Run review across all SKILL.md files in a folder or the entire repo.
Produces a summary table with score per skill and top failure per skill.

```
/review-all pmm-execution
/review-all repo
```

Output:
```
## Repo Review Summary
Spec version: SKILL-SPEC v2.0.0
Date: [date]

| Skill | Score | Status | Top failure |
|---|---|---|---|
| pre-mortem | 19/19 | ✅ PASS | — |
| go-to-market-strategy | 16/19 | ❌ FAIL | S3: Pre-flight missing |
| beachhead-segment | 18/19 | ✅ PASS | Q3: Evals unverified |
| writing-assistant | 14/19 | ❌ FAIL | S1, S2, S7 missing |

Skills failing: [N]
Skills passing: [N]
Lowest score: [skill-name] ([X]/19)
Recommended first fix: [skill-name] — [reason]
```

---

### /diff [skill-name] [before-version] [after-version]
Compare two versions of a skill and confirm which spec checks improved.
Use after upgrading a skill to verify the upgrade landed correctly.

```
/diff go-to-market-strategy v1.0.0 v2.0.0
```

Output:
```
## Diff Review — go-to-market-strategy
v1.0.0 → v2.0.0

Checks gained: ✅ [list]
Checks lost: ❌ [list — flag if regression]
Net change: [+N / -N / no change]
New score: [X]/19
```

---

### /fix [skill-name] [check-id]
Generate the exact text needed to fix a specific failing check for a named skill.
Use to get copy-paste-ready content rather than re-reading the full report.

```
/fix go-to-market-strategy S3
/fix writing-assistant S1
```

Output:
```
Fix for [skill-name] — Check [ID]: [Check name]

Paste this into [exact location in SKILL.md]:

[exact markdown content to add]

After adding: re-run /review [skill-name] to confirm pass.
```

---

## Operating Rules

- **Load SKILL-SPEC before the skill.** The spec is the standard. Reading the skill
  first risks anchoring on what's there rather than what's required.
- **Read the full SKILL.md before scoring.** Partial reads produce false failures.
  A section that appears to be missing might be present further in the file.
- **Identify tier before applying tier checks.** T3 skills are not penalised for
  missing a self-improvement loop. T1 skills are. Wrong tier = wrong checklist.
- **Every failure gets a specific fix.** "Add a Trigger section" is not a fix.
  The exact sub-fields, format, and content type required must be stated.
- **No partial credit on binary checks.** A section either exists with the right
  content or it doesn't. Partial is only valid when a section exists but is
  structurally incomplete.
- **Review is read-only.** This skill never writes to any file. It produces
  a report. The human decides what to fix and commits it.
- **Q3 (evals) cannot be verified from SKILL.md content alone.** Always flag this
  check as "cannot verify — confirm `evals/` folder exists in repo" rather than
  marking it as a pass or fail from file content.
- **The fix order matters.** Failing frontmatter checks first, then missing required
  sections, then tier-appropriate sections, then quality checks. A skill with
  broken frontmatter should not be shipping regardless of section quality.
- **`n.v.t.` is a valid answer.** A skill with `n.v.t.` under Pre-flight passes
  that check. A skill with an empty Pre-flight section fails it. The distinction
  matters — don't penalise deliberate `n.v.t.` declarations.
- **Batch mode surfaces the lowest score first.** When running `/review-all`,
  the recommended fix order starts with the lowest-scoring skill, not alphabetical.

---

## Quality Gate

Runs after report is generated, before delivery.

| Check | Standard | Pass = |
|---|---|---|
| SKILL-SPEC loaded | Spec read before target skill | Yes |
| Target skill read in full | No partial read | Yes |
| Tier identified | Stated before scoring begins | Yes |
| All 19 checks evaluated | No check skipped or omitted | Yes |
| Every ❌ has a specific fix | No vague directions | Yes |
| Score stated as X/19 | Numerical score with pass/fail status | Yes |
| Fix order present | Prioritised sequence, not alphabetical | Yes |
| Q3 flagged correctly | Evals check noted as unverifiable from file | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load `SKILL-SPEC.md` — if version has changed since last review session,
   note the version delta and surface which checks are new or changed.
2. Check `knowledge/review/rules.md` if it exists — apply confirmed patterns.
3. Check `knowledge/review/hypotheses.md` — note any pattern testable today.

### After every session:
1. Note which check most commonly fails across the skills reviewed.
   Log to `knowledge/review/hypotheses.md`.
2. If same check fails across 3+ different skills → propose to
   `knowledge/review/rules.md`: "Check [X] is the most common failure point —
   flag proactively in future reviews before running full checklist."
3. Log session: skill(s) reviewed, scores, most common failure, time to fix estimates.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed across reviewed skills]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v1.0.0 — 2026-06-06
Initial build. Root-level meta skill — operates across all four plugins.

Architecture decisions:
- Context-agnostic: no brain file, no MCP sources. Intentional — review must
  be objective and unaffected by company context.
- 19-point checklist directly mirrors SKILL-SPEC v2.0.0 Section 13.
- Tier detection before scoring — prevents wrong checklist application.
- Four commands: /review (single), /review-all (batch), /diff (version compare),
  /fix (copy-paste repair content).
- Q3 (evals) permanently flagged as "cannot verify from file" — requires manual
  repo check. Documented explicitly to prevent false passes.
- Read-only by design. No writes under any circumstance.
- Fix specificity rule: every failure must have exact content to add, not
  a direction to add something.
