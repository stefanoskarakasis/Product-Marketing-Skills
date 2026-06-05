# SKILL-SPEC.md
## Product Marketing Skills — Skill Authoring Standard

**Version:** 1.0.0  
**Last updated:** 2026-06-05  
**Applies to:** All skills in this repository  
**Owner:** Stefanos Karakasis

This is the canonical standard every skill in this repo must meet.  
The `review` meta skill enforces it. New skills ship only when they pass it.  
Existing skills are upgraded to it on the improvement schedule in `ROADMAP.md`.

---

## 1. What a Skill Is (and Isn't)

A skill is a **structured instruction set** that tells Claude how to behave when invoked. It is not documentation. It is not a feature list. It is not a README.

A skill that reads like a README will produce README-quality output.  
A skill that reads like an operating manual produces operating-manual-quality output.

**The test:** Could a new PMM follow this skill and know exactly what to do at every step, in every edge case, without asking a question? If no — it's not done.

---

## 2. File Structure

Every skill lives in its own directory and must contain:

```
skills/skill-name/
├── SKILL.md          ← Required. Main instruction file. Max 500 lines.
├── evals/
│   └── skill-name.eval.md   ← Required. At least 3 test cases.
├── config/           ← Optional. Reference data, frameworks, defaults.
└── templates/        ← Optional. Output templates, examples.
```

**Hard rules:**
- `SKILL.md` must stay under 500 lines. Move reference material to `config/` or `references/`.
- Directory name must exactly match the `name` field in frontmatter.
- The `evals/` folder is not optional. A skill without evals has no quality floor.

---

## 3. Frontmatter — Required Fields

Every `SKILL.md` opens with YAML frontmatter. No exceptions.

```yaml
---
name: skill-name
version: 1.0.0
description: >
  One to four sentences. What this skill does. When to trigger it (include
  trigger phrases). What it outputs. What related skills it chains with.
  Max 1024 characters. This is what surfaces in skill discovery — write it
  to be found, not to be complete.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent   # or: context-agnostic
  quality_gate: true          # or: false (only for thin utility skills)
last_updated: YYYY-MM-DD
---
```

### Field rules

| Field | Required | Rule |
|---|---|---|
| `name` | Yes | Lowercase, hyphens only. Matches directory name exactly. No `--`. |
| `version` | Yes | Semantic versioning: `MAJOR.MINOR.PATCH`. Patch = wording fix. Minor = new section or behaviour. Major = structural rebuild. |
| `description` | Yes | 1–1024 chars. Include trigger phrases. Mention related skills. |
| `metadata.author` | Yes | Author name. |
| `metadata.context` | Yes | `brain-dependent` or `context-agnostic`. See Section 8. |
| `metadata.quality_gate` | Yes | `true` for any skill that produces strategic output. `false` only for simple utilities. |
| `last_updated` | Yes | ISO date of last meaningful change. |

---

## 4. Required SKILL.md Sections

Every skill must contain these sections in this order. Section names are fixed — do not rename them.

### 4.1 Skill Header (after frontmatter)

```markdown
# [Skill Name] — [One-line purpose]

[2–3 sentence description of what this skill does, who it's for, and
what makes it different from a generic approach. This is the first thing
Claude reads — make it load the right mental frame immediately.]
```

### 4.2 `## ⓪ CONTEXT LOAD`

Defines what context this skill reads before doing anything else.

**For brain-dependent skills:**
```markdown
## ⓪ CONTEXT LOAD

Load `/foundation/brain.md` before intake. Extract:
- [Section X]: [What to pull and why]
- [Section Y]: [What to pull and why]

If brain file missing: surface once, non-blocking:
> "No PMM context found. Run `product-marketing-context` to make this sharper.
> Continuing with assumption-based output."

If a loaded section is marked 🔴 Placeholder: flag it before proceeding.
```

**For context-agnostic skills:**
```markdown
## ⓪ CONTEXT LOAD

This skill is context-agnostic. Do not load `/foundation/brain.md`.
Do not apply any prior company context, ICP, or positioning assumptions.
Start from the user's input only.
```

### 4.3 `## RELATED SKILLS`

Which skills to chain to, and when. Format:

```markdown
## RELATED SKILLS

- **skill-name** → [When to route here, what it adds]
- **skill-name** → [When to route here, what it adds]
```

Minimum 2 related skills. If a skill has no logical connections, it probably shouldn't exist as a standalone skill.

### 4.4 `## ① INTAKE`

How the skill gathers input before producing output. Rules:
- Ask questions in **one conversational message**, not one by one.
- Always reflect back the user's context before proceeding.
- Never generate output before completing intake.
- If user provides a document: read it fully, extract assumptions, reflect back before analysis.

### 4.5 Numbered execution sections `## ② ... ③ ... ④`

The core logic of the skill. Each section is a discrete step.

Rules:
- Number every section with a circled digit: ①②③④⑤⑥⑦⑧⑨
- Each section has one job. If a section does two things, split it.
- Use tables for classification logic, not prose.
- Use code blocks for output format templates.
- Use `> ⚠️` callouts for rules that must not be skipped.

### 4.6 `## OUTPUT STRUCTURE`

The exact format the skill must produce. Always include:
- A code block showing the full output template with placeholder values.
- Explicit instruction on formatting (markdown, tables, line breaks).
- What must always be present vs. what is conditional.

### 4.7 `## OPERATING RULES`

A flat list of non-negotiable rules for this skill. Plain English. One rule per line. These are the lines a `verify` skill will check against.

Format:
```markdown
## OPERATING RULES

- **Rule statement.** Reason or consequence.
- **Rule statement.** Reason or consequence.
```

Minimum 6 rules. If you can't write 6, the skill doesn't have enough logic to justify existing.

### 4.8 `## QUALITY GATE`

A table of checks that runs after output generation and before delivery. Required for all skills where `quality_gate: true`.

```markdown
## QUALITY GATE

Runs after output generation. Surface failures before delivering — never after.

| Check | Standard | Pass = |
|---|---|---|
| [Check name] | [What it tests] | [Pass condition] |
```

Minimum 5 checks. Each check must be binary (pass/fail), not subjective.

### 4.9 `## SELF-IMPROVEMENT LOOP`

How this skill captures learnings and writes them back. Required for all strategic skills. Format:

```markdown
## SELF-IMPROVEMENT LOOP

### Before every session:
1. [What to read]
2. [What to check]

### After every session:
1. [What to capture]
2. [Where to write it]

**Self-Improvement Trigger format:**
Surface before encoding. Never encode silently.

> 🔁 SELF-IMPROVEMENT TRIGGER
> Pattern: [what was observed]
> Proposed update: [exact change]
> Location: [file path]
> Awaiting approval before encoding.
```

### 4.10 `## CHANGELOG`

Every meaningful change logged. Most recent first.

```markdown
## CHANGELOG

### v[X.Y.Z] — YYYY-MM-DD
[What changed and why. Not just "updated" — what specifically changed.]

### v1.0.0 — YYYY-MM-DD
Initial release.
```

---

## 5. Eval Format

Every skill needs an eval file at `evals/skill-name.eval.md`.

Minimum 3 test cases. Each test case must include:

```markdown
## Test Case [N]: [Descriptive name]

**Input:**
[Realistic user prompt or scenario]

**Expected output includes:**
- [Specific element that must be present]
- [Specific element that must be present]
- [Specific element that must be present]

**Expected output excludes:**
- [What should NOT appear]

**Pass condition:**
[Single sentence defining what "correct" looks like for this case]
```

One test case must be an **edge case** (missing context, ambiguous input, or conflicting signals).  
One test case must test the **quality gate** specifically.

---

## 6. Line Budget and Offloading

`SKILL.md` has a hard 500-line limit. This is not a suggestion.

When you hit the limit:
- Move detailed reference frameworks to `config/[framework-name].md`
- Move output templates to `templates/[template-name].md`
- Move long examples to `references/[example-name].md`
- Reference them in SKILL.md: `→ See config/framework-name.md`

This keeps `SKILL.md` fast to load and easy to scan. Skills that are hard to scan produce inconsistent output because Claude doesn't reliably read all of a long file.

---

## 7. Writing Style

**Voice:** Direct and instructional. Second person ("When you're planning...").  
**Length:** Short paragraphs. 2–4 sentences max per paragraph.  
**Lists:** Use for steps, rules, checks. Not for prose.  
**Tables:** For classification logic, scoring, reference data.  
**Bold:** For key terms, rule statements, non-negotiables.  
**Callouts (`> ⚠️`):** For rules that must not be skipped. Use sparingly — if everything is urgent, nothing is.  
**Emojis:** Only as navigational markers (① ② ⓪ 🐯 🔁 ⚠️). Not decorative.  
**No "this skill will..."** — Write the instructions directly, not a description of them.

---

## 8. Context Classification: Brain-Dependent vs Context-Agnostic

This is the most important architectural decision for each skill.

### Brain-Dependent Skills

These skills **must** load `/foundation/brain.md` before running. They use company-specific ICP, positioning, alternatives, voice, and proof points to personalise output.

**Skills in this category:**
- `positioning-messaging` — output depends entirely on your alternatives and ICP
- `competitive-battlecard` — depends on your positioning and proof points
- `go-to-market-strategy` — depends on your ICP, tier history, competitive context
- `buyer-personas` — depends on your ICP and product context
- `value-prop-statements` — depends on your alternatives and positioning
- `gaccs-brief` — depends on your ICP, voice, and proof points
- `stakeholder-maps` — depends on your GTM motion
- `retro` — depends on your launch history
- `pre-mortem` — depends on your ICP, positioning, and GTM motion
- `workflow-orchestrator` — reads and writes brain across all sections
- `ci-stakeholder-briefing` — depends on your competitive landscape
- `pmm-okrs` — depends on your product stage and GTM motion

### Context-Agnostic Skills

These skills **must not** load brain context. They operate on frameworks and universal logic only. This prevents your current positioning from biasing output that should be framework-pure.

**Why this matters:** If `experiment-doc-builder` loads your current ICP, it will unconsciously validate experiments that fit your current ICP rather than challenging them. The framework should be objective.

**Skills in this category:**
- `experiment-doc-builder` — experiment rigour is universal, not company-specific
- `prioritization-frameworks` — scoring frameworks are universal
- `privacy-policy` — legal compliance is not company-specific
- `pmm-resume` — career advice should not be biased by your current company context
- `writing-assistant` — grammar and clarity are universal; voice is passed explicitly by the user, not auto-loaded
- `interview-summary` — synthesis should be unbiased by existing positioning
- `prd` — product requirements structure is universal

**The rule:** If the skill's quality depends on knowing your product — it's brain-dependent. If the skill's quality depends on a universal framework — it's context-agnostic. When in doubt, make it agnostic.

---

## 9. Brain Read/Write Contract

For every brain-dependent skill, declare exactly what it reads and writes.

```markdown
## BRAIN CONTRACT

**Reads:**
- Section 2 (ICP): [What specifically is extracted]
- Section 3 (Positioning): [What specifically is extracted]

**Writes:**
- Section 7 (Launch History): [What is written back and when]

**Never writes to:** Section 1, Section 6
```

This prevents skills from silently overwriting brain sections they shouldn't touch.

---

## 10. Version Increment Rules

| Change type | Increment |
|---|---|
| Typo or wording fix | PATCH (1.0.0 → 1.0.1) |
| New section, new check, new operating rule | MINOR (1.0.0 → 1.1.0) |
| Restructured logic, changed intake, new output format | MAJOR (1.0.0 → 2.0.0) |
| Patched from a live session finding | PATCH with session note in changelog |

Increment `last_updated` on every change, regardless of increment size.

---

## 11. The `review` Meta Skill Checklist

When the `review` meta skill audits a `SKILL.md`, it checks these in order. This is the same list you use when self-reviewing before committing.

**Frontmatter (5 checks):**
- [ ] All required fields present
- [ ] `name` matches directory name
- [ ] `description` includes trigger phrases
- [ ] `metadata.context` declared
- [ ] `version` and `last_updated` present

**Structure (9 checks):**
- [ ] `## ⓪ CONTEXT LOAD` present and correctly typed for context classification
- [ ] `## RELATED SKILLS` present with ≥2 entries
- [ ] `## ① INTAKE` present — asks questions in one message, reflects back before proceeding
- [ ] Numbered execution sections present
- [ ] `## OUTPUT STRUCTURE` present with template in code block
- [ ] `## OPERATING RULES` present with ≥6 rules
- [ ] `## QUALITY GATE` present (if `quality_gate: true`) with ≥5 checks
- [ ] `## SELF-IMPROVEMENT LOOP` present (for strategic skills)
- [ ] `## CHANGELOG` present with ≥1 entry

**Quality (5 checks):**
- [ ] SKILL.md is ≤500 lines
- [ ] No section reads like a README or documentation
- [ ] Output template is complete and realistic
- [ ] Evals file exists with ≥3 test cases including one edge case
- [ ] Brain contract declared (if brain-dependent)

**Pass threshold:** 17/19 checks. Skills below this threshold are flagged for improvement before next use.

---

## 12. Skill Tiers (Internal Classification)

Not all skills are equal in complexity or strategic importance. Knowing the tier tells you how much investment to put into a skill.

| Tier | Description | Skills | Required sections |
|---|---|---|---|
| **T1 — Strategic** | High-stakes output, used in executive or customer-facing contexts | pre-mortem, positioning-messaging, competitive-battlecard, go-to-market-strategy | All sections required. Quality gate mandatory. Self-improvement loop mandatory. |
| **T2 — Execution** | Day-to-day PMM work, used frequently, medium stakes | experiment-doc, prd, retro, stakeholder-maps, gaccs-brief, pmm-okrs, buyer-personas | All sections required. Quality gate required. |
| **T3 — Utility** | Tactical outputs, lower stakes | writing-assistant, pmm-resume, privacy-policy, interview-summary, prioritization-frameworks | Context load, intake, output structure, operating rules required. Quality gate optional. |
| **T4 — Meta** | Skills that operate on other skills | review, learn, verify, workflow-orchestrator, product-marketing-context | Custom — defined per meta skill. |

---

## 13. What Makes a Skill "Best in Class"

A best-in-class skill has five properties:

**1. It fails gracefully.** Missing context, vague input, or interrupted sessions are handled explicitly — not silently ignored or producing generic output.

**2. It enforces its own quality.** The quality gate runs before output is delivered. A skill that can produce a bad output without flagging it is not production-grade.

**3. It gets smarter over time.** The self-improvement loop is not cosmetic. Patterns surface, get approved, get encoded. The 10th session is meaningfully sharper than the first.

**4. It knows what it doesn't do.** The operating rules state what the skill will NOT do. Boundaries are as important as capabilities.

**5. It hands off cleanly.** Related skills are named with specific routing conditions — not "you could also run X." The handoff logic is precise enough that the user never wonders what to do next.

---

*This spec is a living document. Update it when patterns emerge across multiple skills that should be standardised. The spec version should increment whenever a new requirement is added.*
