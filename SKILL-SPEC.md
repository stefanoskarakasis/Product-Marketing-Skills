# SKILL-SPEC.md
## Product Marketing Skills — Skill Authoring Standard

**Version:** 2.1.0  
**Last updated:** 2026-08-22  
**Applies to:** All skills in this repository  
**Owner:** Stefanos Karakasis

This is the canonical standard every skill in this repo must meet.  
The `meta-review` skill enforces it. New skills ship only when they pass it.  
There is no separate improvement-schedule document — this spec itself is
the record of what's required, and it's updated in place as standards change.

---

## 1. What a Skill Is (and Isn't)

A skill is a **structured instruction set** that tells Claude how to behave when invoked. It is not documentation, a feature list, or a README.

A skill that reads like a README produces README-quality output.  
A skill that reads like an operating manual produces operating-manual-quality output.

**The test:** Could a new PMM follow this skill and know exactly what to do at every step, in every edge case, without asking a question? If no — it's not done.

---

## 2. File Structure

Every skill lives in its own directory:

```
skills/skill-name/
├── SKILL.md                      ← Required. Main instruction file. Max 500 lines.
├── evals/
│   └── skill-name.eval.md        ← Required. At least 3 test cases.
├── config/                       ← Optional. Reference data, frameworks, defaults.
└── templates/                    ← Optional. Output templates, examples.
```

**Hard rules:**
- `SKILL.md` stays under 500 lines. Move reference material to `config/` or `references/`.
- Directory name must exactly match the `name` field in frontmatter.
- `evals/` is not optional. A skill without evals has no quality floor.
- **Do not have a `SKILL.md` in a template folder** — Claude Code treats any file named `SKILL.md` as a loadable skill.

---

## 3. Frontmatter — Required Fields

Every `SKILL.md` opens with YAML frontmatter:

```yaml
---
name: skill-name
version: 1.0.0
description: >
  What this skill does + 3–5 trigger phrases verbatim. Target 300–600 chars.
  Trigger phrases belong here — they drive auto-fire. Explanatory prose
  belongs in the H1 paragraph of the body, not here.
  Example: "Assigns launch tier and builds GTM strategy briefs. Trigger on:
  'launch this', 'what tier is this', 'GTM strategy for', 'run GTM workflow'."
metadata:
  author: Stefanos Karakasis
  context: brain-dependent        # or: context-agnostic — see Section 8
  quality_gate: true              # false only for simple utilities
last_updated: YYYY-MM-DD
---
```

### Field rules

| Field | Required | Rule |
|---|---|---|
| `name` | Yes | Lowercase, hyphens only. Matches directory name exactly. No `--`. |
| `version` | Yes | Semantic versioning. See Section 10. |
| `description` | Yes | 300–600 chars. Trigger phrases verbatim. Mention related skills for scope boundaries. |
| `metadata.author` | Yes | Author name. |
| `metadata.context` | Yes | `brain-dependent` or `context-agnostic`. See Section 8. |
| `metadata.quality_gate` | Yes | `true` for any skill producing strategic output. `false` for simple utilities only. |
| `last_updated` | Yes | ISO date of last meaningful change. |

---

## 4. The Seven Required Sections

Every `SKILL.md` must contain exactly these seven sections, in this order. **Do not rename them. Do not omit them.** Use `n.v.t.` if a section doesn't apply — that's the whole point. An omitted section says nothing. `n.v.t.` says "I considered this and it doesn't apply."

After frontmatter, open with:

```markdown
# Skill Name

One paragraph. What this skill does and why it exists. No commands, no section
headers — just the essence. Someone reading this paragraph should know immediately
whether this is the right skill.
```

Then the seven sections:

---

### Section 1: `## Trigger`

When to use this skill and when not to. Explicit routing to other skills.

```markdown
## Trigger

- **When:** The condition that fires this skill. One sentence.
- **Not for:** Explicit exclusions — prevents scope creep and overlap.
  Reference the correct skill by name.
- **Example prompts:**
  - "exact trigger phrase 1"
  - "exact trigger phrase 2"
  - "edge case phrasing that should also work"
```

**Why this matters:** Without explicit exclusions, skills accumulate scope silently. After 10 skills, nobody knows where one ends and another begins. Name the boundary.

---

### Section 2: `## Inputs`

What this skill needs before it can run.

```markdown
## Inputs

- **Args:** What the user passes. CLI-style if applicable. `n.v.t.` if none.
- **Defaults:** What happens if no arg is given. `n.v.t.` if no defaults.
- **Context keys:** Which files, brain sections, or external resources are
  needed before running. List file paths explicitly.
  n.v.t. if context-agnostic and no files needed.
```

---

### Section 3: `## Pre-flight`

Dependency checks and early-exit conditions. Running before anything else.

```markdown
## Pre-flight

- [Dependency check — what must exist or be loaded]
- [Early-exit condition — when failing fast beats degraded output]
- n.v.t. if no pre-flight needed — write it explicitly, don't omit it.
```

**The `n.v.t.` rule applies here most often.** Simple utility skills genuinely have no pre-flight. Write `n.v.t.` explicitly so reviewers know it was considered.

---

### Section 4: `## Steps`

The core logic. Each step is a discrete, named action.

**Step header convention:** Always include a short name in imperative form.

```markdown
## Steps

### Step 1: Load Context

[Action. Concrete. What to read, what to extract.]

### Step 2: Run Intake

[Next action.]

### Step N: Deliver Output

[Closing action.]
```

**Why named steps matter:** Cross-references in memory files and knowledge logs use step names. If you renumber steps, names keep references stable. `"See Step 4 (Intake)"` survives a re-order. `"See Step 4"` doesn't.

Rules for steps:
- Each step has one job. Split if a step does two things.
- Use code blocks for commands, queries, output templates.
- Use `> ⚠️` callouts for rules that cannot be skipped. Use sparingly — if everything is urgent, nothing is.
- Idempotent where possible.

---

### Section 5: `## Outputs`

What this skill produces.

```markdown
## Outputs

- **Files written:** path → what's in it. n.v.t. if pure read-only.
- **Chat output format:** markdown shape, with example or reference to
  example in appendix. n.v.t. if no chat output.
- **External side effects:** DB writes, external services triggered.
  n.v.t. if none.
```

**Convention — output templates go in a code fence.** If this section or an appendix shows a template with H2/H3 headers, wrap it in ` ```markdown … ``` `. Otherwise every parser (skill audit, plugin sync) reads those raw `##` lines as skill sections — producing broken audits.

---

### Section 6: `## Verification`

How to confirm the skill ran correctly. Concrete and checkable.

```markdown
## Verification

- [How to verify the output is correct. Concrete commands or checks.]
- [What the expected result looks like.]
- n.v.t. only if the output is self-evidently verifiable with no steps needed.
```

This is not a quality gate (that's in Section 9). Verification is for the user to confirm success after the skill completes.

---

### Section 7: `## Do Not Use For`

Explicit routing away from this skill. Every skill has boundaries.

```markdown
## Do Not Use For

- **skill-name** — When to use that skill instead. One sentence.
- **skill-name** — When to use that skill instead.
- n.v.t. if this skill has no overlap with other skills — write it explicitly.
  n.v.t. here means: "overlap was considered and there is none."
```

**This is the most important section for a multi-skill system.** Without it, users hit the wrong skill and get confused. With it, the routing is baked in.

---

## 5. Additional Required Sections (Strategic Skills)

For Tier 1 and Tier 2 skills (see Section 12), add these after the seven required sections:

### `## Operating Rules`

Non-negotiable rules for this skill. One rule per line. These are what `verify` checks against.

```markdown
## Operating Rules

- **Rule statement.** Reason or consequence.
- **Rule statement.** Reason or consequence.
```

Minimum 6 rules for T1/T2 skills. If you can't write 6, the skill doesn't have enough defined behaviour to be production-grade.

### `## Quality Gate`

Runs after output generation, before delivery. Required for all skills where `quality_gate: true`.

```markdown
## Quality Gate

Runs after output generation. Surface failures before delivering — never after.

| Check | Standard | Pass = |
|---|---|---|
| [Check name] | [What it tests] | [Pass condition] |
```

Minimum 5 checks. Each check must be binary (pass/fail), not subjective.

### `## Self-Improvement Loop` — not required yet

**As of v2.1.0 of this spec, no skill is required to have this section.**
The version this spec previously mandated described a per-skill promotion
pipeline (`knowledge/rules.md`, `knowledge/hypotheses.md`, a "confirmed
3+ times" graduation rule, session logs to files no skill actually wrote
to) that was never real anywhere in this repo — it existed only as
prose, not as working behaviour, and was removed skill-by-skill across
Workstream 4b.

The repo's actual, working compounding mechanism today is simpler and
already real: any skill can read `/context/meta-patterns.md` at its own
Pre-flight step for guardrails that apply to it, and `meta-synthesis`
periodically scans `/context/skill-sessions.md` for repeated patterns
and proposes new guardrails or brain updates, gated on explicit user
approval. See the `meta-synthesis` skill for the reference
implementation.

A real, repo-wide self-improvement design — one where skills actually
log sessions, meta-synthesis actually has something to read, and this
spec can honestly require it again — is planned as a deliberate, later
pass across every skill, not something to bolt back on piecemeal per
skill. Until that pass happens, do not add a `## Self-Improvement Loop`
section to any skill; it would describe behaviour the skill doesn't
perform.

### `## Changelog` — not required

**As of v2.1.0 of this spec, no skill should have a `## Changelog`
section.** Version history belongs in this repo's git log, which is
the actual audit trail — a hand-maintained changelog duplicates it,
drifts from it, and was removed from every `SKILL.md` in the repo
across Workstream 4b. `metadata.last_updated` in frontmatter is
sufficient for "when did this last change" at a glance.

---

## 6. Appendix Conventions

Optional content goes after the seven required sections. Use these canonical appendix names so skill-audit tooling can skip them correctly:

| Appendix name | Use for |
|---|---|
| `## Gotchas` | Edge cases, traps, knowledge that doesn't follow from the steps |
| `## Voice reference` | Link to voice/tone reference file |
| `## Example output` | Reference illustration of what the skill produces |
| `## Edge cases` | Optional, with suffix if needed: `Edge cases — delivery` |
| `## When to offer proactively` | When Claude should suggest this skill unprompted |
| `## Dialog mode` | Opt-in conversational behaviour for iterative skills |
| `## Reference` | External docs, links |

**Binding appendices** — those that are part of the flow, not just reader notes — get `(appendix — reference for Step N)` in the title. Example: `## Feedback format (appendix — reference for Step 8)`. This makes it visible that the appendix is part of the execution path.

---

## 7. The `n.v.t.` Rule

This is the single most important consistency mechanism in the spec.

**Every section must be present. Always.**

If a section doesn't apply to a skill, write `n.v.t.` (not applicable) under it — do not omit the section.

- An omitted section says nothing about whether it was considered.
- `n.v.t.` says: "this was considered and doesn't apply."

These are completely different signals. The second is auditable. The first is not.

**This rule applies to all seven required sections and to the `## Do Not Use For` section specifically.** A `## Do Not Use For` with `n.v.t.` says: "there are no overlapping skills." A missing `## Do Not Use For` says nothing — and after 15+ skills, that silence causes real confusion.

---

## 8. Context Classification: Brain-Dependent vs Context-Agnostic

The most important architectural decision for each skill. Declared in frontmatter as `metadata.context`.

### Brain-Dependent (`brain-dependent`)

Must load `/foundation/brain.md` before running. Output depends on company-specific ICP, positioning, alternatives, voice, or proof points.

Load instruction for brain-dependent skills:

```markdown
## Pre-flight

- Load `/foundation/brain.md`. Extract: [Section X → what to pull and why].
- If brain file missing: surface once, non-blocking:
  > "No PMM context found. Run `product-marketing-context` to make this
  > significantly sharper. Continuing with assumption-based output."
- If a loaded section is marked 🔴 Placeholder: flag before proceeding.
```

**Brain-dependent skills:** `positioning-messaging`, `go-to-market-strategy`, `gaccs-brief`, `stakeholder-maps`, `retro`, `pre-mortem`, `workflow-orchestrator`, `pmm-okrs`, `beachhead-segment`, `product-marketing-context`

### Context-Agnostic (`context-agnostic`)

Must **not** load brain context. Operates on universal frameworks and the user's input only.

Load instruction for context-agnostic skills:

```markdown
## Pre-flight

- This skill is context-agnostic. Do not load `/foundation/brain.md`.
- Do not apply prior company context, ICP, or positioning assumptions.
- Start from the user's input only.
```

**Why this matters:** If `experiment-doc-builder` loads your current ICP, it validates experiments that fit your current ICP instead of stress-testing them. The framework must be objective.

**Context-agnostic skills:** `experiment-doc-builder`, `prioritization-frameworks`, `privacy-policy`, `pmm-resume`, `writing-assistant`, `interview-summary`, `prd`

**The rule:** If output quality depends on knowing your product → brain-dependent. If output quality depends on a universal framework → context-agnostic. When in doubt, choose agnostic.

---

## 9. Brain Read/Write Contract

For every brain-dependent skill, declare exactly what it reads and writes. Add this block to `## Inputs`:

```markdown
**Brain contract:**
- Reads: Section 2 (ICP) — [what specifically], Section 3 (Positioning) — [what specifically]
- Writes: Section 2 (ICP) — [what is written and when]
- Never writes to: Section 1, Section 6
```

This prevents skills from silently overwriting sections they shouldn't touch.

---

## 10. Version Increment Rules

| Change type | Increment |
|---|---|
| Typo, wording fix, minor clarification | PATCH (1.0.0 → 1.0.1) |
| New section, new check, new operating rule, new step | MINOR (1.0.0 → 1.1.0) |
| Restructured logic, changed intake, new output format, new section order | MAJOR (1.0.0 → 2.0.0) |
| Patched from a live session finding | PATCH with session note in changelog |

Always update `last_updated` on every change regardless of increment size.

---

## 11. Eval Format

Every skill needs `evals/skill-name.eval.md`. Minimum 3 test cases.

```markdown
## Test Case N: Descriptive name

**Input:**
[Realistic user prompt or scenario]

**Expected output includes:**
- [Specific element that must be present]
- [Specific element that must be present]

**Expected output excludes:**
- [What should NOT appear]

**Pass condition:**
[Single sentence defining what "correct" looks like]
```

One test case must be an **edge case** (missing context, ambiguous input, conflicting signals).  
One test case must test the **quality gate** specifically.

---

## 12. Skill Tiers

| Tier | Description | Examples | Requirements |
|---|---|---|---|
| **T1 — Strategic** | High-stakes, executive or customer-facing output | pre-mortem, positioning-messaging, competitive-battlecard, go-to-market-strategy | All 7 sections + operating rules + quality gate |
| **T2 — Execution** | Day-to-day PMM work, high frequency, medium stakes | experiment-doc, prd, retro, stakeholder-maps, gaccs-brief, pmm-okrs, buyer-personas | All 7 sections + quality gate |
| **T3 — Utility** | Tactical outputs, lower stakes | writing-assistant, pmm-resume, privacy-policy, interview-summary, prioritization-frameworks | All 7 sections. Quality gate optional. |
| **T4 — Meta** | Skills that operate on other skills | meta-review, meta-learn, meta-verify, meta-synthesis, workflow-orchestrator, product-marketing-context | Custom per meta skill. All 7 sections still required. |

---

## 13. The `review` Meta Skill Checklist

When the `review` meta skill audits a `SKILL.md`, it checks these in order. Use this list for self-review before committing.

**Frontmatter (5 checks):**
- [ ] All required fields present
- [ ] `name` matches directory name exactly
- [ ] `description` is 300–600 chars and includes trigger phrases verbatim
- [ ] `metadata.context` declared as `brain-dependent` or `context-agnostic`
- [ ] `version` and `last_updated` present

**Seven required sections (7 checks):**
- [ ] `## Trigger` — includes When, Not for, Example prompts
- [ ] `## Inputs` — all three sub-fields present (or `n.v.t.`)
- [ ] `## Pre-flight` — present (or explicit `n.v.t.`)
- [ ] `## Steps` — named steps in imperative form, at least 2 steps
- [ ] `## Outputs` — all three sub-fields present (or `n.v.t.`)
- [ ] `## Verification` — concrete and checkable (or explicit `n.v.t.`)
- [ ] `## Do Not Use For` — present with routing (or explicit `n.v.t.`)

**Tier-appropriate sections (2 checks):**
- [ ] `## Operating Rules` present with ≥6 rules (T1/T2)
- [ ] `## Quality Gate` present with ≥5 binary checks (T1/T2 where `quality_gate: true`)

**Quality (3 checks):**
- [ ] `SKILL.md` is ≤500 lines
- [ ] Output template is in a code fence (not raw markdown headers)
- [ ] Evals file exists with ≥3 test cases including one edge case

**Pass threshold:** 15/17 checks. Skills below this are flagged for improvement before next use.

**Not checked (by design):** `## Self-Improvement Loop` and `## Changelog`
are not part of this checklist. See Section 5 — neither is required
under this version of the spec.

---

## 14. What Makes a Skill "Best in Class"

A best-in-class skill has five properties:

**1. It fails gracefully.** Missing context, vague input, and interrupted sessions are handled explicitly — not silently producing generic output.

**2. It enforces its own quality.** The quality gate runs before output is delivered. A skill that can produce a bad output without flagging it is not production-grade.

**3. It knows its boundaries.** The `## Do Not Use For` section names where the skill ends and routes clearly to what comes next. Users never wonder whether they're in the right skill.

**4. It compounds through the shared system, not its own private loop.** No individual skill runs its own self-improvement pipeline. `meta-synthesis` is where patterns get detected across sessions and skills, and any resulting guardrail or brain update goes live for every skill to read at Pre-flight. A skill gets smarter over time by being part of that shared system — not by inventing its own memory.

**5. It hands off cleanly.** The `## Trigger` section names specific routing conditions — not vague "you could also run X." The handoff is precise enough that the user never wonders what to do next.

---

## 15. SKILL.md Template

Copy this to `skills/<skill-name>/SKILL.md` when creating a new skill. Fill every section. Use `n.v.t.` where genuinely not applicable — never leave a section blank or omit it.

```markdown
---
name: skill-name
version: 1.0.0
description: >
  What this skill does + 3–5 trigger phrases verbatim. 300–600 chars.
  Trigger phrases here drive auto-fire. Explanatory prose goes in the body.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: YYYY-MM-DD
---

# Skill Name

One paragraph. What this skill does and why it exists. No commands, no
section headers — just the essence. Someone reading this should know
immediately whether this is the right skill.

## Trigger

- **When:** [Condition. One sentence.]
- **Not for:** [Explicit exclusions with routing to correct skill.]
- **Example prompts:**
  - "[exact phrase 1]"
  - "[exact phrase 2]"
  - "[edge case that should also work]"

## Inputs

- **Args:** [n.v.t. if none]
- **Defaults:** [n.v.t. if no defaults]
- **Context keys:** [Files, brain sections, external resources needed.
  n.v.t. if context-agnostic.]
  - **Brain contract:** Reads: [sections]. Writes: [sections]. Never writes to: [sections].

## Pre-flight

- [Dependency check or early-exit condition]
- n.v.t.

## Steps

### Step 1: [Name — imperative]

[Action. Concrete.]

### Step 2: [Name]

[Next action.]

### Step N: [Deliver Output]

[Closing action.]

## Outputs

- **Files written:** [path → what's in it. n.v.t. if read-only.]
- **Chat output format:** [markdown shape. n.v.t. if no chat output.]
- **External side effects:** [n.v.t. if none.]

## Verification

- [How to confirm the skill ran correctly. Concrete.]
- n.v.t.

## Do Not Use For

- **[skill-name]** — [When to use that skill instead.]
- n.v.t.

---

## Operating Rules

- **Rule.** Reason.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| [Check] | [What it tests] | [Pass condition] |
```

No `## Self-Improvement Loop` or `## Changelog` section — neither is
required under this version of the spec. See Section 5.

---

*This spec is a living document. When patterns emerge across multiple skills that should be standardised, update the spec and increment its version. The spec version tracks separately from individual skill versions.*
