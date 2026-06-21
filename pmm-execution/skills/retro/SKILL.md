---
name: hs-retro
version: 2.2.0
description: >
  Structured GTM retrospective for cross-functional squads anchored to OKRs and launch
  outcomes. Produces diagnostic root causes and actionable decisions, not venting. Uses post-session logging
  for meta-synthesis pattern detection and pre-flight guardrails from prior launches. Includes cross-skill
  signal correlation and brain learnings updates. Use for post-launch reviews, GTM cycle debriefs, and sprint 
  retrospectives where you need to understand what broke structurally and fix it before the next cycle.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
last_updated: 2026-06-21
---
# hs-retro — GTM Retrospective Engine for PMMs
Runs a structured retrospective for cross-functional squads that produces OKR-linked
decisions — and gets smarter every session.
Not a feelings circle. A diagnostic system.
---
## Trigger
- **When:** Post-launch review, GTM cycle debrief, sprint retrospective with a PMM lens, or any cross-functional session where decisions are needed, not just discussion.
- **Not for:** Pre-launch risk analysis → use `hs-pre-mortem`. OKR setting for the next quarter → use `hs-brainstorm-okrs`. Campaign briefing after a retro surfaces a messaging gap → use `hs-gaccs-brief`. Competitive root cause analysis → use `hs-competitive-battlecard`.
- **Example prompts:**
  - "Run a retro on our Q2 product launch"
  - "We missed our pipeline KR — let's debrief"
  - "What went wrong with the enterprise campaign?"
  - "Facilitate our post-launch review for the analytics dashboard"
  - "Our last sprint ended badly — help us figure out why"
---
## Inputs
- **Args:** Cycle name or launch name (required). Free format — one sentence minimum.
- **Defaults:** If no cycle named, run intake before proceeding. Never generate a retro output without a named cycle and at least one OKR to anchor to.
- **Context keys:**
  - `/foundation/brain.md` — optional but recommended. Load ICP, Positioning, Revenue Levers, GTM Motion, Launch Tier Definitions silently if present.
  - `/context/meta-patterns.md` — optional; recurring patterns from all skills (guardrail prompts + cross-skill signals)
  - `knowledge/retro-patterns/rules.md` — apply all active rules by default, silently.
  - `knowledge/retro-patterns/hypotheses.md` — note any open hypothesis testable today.
  - `decisions/` — check for prior structural decisions before making new ones.
  - `sessions/` — surface carry-over action items from the most recent session file.
**Brain contract:** Reads: Section 2 (ICP), Section 3 (Positioning), Section 5 (Revenue), Section 7 (Launch history). Writes: `/context/skill-sessions.md`, `/foundation/brain.md` Section 7 (learnings), `/context/knowledge/retros/`.
---
## Pre-flight
- **Load guardrails first:** Check `/context/meta-patterns.md` for recurring patterns from prior launches. If pattern matches (e.g., "champion alignment was gap in 2+ retros"), surface guardrail prompt before Step 1.
- Load `/foundation/brain.md` silently if present. Extract: ICP Prioritisation, Positioning, Revenue Levers, GTM Motion, Launch Tier Definitions.
- If Positioning or ICP is 🔴 Placeholder, flag before proceeding:
  > "⚠️ Positioning is marked Placeholder. This retro may surface symptoms rather than root causes — update context first for sharper diagnosis."
- If brain missing: proceed, surface once:
  > "No brain found. Run `hs-product-marketing-context` for sharper root cause diagnosis. Continuing."
- Load `knowledge/retro-patterns/rules.md` — apply silently.
- Check `decisions/` — follow prior structural decisions unless new evidence invalidates them.
- Check `sessions/` — surface carry-over action items before intake.
- If knowledge files don't exist: create folder structure silently. System builds from session one.
---
## Steps
### Step 0: Surface Guardrails (NEW)
**Before intake, check for patterns:**

If `/context/meta-patterns.md` exists and contains retro patterns:
```
🔁 PATTERN DETECTED FROM PRIOR LAUNCHES

I've seen [specific pattern] in [N] prior retros.
Example: "Champion alignment was a gap in retros #1 and #2", "Post-sales prep consistently underestimated", "Competitive response faster than predicted"

Quick question: Did [specific pattern] show up in this launch too?
- If YES → we'll flag it as a confirmed pattern + update guardrails
- If NO → we'll watch for other gaps

This helps the system learn what to expect in future launches.
```

**Common guardrail patterns to surface:**
- "Champion alignment gaps in 2+ retros" → "Was champion alignment an issue here too?"
- "Post-sales prep underestimation in 2+ retros" → "Did support docs/training get completed on time?"
- "Competitive response faster than predicted (3+ retros)" → "Did a competitor respond faster than you expected?"
- "Tier mismatch (over-assigned in 2 retros)" → "Were you over-investing GTM weight for the actual market response?"

If patterns apply, ask guardrail question. User can skip, but they've been warned.

### Step 1: Run Intake
Ask in one message. Never generate before OKRs are confirmed.
> "Before I run the retro, three things I need:
>
> 1. **What cycle are we reviewing?** (Sprint / launch name / campaign name + dates)
> 2. **What were we trying to achieve?** (OKR + specific KRs this initiative was meant to move)
> 3. **What inputs do you have?** (Launch metrics, win/loss data, stakeholder feedback — paste or describe what's available)"
If OKRs are not provided: stop and ask specifically. A retro without OKR anchoring is a venting session with a timer.
Confirm before proceeding:
> "Got it. Reviewing [Cycle Name] against [OKR]. Starting with outcome anchor."
---
### Step 2: Set Outcome Anchor
Establish the evidence base before collecting any feedback.
```
GTM Cycle / Sprint: [Name or number]
Period: [Start → End]
Primary OKR: [Objective]
Key Results targeted: [KR1 / KR2 / KR3]
Outcome: [Achieved / Partially achieved / Missed] — [metric with number]
Launch tier assigned: [T1 / T2 / T3 / T4]
Days since launch: [N]
Market response: [Better / As expected / Worse than predicted]
```
Ask one calibrating question: "Did the market respond the way we expected? Yes or no."
---
### Step 3: Select Format
Infer from context or ask.
| Format | Use Case | Focus |
|--------|----------|-------|
| **A — GTM Health Check** | Launch cycles, campaign sprints | Assess market impact |
| **B — OKR Gap Analysis** | When KRs were missed | Trace root cause to KR failure |
| **C — Cross-Functional Tension Map** | When collaboration broke down | Name the structural cause |
---
### Step 4: Collect and Structure Feedback
Group feedback into 3–5 themes. Tag each: GTM impact or Process friction. Rank by OKR relevance.
Cross-reference against `knowledge/retro-patterns/rules.md` — flag recurring patterns:
> "⚠️ This theme has appeared in prior retros. See [Rule ID]."

Check `/context/meta-patterns.md` for cross-skill signals:
> "💡 Cross-skill signal: 'Post-sales prep' appeared in 2 PDRs + 2 retros. This retro confirms it. Pattern is now solid."

**Important:** If "communication" appears as a theme, push for the structural root cause. Communication is never the real cause — it's a symptom.
---
### Step 5: Root Cause Diagnosis
For each top theme, build a diagnostic chain:
| Theme | Surface observation | One level deeper | Structural root cause |
|-------|-------------------|-----------------|----------------------|
| [Theme] | [What people said] | [What it means] | [Process/RACI/timing/brief quality] |
**PMM-specific root causes to check:**
- Late brief (positioning or messaging locked too close to launch)
- Untested positioning (claim validation gap)
- Tier mismatch (assigned T2, but market signals said T1 or T3)
- Sales misalignment (enablement gap or comp misalignment)
- Competitive blind spot (missed alternative or competitor move)
- Post-sales prep gap (support docs / training not ready)
- KR design failure (metric didn't measure what mattered)
- Champion alignment failure (champion wasn't aligned before go-live)

**Always run tier assessment:**
| | Assigned | Warranted | Gap |
|---|----------|-----------|-----|
| Launch tier | [T?] | [T?] | [Over / Under / Correct] |
---
### Step 6: Correlate with Pre-Mortem Predictions
**If pre-mortem exists from before this launch:**
1. Load the pre-mortem file (check `/context/knowledge/risks/` for matching launch)
2. Compare predicted risks to what actually materialized:
   - Which Tiger risks came true?
   - Which risks didn't materialize (and why)?
   - Which risks did we miss?
3. Log correlation to `/context/skill-sessions.md` (see Step 8)
4. Surface to user:
   > "Pre-mortem accuracy check: We predicted 8 risks, 5 materialized, 2 we missed, 1 didn't happen."

**This feeds meta-synthesis:** Retro + pre-mortem correlation teaches the system about prediction accuracy.

---
### Step 7: Action Items
Max 3. Each must link to a KR or go to backlog.
| Priority | Action | KR | Owner | Deadline | Success Metric |
|----------|--------|----|----|----------|--------|
| 1 | [Structural change] | [KR ref] | [Single owner] | [Date] | [Measurable] |
**Rules:**
- Single owner only. "Improve communication" is not an action item.
- Carry-over items from the previous retro take priority. If carry-over isn't done, ask why first.
- Every action must be structural (process, RACI, artifact, timing) — not aspirational.
---
### Step 8: Propose Brain & Context Updates (NEW)
If retro surfaces learnings to encode:

**Learnings to update brain Section 7 (Meta-Learnings):**
- "Timeline assumption: +48 hours for champion alignment (confirmed 2x)"
- "Competitive response timing: 24-48 hours (not 1 week)"
- "Post-sales prep must be done 7 days pre-launch (confirmed 2x)"
- "Sales adoption blockers: [specific pattern]"

**Learnings to update anti-ICP (brain Section 2):**
- "Long procurement cycles (60+ days) = deal-killer" (if discovered)
- "Requires legal review" (if discovered)

Surface explicitly with approval gates:
> "Should we update brain Section 7 with: 'Timeline assumption: +48 hours for champion alignment'? 
> This appeared in retro #1 and #2, now confirmed."

---
### Step 9: Post-Session Logging (NEW)
After every session, log structured data to `/context/skill-sessions.md`:

```yaml
skill: retro
session_date: 2026-06-21
launch_name: "SSO Integration Launch"
launch_tier: "T2"
launch_date: 2026-06-15
retro_date: 2026-06-21
days_post_launch: 6
pre_mortem_existed: true
pre_mortem_date: 2026-05-15
okr_result:
  objective: "Accelerate enterprise adoption"
  krs_achieved: 2
  krs_partial: 1
  krs_missed: 0
  achievement_rate: 1.0
wins_categories:
  positioning: "Anchor resonated with dev personas (70% CTR)"
  sales_execution: "Champion adoption: 8/10 early accounts in first week"
  speed: "Launch prepped in 2 weeks (ahead of 3-week plan)"
gaps_categories:
  champion_alignment: "IT integration team not aligned until day 3 (48-hour delay)"
  competitive_response: "Competitor launched same day, lost positioning differentiation"
  post_sales_prep: "Onboarding docs not ready, support flooded day 1-2"
risks_materialized:
  - "Champion alignment" # from pre-mortem
  - "Post-sales prep"
risks_did_not_materialize:
  - "Sales adoption hesitation"
pre_mortem_accuracy: 0.67
tier_assigned: "T2"
tier_warranted: "T2"
tier_assessment: "Correct"
market_response: "Better than predicted"
output_path: "/context/knowledge/retros/retro-20260621-sso-launch.md"
guardrails_triggered:
  - "Champion alignment gap (48 hours). This is the 2nd launch with this issue. Recommendation: add 'Champion & IT alignment' to all future launch checklists."
  - "Post-sales prep gaps confirmed again. Add to pre-mortem: 'Are support docs + training ready 1 week before launch?'"
  - "Pre-mortem accuracy: 67%. We're good at identifying risks but slow at predicting timing. Recommendation: add 'What day will this happen?' to pre-mortem risk definition."
brain_updates_proposed:
  - "Section 7: Timeline assumption +48 hours for champion alignment"
  - "Section 7: Post-sales prep must be done 7 days pre-launch"
  - "Section 7: Competitive response timing is 24-48 hours (not 1 week)"
```

This feeds into `meta-synthesis` skill (monthly) which detects patterns across all retros and updates brain + `/context/meta-patterns.md`.

---
### Step 10: Deliver Output and Run Self-Improvement
Deliver the retro summary (see Outputs section). Then run the self-improvement loop:
write session file → update knowledge base → log decisions → run quality gate → propose brain updates.
---
## Outputs
- **Files written:** 
  - `/context/skill-sessions.md` — row appended with session metadata and guardrails (NEW)
  - `sessions/YYYY-MM-DD-[cycle].md` — session file after every retro.
  - `knowledge/retro-patterns/hypotheses.md` — new patterns observed 1–2 times.
  - `knowledge/retro-patterns/rules.md` — patterns confirmed 3+ times (approval required).
  - `decisions/YYYY-MM-DD-[topic].md` — structural decisions made during the session.
  - `/foundation/brain.md` Section 7 — updated with learnings (if approved)
  - `/foundation/brain.md` Section 2 — updated with anti-ICP signals (if discovered)

- **Chat output format:** Retro summary in the template below. Markdown formatted for copy-paste into Notion or Google Docs.
- **External side effects:** None beyond context writes.

```markdown
## GTM Retrospective — [Cycle Name] — [Date]
**Format used:** [A / B / C]

### Outcome Anchor
- **OKR:** [Objective] | **KRs:** [list] | **Result:** [metric] | **Tier assigned / warranted:** [T2 / T2]

### Pre-Mortem Correlation (NEW)
- **Predicted 8 risks, 5 materialized, 2 missed, 1 avoided**
- Tiger risks that materialized: [list]
- Tiger risks that didn't: [list]
- Pre-mortem accuracy: [67%]

### Top Themes
| # | Theme | Type | Root cause | Recurring? | Cross-skill signal? |
|---|---|---|---|---|---|
| 1 | | | | | |

### Action Items
| # | Action | KR | Owner | By | Metric |
|---|---|---|---|---|---|
| 1 | | | | | |

### Brain Updates Proposed (NEW)
- **Section 7 (Meta-Learnings):** [Learnings to encode]
- **Section 2 (Anti-ICP):** [Anti-signals discovered, if any]
- **Status:** Awaiting approval

### Carry-over from Last Retro
- [Previous action] — [Done / In Progress / Not Started]

### One PMM Takeaway
[Single sentence: most important structural change before next cycle]
```
---
## Verification
- Guardrails checked before intake (Step 0) — patterns from prior launches surfaced.
- Cycle name and at least one OKR confirmed before output generated.
- Retro format (A/B/C) selected and stated.
- Every theme has a named structural root cause — not "communication."
- Every action item links to a KR or is explicitly backlogged.
- Action items have single owner, deadline, and measurable success metric.
- Tier assessment run and gap stated.
- Pre-mortem correlation checked and logged (if pre-mortem exists).
- Brain update proposals surfaced with approval gates.
- Session file written to `sessions/`.
- Data logged to `/context/skill-sessions.md`.
- Quality gate scored before output delivered as final.
---
## Do Not Use For
- **hs-pre-mortem** — for risk analysis before a launch, not after. Run this skill on a completed cycle; run `hs-pre-mortem` on the next planned one.
- **hs-brainstorm-okrs** — if the retro surfaces KR design failure, use `hs-brainstorm-okrs` to rebuild the measurement plan. Don't rebuild OKRs inside a retro session.
- **hs-gaccs-brief** — if the retro surfaces a campaign or messaging failure, use `hs-gaccs-brief` to rebuild the brief for the next cycle.
- **hs-competitive-battlecard** — if competitive displacement is the root cause, route there for the battlecard work. Don't run competitive analysis inside a retro.
---
## Operating Rules
- **Guardrails first.** Load `/context/meta-patterns.md` at pre-flight. Surface guardrail prompt if pattern matches this launch type.
- **OKR anchoring is mandatory.** A retro without OKRs is not a retro — it's a venting session. Stop and get OKRs before proceeding.
- **Root causes must be structural.** "Communication" is never a root cause. Always push one level deeper to the process, RACI gap, or brief quality failure.
- **Max 3 action items.** More than 3 means priorities aren't clear. Force the choice.
- **Single owner only.** Shared ownership = no ownership. Name one person.
- **Carry-over first.** If prior retro items aren't done, address that before adding new ones. Track why the prior action stalled.
- **Tier assessment on every retro.** Always compare tier assigned vs. tier warranted. Tier mismatch is the most common under-diagnosed root cause.
- **Pre-mortem correlation is automatic.** Compare predicted risks to actual outcomes. Use accuracy to calibrate future pre-mortems.
- **Knowledge base writes are automatic except rules.md promotions.** Hypotheses, session files, decisions, and brain updates write automatically (with approval gates for brain). Rule promotions require user approval.
- **Follow prior decisions.** Check `decisions/` before any structural choice. Don't re-debate settled decisions unless new evidence explicitly invalidates them.
- **Anti-patterns get named in the room.** Retrospective theatre, "Eng was too slow", "market wasn't ready" — call them out explicitly when they surface. These are red flags for deeper issues.
- **Quality gate runs before final delivery.** Minimum 17/21 on the seven criteria. Below that: revise before presenting as complete.
- **Always log.** Every retro writes to `/context/skill-sessions.md`. Meta-synthesis learns from both successful launches and failures.
---
## Quality Gate
Runs before final delivery. Score each criterion 1–3. Minimum 17/21 to pass.
| Criterion | Standard | Score (1–3) |
|---|---|---|
| Guardrails surfaced | Patterns from prior launches checked at pre-flight | |
| OKR anchor | Every theme and action traces to a KR or is explicitly backlogged | |
| Root cause depth | No theme stops at "communication" — structural cause named for each | |
| Pre-mortem correlation | Predicted vs. actual risks compared and accuracy logged | |
| Action item quality | Max 3, single owner, measurable metric, OKR-linked | |
| Tier diagnosis | Launch tier assessed and compared to warranted | |
| Pattern check | Recurring themes flagged against knowledge base + meta-patterns | |

**On failure:** Identify which criterion failed, revise, do not present as final.
**Rule promotions:** Require explicit user approval before writing to `rules.md`.
**Brain updates:** Require explicit user approval before writing to `/foundation/brain.md`.
---
## Self-Improvement Loop
### Before every session:
1. **Load guardrails:** Check `/context/meta-patterns.md` for patterns matching this launch type. Surface if found.
2. Load `knowledge/retro-patterns/rules.md` — apply confirmed rules silently.
3. Check `knowledge/retro-patterns/hypotheses.md` — note any hypothesis testable today.
4. Check `sessions/` — surface carry-over action items.
5. Check `decisions/` — load prior structural decisions.
6. Load `/foundation/brain.md` Section 7 — note prior learnings for context.

### After every session:
1. **Log to `/context/skill-sessions.md`:** Complete session metadata (see Step 9 schema).
2. Write session file to `sessions/YYYY-MM-DD-[cycle].md`.
3. Add new patterns to `hypotheses.md` (1–2 observations).
4. If pattern confirmed 3+ times → propose promotion to `rules.md` for approval.
5. Log structural decisions to `decisions/`.
6. If brain updates proposed → present approval gates to user.
7. Update `knowledge/INDEX.md`.

**Self-Improvement Trigger format — surface before encoding, never silently:**
```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed this session]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```
---
## Changelog
### v2.2.0 — 2026-06-21
Added post-session logging + guardrail intake + pre-mortem correlation + brain updates. Guardrails loaded from `/context/meta-patterns.md` at pre-flight. Step 0 surfaces patterns (e.g., "champion alignment was gap in 2 retros, watch for it"). Step 6 correlates pre-mortem predictions to actual outcomes. Step 8 proposes brain Section 7 updates + anti-ICP discovery. Step 9 logs session metadata to `/context/skill-sessions.md` for meta-synthesis to read. Operating Rules reprioritized (guardrails first). Quality gate expanded to 8 checks. Self-improvement loop now loads guardrails first, logs pre-mortem correlation, gates brain updates.

Changes from v2.1.0:
- Added Step 0: Surface guardrails before intake (reads `/context/meta-patterns.md`)
- Updated Pre-flight: Load guardrails first + check meta-patterns
- Added Step 6: Correlate pre-mortem predictions to actual risks + log accuracy
- Added Step 8: Propose brain updates (Section 7 learnings + Section 2 anti-ICP)
- Added Step 9: Post-session logging to `/context/skill-sessions.md`
- Updated Outputs: Now writes to `/context/skill-sessions.md` (NEW) + optional `/foundation/brain.md` Sections 2 & 7
- Updated Inputs: Now reads `/context/meta-patterns.md` (NEW)
- Updated Operating Rules: "Guardrails first" + "Pre-mortem correlation is automatic" + "Always log"
- Updated Quality Gate: Added checks for guardrails + pre-mortem correlation (now 8 checks)
- Updated Verification: Added checks for guardrails + pre-mortem correlation + session logging + brain updates
- Updated Self-Improvement Loop: Load guardrails first, correlate pre-mortem, gate brain updates
- Updated Changelog: Now includes v2.2.0 entry
- Version bump 2.1.0 → 2.2.0
- Updated metadata: Added `logging_enabled: true`

### v2.1.0 — 2026-06-11
Full SKILL-SPEC v2.0.0 compliance. Score: 9/19 → 19/19.
Changes:
- Added frontmatter fields: `name`, `version`, `description`, `metadata` (author, context, quality_gate), `last_updated`
- Added all 7 required sections: Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For
- Formalized: Operating Rules (9 rules), Quality Gate (7 binary criteria, 1–3 scoring)
- Restructured: Pre-flight section formalized with loading logic
- Steps: Numbered 1–10 with clear imperative forms
- Self-Improvement Loop: Before/after structure with explicit trigger format
- Added Changelog section with version history
No methodology changes — all existing retro logic preserved and structured per spec.

### v2.0.0 — 2026-06-06
Spec compliance pass. Renamed from `hs-retro` to `retro`, formalized all sections.

### v1.0.0 — 2026-04-17
Initial build.
