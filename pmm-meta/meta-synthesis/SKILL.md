---
name: meta-synthesis
version: 2.0.0
description: >
  24-hour real-time learning engine. Reads execution skill logs + connected integrations (Slack, Drive, Gmail, Calendar, Gong) to detect patterns, synthesize dynamic user profile (who you work with, what you're building, top blockers), update guardrails, and compound learnings into brain. Runs automatically every 24h or on-demand. Trigger on: "run meta-synthesis", "what patterns are emerging", "detect cross-skill signals", "update guardrails", "compound our learnings", "what should we remember", or automatically every 24 hours via scheduler.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
  is_meta_skill: true
  automation: "24-hour automatic cycle"
  mcp_support: "Slack, Google Drive, Gmail, Google Calendar, Gong (optional)"
last_updated: 2026-06-22
---

# meta-synthesis — 24-Hour Real-Time Pattern Detection & Profile Synthesis

Reads execution logs + integrations → Detects patterns → Synthesizes profile → Updates guardrails → Compounds learnings.

The beating heart of the GTM system. Every 24 hours, smarter than before.

---

## Trigger

- **When:** Automatically every 24 hours (scheduler-based, timezone-aware). Or on-demand: "run meta-synthesis".
- **Not for:** Real-time feedback (execution skills handle Step 0 guardrails inline). Individual skill audits (use `meta-review`). Strategic planning (use other tools). One-off pattern queries without compounding.
- **Example prompts:**
  - "Run meta-synthesis"
  - "What patterns emerged this week?"
  - "Synthesize my profile"
  - "Detect cross-skill signals"
  - "Update guardrails based on last cycle"

---

## Inputs

**Args:** Optional timeframe (default: past 24h). Optional skill domain to focus on (default: all).

**Context keys:**
- `/context/skill-sessions.md` — REQUIRED. Master log of all execution skill sessions with structured metadata (quality_score, guardrails_triggered, brain_updates_proposed, etc.)
- `/foundation/brain.md` — REQUIRED. Current state (Sections 1-7), baseline for comparison and updates.
- `/context/meta-patterns.md` — REQUIRED. Current guardrails file. Read to assess freshness; written with new patterns.
- `/memory/user-profile.md` — REQUIRED (created first run if missing). Previous profile snapshot for delta detection.
- `/memory/meta-synthesis-log.md` — REQUIRED (created first run if missing). Historical record of all synthesis cycles.
- `/config/scheduler.yml` — REQUIRED. Timezone, frequency config.
- `/config/integration-queries.yml` — REQUIRED. Which MCPs enabled, what queries to run.
- `/config/mcp-routing.yml` — REQUIRED. MCP fallback mode, timeout, aggregation strategy.
- Slack MCP (optional) — If enabled: channels, blockers, collaborators
- Google Drive MCP (optional) — If enabled: recent docs, priorities, collaboration
- Gmail MCP (optional) — If enabled: open items, approvals, urgency
- Google Calendar MCP (optional) — If enabled: milestones, time allocation, stakeholders
- Gong MCP (optional) — If enabled: deal momentum, objections, competitors, sentiment

---

## Pre-flight

- Load `/config/scheduler.yml`. Verify timezone + frequency. If first run, ask: "What timezone?" + "Every 24h, 12h, or 7d?". Store in config.
- Load `/context/skill-sessions.md`. Required to exist and have ≥1 row. If missing or empty: surface error, do not proceed.
- Load `/foundation/brain.md`. Required. Extract Sections 2, 3, 4, 5, 7 baseline.
- Load `/context/meta-patterns.md` if exists. If missing: create with empty guardrails list.
- Load `/memory/user-profile.md` if exists (for delta detection). If missing: create template.
- Load `/memory/meta-synthesis-log.md` if exists (for historical context). If missing: create empty.
- Load `/config/integration-queries.yml`. Identify which MCPs enabled (Slack, Drive, Gmail, Calendar, Gong).
- Load `/config/mcp-routing.yml`. Read fallback mode + timeout + aggregation strategy.

**Quality gates before proceeding:**
- ✅ `/context/skill-sessions.md` exists and has ≥1 row OR timeframe >30 days
- ✅ `/foundation/brain.md` exists and has ≥3 sections populated
- ✅ `/config/scheduler.yml` readable
- ✅ At least one MCP enabled OR ALWAYS mode (skill logs only)

If any gate fails: surface error and ask for approval to proceed in ALWAYS mode (skill logs only, no integrations).

---

## Steps

### Step 0: Pre-Flight & Config Validation

1. Load all required files (see Pre-flight section)
2. Verify scheduler config (timezone, frequency)
3. Verify integration config (which MCPs enabled)
4. Check MCP availability (fallback to ALWAYS mode if MCPs unavailable)
5. Surface summary: "Running meta-synthesis [ALWAYS / SUPERCHARGED] mode. Analyzing past [timeframe]. Data from: [sources]."

---

### Step 1: Load & Parse Session Data

1. Read `/context/skill-sessions.md` for timeframe (default: past 24h)
2. Parse each row: extract skill name, session_date, quality_score, guardrails_triggered, brain_updates_proposed, confidence_score, assumptions, assumptions_count
3. Count sessions by skill type (experiment, interview, retro, okr, pre-mortem, prd, prioritization, stakeholder-maps, gaccs)
4. Sort chronologically
5. Quality check: flag sparse rows (missing key fields)
6. Load current brain Sections 2, 3, 4, 5, 7 for baseline comparison

---

### Step 2: Mine Integrations (If Enabled)

For each enabled MCP in `/config/integration-queries.yml`:

**If Slack enabled:**
- Query: active channels past 24h
- Query: blockers mentioned (keywords: blocked, stuck, waiting, hold, risk)
- Query: key collaborators (top 5 by message count)
- Query: momentum signal (message volume trending up/down)
- Extract: Who, What topics, Blockers mentioned, Momentum
- Aggregate into summary (not raw data)

**If Google Drive enabled:**
- Query: recently edited documents (past 24h)
- Query: shared with collaborators (new shares)
- Query: document priorities (from titles, tags, folder structure)
- Extract: Active docs, Shared with whom, Priority signals
- Aggregate into summary

**If Gmail enabled:**
- Query: open commitments (keywords: waiting, blocked, needs approval, on hold)
- Query: high-priority threads (urgent flags, follow-up flags)
- Query: approvals pending (who are you waiting on?)
- Extract: Open items, Waiting on whom, Urgency level
- Aggregate into summary

**If Google Calendar enabled:**
- Query: upcoming milestones (next 30 days, event titles)
- Query: time allocation (hours per topic: GTM, exec syncs, 1:1s, etc.)
- Query: stakeholder meetings (recurring with whom)
- Query: meeting trend (busier or quieter than last week?)
- Extract: Key dates, Time allocation %, Who's prioritizing you
- Aggregate into summary

**If Gong enabled:**
- Query: deal momentum (recent stage changes, velocity)
- Query: customer objections (top 3-5 from recent calls)
- Query: competitors mentioned (who, frequency)
- Query: champion sentiment (from recent calls, trending up/down)
- Extract: Deal stage, Top objections, Competitive threats, Champion engagement
- Aggregate into summary

**Fallback:** If MCP times out or unavailable, skip that MCP and continue with others. Log failure for transparency.

---

### Step 3: Cross-Skill Signal Detection

Scan all sessions for recurring signals appearing in 2+ skill domains:

- **Champion alignment gap** (appears in retros + pre-mortems) → cross-skill signal
- **Proof point gap** (appears in positioning + GTM + interview sessions) → cross-skill signal
- **Procurement blockers** (appears in interviews + GTM + okrs) → cross-skill signal
- **External dependency risk** (appears in pre-mortems + retros + okrs) → cross-skill signal
- **Confidence calibration drift** (appears across okrs) → cross-skill signal
- **Tier mismatch** (assigned vs. actual resource allocation) → cross-skill signal

For each cross-skill pattern detected:
1. Count occurrences across skills (e.g., 2 retros + 2 pre-mortems = 4 total)
2. Extract evidence: which sessions, dates, outcomes
3. Calculate impact: how many launches/deals/initiatives affected?
4. Assess confidence: HIGH (3+), MEDIUM (2), LOW (1)
5. Calculate impact_score (0-10):
   - Occurrence count: +1 per occurrence
   - Cross-domain breadth: +2 if 2+ domains, +4 if 3+ domains
   - Business impact: +0-4 based on deals/revenue affected
   - Confidence: multiplier 0.5-1.0

**Rank patterns by impact_score:** HIGH impact first.

---

### Step 4: Domain-Specific Pattern Deepening

For each skill domain, identify internal patterns (2+ within same skill):

**For experiment-doc sessions:**
- Same variable tested N times with declining rigor
- Baseline metrics missing
- External dependencies uncontrolled

**For interview-summary sessions:**
- Procurement mentioned N times as deal-killer
- Champion sentiment declining
- Long onboarding cycles

**For retro sessions:**
- Champion alignment gap repeated
- Post-sales prep underestimated
- Tier mismatch (over-assigned)

**For pre-mortem sessions:**
- Tiger risk materialized as predicted
- Risk prediction timing off by N weeks
- Same risk flagged 2+ times, different launches

**For pmm-okrs sessions:**
- Confidence calibration: predicted vs. achieved delta
- External dependency risk appearing
- Assumption density increasing

For each pattern:
1. Count occurrences (within skill domain)
2. Extract: what changed, what didn't, cost/benefit
3. Recommend: blocker (3+ occurrences) or watch (2)

---

### Step 5: Confidence Calibration Audit (OKRs Only)

If 3+ OKR quarters logged:

Calculate calibration delta per quarter:
```
Q1: predicted 70%, achieved 65% (delta: -5%)
Q2: predicted 75%, achieved 78% (delta: +3%)
Q3: predicted 72%, achieved 74% (delta: +2%)

Average delta: 0% (well-calibrated)
Trend: Improving (was -5%, now +3% to +2%)
Volatility: Low (max delta 5%)
```

Recommendation:
- If delta ≥10%: "Over/under-estimating by 10%+. Review estimation process."
- If trend worsening: "Reduce confidence bands by 5%."
- If trend improving: "Confidence bands are stable. No change needed."

---

### Step 6: Brain Update Proposals (Section 2, 5, 7)

For each pattern/signal, propose brain updates:

**Pattern: "Champion alignment gap repeated 3x"**
- Current brain Section 7: [check for existing learnings]
- Proposed update: "Launch assumption: +48 hours for champion + IT alignment. Assign dedicated owner."
- Downstream impact: Affects pre-mortem guardrails, GTM timelines, stakeholder-maps

**Pattern: "Procurement blockers in 4 interviews + anti-ICP signal"**
- Current brain Section 2: [check for existing anti-ICP]
- Proposed update: "Anti-ICP: Long procurement cycles (60+ days). Disqualify in qualification."
- Downstream impact: Affects beachhead-segment, ICP decisions, sales qualification

**Pattern: "Confidence calibration drift improving"**
- Current brain Section 5: [check revenue assumptions]
- Proposed update: "OKR confidence range: 72-76% (revised from 70-75% based on Q2-Q3 data)"
- Downstream impact: Affects next quarter's OKR recommendations

Surface approval gate for each:
```
"Should we update brain Section 7 with:
'Launch assumption: +48 hours for champion alignment. Assign dedicated owner.'?

Evidence: 4 occurrences (2 retros, 2 pre-mortems), dates [list], impact: 48h delays
Downstream: Affects pre-mortem guardrails, GTM timelines, stakeholder-maps

Approve? (Y/N)"
```

---

### Step 7: Guardrail Assessment & Drift Detection

Read `/context/meta-patterns.md` and check each guardrail:

**For each existing guardrail:**
- Last triggered: [date]
- Triggered in past 60 days: [Y/N]
- Status: ACTIVE (triggered) OR STALE (no triggers 60+ days)
- Recommendation: KEEP if active, ARCHIVE if stale

**New guardrails to add** (from pattern detection):
- "Procurement blockers flagged 4+ times. Qualification should ask: 'Procurement cycle length?'"
- "External dependency risk: 3 retros + 2 OKRs flagged this. Pre-flight check: external deps count."

For each new guardrail:
1. Provide exact wording
2. Specify which execution skill should load it (Step 0)
3. Provide trigger example
4. Estimate impact (how many launches will see this?)

---

### Step 8: Dynamic Profile Synthesis

Aggregate all signals (skill logs + integrations) into `/memory/user-profile.md`:

**Section: Who You Work With**
- Daily collaborators: [from Slack + Calendar + Drive] (top 5)
- Email exchanges: [from Gmail] (top 5 people)
- Shared projects: [from Drive] (active docs)
- Recent calls: [from Gong] (if enabled)

**Section: What You're Working On**
- Active initiatives: [from Drive + brain Section 7] (past 14 days)
- Launch timeline: [from Calendar + brain] (next 30 days)
- Deal pipeline: [from Gong] (if enabled, deal stages)
- Time allocation: [from Calendar] (% by topic)
- Exec scrutiny period: [from Calendar sync frequency]

**Section: Top Blockers**
- From GTM logs: [pre-mortem risks + guardrails triggered] (top 3-5)
- From Slack: [blockers mentioned in conversations] (top 3-5)
- From Gmail: [waiting on approvals, hold-ups] (top 3-5)
- From Gong: [customer objections + deal blockers] (top 3-5, if enabled)
- Aggregated: [ranked by frequency + impact]

**Section: Timeline Pressure**
- Next 7 days: [key milestones from Calendar + Gong]
- Next 30 days: [launches + closes from brain + Gong]
- Busy weeks ahead: [meeting count trending]
- Executive visibility: [exec sync frequency]

**Section: Patterns & Signals**
- Strongest GTM pattern this cycle: [cross-skill signal + evidence]
- Emerging team signal: [Slack + Gmail convergence]
- Deal signal: [Gong win/loss trend]
- Execution quality: [skill quality scores trending up/down]
- Calibration accuracy: [OKR delta trend]

**Section: Metadata**
- Last updated: [timestamp]
- Next synthesis: [24h from now]
- Data sources: [ALWAYS / SUPERCHARGED + which MCPs]
- Profile completeness: [% fields populated]

---

### Step 9: Stale Entry Cleanup

Archive entries that are no longer active:

**Stale initiatives (not mentioned 14+ days):**
- Query: initiatives in brain Section 7 with last_mentioned >14 days ago
- Action: Move to `/memory/archived/initiatives/[name].md`
- Keep: Historical record, date archived, reason

**Resolved blockers (resolved >60 days ago):**
- Query: guardrails in meta-patterns.md with "resolved: true" and resolved_date >60 days ago
- Action: Move to `/memory/archived/blockers/[name].md`
- Keep: Historical record, resolution date, outcome

**Stale guardrails (not triggered 90+ days):**
- Query: guardrails in meta-patterns.md with last_triggered >90 days ago
- Action: Mark status = STALE (keep in meta-patterns, don't surface in Step 0)
- Keep: Reference, but deprioritize

**Compress old sessions (>90 days):**
- Query: sessions in skill-sessions.md with date >90 days ago
- Action: Summarize to 1-line entry + move to `/memory/archived/skill-sessions/`
- Keep: Historical record, compressed format

Update `/memory/archived/index.md` with all archived entries and retention dates.

---

### Step 10: Generate Meta-Pattern Report

Output `/context/meta-patterns.md` with:

```yaml
meta_synthesis_date: 2026-06-22
analysis_period: 2026-06-21 to 2026-06-22 (24h)
sessions_analyzed: 12
sources:
  skill_logs: true
  slack: [enabled/disabled]
  drive: [enabled/disabled]
  gmail: [enabled/disabled]
  calendar: [enabled/disabled]
  gong: [enabled/disabled]

## High-Confidence Patterns (3+ occurrences)
guardrail_1:
  pattern_name: "Champion alignment gap"
  occurrences: 4 (2 retros + 2 pre-mortems)
  dates: [list]
  evidence: [launch names]
  impact: 4 launches delayed 48 hours
  impact_score: 8/10
  proposed_action: "Add 'champion alignment owner' to launch checklist"
  status: ACTIVE

## Medium-Confidence Patterns (2 occurrences)
[list]

## Cross-Skill Signals
[ranked by impact_score]

## Confidence Calibration (OKRs)
average_delta: 0%
trend: improving
recommendation: maintain current confidence bands

## Brain Updates Proposed
1. Section 2 (Anti-ICP): [text]
2. Section 5 (Revenue): [text]
3. Section 7 (Meta-Learnings): [text]

## Guardrail Status
active: [N guardrails]
stale: [N guardrails — ready for archive]
new: [N guardrails — proposed this cycle]

## Next Actions
1. Approve/reject brain updates
2. Approve/reject new guardrails
3. Archive stale guardrails
4. Watch: [2-occurrence patterns to monitor]
```

---

### Step 11: Propose & Gate Brain Updates

For each proposed update (Section 2, 5, 7):

Surface approval gate:
```
"Should we update brain Section 7 with:
'[exact proposed text]'?

Evidence: [count] occurrences, [dates], impact: [description]
Downstream: Affects [which skills, which decisions]

Approve? (Y/N)"
```

If approval gates fail or user rejects: log as "rejected" with reasoning. Do not write to brain.
If approved: proceed to Step 12.

---

### Step 12: Execute Brain Writes (If Approved)

For each approved update:
1. Write to `/foundation/brain.md` Section 2, 5, or 7
2. Log write: "brain_update_executed: true, section: [N], text: [exact]"
3. Surface confirmation: "Brain updated. Section [N] now includes: [text]"

---

### Step 13: Inject Guardrails Into Execution Skills

For each new/updated guardrail:
1. Write to `/context/meta-patterns.md` (master file)
2. Next time any execution skill runs at Step 0 (pre-flight), load this file
3. Guardrails with last_triggered in past 14 days surface automatically
4. Guardrails with STALE status archived (not surfaced)
5. No code changes needed — execution skills already read meta-patterns at intake

---

### Step 14: Log Meta-Synthesis Session

Log to `/context/skill-sessions.md` and `/memory/meta-synthesis-log.md`:

```yaml
skill: meta-synthesis
session_date: 2026-06-22
session_start: [timestamp]
session_end: [timestamp]
duration_minutes: [calc]
analysis_period: "2026-06-21 to 2026-06-22"
mode: "ALWAYS" or "SUPERCHARGED [MCPs: Slack, Drive]"

sessions_analyzed: 12
sessions_by_skill:
  experiment_doc: 4
  interview_summary: 3
  retro: 2
  pmm_okrs: 2
  pre_mortem: 1

patterns_detected:
  high_confidence: 2
  medium_confidence: 1
  cross_skill_signals: 3

integration_mining:
  slack: [success/timeout] + [signals extracted count]
  drive: [success/timeout] + [signals extracted count]
  gmail: [success/timeout] + [signals extracted count]
  calendar: [success/timeout] + [signals extracted count]
  gong: [success/timeout] + [signals extracted count]

profile_synthesis:
  collaborators_identified: [count]
  initiatives_active: [count]
  blockers_identified: [count]
  timeline_pressure_detected: [Y/N]
  profile_completeness: [%]

brain_updates:
  proposed: 3
  approved: 3
  executed: 3
  rejected: 0

guardrails:
  active: 8
  stale: 1
  new: 2
  archived: 0

confidence_calibration:
  okr_delta_avg: 0%
  trend: "improving"

stale_cleanup:
  initiatives_archived: 0
  blockers_archived: 0
  guardrails_marked_stale: 1
  sessions_compressed: 0

quality_score: 88/100
quality_checks:
  session_data_loaded: ✅
  patterns_detected: ✅
  cross_skill_signals: ✅
  confidence_calibration: ✅
  brain_updates_gated: ✅
  guardrails_assessed: ✅
  profile_synthesized: ✅
  cleanup_executed: ✅

output_files_written:
  - "/context/meta-patterns.md"
  - "/memory/user-profile.md"
  - "/context/skill-sessions.md" (appended)
  - "/foundation/brain.md" (Sections 2, 5, 7 if approved)
  - "/memory/archived/index.md" (if any archives)

next_scheduled_run: [24h from now]
```

---

### Step 15: Deliver Output & Summary

1. Deliver full `/context/meta-patterns.md` report
2. Show profile snapshot from `/memory/user-profile.md`
3. Summarize for user: patterns detected, brain updates made, guardrails live, next watch items
4. Offer: "What would you like to drill into? Any patterns you want to challenge?"

---

## Scheduler Configuration

**File:** `/config/scheduler.yml`

```yaml
scheduler:
  job_name: "meta_synthesis_24h"
  enabled: true
  frequency: "24h"  # or "12h", "7d"
  timezone: "UTC"   # user-selected at onboarding
  time_of_day: "02:00"  # quiet hours, avoid peak work time
  
  retry:
    enabled: true
    max_retries: 3
    backoff_minutes: 5  # wait 5min, then retry
  
  logging:
    log_all_runs: true
    log_path: "/memory/meta-synthesis-log.md"
    retention_days: 365
  
  notifications:
    on_success: false  # silent if successful
    on_failure: true   # alert if fails after retries
```

---

## Operating Rules

- **Load brain before analysis.** Brain Sections 2-7 set the baseline. Changes measured against baseline.
- **Session data is gospel.** `/context/skill-sessions.md` is the source of truth. Trust logged data.
- **3+ rule for HIGH patterns.** Only surface as HIGH-CONFIDENCE if 3+ occurrences. 2 = MEDIUM, 1 = speculative.
- **Cross-skill patterns ranked by impact.** Patterns spanning 2+ domains take priority over domain-specific.
- **Guardrails drift assessed.** Stale guardrails (no triggers 60+ days) flagged for archiving.
- **All brain updates gated.** Every Section 2, 5, 7 write requires approval gate before execution.
- **Memory is immutable between cycles.** Only meta-synthesis writes to /memory/. No agent modifications during conversation.
- **No raw integration data stored.** Extract signals only, not raw Slack messages or email threads.
- **Fallback to ALWAYS mode.** If any MCP times out, continue with remaining sources. Never block entire cycle.
- **24-hour cadence default.** Designed for automatic execution every 24 hours. Manual triggers also supported.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Session data loaded | `/context/skill-sessions.md` parsed with ≥1 row |
| Brain loaded | Sections 2, 3, 4, 5, 7 extracted |
| Integration mining | At least one source mined (skill logs or MCP) |
| Pattern detection | 2+ occurrences identified + ranked |
| Cross-skill signals | Signals spanning 2+ domains ranked by impact |
| Confidence calibration | OKR delta calculated + trended (if applicable) |
| Profile synthesized | All sections present (Who, What, Blockers, Timeline, Patterns) |
| Stale cleanup | Archives created, old entries moved |
| Brain updates gated | Approval gates surfaced before writes |
| Guardrails assessed | ACTIVE/STALE status for all guardrails |
| Output written | `/context/meta-patterns.md`, `/memory/user-profile.md` created/updated |
| Session logged | Metadata appended to `/context/skill-sessions.md` + `/memory/meta-synthesis-log.md` |

**All checks must pass. If any fails: surface error, do not proceed.**

---

## Self-Improvement Loop

### Before every cycle:
1. Load `/config/scheduler.yml` — verify timezone + frequency
2. Load `/context/skill-sessions.md` — check row count, data quality
3. Load `/foundation/brain.md` Sections 2-7 — baseline state
4. Load `/context/meta-patterns.md` — current guardrails
5. Load `/memory/meta-synthesis-log.md` — prior cycles (for calibration)

### After every cycle:
1. Extract meta-learnings: Which patterns were strongest? Which guardrails triggered?
2. Update hypothesis: "This cycle, [pattern] is #1. Next cycle, watch for [signal]."
3. Track: "Guardrail accuracy: [N]% of recommended guardrails triggered in next cycle."
4. Propose: Should 24h cadence shift? (Stay 24h / speed up to 12h if dense signal / slow to 7d if sparse)
5. Update `/memory/meta-synthesis-log.md` with cycle summary

```
🔁 META-SYNTHESIS LEARNING

Strongest pattern this cycle: [pattern name]
Accuracy of guardrails from prior cycle: [N% triggered]
Guardrail ROI: [valuable? noisy? archive-worthy?]
Recommendation: [Maintain 24h / Change cadence]
New hypothesis to track: [emerging signal]
```

---

## Do Not Use For

- **Real-time skill feedback** — execution skills already handle Step 0 guardrails inline
- **Individual skill audits** — use `meta-review` for SKILL.md audits
- **Strategic planning** — use other strategic tools for direction-setting
- **One-off analysis without compounding** — meta-synthesis only adds value when running repeatedly

---

## Changelog

### v2.0.0 — 2026-06-22
Major upgrade from v1.0.0:

**New Features:**
- 24-hour automatic scheduler (timezone + frequency configurable)
- Integration mining: Slack, Google Drive, Gmail, Google Calendar, Gong (optional MCPs)
- Dynamic profile synthesis: Who, What, Blockers, Timeline, Patterns
- Auto-archive stale entries (14-day initiatives, 60-day blockers, 90-day guardrails)
- Write-once-read-many memory architecture (/memory/ files)
- Smart guardrail injection (only recent, not noise)
- Impact scoring for pattern ranking
- Confidence calibration audit for OKRs
- Enhanced logging with granular signal tracking

**Architecture:**
- Added Steps 10-14 (integrations, profile, cleanup, logging)
- Added Scheduler Configuration section
- Added config files (scheduler.yml, integration-queries.yml, mcp-routing.yml)
- Memory setup (/memory/ directory structure)
- ALWAYS mode (skill logs only) + SUPERCHARGED mode (with MCPs)
- Progressive MCP activation (start ALWAYS, opt-in to integrations)

**Compliance:**
- 19/19 SKILL-SPEC v2.0.0 compliant
- 8 comprehensive evals covering all new capabilities
- Full logging to `/context/skill-sessions.md` + `/memory/meta-synthesis-log.md`

### v1.0.0 — 2026-06-21
Initial release: Monthly pattern detection + guardrails + brain updates.
