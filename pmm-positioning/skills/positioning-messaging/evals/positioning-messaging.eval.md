# hs-positioning-messaging.eval.md

Eval test cases for `hs-positioning-messaging` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: BUILD Mode — Full Positioning Hierarchy

**Input:**
- Mode: BUILD (or inferred from user request for "full positioning")
- Product: "API-first data platform for real estate workflows"
- Primary persona: "Director of Operations at mid-market real estate brokerage"
- Alternatives: (1) Spreadsheets, (2) Legacy MLS integrations, (3) Manual data entry, (4) Do nothing
- Customer evidence: Win/loss quote from customer ("We spent 40 hours/month reconciling data")

**Expected Behavior:**
1. Phase 1: Discovery runs (one question at a time, never multi-ask)
2. Hard floor validated (product, persona, 3+ alts, outcome)
3. Phase 2A: Market energy identified (M1/M2/M3 — expected: M2, "doing it badly")
4. Phase 2B: Competitive mapping completes (gaps identified)
5. Phase 2C: 3–4 positioning bets generated; user selects one
6. Phase 3: Dunford sequence runs (competitive alts → unique attrs → value translation → segment → category → statement)
7. Positioning statement produced (candidate: "For operations directors in real estate who spend >20 hours/month on data reconciliation, [product] is the API-first platform that [syncs all sources in real-time], unlike [spreadsheets] which [require manual entry]")
8. Phase 4: 4-layer messaging built (strategic narrative, core positioning, pillars, persona cards)
9. Phase 5: Pillars stress-tested (4/4 rubric)
10. Phase 6: Mode output = BUILD (all 4 layers + stress table + approved/forbidden language + validation plan)

**Success Criteria:**
- No skip of phases (all 6 run)
- Discovery is conversational (one question at a time)
- Positioning statement cannot be said by named competitors
- Pillars all pass 4/4 stress-test
- Evidence tier respected (T1/T2 claims anchor pillars; T3 claims flagged)
- 7-point self-verification gate passes
- Output ready to share with sales/marketing teams

**Test Pass:** Comprehensive positioning document produced

---

## Test 2: AUDIT Mode — Score Existing Messaging

**Input:**
- Mode: AUDIT (user pastes existing homepage copy + deck)
- Current messaging: "The leading AI-powered platform for enterprise data management"
- Competitor: "[Competitor] is the leading AI-powered platform for enterprise data management"

**Expected Behavior:**
1. Vision Layer parses any images immediately (extract claims before discovery)
2. VISION FLAGS appear: "leading" (undifferentiated), "AI-powered" (not a differentiator alone), "enterprise" (too broad)
3. Phase 1: Discovery runs (what are you really for, who cares most, what wins you deals?)
4. Competitive mapping reveals: positioning claim is identical to named competitor
5. Phase 5: Stress-test reveals claim fails "UNIQUE" (2/4)
6. Phase 6: AUDIT output format:
   - 5-dimension score (specificity / differentiation / coherence / proof / buyer language)
   - Example: Specificity 3/5, Differentiation 1/5, Coherence 3/5, Proof 2/5, Buyer Language 2/5
   - P1 (red) rewrite queue: messaging statement, "AI-powered" claim, "leading" claim
   - Before/after examples for P1 items
7. Output tells user: "Your messaging is not differentiated. Competitor can say the same things. Recommend rebuild using positioning-messaging BUILD mode."

**Success Criteria:**
- VISION flags caught at intake
- Scoring is multi-dimensional (not just "good/bad")
- Specificity of each weakness is high
- Before/after examples are provided
- Recommendation is clear (rebuild or audit mode)

**Test Pass:** User understands exactly why messaging is weak and what to fix

---

## Test 3: Evidence Tier Violation

**Input:**
- Mode: BUILD
- Product claim: "Integrates with 500+ tools" (no evidence provided)
- Product claim: "Reduces data reconciliation time by 40%" (customer quote provided: "We're saving 40 hours/month")
- Product claim: "AI model trained on [company's] proprietary dataset" (roadmap feature, not yet shipped)

**Expected Behavior:**
1. Phase 1: Evidence tier classified
   - "Integrates with 500+ tools" = T3 (product assertion, not validated)
   - "Reduces time by 40%" = T1 (customer verbatim)
   - "Proprietary AI" = ROADMAP (future feature, not valid)
2. Phase 4: Messaging hierarchy built
3. Phase 5: Stress-test runs
   - T1 claim "40% time reduction" passes all 4/4 → pillar headline candidate
   - T3 claim "500+ integrations" fails test 1 (TRUE?) → marked [T3 — NEEDS VALIDATION], only supporting claim
   - ROADMAP claim flagged `[ROADMAP — NOT YET VALID]` → removed from messaging
4. Phase 6: Output shows:
   - "Saves 40 hours/month" as pillar headline (anchored to T1)
   - "Integrates with 500+ tools" appears as supporting claim with [T3] flag
   - "Proprietary AI" absent from messaging with note: "[ROADMAP] This feature is planned but not yet shipped. Will not mention in external messaging until launch."
5. Self-verification gate passes because all pillars are 4/4 (unvalidated claims were downgraded, not promoted)

**Success Criteria:**
- Evidence tier is enforced (T3 doesn't headline, roadmap is excluded)
- Flags are explicit
- User is aware of validation gaps
- Messaging is built on credible evidence

**Test Pass:** Rigor prevents weak messaging from shipping

---

## Test 4: SALES-ENABLEMENT Mode — Persona Cards + Playbook

**Input:**
- Mode: SALES-ENABLEMENT
- Positioning statement and 3 pillars (from prior BUILD)
- 2 named competitors

**Expected Behavior:**
1. Phase 6: Mode-specific output
   - Persona cards (1–3, each includes):
     - Pain (in their language)
     - Promise (tied to their metric)
     - 3 proof points
     - Objection pre-handled ("But won't this require retraining our team?" — "It integrates with your existing workflows, so adoption is [X] days")
     - Stage-appropriate CTA (for Operations Director: "Schedule 30-min walkthrough with your data team")
   - Competitive playbook (for each competitor):
     - Column: "They say" (competitor's claim)
     - Column: "Their gap" (what they're missing)
     - Column: "We say" (your response)
     - Column: "Never say" (what damages credibility)
2. Output is sales-ready (can be printed or shared in Slack)

**Success Criteria:**
- Persona cards match actual sales motion (CTAs are stage-appropriate)
- Objection handling is specific (not generic)
- Competitive playbook has concrete responses
- Language is sales-friendly (not marketing-speak)

**Test Pass:** Sales team can use output immediately

---

## Test 5: Missing Required Input (Refusal)

**Input:**
- Mode: BUILD
- Product: "SaaS platform for [domain]"
- Persona: (not provided)
- Alternatives: (not provided)

**Expected Behavior:**
1. Phase 1 gets stuck at hard floor
2. Skill surfaces: "Can't proceed with Phase 2. Missing: (1) Primary persona ranked — who has this problem worst, right now? (2) 3+ alternatives, including status quo and do-nothing."
3. Skill blocks progression
4. User must provide both before continuing
5. If fewer than 3 alternatives: "You named 2 alternatives (status quo, build in-house). I need one more: either a direct competitor or the do-nothing option."

**Success Criteria:**
- Refusal is explicit and blocks output
- Reason is clear
- Request is specific (not vague)
- User knows exactly what's required

**Test Pass:** Skill maintains rigor even under time pressure

---

## Test 6: FLETCH Mode — 6-Slide Internal Deck

**Input:**
- Mode: FLETCH
- Positioning statement, 3 pillars, proof points (from prior BUILD)

**Expected Behavior:**
1. Phase 6: Mode output = FLETCH
2. 6-slide deck structure:
   - Slide 1: Segment + trigger ("For Ops Directors who spend >20 hrs/month reconciling data")
   - Slide 2: Alternatives map (competitive landscape visual)
   - Slide 3: Gap ("Spreadsheets require manual entry; [competitor] requires API knowledge")
   - Slide 4: Positioning statement + category
   - Slide 5: Pillars + proof (3 pillars, proof strip per pillar)
   - Slide 6: Homepage wireframe (hero headline, subhead, 3 pillar headlines + descriptions, CTAs)
3. Output is markdown with [SLIDE] markers for easy conversion to PowerPoint

**Success Criteria:**
- 6 slides exactly (not 4, not 8)
- Narrative flows logically
- Wireframe is actionable (can be built from this)
- Approved/forbidden language included

**Test Pass:** Internal deck and homepage wireframe are ready for design

---

## Test 7: Jargon Detection and Removal

**Input:**
- Mode: BUILD (messaging produced)
- Output includes: "We're a best-in-class, disruptive platform that seamlessly integrates your enterprise data"

**Expected Behavior:**
1. Phase 6: Quality Gate runs
2. Jargon check identifies forbidden terms:
   - "best-in-class" ❌
   - "disruptive" ❌
   - "seamlessly" ❌
   - "enterprise-grade" ❌
   - "synergy" ❌
   - "powered by AI" (as standalone) ❌
3. Self-verification fails on Jargon check
4. Skill surfaces: "This messaging contains 3 forbidden terms that weaken credibility. Rewriting now."
5. Revision produces: "We integrate all your data sources in real-time, so your team spends 40 hours/month on revenue work instead of data entry."
6. Recheck passes (no jargon)
7. Output delivered

**Success Criteria:**
- Jargon is caught
- Revision is automatic (not "please rewrite")
- New version is concrete and specific

**Test Pass:** Messaging is clean and credible
