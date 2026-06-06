---
name: pmm-okrs
version: 2.1.0
description: >
  Guides Product Marketing leaders and individual PMMs through building a complete,
  export-ready OKR set for their quarter — including Objective, Key Results, Projects,
  Scorecard metrics, and Exec Summary language. Use when setting quarterly OKRs,
  reviewing existing OKRs, stress-testing KR quality, or building a measurement plan.
  Trigger on: "help me set our OKRs", "are my KRs measurable", "build a scorecard",
  "stress-test this KR", "write OKRs for my team", "present goals to exec team".
  Produces output paste-ready for the PMM OKR Builder spreadsheet or leadership sharing.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# pmm-okrs

A guided OKR builder for Product Marketing teams. Run it at the start of every quarter.
Outputs a complete, review-ready OKR set you can paste directly into the PMM OKR Builder sheet.

---

## Trigger

- **When:** Start of any quarter when setting PMM OKRs. When reviewing or stress-testing
  existing KRs before committing. When building a measurement plan or leadership-ready
  exec narrative from a finalised OKR set.
- **Not for:** Company-level OKR design (not PMM-specific) → general planning tool.
  Revenue forecasting or headcount planning. OKR tooling setup (Lattice, Workday) —
  this skill produces content, not configuration. If no quarterly strategy exists yet →
  run `hs-pmm-strategy` first, then return here.
- **Example prompts:**
  - "Help me set our Q3 OKRs"
  - "Are these KRs measurable enough?"
  - "Build a scorecard for my chosen option"
  - "Write OKRs for my team lead who owns competitive intelligence"
  - "Stress-test this KR: improve win rate in enterprise"
  - "I need to present our goals to the exec team next week"

---

## Inputs

- **Args:** Company objective, PMM mandate, team size, primary metric, biggest challenge,
  ICP, and named competitors. All optional at start — skill gathers via intake flow.
- **Defaults:** If no args provided, run intake flow via `/build`. If partial context
  is provided, infer where possible and surface gaps explicitly before proceeding.
- **Context keys:**
  - `.agents/product-marketing-context.md` — optional but recommended. Load Revenue
    Levers, Goals & KPIs, Big Bet Campaigns, Company Overview silently if present.
  - `knowledge/okrs/rules.md` — apply confirmed OKR craft rules by default.
  - `knowledge/okrs/hypotheses.md` — test any active hypothesis if applicable today.
  - `decisions/` — check for prior decisions before making new recommendations.

---

## Pre-flight

Before starting, check `.agents/product-marketing-context.md`.

**If it exists — load silently:**
- `## Revenue Levers` → align OKRs to the stack-ranked levers
- `## Goals & KPIs` → use North Star + OMTM as anchors
- `## Big Bet Campaigns` → surface as project goals
- `## Company Overview` → stage and business model context

**Confidence awareness:** If loaded sections are 🔴, flag before building OKRs:
> "Revenue Levers is marked as Placeholder — OKRs built on this may need revisiting. Want to update it first?"

**If missing:** Proceed. Surface once:
> "Run `hs-product-marketing-context BUILD` first for sharper OKRs. Continuing."

**Related skills — cross-reference before or after this skill:**
- **hs-pmm-strategy** → run before this skill if no quarterly strategy exists yet
- **hs-product-requirement-doc** → PRDs inform project OKRs; check for alignment
- **hs-gaccs-brief** → campaign briefs should trace back to OKR project goals

---

## Steps

### Step 1 — `/build`
1. Run intake (or infer from pasted context). 2. Load `knowledge/okrs/rules.md`.
3. Check `decisions/` for prior choices in this area. 4. Generate three OKR options.
5. Run independent evaluation pass (Block 3) on all three. 6. Present with Quality Gate
results inline. 7. Log option selection to `decisions/`.

### Step 2 — `/review`
1. Accept pasted OKRs. 2. Run each KR through all five Quality Gates (binary).
3. Flag every failure with an ADVERSARIAL CALLOUT and a rewrite. 4. Return annotated set.

### Step 3 — `/scorecard`
1. Work from OKRs in session or ask user to paste. 2. Map each KR to metric, target,
measurement method. 3. Group by category. 4. Confirm Weight = 100%. 5. Output scorecard.

### Step 4 — `/exec`
1. Confirm OKRs are finalised (not drafts). 2. Translate to one-paragraph exec narrative.

### Step 5 — `/map`
1. For each KR, generate required projects with owner type, effort (S/M/L), timeline.
2. Flag capacity conflicts if team size known.

### Step 6 — `/stress-test [KR]`
1. Accept one KR. 2. Run through five Quality Gates. 3. Return per-gate pass/fail + rewrite.

---

## Outputs

- **Files written:** `decisions/YYYY-MM-DD-{topic}.md` when a strategic OKR choice
  is logged. `knowledge/okrs/hypotheses.md` and `rules.md` when the self-improvement
  loop triggers at session end. No other writes.
- **Chat output format:** Three OKR option blocks in code-fence structured output,
  each with Quality Gate results inline. Scorecard table. Exec Summary paragraph.
  All formatted for direct paste into the PMM OKR Builder spreadsheet.
- **External side effects:** n.v.t.

---

## Verification

- All `/build` output contains three OKR options unless user explicitly requests fewer.
- Every option includes Quality Gate results (five binary checks) before delivery.
- No output delivered before the independent evaluation pass (Block 3) has run.
- Adversarial callouts surface inline before delivery, never post-delivery.
- Decision log written whenever a recommendation will affect the user's quarter.
- `/exec` output produced only from finalised OKRs, not from draft options.
- Scorecard Weight column confirmed to total 100% before output is delivered.

---

## Do Not Use For

- **hs-pmm-strategy** — if no quarterly strategy exists yet, run that first. This skill
  builds OKRs *from* a strategy, not *instead of* one.
- **hs-prioritization-frameworks** — for prioritising *which initiatives* to include in
  a quarter before OKRs are set. Run that upstream, then return here.
- **hs-gaccs-brief** — for campaign planning that traces back to OKRs already set.
  Use after `/build` to brief individual campaigns.
- **Company-level OKR design** — this skill is PMM-specific. Exec team or company
  OKRs require different framing and are out of scope.
- **OKR tooling setup** — this skill produces OKR content, not Lattice/Workday
  configuration or workflow automation.

---

## Reasoning Architecture

### Block 1 — Knowledge Architecture (Learning Loop)

**Before any task:** Load `knowledge/INDEX.md` and relevant domain folders. Apply
`rules.md` by default. Test any active hypothesis if applicable today.

**After any session:** Extract 1–3 insights. Unconfirmed → `hypotheses.md`.
Confirmed 3+ times → auto-promote to `rules.md`. Contradicted → demote to `hypotheses.md`.

> **Environment note:** Persistent `/knowledge/` works in Claude Code and Cowork.
> In Claude.ai chat, surface insights at end of session for manual carry-forward.

### Block 2 — Decision Journal

Check `decisions/` before any recommendation. Log new decisions immediately.

```
File: decisions/YYYY-MM-DD-{topic}.md
Decision / Context / Alternatives / Reasoning / Trade-offs / Supersedes
```

**Log when:** Choosing between OKR options. Recommending a measurement method.
Flagging a failing gate. Any recommendation affecting the user's quarter.

### Block 3 — Independent Evaluation Pass

After generating any output: re-read cold as evaluator. Run all five Quality Gates
binary. Rewrite failures before delivery. Report gate results inline.

---

## Commands

### /build
Builds three OKR options from scratch with Quality Gate results.

**Example prompts:**
- `Help me set our Q3 OKRs. 3-person PMM team, B2B SaaS, company OKR: grow ARR 40%.`
- `Build OKRs for a solo PMM at a Series B. Challenge: positioning isn't landing.`

### /review
Audits existing OKRs against all five Quality Gates. Returns exact fixes.

**Example input:**
```
Objective: Improve go-to-market in mid-market.
KR 1: Launch 4 battlecards. KR 2: Run monthly training. KR 3: Increase pipeline.
```

### /scorecard
Maps each KR to metrics, targets, and measurement methods.

### /exec
Generates one-paragraph exec-ready OKR narrative for QBRs and VP presentations.

### /map
Builds OKR → Projects table with owner type, effort (S/M/L), and timeline.

### /individual [specialty]
Generates OKRs for an individual PMM contributor.
- `/individual positioning` · `/individual competitive` · `/individual gtm`

### /stress-test [KR]
Runs one KR through all five Quality Gates. Returns pass/fail + rewrite.

---

## Output Format

```markdown
═══════════════════════════════════════════
OPTION [A / B / C] — [Strategic Focus]
═══════════════════════════════════════════
OBJECTIVE: [1–2 sentence qualitative goal.]

KR 1 — [Name]: [Outcome. Target. Deadline. Measurement.]
KR 2 — [Name]: [Outcome. Target. Deadline. Measurement.]
KR 3 — [Name]: [Outcome. Target. Deadline. Measurement.]

CONFIDENCE: [X%]
CHOOSE THIS WHEN: [1-sentence fit description.]

KEY PROJECTS: 1. [name — KR] 2. [name — KR] 3. [name — KR]

QUALITY GATE RESULTS:
Gate 1 — Outcome not output:           ✅ / ❌
Gate 2 — Measurable without ambiguity: ✅ / ❌
Gate 3 — Causally linked to objective: ✅ / ❌
Gate 4 — 60–70% confidence:            ✅ / ❌
Gate 5 — Three or fewer KRs:           ✅ / ❌
═══════════════════════════════════════════
```

---

## Quality Gates

| Gate | Test | Fail | Pass |
|---|---|---|---|
| 1 | Outcome, not output | "Launch 4 battlecards" | "Win rate up 8%" |
| 2 | Measurable without ambiguity | "Improve messaging" | "80% resonance from 50 reviews" |
| 3 | Causally linked to objective | PMM doesn't own lever | PMM controls what moves this |
| 4 | 60–70% confidence | >90% or <50% | Ambitious but achievable |
| 5 | Three or fewer KRs | Four or more | Three or fewer |

**Adversarial callout format:**
> ⚠️ ADVERSARIAL CALLOUT: [Issue] — [Why it's a problem and what to write instead.]

---

## Operating Rules

- **Load brain context before intake.** Pre-flight runs silently — never ask for context already loaded.
- **Three options minimum on `/build`.** Choice architecture is the value.
- **Independent evaluation pass is non-negotiable.** Unreviewed output is not delivered.
- **Adversarial callouts surface before delivery, not after.** Rewrites happen during generation.
- **Decision logging is not optional.** Every recommendation affecting the quarter gets logged.
- **Writes only to `decisions/` and `knowledge/`.** No writes to brain file.
- **Confidence range is enforced.** >90% or <50% triggers an adversarial callout.
- **Gate results in table format only.** Binary ✅ / ❌ — no narrative substitution.
- **Scorecard Weight confirmed at 100% before delivery.** Surface discrepancy if unbalanced.
- **`/exec` only from finalised OKRs.** Prompt for option choice if drafts only.

---

## Self-Improvement Loop

Knowledge updates (no approval): hypotheses promoted/demoted per Block 1 rules at session end.

SKILL.md changes (approval required):
```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed across sessions]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.1.0 — 2026-06-06
Spec compliance pass against SKILL-SPEC v2.0.0. Score: 8/19 → 19/19.
Added: Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For,
Operating Rules. Fixed: name field, metadata block, output templates fenced,
quality gates as table, self-improvement loop restructured. Trimmed to <500 lines.

### v2.0.0 — 2026-05-01
Full rebuild: compounding knowledge graph (Block 1), decision journal (Block 2),
independent evaluation pass (Block 3), adversarial callouts, seven commands.
