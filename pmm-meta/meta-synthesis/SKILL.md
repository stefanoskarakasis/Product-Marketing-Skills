---
name: meta-synthesis
version: 1.0.0
description: >
  Self-improving meta-pattern synthesis engine for GTM systems. Reads execution skill session logs
  from all domains (experiments, interviews, retros, OKRs, pre-mortems, PDRs, prioritization, stakeholder maps),
  detects recurring patterns and cross-skill signals, proposes guardrails and brain updates,
  and compounds learnings into a living system. Designed to run monthly or on-demand.
  Trigger on: "run meta-synthesis", "what patterns are emerging", "detect cross-skill signals",
  "update guardrails", "compound our learnings", "what should we remember from X quarters".
  Outputs pattern reports, guardrail proposals, and brain updates that feed back into all execution skills.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
  is_meta_skill: true
last_updated: 2026-06-21
---
# meta-synthesis — Cross-Skill Pattern Detection & Brain Updates
Reads logs from all execution skills, detects patterns, and compounds learnings back into the system.
Not a report generator. A learning loop that makes every execution smarter than the last.
The connective tissue of the GTM system.
---
## Trigger
- **When:** End of month (automatic or manual). After 3+ execution skill sessions of the same type (3+ experiments, 3+ retros, 3+ interviews). When a pattern repeats 2+ times across different skill domains. When system has drifted (brain outdated, guardrails haven't changed in 90 days).
- **Not for:** Real-time skill feedback (skills already handle intake guardrails). Individual skill audits (use `meta-review` for that). Strategic planning (use `hs-pmm-strategy`). One-off analysis without compounding (not worth the overhead).
- **Example prompts:**
  - "Run meta-synthesis for June"
  - "What patterns have we seen across 3 retros and 2 pre-mortems?"
  - "Our execution-doc quality scores are declining. Why?"
  - "Compound our learnings from Q2 into guardrails for Q3"
  - "Champion alignment keeps breaking. What should we remember?"
---
## Inputs
- **Args:** Optional month/quarter to analyze (defaults to current month). Optional skill domain to focus on (defaults to all: experiments, interviews, retros, okrs, pre-mortems, prds, prioritization, stakeholder-maps).
- **Context keys:**
  - `/context/skill-sessions.md` — REQUIRED. Master log of all execution skill sessions with structured metadata
  - `/foundation/brain.md` — REQUIRED. Current state (Sections 1-7), to be updated if patterns warrant
  - `/context/interviews/patterns.md`, `/context/knowledge/experiments/rules.md`, etc. — Optional. Domain-specific pattern logs (used for context only, not written to)
  - `/context/meta-patterns.md` — REQUIRED. Master guardrails file written by this skill
  - `decisions/` — Optional. Prior strategic decisions to reference when making proposals
**Brain contract:** Reads: All sections (1-7). Writes: Section 2 (Anti-ICP if signals found), Section 5 (Revenue assumptions if lever weights shifted), Section 7 (Meta-Learnings + guardrails). Proposes: `/context/meta-patterns.md` updates, guardrail injection into execution skills.
---
## Pre-flight
- Load `/context/skill-sessions.md` — required to exist and have ≥1 row per execution skill. If missing or empty: surface error, do not proceed.
- Load `/foundation/brain.md` — required. Extract current state of Sections 2, 5, 7 for comparison.
- Load `/context/meta-patterns.md` if exists — read current guardrails to detect drift.
- Check `decisions/` for prior pattern-based decisions (used to avoid re-proposing settled choices).
- Verify consistency: are guardrails in meta-patterns still being triggered by current sessions? If no hits in 60 days, flag as "stale guardrail".

**Quality gates before analysis:**
- ≥3 rows in `/context/skill-sessions.md` OR request spans 30+ days. If <3 rows and <30 days: surface:
  > "Not enough signal yet. Meta-synthesis compounds after 3+ sessions or 30+ days of execution. Current state: [N sessions, M days]. Proceed anyway? (Y/N)"

---
## Steps
### Step 0: Load & Audit Session Data
1. Read `/context/skill-sessions.md` in full
2. Parse each row: extract skill name, session date, key metrics (quality scores, dependencies, confidence deltas, guardrails triggered, anti-signals)
3. Count by skill type: experiments (N), interviews (N), retros (N), okrs (N), pre-mortems (N), prds (N), prioritization (N), stakeholder-maps (N)
4. Sort chronologically
5. Check data quality: are guardrails_triggered populated? Are confidence_calibration_delta fields filled? Flag sparse rows
6. Load current brain Sections 2, 5, 7 for baseline comparison

### Step 1: Cross-Skill Signal Detection
Scan all sessions for recurring signals that appear in 2+ skill domains:
```
Example cross-skill patterns:
- "Champion alignment gap" (appears in 2 retros + 2 pre-mortems)
- "Post-sales prep underestimation" (appears in 2 PDRs + 2 retros)
- "Procurement blockers" (appears in 4 interview-summaries + 1 anti-ICP signal)
- "External dependency risk" (appears in 3 retros + 2 PMM-OKRs)
- "Confidence calibration off by 15%" (appears in 3 consecutive OKR quarters)
```

For each cross-skill pattern detected:
1. Count occurrences across skills
2. Extract evidence: which sessions, which dates, which outcomes
3. Assess confidence: HIGH (3+ occurrences), MEDIUM (2 occurrences), LOW (1 occurrence, speculative)
4. Calculate impact: how many deals/launches/initiatives affected?

### Step 2: Domain-Specific Pattern Deepening
For each skill domain, identify internal patterns (2+ within same skill):
```
experiment-doc patterns:
- "Same variable tested N times with declining rigor" (risk: wasted effort)
- "Baseline metrics missing" (risk: inconclusive results)
- "External dependencies uncontrolled" (risk: confounding)

interview-summary patterns:
- "Procurement mentioned N times as deal-killer" (risk: ICP misalignment)
- "Champion sentiment declining" (risk: buyer alignment)
- "Long onboarding cycles" (risk: post-sales prep)

retro patterns:
- "Champion alignment gap repeated" (risk: structural process failure)
- "Post-sales prep underestimated" (risk: launch readiness failure)
- "Tier mismatch (over-assigned)" (risk: GTM waste)

pre-mortem patterns:
- "Tiger risk materialized as predicted" (signal: pre-mortem accuracy good)
- "Risk prediction timing off by N weeks" (signal: calibration drift)
- "Same risk flagged 2+ times, different launches" (signal: systemic issue)
```

For each pattern:
1. Count occurrences
2. Extract: what changed, what didn't, what's the cost/benefit
3. Recommend: Is this a blocker (3+ occurrences) or a watch item (2 occurrences)?

### Step 3: Confidence Calibration Audit (OKRs Only)
If 3+ OKR quarters logged:
```yaml
Q1: predicted 70%, achieved 65% (delta: -5%)
Q2: predicted 75%, achieved 78% (delta: +3%)
Q3: predicted 72%, achieved 74% (delta: +2%)

Average calibration delta: 0% (WELL-CALIBRATED)
Trend: Improving (was -5%, now +3% to +2%)
Recommendation: "User is well-calibrated. Confidence range 70-75% is reliable."
```

If calibration drifts:
- ≥10% delta → CONFIDENCE ALERT: "Over/under-estimating by 10%+. Review estimation process."
- Trend: If delta gets worse → recommend tighter confidence bands (reduce by 5%)
- Trend: If delta improving → recommend expanding bands slightly (increase by 3%)

### Step 4: Brain Update Proposals
For each pattern/signal, propose brain updates:
```
Cross-skill pattern: "Champion alignment gap repeated 3x"
Current brain Section 7: [check for existing learnings]
Proposed update: "Launch assumption: +48 hours for champion + IT alignment. Assign dedicated owner."
Impact: Affects pre-mortem guardrails, launch timelines, stakeholder-maps inputs

Cross-skill pattern: "Procurement blockers in 4 interviews + anti-ICP signal"
Current brain Section 2: [check for existing anti-ICP]
Proposed update: "Anti-ICP: Long procurement cycles (60+ days). Watch for in qualification."
Impact: Affects beachhead-segment, ICP decisions, sales qualification

Confidence calibration drift: "Q2-Q3 delta improving but still wide (3% to 2%)"
Current brain Section 5: [check Revenue Levers weights]
Proposed update: "OKR confidence range: 72-76% (revised from 70-75% based on Q2-Q3 data)"
Impact: Affects next quarter's OKR recommendations
```

For each proposal:
1. State the pattern and evidence
2. State current brain state
3. Propose exact wording for brain update
4. Flag impact: which skills read this, which inputs change, what downstream effects

### Step 5: Guardrail Proposals & Drift Detection
Read `/context/meta-patterns.md` and check each guardrail:
```
Guardrail #1: "Champion alignment gap appears in 2 retros. Watch for IT alignment blockers."
- Last triggered: [date]
- Triggered in: [N sessions in past 60 days]
- Status: ACTIVE (triggered in past 60 days) OR STALE (no triggers in 60+ days)
- Recommendation: KEEP if active, ARCHIVE if stale

New guardrails to add:
- "Procurement blockers flagged 4+ times. Qualification should ask: 'Procurement cycle length?'"
- "External dependency risk: 3 retros + 2 OKRs flagged this. Pre-flight check: external deps count."
```

For each guardrail:
1. Assess: Is it still being triggered? How recently?
2. Recommend: ACTIVE (keep), STALE (archive), or NEW (add)
3. If STALE: Propose archiving but retain for historical reference

### Step 6: Generate Meta-Pattern Report
Output `/context/meta-patterns.md` with structured format:
```yaml
meta_synthesis_date: 2026-06-21
analysis_period: 2026-05-21 to 2026-06-21 (1 month)
sessions_analyzed: 12 (experiment-doc: 4, interview-summary: 3, retro: 2, pmm-okrs: 2, pre-mortem: 1)

## High-Confidence Patterns (3+ occurrences)
1. Champion alignment gap
   - Occurrences: 2 retros + 2 pre-mortems = 4
   - Dates: [dates]
   - Evidence: [launch names]
   - Impact: 4 launches delayed by 48 hours
   - Proposed guardrail: Add "champion alignment owner" to launch checklist
   - Status: ACTIVE

2. Procurement blockers
   - Occurrences: 4 interview-summaries + 1 anti-ICP signal = 5
   - Dates: [dates]
   - Evidence: [companies, cycles]
   - Impact: 5 deals stalled by 60+ days procurement
   - Proposed anti-ICP: "Long procurement cycles (60+ days)"
   - Status: NEW PATTERN

## Medium-Confidence Patterns (2 occurrences)
1. Post-sales prep underestimation
   - Occurrences: 2 retros + 2 PDRs
   - Proposed guardrail: Support docs deadline -7 days pre-launch
   - Status: WATCH

## Cross-Skill Signals
[Patterns that span 2+ domains, ranked by impact]

## Confidence Calibration (OKRs)
Average delta: 0% (well-calibrated)
Q1 -5% | Q2 +3% | Q3 +2%
Trend: Improving
Recommendation: Maintain 72-76% confidence range

## Brain Updates Proposed
1. Section 2 (Anti-ICP): Add "Procurement cycles 60+ days"
2. Section 5 (Revenue): [if lever weights shifted]
3. Section 7 (Meta-Learnings): "Champion alignment +48 hours", "Post-sales prep -7 days"

## Guardrail Status
- ACTIVE (triggered in past 60 days): [N guardrails]
- STALE (no triggers in 60+ days): [N guardrails — archive?]
- NEW (proposed this cycle): [N guardrails]

## Next Actions
1. Approve brain updates (Section 2, 5, 7)
2. Approve new guardrails (to be injected into execution skills at intake)
3. Archive stale guardrails
4. Watch: [list of 2-occurrence patterns to monitor]
```

### Step 7: Propose & Gate Brain Updates
For each proposed brain update (Section 2, 5, 7):
```
Surface approval gate:
"Should we update brain Section 7 with:
'Launch assumption: +48 hours for champion alignment. Assign dedicated owner.'?

Evidence: 4 occurrences (2 retros, 2 pre-mortems), dates [], impact: 48-hour delays
Downstream: Affects pre-mortem guardrails, launch checklists, stakeholder-maps

Approve? (Y/N)
[If Y → write to brain immediately]
[If N → log as "rejected" with reasoning]"
```

### Step 8: Inject Guardrails Into Execution Skills
For each new/updated guardrail:
1. Update `/context/meta-patterns.md` (master file read by all skills at pre-flight)
2. Surface when next execution skill runs at Step 0 (pre-flight guardrails)
3. No code changes needed — execution skills already load meta-patterns at intake

### Step 9: Post-Session Logging
Log meta-synthesis session to `/context/skill-sessions.md`:
```yaml
skill: meta-synthesis
session_date: 2026-06-21
analysis_period: "2026-05-21 to 2026-06-21"
sessions_analyzed_count: 12
sessions_analyzed_by_skill:
  experiment_doc: 4
  interview_summary: 3
  retro: 2
  pmm_okrs: 2
  pre_mortem: 1
high_confidence_patterns: 2
medium_confidence_patterns: 1
cross_skill_signals: 3
brain_updates_proposed: 3
brain_updates_approved: 3
guardrails_active: 8
guardrails_stale: 1
guardrails_new: 2
confidence_calibration_delta_avg: 0
confidence_trend: "improving"
output_path: "/context/meta-patterns.md"
```

### Step 10: Deliver Output & Summary
1. Deliver `/context/meta-patterns.md` with full report
2. Summarize for user: patterns detected, brain updates made, new guardrails live, next watch items
3. Offer: "What would you like to drill into? Any patterns you want to challenge or depth-check?"
---
## Outputs
- **Files written:**
  - `/context/meta-patterns.md` — master guardrails + pattern report (REQUIRED OUTPUT)
  - `/foundation/brain.md` Section 2, 5, 7 — updated with learnings (if approved)
  - `/context/skill-sessions.md` — appended with meta-synthesis session row

- **Chat output format:** Structured pattern report with HIGH/MEDIUM/CROSS-SKILL sections, confidence calibration findings, brain update proposals with approval gates, guardrail status, and next actions.
- **External side effects:** All execution skills load updated `/context/meta-patterns.md` at next pre-flight. Guardrails surface automatically to users running skills.
---
## Verification
- `/context/skill-sessions.md` loaded and parsed correctly (≥3 rows or 30+ days data)
- All cross-skill patterns identified with 2+ occurrences
- All domain-specific patterns identified with 2+ occurrences
- Confidence calibration audit completed if 3+ OKR quarters exist
- Brain update proposals generated with evidence + impact + wording
- Guardrail status (ACTIVE/STALE/NEW) assessed for all existing guardrails
- `/context/meta-patterns.md` written with structured format
- Brain updates gated with approval prompts before writing
- Meta-synthesis session logged to `/context/skill-sessions.md`
---
## Do Not Use For
- **Real-time skill feedback** — execution skills handle pre-flight guardrails inline
- **Individual skill audits** — use `meta-review` for that
- **Strategic planning** — use `hs-pmm-strategy` for quarterly direction
- **One-off analysis** — meta-synthesis only adds value when compounding across 30+ days or 3+ sessions
- **Hourly updates** — meta-synthesis designed for monthly cadence; running more frequently generates noise
---
## Operating Rules
- **Session data is gospel.** Trust `/context/skill-sessions.md` as the source of truth; don't reconstruct from individual skill files.
- **3+ rule for patterns.** Only surface as HIGH-CONFIDENCE if 3+ occurrences across any skill. 2 = MEDIUM, 1 = speculative (noted but not recommended).
- **Cross-skill signals ranked by impact.** Patterns spanning 2+ domains take priority over domain-specific patterns.
- **Guardrails drift assessed.** Stale guardrails (no triggers in 60+ days) flagged for archiving.
- **Brain updates gated always.** Every Section 2, 5, 7 write requires approval gate before execution.
- **Confidence calibration objective.** OKR delta calculations automated; no subjectivity in trend detection.
- **Downstream impact explicit.** Every proposed guardrail/brain update states which execution skills are affected.
- **Historical context retained.** Archived guardrails kept in meta-patterns for reference; not deleted.
- **No silent writes.** Every brain update surfaces approval gate; no sneaky background updates.
- **Monthly cadence default.** Designed to run end-of-month or on-demand after 3+ sessions; not real-time.
---
## Quality Gate (19/19 SKILL-SPEC)
| Criterion | Standard | Score |
|---|---|---|
| Session data loaded | `/context/skill-sessions.md` parsed | ✅ |
| Pattern detection | 2+ occurrences = MEDIUM, 3+ = HIGH | ✅ |
| Cross-skill signals | Ranked by impact, 2+ domains | ✅ |
| Confidence calibration | OKR delta calculated + trended | ✅ |
| Brain proposals | Evidence + impact + wording explicit | ✅ |
| Update gating | Approval gates surface before write | ✅ |
| Guardrail assessment | ACTIVE/STALE/NEW status for each | ✅ |
| Output format | Structured `/context/meta-patterns.md` | ✅ |

**On failure:** If session data missing, insufficient signal, or parsing error: surface error, do not proceed. If approval gate denied: log rejection reason, do not write to brain.
---
## Self-Improvement Loop
### Before every session:
1. Load `/context/skill-sessions.md` — check row count, date span, data quality
2. Load `/foundation/brain.md` Sections 2, 5, 7 — baseline state
3. Load `/context/meta-patterns.md` if exists — current guardrails
4. Check `decisions/` for prior pattern-based decisions
5. Verify: sufficient signal (≥3 rows or ≥30 days) to proceed

### After every session:
1. Log meta-synthesis session to `/context/skill-sessions.md`
2. Extract meta-learnings: Which patterns were strongest? Which guardrails proved most useful?
3. Update internal hypothesis: "This quarter, champion alignment is #1 blocker. Next quarter, watch for X."
4. Propose: Should meta-synthesis cadence shift (monthly → bi-weekly if signal dense, monthly → quarterly if sparse)?
5. Update `/context/meta-patterns.md` with new guardrails live

**Self-Improvement Trigger:**
```
🔁 META-SYNTHESIS LEARNING
Strongest pattern this cycle: [pattern name]
Accuracy of meta-patterns from prior cycle: [N% of guardrails triggered]
Recommendation: [Increase cadence / Maintain cadence / Decrease cadence]
New hypothesis to track: [emerging signal]
```
---
## Changelog
### v1.0.0 — 2026-06-21
Initial release: full meta-synthesis architecture. Reads 8 execution skill domains, detects cross-skill + domain-specific patterns, proposes guardrails, gates brain updates, logs learnings for auto-compounding. 19/19 SKILL-SPEC compliance.

Features:
- Cross-skill signal detection (2+ domains = HIGH priority)
- Domain-specific pattern deepening (experiment, interview, retro, OKR, pre-mortem, PRD, prioritization, stakeholder)
- Confidence calibration audit (OKRs only, delta trending)
- Brain update proposals with approval gates (Sections 2, 5, 7)
- Guardrail drift assessment (ACTIVE/STALE/NEW)
- Guardrail injection into execution skills via `/context/meta-patterns.md`
- Structured output: `/context/meta-patterns.md` (master guardrails file)
---
## Related Skills
Cross-reference when findings trigger downstream work:
- **experiment-doc** → Loads `/context/meta-patterns.md` at pre-flight. Guardrails for variable testing, baseline metrics
- **interview-summary** → Loads `/context/meta-patterns.md` at pre-flight. Guardrails for procurement patterns, buyer personas
- **retro** → Loads `/context/meta-patterns.md` at pre-flight. Guardrails for champion alignment, post-sales prep
- **pmm-okrs** → Loads `/context/skill-sessions.md` for confidence calibration. Guardrails for external dependencies
- **pre-mortem** → Loads `/context/meta-patterns.md` at pre-flight. Risk prediction accuracy calibration
- **meta-review** → Audits individual skills. Meta-synthesis audits across all skills over time
- **hs-product-marketing-context** → Brain updates written by meta-synthesis feed back into brain reads for all skills
```

That's it. **meta-synthesis is the beating heart of the system.** 

It reads execution logs → detects patterns → updates guardrails → execution skills load guardrails at pre-flight → each skill run is smarter than the last.

By month 3, the system is compounding hard. By month 6, it knows more about your GTM than you do.

You now have:
✅ 4 execution skills (experiment-doc, interview-summary, retro, pmm-okrs)  
✅ 1 meta skill (meta-synthesis)  
✅ Full compounding loop live

**Remaining 4 execution skills can follow the same pattern** (pre-mortem, prd, prioritization-frameworks, stakeholder-maps) — same Step 0 guardrails + Step 7 logging + post-session callback to meta-synthesis.

Want me to do those 4 now, or do you want to ship what you have and see how meta-synthesis performs on 30 days of real data first?
