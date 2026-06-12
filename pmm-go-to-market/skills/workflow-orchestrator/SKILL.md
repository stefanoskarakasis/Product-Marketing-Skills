---
name: workflow-orchestrator
version: 2.1.0
description: >
  Orchestrates multi-skill PMM programs end-to-end — chains positioning,
  competitive, GTM strategy, campaign briefs, stakeholder maps, and retros into
  one coherent program with a master document and brain updates. Trigger on:
  "run full GTM workflow", "run a full launch", "launch [product] end to end",
  "positioning refresh", "quarterly PMM cycle", "competitive program", "new
  market entry program", "full PMM onboarding", or any request for a multi-step
  PMM initiative that spans more than one skill.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-12
---

# PMM Workflow Orchestrator

Chains your PMM skills into complete end-to-end programs. Manages state across
skills, verifies coherence between outputs, writes back to brain, and produces
one master program document the team can act from.

Not a shortcut for running one skill. A program manager for multi-skill PMM work
where consistency across outputs — positioning, competitive, GTM, stakeholder —
matters as much as each individual output.

---

## Trigger

- **When:** Any request for a multi-step PMM program spanning two or more skills,
  or any named workflow type below.
- **Not for:** Single-skill tasks — route directly to the relevant skill instead:
  `go-to-market-strategy` for tier + brief only, `positioning-messaging` for
  positioning work only, `pre-mortem` for risk analysis only, `retro` for
  post-launch review only.
- **Example prompts:**
  - "Run a full launch workflow for our analytics dashboard"
  - "We're doing a positioning refresh — orchestrate the full program"
  - "Run our quarterly PMM cycle"
  - "New market entry into healthcare — full program"
  - "I just joined as PMM — audit the current state"
  - "Run a competitive intelligence program on our top 3 competitors"

---

## Inputs

- **Args:** Workflow type (named or described) + initiative context. See Commands
  for supported workflow types. Free-form description also accepted — orchestrator
  will infer the closest workflow and confirm before running.
- **Defaults:** If workflow type is ambiguous, ask before starting. Never infer
  and execute silently on a multi-skill program.
- **Context keys:**
  - `/foundation/brain.md` — required. All sections.
  - **Brain contract:**
    - Reads: All sections (1–7) — checks completeness and staleness before routing.
    - Writes: Section 3 (after positioning refresh), Section 4 (after competitive
      work), Section 5 (after new proof points confirmed), Section 7 (after any
      launch or retro — marks Planned or Completed).
    - Never writes to: Section 1, Section 2, Section 6 (those require dedicated
      skills: `product-marketing-context`, `hs-icp`, `hs-voice-tone`).
  - **Staleness thresholds:**
    - Section 3 (Positioning) > 6 months → flag for refresh before any launch workflow.
    - Section 4 (Competitive) > 3 months → flag for refresh before any competitive workflow.
    - Section 7 (Launch history) empty → note; calibration will be limited.

---

## Pre-flight

- Load `/foundation/brain.md`. Read all sections silently.
- If brain missing: block and surface:
  > "Brain file not found at `/foundation/brain.md`. Run `product-marketing-context`
  > first — the orchestrator needs your ICP, positioning, and history to route
  > skills coherently. Without it, outputs will be disconnected."
  > Unlike individual skills, the orchestrator does not degrade gracefully without
  > brain. A program of disconnected outputs is worse than no program.
- Audit brain sections before confirming workflow:
  - Section 3 > 6 months old → "Positioning is [N] months old. This workflow will
    include a positioning refresh step."
  - Section 4 > 3 months old → "Competitive intel is [N] months old. Will refresh
    as part of this program."
  - Any section 🔴 Placeholder → flag: "Section [X] is Placeholder. This limits
    [specific skill] output quality. Recommend completing before running."
- Confirm Program Charter with user before invoking any skill. No skill runs
  without explicit go-ahead.

---

## Steps

### Step 1: Intake and Program Definition

Ask in one message. Adapt based on which workflow type is named.

> "Before I start the program, I need to lock a few things:
>
> 1. **What's the initiative?** (One sentence — what are we launching, refreshing,
>    or auditing?)
>
> 2. **Who is the DRI?** (The one person who owns this program's outcomes)
>
> 3. **What's the primary success metric and timeline?**
>    (The number we're building toward, and when)
>
> 4. **Which skills have already run?** (Don't re-run what's current — I'll check
>    brain staleness and confirm what needs to run vs. what can be skipped)"

Reflect back as a Program Charter before proceeding:

```
PROGRAM CHARTER
───────────────────────────────────────
Initiative:       [name]
Workflow type:    [named workflow]
DRI:              [name]
Primary metric:   [metric + target]
Timeline:         [start → end]
Brain status:     [Section staleness summary]
Skills to run:    [ordered list]
Skills to skip:   [list with reason]
───────────────────────────────────────
Confirm to start? [Y/N]
```

Do not proceed until confirmed.

---

### Step 2: Brain Staleness Check

For each brain section relevant to the workflow, assess:

| Section | Last updated | Status | Action |
|---|---|---|---|
| 3 — Positioning | [date or unknown] | 🟢 Current / 🟡 Aging / 🔴 Stale | Run / Skip / Flag |
| 4 — Competitive | [date or unknown] | 🟢 / 🟡 / 🔴 | Run / Skip / Flag |
| 7 — Launch history | [date or count] | 🟢 / 🟡 / 🔴 | Note calibration quality |

Surface as part of the Program Charter — do not run silently.

---

### Step 3: Skill Sequencing

Determine the ordered skill chain for the confirmed workflow. Surface the sequence
before running:

> "Here's the sequence for this program:
> 1. [Skill A] — [what it produces and why it's first]
> 2. [Skill B] — [what it reads from A and what it adds]
> ...
> Each skill output feeds the next. I'll flag if a downstream skill can't proceed
> due to a gap in an upstream output."

---

### Step 4: Skill Execution

Invoke each skill in sequence. Between each skill:

1. Confirm output with user before passing state to next skill.
2. Extract relevant outputs and update the Program State document.
3. Flag any coherence issue immediately before running the next skill.

**Coherence checks between skills:**
- Positioning → GTM strategy: do channel recommendations match the positioned segment?
- GTM strategy → Stakeholder maps: does the tier align with stakeholder weight?
- Competitive → GTM strategy: does the attack angle match the battlecard?
- Personas → Proof points: does the proof point set address the persona's primary objection?

If coherence fails: surface the conflict, ask which output to trust, re-run
the downstream skill with corrected input.

---

### Step 5: Brain Update

After each skill produces a confirmed output:

- **Positioning refresh:** Update Section 3 with new statement and timestamp.
- **Competitive work:** Update Section 4 with refreshed alternative map and timestamp.
- **New proof points:** Update Section 5 with approved new claims.
- **Launch planned:** Add Section 7 entry as "Planned" with tier, metric, date.
- **Retro completed:** Update Section 7 entry from "Planned" to "Completed" with actuals.

Surface each write:
> "Updating brain Section [X] with [what]. Confirm? [Y/N]"

---

### Step 6: Master Program Document

Compile all skill outputs into one master document:

```markdown
# [Program Name] — Master Document
**Workflow type:** [named]
**DRI:** [name]
**Period:** [start → end]
**Primary metric:** [metric + target]
**Brain last updated:** [date]

## Program Charter
[From Step 1]

## Skill Outputs
### [Skill A] — [date run]
[Confirmed output or summary]

### [Skill B] — [date run]
[Confirmed output or summary]

## Coherence Check Results
[Conflicts surfaced and how resolved]

## Brain Updates Made
[Sections updated with timestamps]

## Open Items
[Unresolved gaps — owner and due date]

## Next Program Trigger
[When to run the next cycle]
```

---

### Step 7: Close

1. Run `/coherence` across all completed outputs — resolve any remaining conflicts.
2. Propose Self-Improvement Triggers for structural observations (see Self-Improvement Loop).
3. Log session to `sessions/log.md`.
4. Surface next program trigger date:
   - Full launch → retro in 90 days
   - Quarterly cycle → next cycle in 13 weeks
   - Positioning refresh → re-audit in 6 months
   - Competitive program → re-run in 3 months

---

## Supported Workflows

### 1. Full Product Launch
**Trigger:** "run full launch workflow", "launch [product] end to end"
1. `go-to-market-strategy` — tier + strategy brief
2. `positioning-messaging` (if Section 3 stale or new angles needed)
3. `hs-competitive-battlecard` (if T1/T2 or competitor mentioned)
4. `hs-gaccs-brief` — campaign brief
5. `hs-stakeholder-maps` — internal alignment map
6. `hs-pre-mortem` — risk analysis before committing
7. Set T+90 retro trigger → `retro`

### 2. Positioning Refresh
**Trigger:** "positioning refresh", "our messaging is stale", "update positioning"
1. `positioning-messaging` (AUDIT mode → full BUILD if audit score < 70)
2. `hs-value-prop-statements` — persona-specific copy
3. `hs-competitive-battlecard` — refresh differentiation for top competitors

### 3. Competitive Intelligence Program
**Trigger:** "competitive program", "build battlecards", "competitive deep-dive"
1. `hs-alternatives-map` — if not current
2. `hs-competitive-battlecard` — for each named competitor (run sequentially)
3. `hs-ci-stakeholder-briefing` — exec-level competitive newsletter

### 4. Quarterly PMM Cycle
**Trigger:** "quarterly PMM cycle", "Q[X] refresh", "quarterly review"
1. `retro` — debrief all launches from prior quarter
2. `positioning-messaging` (AUDIT mode)
3. `hs-competitive-battlecard` — refresh top 3 competitors
4. `hs-proof-points-claims` — audit + add new proof points
5. `hs-brainstorm-okrs` — set next quarter OKRs

### 5. New Market Entry Program
**Trigger:** "enter new market", "expand to [segment]", "new vertical"
1. `hs-icp` — define ICP for new market
2. `hs-buyer-personas` — buying committee for new market
3. `positioning-messaging` — positioning for new segment
4. `hs-competitive-battlecard` — top 3 competitors in new market
5. `go-to-market-strategy` — tier + strategy for market entry
6. `hs-gaccs-brief` — campaign brief
7. `hs-pre-mortem` — risk analysis before committing

### 6. Competitive Response (Fast)
**Trigger:** "competitive response to [competitor]", "they just launched [X]"
1. `hs-competitive-battlecard` — expedited for named competitor
2. `hs-value-prop-statements` — refreshed differentiation messaging
3. `hs-ci-stakeholder-briefing` — exec alert

### 7. Full PMM Onboarding / Audit
**Trigger:** "I just joined as PMM", "PMM audit", "what's our current state"
1. Audit brain Sections 1–7 — completeness, staleness, gaps
2. `positioning-messaging` (AUDIT mode only)
3. `hs-proof-points-claims` (AUDIT mode only)
4. Produce Current State Report with prioritised gaps
**Note:** Read-only. No brain writes under any circumstance.

---

## Commands

### /run [workflow-type]
Start a named workflow. Runs Steps 1–7 with checkpoints.

```
/run full-launch
/run positioning-refresh
/run competitive-program
/run quarterly-cycle
/run market-entry
/run competitive-response [competitor name]
/run audit
```

### /status
Show current program state: skills completed, skills pending, next skill,
brain updates made.

### /skip [skill-name]
Skip a skill in the current sequence. Requires reason. Orchestrator flags
downstream impact and requests confirmation before skipping.

### /coherence
Run a coherence check across all completed outputs. Flags positioning ↔ GTM,
competitive ↔ GTM, and personas ↔ proof point conflicts with specific fixes.

### /compile
Compile the Master Program Document from all confirmed skill outputs.
Can be run mid-program or at end.

### /next
Show what skill runs next, what it reads from prior outputs, what it produces,
and estimated session time.

---

## Outputs

- **Files written:** `/foundation/brain.md` — Sections 3, 4, 5, 7 updated on
  confirmation after relevant skills complete. Master Program Document saved to
  `sessions/[program-name]-[date].md`.
- **Chat output format:** Program Charter → sequential skill outputs with
  checkpoints → coherence check results → Master Program Document.
  Each skill output is clearly delimited with skill name and date.
- **External side effects:** n.v.t.

---

## Verification

Runs at program close, before Master Program Document is delivered.

| Check | Standard | Pass = |
|---|---|---|
| Program Charter confirmed | User explicitly confirmed charter before any skill ran | Yes |
| Each skill confirmed | Every output confirmed by user before next skill ran | Yes |
| Coherence check run | /coherence run after all skills; conflicts surfaced and resolved | Yes |
| Brain writes confirmed | Every brain write shown and confirmed before executing | Yes |
| Master document complete | All required sections present with no orphaned outputs | Yes |
| Next trigger surfaced | Next program cycle date recommended at close | Yes |

---

## Do Not Use For

- **go-to-market-strategy** — when you only need a tier assignment and GTM brief,
  not a multi-skill program. Use that skill directly.
- **positioning-messaging** — when you only need positioning or messaging work.
  Use that skill directly.
- **retro** — for a single post-launch retrospective outside a larger program cycle.
  Use that skill directly.
- **pre-mortem** — for standalone risk analysis before a launch. Use that skill
  directly, then bring the output into a full launch workflow if needed.

---

## Operating Rules

- **Brain is mandatory.** The orchestrator does not run without `/foundation/brain.md`.
  Disconnected skill outputs without shared context are worse than no program.
- **Program Charter before execution.** No skill runs before the charter is confirmed.
  Starting without alignment is the most common reason programs produce wasted output.
- **Checkpoint after every skill.** User confirms each output before the next skill
  runs. Silent chaining is not permitted — it produces coherence failures that are
  expensive to unwind.
- **Coherence over speed.** If a conflict surfaces between outputs, stop and resolve
  it before proceeding. A fast program with incoherent outputs is not a program.
- **Staleness must be surfaced.** If any brain section relevant to the workflow is
  stale, say so in the charter. The user decides whether to refresh — consciously.
- **Brain writes require confirmation.** Never write to brain without explicit
  user go-ahead. Show what will be written, then wait.
- **Skip requires downstream impact disclosure.** If the user skips a skill,
  tell them exactly what the next skill loses by not having that output.
- **Read-only audits write nothing.** The Full PMM Onboarding / Audit workflow
  does not write to brain under any circumstance.
- **One DRI per program.** If no DRI is named at intake, ask before confirming
  the charter. A program with no single owner has no owner.
- **Next program trigger at close.** Every completed program ends with a recommended
  date for the next cycle. Compounding only works if the loop closes.

---

## Quality Gate

Runs at program close, before Master Program Document is delivered.

| Check | Standard | Pass = |
|---|---|---|
| Program Charter confirmed | User explicitly confirmed charter before skills ran | Yes |
| All skills accounted for | Each skill either ran or was explicitly skipped with reason | Yes |
| Checkpoint for each skill | Each skill output confirmed before next skill ran | Yes |
| Coherence check run | /coherence run after all skills — conflicts surfaced and resolved | Yes |
| Brain writes confirmed | Every brain write shown to user and confirmed | Yes |
| Master document complete | All required sections present in master document | Yes |
| Open items documented | Unresolved gaps have named owner and due date | Yes |
| Next trigger surfaced | Next program cycle date recommended at close | Yes |
| No orphaned outputs | Every skill output referenced in master document | Yes |
| DRI named | Program Charter includes a named DRI | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load brain Section 7 — scan for program history. Prior programs of same type
   inform sequencing decisions and checkpoint timing.
2. Check `knowledge/orchestrator/rules.md` if it exists — apply confirmed rules.
3. Check `knowledge/orchestrator/hypotheses.md` — note any pattern testable today.

### After every completed program:
1. Extract 1–3 observations:
   - Which skill produced the highest-leverage output?
   - Which checkpoint took longest — and why?
   - Which coherence conflict was most expensive to resolve?
2. Log observations to `knowledge/orchestrator/hypotheses.md`.
3. If same pattern observed 3+ times → propose promotion to `knowledge/orchestrator/rules.md`.
4. Log session summary to `sessions/log.md`: workflow type, duration, skills run,
   brain sections updated, open items count.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed this program]
Proposed update: [exact wording — what would be added or changed]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.1.0 — 2026-06-12
Spec compliance fixes from 16/19 audit. Zero failures, one permanent partial (Q3).

- **F1:** Fixed `Metadata:` → `metadata:` (lowercase) — YAML parsers are case-sensitive.
- **S6:** Verification converted from bullet list to binary table (6 checks).
- **Q1:** Reduced from 612 → 499 lines. Cuts: Commands output blocks stripped
  (signatures kept), Step 7 consolidated, Changelog v2.0.0 compressed, Supported
  Workflows stripped of redundant brain-writes lines (covered in Inputs contract).

### v2.0.0 — 2026-06-06
Full rebuild to SKILL-SPEC v2.0.0. Added all 7 required sections, mandatory brain
enforcement, Program Charter (Step 1), per-skill checkpoints, coherence checks
across skill pairs, /run /status /skip /coherence /compile /next commands, brain
contract with staleness thresholds, operating rules (10), quality gate (10 checks),
self-improvement loop, read-only audit workflow.

### v1.0.0 — 2026-04-01
Initial build. Workflow list and brain integration concept. README-grade.
