---
name: pmm-okrs
version: 2.2.0
description: >
  Guides Product Marketing leaders and individual PMMs through building a complete,
  export-ready OKR set for their quarter — including Objective, Key Results, Projects,
  Scorecard metrics, and Exec Summary language. Includes post-session logging for meta-synthesis
  pattern detection and pre-flight guardrails from prior quarters. Use when setting quarterly OKRs,
  reviewing existing OKRs, stress-testing KR quality, or building a measurement plan.
  Trigger on: "help me set our OKRs", "are my KRs measurable", "build a scorecard",
  "stress-test this KR", "write OKRs for my team", "present goals to exec team".
  Produces output paste-ready for the PMM OKR Builder spreadsheet or leadership sharing.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
last_updated: 2026-06-21
---
# pmm-okrs
A guided OKR builder for Product Marketing teams. Run it at the start of every quarter.
Outputs a complete, review-ready OKR set you can paste directly into the PMM OKR Builder sheet.
Learns from prior quarters to improve confidence calibration and KR quality.
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
  - `/context/meta-patterns.md` — optional; recurring patterns from all skills (guardrail prompts)
  - `knowledge/okrs/rules.md` — apply confirmed OKR craft rules by default.
  - `knowledge/okrs/hypotheses.md` — test any active hypothesis if applicable today.
  - `decisions/` — check for prior decisions before making new recommendations.
  - `/context/skill-sessions.md` — optional; prior quarter OKR data for confidence calibration
**Brain contract:** Reads: Section 2 (ICP), Section 3 (Positioning), Section 5 (Revenue), Section 6 (Goals). Writes: `/context/skill-sessions.md`, `/foundation/brain.md` Section 5 (if lever weights change).
---
## Pre-flight
**Load guardrails first:** Check `/context/meta-patterns.md` for recurring OKR patterns. If pattern matches (e.g., "confidence calibration off by 15% in Q2-Q3"), surface guardrail prompt before Step 1.

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

**Load prior quarter data:** Check `/context/skill-sessions.md` for last quarter's OKR results to calibrate confidence:
> "Last quarter: confidence was 75%, actual achievement was 78%. You're well-calibrated. Recommend similar range this quarter."

**Related skills — cross-reference before or after this skill:**
- **hs-pmm-strategy** → run before this skill if no quarterly strategy exists yet
- **hs-product-requirement-doc** → PRDs inform project OKRs; check for alignment
- **hs-gaccs-brief** → campaign briefs should trace back to OKR project goals
- **meta-synthesis** → after 3+ quarters logged, meta-synthesis detects OKR patterns
---
## Steps
### Step 0: Surface Guardrails (NEW)
**Before intake, check for patterns:**

If `/context/meta-patterns.md` exists and contains OKR patterns:
```
🔁 PATTERN DETECTED FROM PRIOR QUARTERS

I've detected [specific pattern] in [N] prior quarters.
Example: "Confidence off by 15%", "External dependency blockers 3+ times", "KR design failure on 'improve adoption'"

Quick question: Are you seeing this pattern again in Q4?
- If YES → we'll flag it as a confirmed problem + propose a fix
- If NO → we'll watch for other patterns

This helps calibrate your confidence and KR design.
```

**Common guardrail patterns to surface:**
- "Confidence too high (90%+) but achievement 65%" → "Recommend: set confidence 70% or below"
- "External dependencies blocked 3+ KRs" → "Build dependency risk into confidence"
- "KR too vague again ('improve adoption')" → "Be specific: 'Adoption in SMB segment 60% → 75%'"
- "Lever weight assumptions changed mid-quarter" → "Lock lever weights at start"

If patterns apply, ask guardrail question. User can skip, but they've been warned.

### Step 1 — `/build`
1. Run intake (or infer from pasted context). 
2. Load `knowledge/okrs/rules.md` + check guardrails from `/context/meta-patterns.md`.
3. Check `decisions/` for prior choices in this area. 
4. Check `/context/skill-sessions.md` for prior quarter confidence calibration.
5. Generate three OKR options.
6. Run independent evaluation pass (Block 3) on all three. 
7. Present with Quality Gate results inline + confidence recommendations based on prior quarters.
8. Log option selection to `decisions/`.
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
3. Cross-reference against guardrails: "External dependencies flagged in 3 prior quarters. This KR has 2. Accept risk?"
### Step 6 — `/stress-test [KR]`
1. Accept one KR. 
2. Run through five Quality Gates. 
3. Return per-gate pass/fail + rewrite.

### Step 7: Post-Session Logging (NEW)
After every session, log structured data to `/context/skill-sessions.md`:

```yaml
skill: pmm-okrs
session_date: 2026-06-21
quarter: "Q3 2026"
okr_set_version: 1
objectives_count: 3
key_results_count: 9
confidence_level: "medium"
confidence_range: "65-70%"
krs_with_baseline_metrics: 9
krs_with_tracking_mechanism: 7
krs_with_stretch_factor: 6
aggressive_vs_conservative: "mixed"
dependencies_identified: true
dependencies_external: 3
dependencies_internal: 1
prior_quarter_okrs:
  - quarter: "Q2 2026"
    krs_achieved: 7
    krs_partial: 1
    krs_missed: 1
    achievement_rate: 0.78
    confidence_predicted: 0.75
current_vs_prior_stretch: "more_aggressive"
confidence_vs_last_quarter: "higher"
confidence_calibration_delta: "+2%"
output_path: "/foundation/okrs/Q3-2026-PMM-OKRs.md"
guardrails_triggered:
  - "External dependencies: 3 (same as Q2). Last quarter we missed 1 KR due to external dependency. Recommend: align with dependent teams by Week 1 of Q3."
  - "Stretch factor: 6/9 KRs are ambitious (2x+). This is higher than Q2 (4/8). Recommend: ensure team capacity supports this."
  - "Confidence calibration: Q2 predicted 75%, achieved 78%. You're well-calibrated. Recommend similar range (72-78%) for Q3."
brain_updates_proposed: []
```

This feeds into `meta-synthesis` skill (monthly) which detects OKR patterns across quarters and updates guardrails.

### Step 8: Deliver Output and Log Learning
Deliver the OKR set. Then run the self-improvement loop:
write session file → update knowledge base → log decisions → run quality gate → propose confidence adjustments.
---
## Outputs
- **Files written:** 
  - `/context/skill-sessions.md` — row appended with session metadata and guardrails (NEW)
  - `decisions/YYYY-MM-DD-{topic}.md` when a strategic OKR choice is logged.
  - `knowledge/okrs/hypotheses.md` and `rules.md` when the self-improvement loop triggers at session end.

- **Chat output format:** Three OKR option blocks in code-fence structured output,
  each with Quality Gate results inline. Scorecard table. Exec Summary paragraph.
  All formatted for direct paste into the PMM OKR Builder spreadsheet.
- **External side effects:** None beyond context writes.
---
## Verification
- Guardrails checked before intake (Step 0) — patterns from prior quarters surfaced.
- All `/build` output contains three OKR options unless user explicitly requests fewer.
- Every option includes Quality Gate results (five binary checks) before delivery.
- No output delivered before the independent evaluation pass (Block 3) has run.
- Adversarial callouts surface inline before delivery, never post-delivery.
- Decision log written whenever a recommendation will affect the user's quarter.
- `/exec` output produced only from finalised OKRs, not from draft options.
- Scorecard Weight confirmed at 100% before delivery.
- Confidence calibration checked against `/context/skill-sessions.md` prior quarter data.
- Session logged to `/context/skill-sessions.md` with all metadata.
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
**Before any task:** 
1. Load `knowledge/INDEX.md` and relevant domain folders. 
2. Apply `rules.md` by default. 
3. Test any active hypothesis if applicable today.
4. Load `/context/meta-patterns.md` for cross-skill guardrails.
5. Load `/context/skill-sessions.md` for prior quarter confidence calibration.

**After any session:** 
1. Extract 1–3 insights. 
2. Unconfirmed → `hypotheses.md`.
3. Confirmed 3+ times → auto-promote to `rules.md`. 
4. Contradicted → demote to `hypotheses.md`.
5. Log confidence calibration delta for future quarters.

> **Environment note:** Persistent `/knowledge/` works in Claude Code and Cowork.
> In Claude.ai chat, surface insights at end of session for manual carry-forward.
### Block 2 — Decision Journal
Check `decisions/` before any recommendation. Log new decisions immediately.
```
File: decisions/YYYY-MM-DD-{topic}.md
Decision / Context / Alternatives / Reasoning / Trade-offs / Supersedes
```
**Log when:** 
- Choosing between OKR options. 
- Recommending a measurement method.
- Flagging a failing gate. 
- Any recommendation affecting the user's quarter.
- Confidence calibration adjustments based on prior quarter data.
### Block 3 — Independent Evaluation Pass
After generating any output: re-read cold as evaluator. Run all five Quality Gates
binary. Rewrite failures before delivery. Report gate results inline.

**Confidence calibration check:** Compare predicted confidence vs. actual achievement from prior quarter. Adjust recommendations:
```
Last quarter: Predicted 75%, Achieved 78% → You're well-calibrated
This quarter: Recommend 72-78% confidence range
```
---
## Commands
### /build
Builds three OKR options from scratch with Quality Gate results and confidence calibration.
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
Builds OKR → Projects table with owner type, effort (S/M/L), and timeline. Cross-references guardrails.
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
CONFIDENCE REASONING: [Based on prior quarter calibration: if last quarter predicted 75% achieved 78%, recommend similar range]
CHOOSE THIS WHEN: [1-sentence fit description.]
KEY PROJECTS: 1. [name — KR] 2. [name — KR] 3. [name — KR]
QUALITY GATE RESULTS:
Gate 1 — Outcome not output:           ✅ / ❌
Gate 2 — Measurable without ambiguity: ✅ / ❌
Gate 3 — Causally linked to objective: ✅ / ❌
Gate 4 — 60–70% confidence:            ✅ / ❌
Gate 5 — Three or fewer KRs:           ✅ / ❌
GUARDRAILS: [Cross-skill patterns from prior quarters, if any]
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
- **Guardrails first.** Load `/context/meta-patterns.md` at pre-flight. Surface guardrail prompt if pattern matches this quarter's planning.
- **Load brain context before intake.** Pre-flight runs silently — never ask for context already loaded.
- **Load prior quarter data for confidence calibration.** Check `/context/skill-sessions.md` before confidence recommendations.
- **Three options minimum on `/build`.** Choice architecture is the value.
- **Independent evaluation pass is non-negotiable.** Unreviewed output is not delivered.
- **Adversarial callouts surface before delivery, not after.** Rewrites happen during generation.
- **Decision logging is not optional.** Every recommendation affecting the quarter gets logged.
- **Writes only to `decisions/`, `knowledge/`, and `/context/skill-sessions.md`.** No writes to brain file.
- **Confidence range is enforced.** >90% or <50% triggers an adversarial callout. Calibrate against prior quarter achievement.
- **Gate results in table format only.** Binary ✅ / ❌ — no narrative substitution.
- **Scorecard Weight confirmed at 100% before delivery.** Surface discrepancy if unbalanced.
- **`/exec` only from finalised OKRs.** Prompt for option choice if drafts only.
- **Always log.** Every quarter's OKR session logged to `/context/skill-sessions.md`. Meta-synthesis learns from achievement rates across quarters.
---
## Quality Gate
Runs before final delivery. Score each criterion 1–3. Minimum 17/21 to pass.
| Criterion | Standard | Score (1–3) |
|---|---|---|
| Guardrails surfaced | `/context/meta-patterns.md` checked at pre-flight | |
| Confidence calibration | Prior quarter data checked for adjustment recommendations | |
| Three options minimum | All `/build` delivers 3 options with Quality Gate results | |
| Independent evaluation | All output reviewed cold before delivery | |
| Adversarial callouts | All gate failures surfaced inline with rewrites | |
| Decision logging | Strategic OKR choices logged to `decisions/` | |
| Scorecard validation | Weight totals 100% confirmed before delivery | |

**On failure:** Identify which criterion failed, revise, do not present as final.
---
## Self-Improvement Loop
### Before every session:
1. **Load guardrails:** Check `/context/meta-patterns.md` for patterns matching this quarter. Surface if found.
2. Load `knowledge/INDEX.md` and relevant domain folders. 
3. Apply `rules.md` by default. 
4. Test any active hypothesis if applicable today.
5. Check `decisions/` for prior choices in this area.
6. **Load prior quarter data:** Check `/context/skill-sessions.md` for last quarter's OKR results + confidence calibration.
7. Propose confidence range based on prior quarter accuracy.

### After every session:
1. **Log to `/context/skill-sessions.md`:** Complete session metadata (see Step 7 schema).
2. Extract 1–3 insights. 
3. Unconfirmed → `hypotheses.md`.
4. Confirmed 3+ times → auto-promote to `rules.md`. 
5. Contradicted → demote to `hypotheses.md`.
6. Log confidence calibration delta (predicted vs. actual achievement).
7. Update `knowledge/INDEX.md`.

**Self-Improvement Trigger format — surface before encoding, never silently:**
```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed across quarters]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

**Confidence Calibration Trigger:**
```
📊 CONFIDENCE CALIBRATION UPDATE
Q2 predicted: 75% | Achieved: 78% | Delta: +3%
Q3 recommendation: Aim for 72-78% confidence range
Reasoning: You're well-calibrated; apply same range this quarter.
```
---
## Changelog
### v2.2.0 — 2026-06-21
Added post-session logging + guardrail intake + prior quarter confidence calibration. Guardrails loaded from `/context/meta-patterns.md` at pre-flight. Step 0 surfaces patterns (e.g., "confidence too high last quarter"). Step 1 now loads `/context/skill-sessions.md` for prior quarter data. Step 7 logs session metadata to `/context/skill-sessions.md` for meta-synthesis. Step 5 cross-references guardrails for dependency risks. Output template now includes "CONFIDENCE REASONING" section. Operating Rules reprioritized (guardrails + confidence calibration first). Quality gate expanded to 8 checks. Self-improvement loop now loads guardrails + prior quarter data first.

Changes from v2.1.0:
- Added Step 0: Surface guardrails before intake (reads `/context/meta-patterns.md`)
- Updated Pre-flight: Load guardrails first + check `/context/skill-sessions.md` for prior quarter calibration
- Updated Step 1: Load prior quarter data for confidence recommendations
- Updated Step 5: Cross-reference guardrails for dependency risk context
- Added Step 7: Post-session logging to `/context/skill-sessions.md`
- Updated Output Template: Added "CONFIDENCE REASONING" + "GUARDRAILS" sections
- Updated Outputs: Now writes to `/context/skill-sessions.md` (NEW)
- Updated Inputs: Now reads `/context/meta-patterns.md` (NEW) + `/context/skill-sessions.md` (NEW)
- Updated Operating Rules: "Guardrails first" + "Confidence calibration checked" + "Always log"
- Updated Quality Gate: Added checks for guardrails + confidence calibration (now 8 checks)
- Updated Verification: Added checks for guardrails + confidence calibration + session logging
- Updated Self-Improvement Loop: Load guardrails + prior quarter data first, log confidence delta
- Updated Changelog: Now includes v2.2.0 entry
- Updated metadata: Added `logging_enabled: true`
- Version bump 2.1.0 → 2.2.0

### v2.1.0 — 2026-06-06
Spec compliance pass against SKILL-SPEC v2.0.0. Score: 8/19 → 19/19.
Added: Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For,
Operating Rules. Fixed: name field, metadata block, output templates fenced,
quality gates as table, self-improvement loop restructured. Trimmed to <500 lines.
### v2.0.0 — 2026-05-01
Full rebuild: compounding knowledge graph (Block 1), decision journal (Block 2),
independent evaluation pass (Block 3), adversarial callouts, seven commands.
---
## Evals Updates (NEW)

Create: `/pmm-execution/skills/pmm-okrs/evals/pmm-okrs.eval.md`

```markdown
# pmm-okrs Evals

## Eval 1: Guardrails surface before intake
**Scenario:** User starts `/build` for Q3. `/context/meta-patterns.md` contains "confidence too high 2x, external dependencies blocked 1x"
**Expected:** Guardrail prompt surfaces before Step 1 intake
**Input:** `/build Q3 2026 for 3-person PMM team`
**Output check:** 
- Does guardrail appear? YES/NO
- Does guardrail match pattern from meta-patterns? YES/NO
- Can user skip guardrail? YES/NO

## Eval 2: Confidence calibration recommended
**Scenario:** `/context/skill-sessions.md` shows Q2: predicted 75%, achieved 78%
**Expected:** Step 1 surfaces recommendation for Q3 confidence range (72-78%)
**Input:** `/build Q3 2026`
**Output check:**
- Confidence reasoning section present? YES/NO
- References Q2 calibration? YES/NO
- Recommends 72-78% range? YES/NO

## Eval 3: Three options delivered with Quality Gates
**Scenario:** User runs `/build` without prior OKRs
**Expected:** Three OKR options, each with 5-gate results (✅/❌ table)
**Input:** `/build Q3 OKRs for SMB focus`
**Output check:**
- Three options present? YES/NO
- Quality Gate table in each option? YES/NO
- Gate results binary (✅/❌)? YES/NO
- No narrative substitutions? YES/NO

## Eval 4: Session logged to /context/skill-sessions.md
**Scenario:** User completes `/build` and `/scorecard`
**Expected:** Entry written to `/context/skill-sessions.md` with full metadata
**Input:** `/build` + `/scorecard`
**Output check:**
- Session logged? YES/NO
- Contains: quarter, objectives_count, krs_with_baseline_metrics? YES/NO
- Contains: prior_quarter_okrs data? YES/NO
- Contains: guardrails_triggered? YES/NO
- Contains: confidence_calibration_delta? YES/NO

## Eval 5: Adversarial callouts surface inline
**Scenario:** User submits OKRs with vague KR ("improve adoption")
**Expected:** Callout surfaces during `/review` with rewrite before delivery
**Input:** `/review` with vague KR
**Output check:**
- Callout appears? YES/NO
- Format: ⚠️ ADVERSARIAL CALLOUT: [Issue]? YES/NO
- Rewrite provided? YES/NO
- Rewrite is specific? YES/NO

## Eval 6: Scorecard Weight confirmed at 100%
**Scenario:** User runs `/scorecard` with weights that don't total 100%
**Expected:** Discrepancy surfaced, scorecard not delivered
**Input:** `/scorecard` with 4 metrics weighted 30%, 30%, 20%, 15%
**Output check:**
- Discrepancy detected? YES/NO
- Totals 95% mentioned? YES/NO
- Scorecard held from delivery? YES/NO
- Prompt to rebalance given? YES/NO

## Eval 7: Prior quarter dependency risks flagged in `/map`
**Scenario:** `/context/skill-sessions.md` shows "external dependencies blocked in Q2"
**Expected:** `/map` output flags this risk for current KRs
**Input:** `/map` with 3 KRs containing external dependencies
**Output check:**
- Guardrail about prior quarter blockers? YES/NO
- Specific to external dependencies? YES/NO
- Asks user to accept risk? YES/NO

## Eval 8: Decision logging on strategic choice
**Scenario:** User selects Option B from `/build` (not Option A)
**Expected:** Decision logged to `decisions/YYYY-MM-DD-{topic}.md`
**Input:** User selects Option B
**Output check:**
- Decision file created? YES/NO
- Contains: Decision / Context / Alternatives / Reasoning? YES/NO
- References Option A as alternative? YES/NO
```
---
## Related Skills
Cross-reference when findings trigger downstream work:
- **hs-pmm-strategy** → run before this skill if no quarterly strategy exists
- **hs-product-requirement-doc** → PRDs inform project OKRs; check alignment
- **hs-gaccs-brief** → campaign briefs should trace back to OKR projects
- **meta-synthesis** → after 3+ quarters logged, detects OKR patterns + confidence trends
- **hs-retro** → after quarter closes, retro compares actual vs. predicted OKRs
