---
name: meta-synthesis.eval
version: 2.0.0
description: >
  Comprehensive eval suite for meta-synthesis v2.0.0. Tests: scheduler trigger, integration mining,
  profile synthesis, stale cleanup, pattern detection, guardrail injection, brain gating, logging,
  and end-to-end 24h workflow with fallback modes. 8 scenarios covering ALWAYS mode, SUPERCHARGED
  mode, integration failures, and compounding learnings across multiple cycles.
---

# Meta-Synthesis v2.0.0 — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/config/scheduler.yml`, `/config/integration-queries.yml`, `/config/mcp-routing.yml`
2. Populates `/context/skill-sessions.md` with sample sessions (24h to 90d of data)
3. Populates `/foundation/brain.md` with baseline context (Sections 2-7)
4. Populates `/context/meta-patterns.md` with existing guardrails
5. Creates `/memory/` directory structure
6. Runs meta-synthesis v2.0.0 for given mode (ALWAYS or SUPERCHARGED)
7. Validates outputs: profile, guardrails, brain updates, logging

---

## Eval 1: Scheduler Trigger (24-Hour Automation)

**Scenario:** Configure scheduler.yml with timezone "America/New_York" and frequency "24h". Verify meta-synthesis triggers automatically at 2 AM ET every day.

**Test Data:**
```yaml
scheduler:
  frequency: "24h"
  timezone: "America/New_York"
  time_of_day: "02:00"
  enabled: true
```

**Expected Output:**
- ✅ Scheduler loaded correctly (timezone, frequency)
- ✅ First cycle runs at configured time
- ✅ Cycle completes within timeout (10 min)
- ✅ Run logged to `/memory/meta-synthesis-log.md` with timestamp
- ✅ Next run scheduled for +24h

**Pass Criteria:**
- Scheduler config parsed without errors
- Timezone respected (2 AM in user's timezone, not UTC)
- Retry logic works (if cycle fails, retries up to 3 times)
- Run logged with exact start/end timestamps
- Quality score present in log

---

## Eval 2: Integration Mining — ALWAYS Mode (No MCPs)

**Scenario:** All MCPs disabled in config. Meta-synthesis runs with only `/context/skill-sessions.md` + `/foundation/brain.md`. Verify profile synthesizes from skill logs alone.

**Test Data:**
```yaml
integrations:
  slack:
    enabled: false
  google_drive:
    enabled: false
  gmail:
    enabled: false
  google_calendar:
    enabled: false
  gong:
    enabled: false
```

**Skill Sessions:** 12 sessions past 24h (experiment, interview, retro, okr, pre-mortem)

**Expected Output:**
```markdown
# User Profile — ALWAYS Mode
Mode: ALWAYS (no integrations)
Data sources: Skill logs only

## Who You Work With
⚠️ MISSING DATA — Connect integrations to see collaborators

## What You're Working On
- [3 initiatives from brain Section 7]

## Top Blockers
- [Top 3-5 from guardrails triggered + pre-mortem risks]

## Timeline Pressure
⚠️ MISSING DATA — Connect Calendar to see milestones

## Patterns & Signals
- Strongest: [cross-skill signal from logs]
- Quality: [avg skill quality score]
```

**Pass Criteria:**
- Profile generated successfully
- "Who You Work With" shows placeholder for missing Slack/Calendar
- "What You're Working On" populated from brain
- "Top Blockers" populated from guardrails + pre-mortems
- Mode labeled as "ALWAYS"
- No errors from missing MCPs

---

## Eval 3: Integration Mining — SUPERCHARGED Mode (With Slack + Drive)

**Scenario:** Slack + Drive enabled, others disabled. Verify integration queries run and signals extracted.

**Test Data:**
```yaml
integrations:
  slack:
    enabled: true
  google_drive:
    enabled: true
  gmail:
    enabled: false
  google_calendar:
    enabled: false
  gong:
    enabled: false
```

**Mock Slack Signals:**
- Active channels: #gtm, #launches, #sales
- Blockers mentioned: "procurement blocked", "waiting CFO", "legal review stuck"
- Top collaborators: alice (45 msgs), bob (32 msgs), carol (28 msgs)
- Momentum: ↑ 15% vs last week

**Mock Drive Signals:**
- Recently edited: Q3-Roadmap.doc (2h ago), GTM-Brief-Sept.doc (4h ago)
- Shared with: 5 collaborators
- Priority docs: 3 docs in "Priority" folder

**Expected Output:**
```markdown
# User Profile — SUPERCHARGED Mode
Mode: SUPERCHARGED (Slack, Drive)

## Who You Work With
- alice — 45 messages in #gtm, #launches
- bob — 32 messages in #sales, #launches
- carol — 28 messages in #gtm
- [Shared drive docs with 5 people]

## What You're Working On
- Q3-Roadmap (last edited 2h ago)
- GTM-Brief-Sept (last edited 4h ago)
- [Brain initiatives]

## Top Blockers
- Procurement: blocked on procurement approval (mentioned 3x in Slack)
- Finance: CFO sign-off waiting (mentioned 2x in Slack)
- Legal: legal review stuck (mentioned 1x in Slack)
- [From guardrails + pre-mortems]

## Patterns & Signals
- Team momentum: ↑ 15% (Slack activity trending up)
- Active docs: 2 docs edited in past 24h (high velocity)
```

**Pass Criteria:**
- Slack queries executed successfully
- Drive queries executed successfully
- Collaborator names extracted correctly
- Blocker keywords detected ("blocked", "waiting", "stuck")
- Momentum trend calculated (↑ / ↓ / stable)
- Profile now includes team + strategic signals
- Mode labeled as "SUPERCHARGED (Slack, Drive)"

---

## Eval 4: Integration Timeout & Fallback to ALWAYS

**Scenario:** Slack enabled but times out (returns error after 30s). Drive succeeds. Verify system falls back gracefully to ALWAYS mode + continues with Drive signals.

**Test Data:**
```yaml
integrations:
  slack:
    enabled: true
    timeout_seconds: 30
  google_drive:
    enabled: true
```

**Mock Behavior:** Slack MCP doesn't respond within 30s. Drive MCP responds normally.

**Expected Output:**
```markdown
# User Profile — ALWAYS + Partial SUPERCHARGED
Mode: ALWAYS + SUPERCHARGED (Drive only)
Note: Slack signals unavailable this cycle (timeout after 30s, max retries exhausted)

## Who You Work With
[From Drive only — shared collaborators]
⚠️ Slack collaborators unavailable this cycle

## What You're Working On
- [From Drive + brain]

## Top Blockers
- [From Drive + guardrails + pre-mortems]
- ⚠️ Slack blockers unavailable this cycle

## Patterns & Signals
- Team momentum: ⚠️ Unavailable (Slack timeout)
- [From Drive + skill logs]
```

**Pass Criteria:**
- Slack timeout detected
- Retry logic triggered (up to 3 retries)
- After max retries, system continues with other sources
- Drive queries still execute
- Profile includes Drive signals
- Note surfaced: "Slack signals unavailable"
- Synthesis completes (doesn't block on Slack failure)
- Logged: "slack: timeout after retries"

---

## Eval 5: Pattern Detection & Ranking (Cross-Skill Signals)

**Scenario:** 12 skill sessions analyzed. Cross-skill patterns detected (2+ occurrences across domains). Verify impact scoring and ranking.

**Test Data:**
```yaml
Sessions:
  - retro #1: champion_alignment_gap (date: 6/20)
  - retro #2: champion_alignment_gap (date: 6/21)
  - pre_mortem #1: champion_alignment_gap (date: 6/22)
  - pre_mortem #2: champion_alignment_gap (date: 6/22)
  - interview #1: procurement_blockers (date: 6/21)
  - interview #2: procurement_blockers (date: 6/21)
  - interview #3: procurement_blockers (date: 6/20)
  - interview #4: procurement_blockers (date: 6/19)
  - okr #1: external_dependency_risk (date: 6/20)
  - okr #2: external_dependency_risk (date: 6/21)
  - experiment #1: baseline_metrics_missing (date: 6/22)
  - gaccs #1: proof_points_gap (date: 6/21)
```

**Expected Pattern Ranking:**
1. **HIGH: Procurement Blockers** (4 occurrences in interview domain)
   - Impact score: 8/10 (high frequency + cross-reference with guardrails)
   - Recommendation: "Procurement blockers flagged 4x. Update anti-ICP."

2. **HIGH: Champion Alignment Gap** (4 occurrences across retro + pre-mortem)
   - Impact score: 7/10 (cross-skill + business impact: delays)
   - Recommendation: "Add champion alignment owner to launch checklist."

3. **MEDIUM: External Dependency Risk** (2 occurrences in okr domain)
   - Impact score: 5/10 (medium frequency, specific to one domain)
   - Recommendation: "Watch for external dependencies in pre-flight."

4. **LOW: Baseline Metrics Missing** (1 occurrence)
   - Impact score: 2/10 (single occurrence)
   - Note: Monitor, not yet a rule

**Pass Criteria:**
- Patterns detected: ≥2 occurrences grouped correctly
- Impact score calculated: Occurrence count + cross-domain breadth + business impact
- Ranking by impact_score: HIGH (7+) > MEDIUM (4-6) > LOW (<4)
- Confidence assessed: HIGH (3+), MEDIUM (2), LOW (1)
- Recommendation generated per pattern
- Output sorted by impact (not alphabetical)

---

## Eval 6: Profile Synthesis (All Sections Complete)

**Scenario:** Full profile synthesized with all sections populated. Verify structure, content quality, metadata accuracy.

**Test Data:** Same 12 sessions + Slack/Drive signals

**Expected Output Structure:**
```
✅ Who You Work With (populated from Slack + Drive + Calendar)
✅ What You're Working On (populated from Drive + brain + Calendar)
✅ Top Blockers (populated from logs + Slack + Gmail + Gong)
✅ Timeline Pressure (populated from Calendar + brain dates)
✅ Patterns & Signals (populated from meta-synthesis)
✅ Last Week's Key Updates (decisions, risks materialized, assumptions validated)
✅ Next 24 Hours: What to Watch (top 3 items)
✅ Metadata (last updated, next sync, data sources, completeness %)
```

**Content Validation:**
- Collaborator names: Real (from actual Slack/Drive, not fabricated)
- Initiatives: From brain Section 7 or active Drive docs (real)
- Blockers: From actual guardrails / interviews / pre-mortems (real)
- Dates: All formatted YYYY-MM-DD, no future dates
- Patterns: Grounded in actual session data (evidenced)

**Metadata Validation:**
- Last updated: Exact timestamp of synthesis run
- Next sync: +24h from now
- Mode: ALWAYS / SUPERCHARGED [MCPs]
- Completeness: % fields populated (should be 90-100%)
- Quality score: 0-100 (based on gates)

**Pass Criteria:**
- All 8 sections present
- All sections have real content (not placeholders)
- All dates valid (no future dates)
- All collaborator names match actual sources
- Metadata accurate
- Profile is <1500 words (concise, scannable)
- Profile is readable by execution skills at Step 0

---

## Eval 7: Stale Cleanup & Archiving

**Scenario:** Entries in `/context/skill-sessions.md` and `/memory/user-profile.md` are old. Verify cleanup logic archives correctly.

**Test Data:**
```yaml
Stale entries:
  - Initiative "Q2 Planning" (last mentioned 30 days ago)
  - Blocker "Legal review" (resolved 90 days ago, marked resolved: true)
  - Guardrail "Low Pain segments" (last triggered 120 days ago)
  - Skill sessions >90 days old (30 entries)
```

**Expected Behavior:**
1. Initiative Q2 Planning (>14 days) → Move to `/memory/archived/initiatives/Q2-Planning.md`
2. Blocker Legal Review (resolved, >60 days) → Move to `/memory/archived/blockers/Legal-Review.md`
3. Guardrail (>90 days no trigger) → Mark status: STALE in `/context/meta-patterns.md` (keep, don't surface)
4. Sessions >90 days → Compress to 1-line summary, move to `/memory/archived/skill-sessions/`
5. Update `/memory/archived/index.md` with all archived entries

**Archive File Format:**
```markdown
# [Entry Name] — Archived
**Archive Date:** 2026-06-22
**Reason:** Initiative not mentioned in 14+ days
**Original Entry:**
[Full entry content]
**Status:** Archived
```

**Pass Criteria:**
- Stale initiatives archived (>14 days no mention)
- Resolved blockers archived (>60 days)
- Guardrails marked STALE (>90 days no trigger, not archived)
- Old sessions compressed + archived
- Archive index updated with all entries + retention dates
- Removed from active profile (not surfaced in next cycle)
- Historical record preserved (can retrieve if needed)

---

## Eval 8: End-to-End Workflow (Full 24h Cycle with Compounding)

**Scenario:** Multi-cycle test. Run meta-synthesis twice, 24h apart. Verify system compounds learnings: guardrails from Cycle 1 trigger in Cycle 2, patterns strengthen, confidence improves.

**Cycle 1 Data:**
```yaml
Sessions (Cycle 1): 10 sessions, 3 domains
Detected patterns:
  - "Champion alignment gap" (2 occurrences, new)
  - "Proof points gap" (1 occurrence, new)
Proposed guardrails: 2
Brain updates: 1 (Section 7)
Quality score: 82/100
```

**Cycle 2 Data (24h later):**
```yaml
Sessions (Cycle 2): 8 new sessions, 2 domains
These sessions reference Cycle 1 patterns:
  - "Champion alignment gap" mentioned 3 more times (total: 5 now)
  - "Proof points gap" mentioned 2 more times (total: 3 now)
  - New pattern: "External dependency risk" (2 occurrences)
Proposed guardrails: 3 (2 from Cycle 1 confirmed, 1 new)
Brain updates: 2 (Section 7, Section 5)
Quality score: 87/100
```

**Expected Compounding:**
```
Cycle 1 Output:
  guardrail_1: "Champion alignment gap" (confidence: MEDIUM, 2 occurrences)
  guardrail_2: "Proof points gap" (confidence: LOW, 1 occurrence)

Cycle 2 Output:
  guardrail_1: "Champion alignment gap" (confidence: HIGH, 5 occurrences) ← PROMOTED
  guardrail_2: "Proof points gap" (confidence: MEDIUM, 3 occurrences) ← UPGRADED
  guardrail_3: "External dependency risk" (confidence: MEDIUM, 2 occurrences) ← NEW

Execution Skill Step 0 (Cycle 2):
  ✅ Load guardrail_1: "Champion alignment gap" (now HIGH confidence, more likely to surface)
  ✅ Load guardrail_2: "Proof points gap" (now MEDIUM, surfaces)
  ✅ Load guardrail_3: "External dependency risk" (MEDIUM, surfaces)

Result: Cycle 2 execution skills are smarter, see more patterns, make better decisions
```

**Logging Validation:**
- `/memory/meta-synthesis-log.md` has 2 entries (Cycle 1 + Cycle 2)
- Cycle 1 logs guardrail promotions + confidence upgrades
- Cycle 2 logs guardrail accuracy ("Guardrails from Cycle 1: 100% triggered again")
- Confidence trend visible: Cycle 1 avg 82 → Cycle 2 avg 87 (↑ improving)

**Pass Criteria:**
- Cycle 1 completes (profile, guardrails, logging)
- Cycle 2 runs 24h later successfully
- Patterns from Cycle 1 referenced in Cycle 2 (compounding)
- Confidence upgraded if pattern appears 2+ more times
- Guardrail accuracy logged (% from prior cycle triggered again)
- Quality trend visible (score improving or stable)
- Brain Section 7 accumulates learnings (no overwrites, additive)
- Profile updates correctly (stale entries from Cycle 1 cleaned, new signals added)

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|---|---|---|
| 1 | Scheduler trigger | 24h automation works, timezone respected, retry logic succeeds |
| 2 | ALWAYS mode | Profile synthesized from skill logs only, no MCP failures |
| 3 | Integration mining (Slack + Drive) | Signals extracted, profile enriched with team + strategic |
| 4 | MCP timeout & fallback | Slack times out, Drive continues, profile partial but completes |
| 5 | Pattern detection & ranking | Patterns detected 2+, ranked by impact, confidence accurate |
| 6 | Profile synthesis | All 8 sections present, content real, metadata accurate |
| 7 | Stale cleanup | Archives created, old entries removed, index updated |
| 8 | End-to-end workflow + compounding | Multi-cycle test, patterns strengthen, guardrails promoted, quality improves |

---

## Running the Evals

```bash
# Run all 8 evals
for i in {1..8}; do
  echo "Running eval $i..."
  # [invoke meta-synthesis v2.0.0 with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke meta-synthesis v2.0.0 with eval N test data]
# [validate against eval N pass criteria]

# Run end-to-end (Eval 8 in isolation)
# [Cycle 1: invoke, verify outputs]
# [Wait 24h or simulate time]
# [Cycle 2: invoke, verify compounding]
```

---

## Changelog

### v2.0.0 — 2026-06-22
Initial eval suite for meta-synthesis v2.0.0:
- 8 comprehensive scenarios covering all new features
- Scheduler automation testing (24h cycle)
- Integration mining (ALWAYS + SUPERCHARGED modes)
- Pattern detection and ranking
- Profile synthesis with all sections
- Stale entry cleanup and archiving
- End-to-end multi-cycle workflow with compounding
- 100% coverage of v2.0.0 SKILL.md features
