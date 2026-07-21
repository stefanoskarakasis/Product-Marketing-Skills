---
name: meta-learn.eval
version: 2.0.0
description: >
  Comprehensive eval suite for meta-learn v2.0.0. Tests: auto-trigger detection,
  three-question extraction, pattern classification, cross-skill routing, hypothesis
  confirmation/contradiction, approval gates, knowledge base writes, and session logging.
  8 scenarios covering ALWAYS mode (skill logs only), SUPERCHARGED mode (integrations),
  compounding learnings across sessions, and edge cases.
---

# Meta-Learn v2.0.0 — Eval Suite

## Setup (Universal)

Each eval:
1. Simulates a skill session completion (skill name, duration, outputs)
2. Provides session content (brief summary or full output)
3. Triggers meta-learn (auto or manual)
4. Evaluates: extraction → classification → routing → approval gates → writes → logging
5. Validates outputs: patterns extracted, files written, hypotheses updated, session logged

---

## Eval 1: Auto-Trigger Detection (Clean Session)

**Scenario:** go-to-market-strategy session completes (18 min, outputs GTM brief, success metrics). Meta-learn auto-detects completion and initiates learning capture.

**Test Data:**
```
Skill: go-to-market-strategy
Duration: 18 minutes
Outputs: 
  - GTM brief (T2 launch, 3 channels, 90-day timeline)
  - Success metrics (pipeline target, customer acquisition cost)
  - Competitive positioning (vs. 2 incumbents)
Session end: Detected (user confirms output complete)
```

**Expected Output:**
- ✅ Skill name detected correctly (go-to-market-strategy)
- ✅ Session duration captured (18 min)
- ✅ Outputs listed (3 files/documents)
- ✅ Session status: COMPLETE (not mid-session)
- ✅ Auto-trigger event logged
- ✅ Three extraction questions asked (not assumptions made)

**Pass Criteria:**
- Auto-detection works (no manual "/learn" needed)
- Session completion confirmed before extraction begins
- Three questions asked before proceeding
- No patterns extracted without user input

---

## Eval 2: Three-Question Extraction (Clear Learnings)

**Scenario:** User answers all three questions with concrete insights. Meta-learn extracts patterns from answers.

**Test Data:**
```
Session: retro on Q2 launch
Answers:
  1. Surprised: "The tier was assigned T2 but performed at T1 signal ($280K pipeline vs $90K target).
     We under-invested in enablement but the segment was hotter than expected."
  2. Wrong: "The skill suggested tier mismatch was a process failure. It was actually a signal
     reading failure — we had the data but didn't weight it correctly."
  3. Missing: "No prompt to check win/loss data before tier assignment. We had 65% win rate
     in this segment, should have been a T1 indicator."
```

**Expected Output:**
```
Pattern 1: "Win/loss data >60% in segment should raise tier to T1, not stay T2"
  From: Missing (launch retro)
  Classification: New Pattern
  Confidence: High (direct evidence: 65% win rate → T1 performance)
  Source: go-to-market-strategy domain
  Recommendation: Routing decision pending (cross-skill check)

Pattern 2: "Signal weighting error in tier assignment (prioritized revenue target over win rate)"
  From: Wrong (skill was factually incorrect in diagnosis)
  Classification: Skill Gap (identifies gap in tier assignment logic)
  Confidence: High (explicit call-out)
  Source: meta-learn gap
  Recommendation: Route to /knowledge/meta/skill-gaps/go-to-market-strategy.md (approval needed)

Pattern 3: "GTM tier assignment process missing: check win/loss data step"
  From: Missing (workflow gap)
  Classification: Skill Gap + Cross-Skill Signal (also flagged in beachhead-segment)
  Confidence: High
  Source: process improvement
  Recommendation: Route to /knowledge/meta/skill-gaps/ + check if beachhead-segment has same gap
```

**Pass Criteria:**
- All three answers captured and restated specifically
- Patterns are falsifiable (not vague)
- Distinction clear: Surprising vs. Wrong vs. Missing
- Each pattern has source and classification
- No pattern extracted before user input confirmed

---

## Eval 3: Cross-Skill Pattern Routing (3 Domains)

**Scenario:** Pattern appears in 3 skill domains (beachhead, gtm, sales). Meta-learn detects cross-skill signal and routes to global knowledge base.

**Test Data:**
```
Pattern: "Champion alignment is critical to success"
Session 1 (beachhead-segment): "Champion was misaligned with use case pain, segment underperformed"
Session 2 (go-to-market-strategy): "Top 3 risks: lack of champion alignment pre-launch"
Session 3 (hs-competitive-battlecard): "We lost 2 deals where champion was not champion of our solution"

Detected domains: beachhead + gtm + sales (3 domains)
Cross-skill signal rule: champion_alignment (threshold: 2 domains) → TRIGGER ✓
```

**Expected Output:**
```
Routing Decision:
  Pattern: "Champion alignment predicts success"
  Domains: beachhead + gtm + sales (3 skills)
  Cross-skill rule: champion_alignment ✓ MATCH (keywords ✓, domains ✓, threshold 2 met ✓)
  Impact score: 9/10 (high impact on deal flow + positioning + selection)
  
  Route: /knowledge/global/deal-signals.md (global, not domain-specific)
  Confidence: HIGH (3 domains, cross-skill rule matched)
  Approval gate: REQUIRE (new file + global scope + first time crossing 3 domains)
  
  Proposed guardrail: "Champion alignment" (watch for promotion threshold)
  Status: Currently MEDIUM confidence (3 confirmations), needs 5 for HIGH
```

**Pass Criteria:**
- Cross-skill signal detected correctly (config/routing.yml match)
- Routed to global/deal-signals.md (not domain-specific)
- Approval gate triggered (global file + new entry)
- Confidence calculated correctly (3 domains)
- Guardrail promotion flagged (if applicable)

---

## Eval 4: Hypothesis Confirmation (H3 Champion Sentiment)

**Scenario:** Session confirms open hypothesis "Champion sentiment predicts deal velocity". Meta-learn updates hypothesis status and confidence.

**Test Data:**
```
Session: retro on Q2 deals
Finding: "2 deals slowed significantly when champion engagement dropped (confirmed via Gong).
1 deal moved fast despite champion disengagement (counterexample)."

Open hypothesis H3: "Champion sentiment predicts deal velocity"
  Current status: TRACKING (3 confirmations)
  Current confidence: MEDIUM
  Confirmation criteria: Gong data + deal progression correlation

Session evidence:
  - Explicit confirmation: 2 deals slowed with declining champion (matches H3 exactly)
  - Partial contradiction: 1 deal moved fast despite weak champion (contradicts H3 in one case)
```

**Expected Output:**
```
Hypothesis Check:
  H3: "Champion sentiment predicts deal velocity"
  Session evidence: ✅ CONFIRMED + ⚠️ PARTIAL CONTRADICTION
  
  Confirmations: 3 prior + 1 new = 4 total
  Contradictions: 0 prior + 1 weak = 1 total
  
  Confidence calculation:
    Base: 4 confirmations = HIGH? No, need 5 for HIGH
    Penalty: -0.5 for weak contradiction
    Result: 4 - 0.5 = 3.5 (rounds to MEDIUM, but trending HIGH)
  
  New status: TRACKING (need 1 more confirmation for 5 total)
  Next action: "One more confirmation → HIGH confidence → eligible for guardrail promotion"
  
  Update /knowledge/global/hypotheses.md:
    H3 evidence count: 4 confirmations, 1 weak contradiction
    Confidence: MEDIUM (was MEDIUM, stable but trending HIGH)
    Status: TRACKING (close to CONFIRMED, 1 confirmation away)
```

**Pass Criteria:**
- Hypothesis identified from config/hypothesis-tracking.yml
- Confirmation status calculated correctly (explicit vs. inferred)
- Confidence updated: 3 → 4 confirmations
- Weak contradiction logged but counted (weight -0.5)
- Guardrail promotion threshold checked (5 confirmations, currently 4)
- Hypothesis file updated with new evidence

---

## Eval 5: Hypothesis Contradiction (H2 Pricing Elasticity)

**Scenario:** New pricing research contradicts open hypothesis H2 "Pricing elasticity varies by segment". Meta-learn marks hypothesis as contradicted and proposes closure.

**Test Data:**
```
Session: beachhead analysis with pricing data
Finding: "Pricing research across 50 accounts shows uniform willingness to pay ($X/user).
No significant variance by segment type. Contradicts earlier assumption."

Open hypothesis H2: "Pricing elasticity varies significantly by segment"
  Current status: TRACKING (1 confirmation)
  Current confidence: LOW
  Evidence: Prior session suggested WTP variance

Session evidence:
  - Direct contradiction: Pricing study shows uniform pricing (2+ sources, statistically significant)
  - This is 1 direct contradiction (weight -1.0)
```

**Expected Output:**
```
Hypothesis Check:
  H2: "Pricing elasticity varies by segment"
  Session evidence: ❌ CONTRADICTED
  
  Confirmations: 1 prior + 0 new = 1 total
  Contradictions: 0 prior + 1 direct = 1 total
  
  Confidence: LOW (1 confirmation) → CONTRADICTED status (1+ direct contradiction)
  
  Decision: Close hypothesis as DISPROVEN
  Status update: TRACKING → CONTRADICTED
  
  Learning: Pricing appears uniform across segments; future GTM work should assume
  single pricing strategy, not segment-specific variation. Extract this insight
  to /knowledge/global/pricing-strategy.md
  
  Approval required: YES (hypothesis closure + learning extraction)
```

**Pass Criteria:**
- Contradiction detected correctly (config: 2+ sources = direct contradiction)
- Hypothesis status changed to CONTRADICTED
- Learning extracted (uniform pricing strategy)
- Approval gate triggered (hypothesis closure)
- New pattern ("uniform pricing") routed appropriately

---

## Eval 6: Approval Gate Triggered (New Global File)

**Scenario:** Pattern needs to go to global knowledge base (new file). Approval gate blocks auto-write and shows user proposed text.

**Test Data:**
```
Pattern: "Messaging clarity drives sales velocity"
Domains: gtm + sales (2 skills)
Routing: /knowledge/global/messaging-clarity.md (NEW FILE)
Approval gate: NEW FILE + GLOBAL SCOPE → REQUIRE APPROVAL
```

**Expected Output:**
```
APPROVAL REQUIRED: New Global Knowledge Base File

Gate: New file creation + global knowledge base entry
Target: /knowledge/global/messaging-clarity.md (DOES NOT EXIST YET)

Proposed content:
---
# Messaging Clarity as Sales Velocity Predictor
Date: 2026-07-21
Skill Sources: go-to-market-strategy, hs-competitive-battlecard
Confidence: MEDIUM (2 confirmations)

Pattern: When positioning messaging is ambiguous or internally inconsistent,
sales cycles extend 25% and lose rate increases 15%.

Evidence:
  - GACCS brief noted inconsistent messaging across channels
  - Retro on Q2 campaign: Sales team confirmed messaging confusion in calls

Recommendation: Clarify positioning before launch. Validate message consistency
across sales collateral, website, and customer comms.

Next update: TBD (need 3+ confirmations for HIGH confidence)
---

Approval required because: New file + global scope + 2 domains (cross-skill)

OK to write? [yes] [no] [edit]
```

**Pass Criteria:**
- Approval gate triggered (new file detection)
- Exact proposed text shown (not just summary)
- Target file path correct and verified (doesn't exist)
- Gate reason explained to user
- User can approve, reject, or edit
- No write happens without explicit approval

---

## Eval 7: Multi-Session Compounding (Pattern Strengthens)

**Scenario:** Same pattern observed in consecutive sessions. Meta-learn detects compounding and updates confidence level.

**Test Data:**
```
Session 1 (2026-07-18): Pre-mortem identifies champion alignment as top 3 risk
  Pattern: "Weak champion alignment kills deals"
  Confidence: LOW (1 observation)
  File: /knowledge/sales/champion-alignment.md (created)

Session 2 (2026-07-20): Retro confirms champion disengagement in 2 deals
  Pattern: Same (champion alignment)
  Confidence update: LOW → MEDIUM (2 confirmations)
  File: /knowledge/sales/champion-alignment.md (updated, not new)

Session 3 (2026-07-21): Go-to-market-strategy flags champion engagement as success factor
  Pattern: Same (champion alignment)
  Confidence update: MEDIUM → HIGH (3 confirmations, cross-domain = 3 skills)
  File: /knowledge/sales/champion-alignment.md (updated)
  
  NEW: Cross-domain signal triggered (3 domains: sales, gtm, beachhead)
  NEW: Route to global/deal-signals.md (escalate from domain to global)
  NEW: Guardrail promotion candidate flagged
```

**Expected Output:**
```
Compounding Detected:
  Pattern: "Champion alignment predicts deal success"
  Prior history: 2 observations (LOW → MEDIUM confidence)
  New observation: 1 confirmation (Session 3)
  
  Total: 3 confirmations
  Domains: sales + gtm + beachhead (3 domains, cross-skill ✓)
  
  Confidence progression: LOW (1) → MEDIUM (2) → HIGH (3+, cross-domain)
  
  Actions:
    1. ✅ Update /knowledge/sales/champion-alignment.md (MEDIUM → HIGH confidence)
    2. ✅ Escalate to /knowledge/global/deal-signals.md (first global routing)
    3. ✅ Flag for guardrail promotion (HIGH confidence + cross-domain)
    4. ✅ Update hypothesis H3 status (if exists): +1 confirmation
  
  Impact: Future skill sessions load champion-alignment guardrail in pre-flight
  Approval: Required (escalation to global + guardrail promotion candidate)
```

**Pass Criteria:**
- Pattern recognized as repeat observation (same name/content as prior)
- Confidence level updated correctly (LOW → MEDIUM → HIGH)
- Compounding detected (multiple sessions, same pattern)
- Cross-domain escalation triggered (3 domains)
- Guardrail promotion flagged (for meta-synthesis)
- Session log tracks compounding (pattern count increases)

---

## Eval 8: Session Closes Without Patterns (Clean No-Op)

**Scenario:** User answers all three questions as "nothing surprised, nothing wrong, nothing missing". Meta-learn closes cleanly with log entry, no knowledge base writes.

**Test Data:**
```
Session: GACCS brief (completed successfully)
User answers:
  1. Surprised: "Nothing — the brief went as expected."
  2. Wrong: "Nothing I'd change about the skill output."
  3. Missing: "Everything was there. Process was smooth."
```

**Expected Output:**
```
✓ Extraction Complete

Patterns extracted: 0
Summary: No learnings to capture this session — that's valid.

Session log entry (automatic, no approval needed):
  Date: 2026-07-21
  Skill: hs-gaccs-brief
  Duration: 22 min
  Patterns: 0
  Hypothesis updates: 0
  Knowledge base writes: 0
  Quality: Clean close ✓

Next session: Your learnings compound across every session.
Even sessions with no new patterns are valuable (validates current processes).
```

**Pass Criteria:**
- No forced patterns when user says "nothing"
- Session still logged (historical record kept)
- Clean close message (not a failure, just no learnings)
- Zero knowledge base writes (no approval gates triggered)
- Session log entry created (automatic)

---

## Eval 9: Skill Gap Identified & Routed

**Scenario:** User identifies gap in a skill's logic. Meta-learn routes to skill gap file and flags for skill review.

**Test Data:**
```
Session: Pre-mortem on new launch
User says (Missing): "Pre-mortem asks about risks, but doesn't ask about champion
alignment pre-execution. We should know if the champion is aligned on the use case
BEFORE we launch. This is a pre-flight checklist item, not a post-mortem item."

Skill gap identified: hs-pre-mortem missing champion-alignment pre-flight check
```

**Expected Output:**
```
Skill Gap Detected:
  Skill: hs-pre-mortem
  Gap: Missing champion alignment assessment in pre-flight
  Why it matters: Champion misalignment is a deal-killer risk (flagged in H3, high-impact)
  
  Route: /knowledge/meta/skill-gaps/hs-pre-mortem.md
  
  Approval gate: REQUIRE (skill feedback should be deliberate)
  
  Proposed file content:
  ---
  # Pre-Mortem Skill Gap: Champion Alignment Pre-Check
  Date: 2026-07-21
  Reported by: [User]
  Severity: HIGH (matches H3: champion alignment predicts deal success)
  
  Gap: Pre-mortem doesn't explicitly check champion alignment BEFORE the execution phase.
  
  Recommendation: Add Step 2.5 (pre-flight):
  "Is your champion aligned with the use case pain we're solving?"
  "If champion misalignment, add to top 3 risks."
  
  Action: Route to meta-review for pre-mortem quality audit
  ---
  
  Approval needed: [yes] [no]
```

**Pass Criteria:**
- Skill gap identified correctly (not a pattern, a skill limitation)
- Routed to /knowledge/meta/skill-gaps/ (not domain)
- Approval gate triggered (skill feedback is high-stakes)
- Severity assessed (impact on other skills)
- Recommendation clear (what should change)

---

## Eval 10: End-to-End Workflow (Multi-Session Compounding Over 3 Days)

**Scenario:** Three skill sessions over three days, each generating learnings that compound. Meta-learn tracks cumulative patterns, hypothesis promotions, and guardrail creation.

**Cycle 1 (Day 1): Pre-Mortem Session**
```
Input: Pre-mortem on Q3 launch
User surprised by: "Champion misalignment risk (didn't expect to surface)"
Pattern extracted: "Champion alignment is a deal-killer risk"
Domains: Sales
Confidence: LOW (1 observation)
Action: Created /knowledge/sales/champion-alignment.md
Hypothesis: H3 gets +1 confirmation (now 3 total)
Log: Pattern 1 from pre-mortem
```

**Cycle 2 (Day 2): GTM Strategy Session**
```
Input: Go-to-market-strategy brief
User surprised by: "Tier assignment analysis included champion alignment check"
Pattern extracted: "Champion engagement in GTM planning matters"
Domains: GTM
Confidence: Updated /knowledge/sales/champion-alignment.md (2 observations now)
Hypothesis: H3 gets +1 confirmation (now 4 total)
Action: Pattern detected in 2 domains (sales + gtm) → cross-skill rule triggered
Cross-domain routing: Escalate to /knowledge/global/deal-signals.md
Log: Pattern 1 compounded, cross-skill signal triggered
```

**Cycle 3 (Day 3): Retro on Recent Deal**
```
Input: Retro on won deal
User surfaced: "Deal moved fast because champion was aligned (contrast: prior deals with weak champion moved slowly)"
Pattern extracted: "Champion engagement correlates with deal velocity"
Domains: Sales + GTM + (implicit) Beachhead
Confidence: 3 domains → HIGH confidence (5 observations total, 3+ domains)
Hypothesis: H3 reaches 5 confirmations → PROMOTION TO RULE READY
Action: Escalate to global/deal-signals.md (now definitive cross-skill rule)
Guardrail creation: "Champion alignment" guardrail should be created (HIGH confidence)
Log: Pattern compounded to HIGH confidence, guardrail promotion flagged
```

**Expected Meta-Synthesis Impact (24h cycle):**
```
Meta-synthesis cycle (after Day 3) will:
  1. See H3 "Champion sentiment" with 5 confirmations → graduate to rule
  2. See "champion-alignment" guardrail HIGH confidence + cross-domain → activate
  3. Next execution skill (Day 4) loads guardrail at Step 0:
     "Champion alignment predicts deal success: 5 confirmations, high-confidence rule"
  4. Skills reference guardrail in decision-making
  5. Quality metrics show: skills that load this guardrail have better outcomes

Quality trend:
  Day 1: Guardrails loaded = 8 (baseline)
  Day 2: Guardrails loaded = 8 (no change)
  Day 3: Guardrails loaded = 9 (champion-alignment added)
  
  Avg quality score: 84 → 84 → 87 (↑ improving)
```

**Pass Criteria:**
- Three sessions captured and logged
- Pattern compounding tracked (1 obs → 2 → 3+)
- Cross-skill signal detected (Day 2: 2 domains triggered rule)
- Hypothesis progression tracked (H3: 3 → 4 → 5 confirmations)
- Guardrail promotion flagged (Day 3: ready for creation)
- Meta-synthesis feedback loop validated (future sessions load new guardrail)
- Quality metrics show improvement (more guardrails = smarter skills)

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|---|---|---|
| 1 | Auto-trigger detection | Session completion detected, questions asked, no assumptions |
| 2 | Three-question extraction | All answers captured, patterns falsifiable, classifications correct |
| 3 | Cross-skill routing | Signal detected, routed to global, approval gated, confidence scored |
| 4 | Hypothesis confirmation | Status updated, confidence incremented, guardrail threshold checked |
| 5 | Hypothesis contradiction | Status changed to CONTRADICTED, learning extracted, closed |
| 6 | Approval gates | New file blocked, approval requested, exact text shown |
| 7 | Multi-session compounding | Pattern recognized, confidence upgraded, cross-skill escalation |
| 8 | No-op close | Clean close without forced patterns, session logged |
| 9 | Skill gap routing | Gap identified, routed to meta/, approval gated, severity assessed |
| 10 | End-to-end 3-day workflow | Patterns compound, hypothesis promotes, guardrail flagged, quality improves |

---

## Running the Evals

```bash
# Run all 10 evals
for i in {1..10}; do
  echo "Running eval $i..."
  # [invoke meta-learn v2.0.0 with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke meta-learn v2.0.0 with eval N test data]
# [validate against eval N pass criteria]

# Run end-to-end (Eval 10 in isolation, 3 days simulated)
# [Cycle 1: invoke pre-mortem session, verify pattern & hypothesis]
# [Cycle 2: invoke GTM strategy, verify compounding & cross-skill trigger]
# [Cycle 3: invoke retro, verify guardrail promotion flagged]
# [Verify meta-synthesis cycle sees H3 promotion → guardrail creation]
```

---

## Changelog

### v2.0.0 — 2026-07-21
Comprehensive eval suite for meta-learn v2.0.0:
- 10 scenarios covering all new features
- Auto-trigger detection testing
- Three-question extraction validation
- Cross-skill signal routing
- Hypothesis confirmation/contradiction tracking
- Approval gate logic
- Multi-session compounding
- Skill gap identification
- End-to-end 3-day workflow with guardrail promotion
- 100% coverage of v2.0.0 SKILL.md features
