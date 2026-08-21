---
name: pmm-okrs
version: 2.3.0
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
last_updated: 2026-08-21
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
  build quarterly strategy context in your brain first, then return here.
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
  - `/foundation/brain.md` — recommended. Load Section 2 (ICP), Section 3
    (Alternatives & Positioning), Section 5 (Market Context) silently if present.
  - `/context/meta-patterns.md` — optional; recurring patterns the user has logged from all skills.
---
## Pre-flight
If `/context/meta-patterns.md` exists in the user's workspace, check it for recurring
OKR patterns they've logged. If one applies, surface a guardrail prompt before Step 1.
If it doesn't exist, skip silently.

Before starting, check `/foundation/brain.md`.
**If it exists — load silently:**
- Section 1 (Product Context) → stage and business model context
- Section 2 (ICP Definition) → align OKRs to the named buyer
- Section 5 (Market Context) → align OKRs to macro forces and timing
**Confidence awareness:** If loaded sections are 🔴, flag before building OKRs:
> "Revenue Levers is marked as Placeholder — OKRs built on this may need revisiting. Want to update it first?"
**If missing:** Proceed. Surface once:
> "Run `product-marketing-context` first for sharper OKRs. Continuing."

**Related skills — cross-reference before or after this skill:**
- **prd** → PRDs inform project OKRs; check for alignment
- **gaccs-brief** → campaign briefs should trace back to OKR project goals
---
## Steps
### Step 1 — `/build`
1. Run intake (or infer from pasted context).
2. If the user has prior-quarter OKR results to share, ask for them to calibrate confidence.
3. Generate three OKR options.
4. Run independent evaluation pass (Block 3) on all three.
5. Present with Quality Gate results inline.
### Step 2 — `/review`
1. Accept pasted OKRs.
2. Run each KR through all five Quality Gates (binary).
3. Flag every failure with an ADVERSARIAL CALLOUT and a rewrite.
4. Return annotated set.
### Step 3 — `/scorecard`
1. Work from OKRs in session or ask user to paste.
2. Map each KR to metric, target, measurement method.
3. Group by category.
4. Confirm Weight = 100%.
5. Output scorecard.
### Step 4 — `/exec`
1. Confirm OKRs are finalised (not drafts).
2. Translate to one-paragraph exec narrative.
### Step 5 — `/map`
1. For each KR, generate required projects with owner type, effort (S/M/L), timeline.
2. Flag capacity conflicts if team size known.
### Step 6 — `/stress-test [KR]`
1. Accept one KR.
2. Run through five Quality Gates.
3. Return per-gate pass/fail + rewrite.

### Step 7: Deliver Output
Deliver the OKR set. If the session surfaced a pattern worth remembering for next
quarter (a confidence calibration lesson, a recurring KR-design mistake), name it
explicitly and ask the user where — if anywhere — they'd like it saved.
---
## Outputs
- **Chat output format:** Three OKR option blocks in code-fence structured output,
  each with Quality Gate results inline. Scorecard table. Exec Summary paragraph.
  All formatted for direct paste into the PMM OKR Builder spreadsheet.
- **External side effects:** None. This skill does not write to any file on its own.
---
## Verification
- Guardrails checked before intake, if `/context/meta-patterns.md` exists.
- All `/build` output contains three OKR options unless user explicitly requests fewer.
- Every option includes Quality Gate results (five binary checks) before delivery.
- No output delivered before the independent evaluation pass (Block 3) has run.
- Adversarial callouts surface inline before delivery, never post-delivery.
- `/exec` output produced only from finalised OKRs, not from draft options.
- Scorecard Weight confirmed at 100% before delivery.
---
## Do Not Use For
- **(no dedicated quarterly-strategy skill yet)** — if no quarterly strategy exists yet, use go-to-market-strategy or build it directly in this skill's intake.
- **prioritization-frameworks** — for prioritising *which initiatives* to include in a quarter.
- **gaccs-brief** — for campaign planning that traces back to OKRs already set.
- **Company-level OKR design** — this skill is PMM-specific. Exec team or company
  OKRs require different framing and are out of scope.
- **OKR tooling setup** — this skill produces OKR content, not Lattice/Workday
  configuration or workflow automation.
---
## Reasoning Architecture
### Block 1 — Confidence Calibration
If the user shares last quarter's predicted confidence and actual achievement,
use it to calibrate this quarter's recommendation:
````
Last quarter: Predicted 75%, Achieved 78% → You're well-calibrated
This quarter: Recommend 72-78% confidence range
````
If they don't have this to hand, proceed without it — it sharpens the
recommendation but isn't required.

### Block 2 — Independent Evaluation Pass
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
````
Objective: Improve go-to-market in mid-market.
KR 1: Launch 4 battlecards. KR 2: Run monthly training. KR 3: Increase pipeline.
````
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
````markdown
═══════════════════════════════════════════
OPTION [A / B / C] — [Strategic Focus]
═══════════════════════════════════════════
OBJECTIVE: [1–2 sentence qualitative goal.]
KR 1 — [Name]: [Outcome. Target. Deadline. Measurement.]
KR 2 — [Name]: [Outcome. Target. Deadline. Measurement.]
KR 3 — [Name]: [Outcome. Target. Deadline. Measurement.]
CONFIDENCE: [X%]
CONFIDENCE REASONING: [If prior-quarter data was shared, reference it here]
CHOOSE THIS WHEN: [1-sentence fit description.]
KEY PROJECTS: 1. [name — KR] 2. [name — KR] 3. [name — KR]
QUALITY GATE RESULTS:
Gate 1 — Outcome not output:           ✅ / ❌
Gate 2 — Measurable without ambiguity: ✅ / ❌
Gate 3 — Causally linked to objective: ✅ / ❌
Gate 4 — 60–70% confidence:            ✅ / ❌
Gate 5 — Three or fewer KRs:           ✅ / ❌
═══════════════════════════════════════════
````
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
- **Use prior quarter data for confidence calibration when the user has it.** Don't require it.
- **Three options minimum on `/build`.** Choice architecture is the value.
- **Independent evaluation pass is non-negotiable.** Unreviewed output is not delivered.
- **Adversarial callouts surface before delivery, not after.** Rewrites happen during generation.
- **Confidence range is enforced.** >90% or <50% triggers an adversarial callout.
- **Gate results in table format only.** Binary ✅ / ❌ — no narrative substitution.
- **Scorecard Weight confirmed at 100% before delivery.** Surface discrepancy if unbalanced.
- **`/exec` only from finalised OKRs.** Prompt for option choice if drafts only.
---
## Quality Gate
Runs before final delivery. Score each criterion 1–3. Minimum 12/15 to pass.
| Criterion | Standard | Score (1–3) |
|---|---|---|
| Guardrails surfaced | `/context/meta-patterns.md` checked if it exists | |
| Three options minimum | All `/build` delivers 3 options with Quality Gate results | |
| Independent evaluation | All output reviewed cold before delivery | |
| Adversarial callouts | All gate failures surfaced inline with rewrites | |
| Scorecard validation | Weight totals 100% confirmed before delivery | |

**On failure:** Identify which criterion failed, revise, do not present as final.
---
## Related Skills
Cross-reference when findings trigger downstream work:
- **prd** → PRDs inform project OKRs; check alignment
- **gaccs-brief** → campaign briefs should trace back to OKR projects
- **retro** → after quarter closes, retro compares actual vs. predicted OKRs
