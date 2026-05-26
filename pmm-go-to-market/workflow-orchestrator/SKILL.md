---
name: workflow-orchestrator
description: "Orchestrates multi-skill PMM workflows end-to-end. Chains all hs- skills + pmm-toolkit skills for complete GTM programs. Reads brain context, writes back to brain after completion. Trigger on: 'run full GTM workflow', 'launch [product]', 'positioning refresh', 'competitive program', 'full PMM cycle', 'quarterly refresh', 'new market entry', or any multi-step PMM initiative. Maintains state across skills, verifies coherence, produces master program document."
---

# PMM Workflow Orchestrator

Orchestrates multi-skill PMM programs end-to-end. Chains your existing skills, passes state between them, writes back to brain, and produces one master program document.

---

## Brain Integration

**This orchestrator READS from brain:**
- Section 1: Product Context
- Section 2: ICP
- Section 3: Positioning (checks staleness)
- Section 4: Alternatives Map (checks gaps)
- Section 5: Proof Points
- Section 6: Voice & Tone
- Section 7: Launch History (for learning)

**This orchestrator WRITES to brain:**
- Updates Section 3 (after positioning refresh)
- Updates Section 4 (after competitive work)
- Updates Section 5 (after new proof points)
- Updates Section 7 (after launch or retro)

---

## Supported Workflows

### 1. Full Product Launch Workflow
**Trigger:** "run full launch workflow", "launch [product]", "full GTM for [product]"

**Sub-skills invoked (in order):**
1. Check brain Section 3 → if stale (>6 months), run `hs-positioning-messaging`
2. Check brain Section 4 → if competitor mentioned or T1/T2, run `hs-competitive-battlecard`
3. Run `hs-buyer-personas` (if Section 2 incomplete or buying committee changed)
4. Run `go-to-market-strategy` (assigns tier, generates strategy)
5. Run `hs-gaccs-brief` (campaign brief)
6. Route to `product-launch-playbook` (if T1/T2) for detailed execution
7. Run `hs-stakeholder-maps` (internal alignment)
8. Set T+90 reminder for `hs-retro`

**Duration:** 6-12 weeks (T1), 4-8 weeks (T2), 2-3 weeks (T3)

**Brain updates:**
- Section 3: Positioning (if refreshed)
- Section 4: Competitive intel
- Section 7: Launch plan (marked "Planned")

---

### 2. Positioning Refresh Workflow
**Trigger:** "refresh positioning", "positioning workshop", "update positioning", "our messaging is stale"

**Sub-skills invoked:**
1. Run `hs-positioning-messaging` (BUILD or AUDIT mode)
2. Update brain Section 3 with new positioning
3. Run `hs-value-prop-statements` (generate persona-specific copy)
4. Update `hs-competitive-battlecard` for all competitors (competitive differentiation section)
5. Run `hs-alternatives-map` (if alternatives changed)

**Duration:** 1-2 weeks

**Brain updates:**
- Section 3: Positioning (full refresh)
- Section 4: Alternatives Map (if changed)

---

### 3. Competitive Intelligence Program
**Trigger:** "competitive program", "competitive deep-dive for [competitor]", "build battlecards", "competitive refresh"

**Sub-skills invoked:**
1. Run `hs-alternatives-map` (if not current)
2. For each top competitor, run `hs-competitive-battlecard`
3. Run `hs-ci-stakeholder-briefing` (generate exec-level competitive newsletter)
4. Update brain Section 4 with all competitive intel

**Duration:** 2-4 weeks

**Brain updates:**
- Section 4: Alternatives Map + all battlecards
- Section 7: Competitive program completion (track quarterly)

---

### 4. Quarterly PMM Cycle
**Trigger:** "quarterly PMM cycle", "Q[X] refresh", "quarterly review", "PMM sprint"

**Sub-skills invoked:**
1. Run `hs-retro` for all launches from previous quarter
2. Run `hs-positioning-messaging` (AUDIT mode → refresh if needed)
3. Run `hs-competitive-battlecard` (refresh top 3 competitors)
4. Run `hs-proof-points-claims` (audit + add new proof points)
5. Run `hs-buyer-personas` (update if ICP shifted)
6. Run `hs-brainstorm-okrs` (set next quarter OKRs)

**Duration:** 3-4 weeks

**Brain updates:**
- Section 3: Positioning (if refreshed)
- Section 4: Competitive intel (refreshed)
- Section 5: Proof points (audited + updated)
- Section 7: Quarterly retros + new OKRs

---

### 5. New Market Entry Program
**Trigger:** "enter new market", "expand to [segment]", "new vertical", "market expansion"

**Sub-skills invoked:**
1. Run `hs-icp` (define ICP for new market)
2. Run `hs-buyer-personas` (buying committee for new market)
3. Run `hs-positioning-messaging` (positioning for new segment)
4. Run `hs-competitive-battlecard` for top 3 competitors in that market
5. Run `go-to-market-strategy` (tier + strategy for market entry)
6. Run `hs-gaccs-brief` (campaign brief)
7. Route to `product-launch-playbook` for execution

**Duration:** 8-12 weeks

**Brain updates:**
- Section 2: ICP (expanded or new segment)
- Section 3: Positioning (adapted for new market)
- Section 4: Competitive landscape (new market)

---

### 6. Post-Launch Retrospective Workflow
**Trigger:** "run retro for [launch]", "post-launch review", "analyze [launch] results", "update brain after launch"

**Sub-skills invoked:**
1. Run `hs-retro` (structured retrospective with cross-functional team)
2. Update brain Section 7 with actual results vs targets
3. Flag tier calibration issues (was tier correct?)
4. Suggest adjustments for next similar launch

**Duration:** 1 week

**Brain updates:**
- Section 7: Launch entry updated from "Planned" to "Completed" with actuals

---

### 7. Competitive Response (Fast)
**Trigger:** "competitive response to [competitor]", "they just launched [feature]", "fast battlecard"

**Sub-skills invoked:**
1. Run `hs-competitive-battlecard` for that competitor (expedited)
2. Run `hs-value-prop-statements` (differentiation messaging)
3. Generate sales enablement assets (comparison one-pager, talk tracks)

**Duration:** 1-2 weeks

**Brain updates:**
- Section 4: Updated competitive intel for that competitor

---

### 8. ICP + Personas Foundation Workflow
**Trigger:** "define our ICP", "who should we sell to", "build personas", "buyer intelligence"

**Sub-skills invoked:**
1. Run `hs-icp` (define/pressure-test ICP)
2. Run `hs-buyer-personas` (buying committee + messaging personas)
3. Run `hs-interview-summary` for any existing customer interviews
4. Update brain Section 2 with ICP + personas

**Duration:** 2-3 weeks

**Brain updates:**
- Section 2: Complete ICP + personas

---

### 9. Voice & Tone Foundation Workflow
**Trigger:** "define our voice", "brand voice guide", "tone of voice", "our copy sounds inconsistent"

**Sub-skills invoked:**
1. Run `hs-voice-tone` (BUILD mode)
2. Update brain Section 6 with voice guide
3. Run `hs-writing-assistant` (test voice on sample copy)

**Duration:** 1 week

**Brain updates:**
- Section 6: Voice & Tone guide

---

### 10. Full PMM Onboarding (New Hire)
**Trigger:** "onboard new PMM", "PMM audit", "what's our current state", "I just joined as PMM"

**Sub-skills invoked (read-only audit):**
1. Audit brain Sections 1-7 (what's complete, what's missing, what's stale)
2. Run `hs-positioning-messaging` (AUDIT mode)
3. Run `hs-proof-points-claims` (audit current claims)
4. Run `hs-competitive-battlecard` (audit existing battlecards)
5. Produce "Current State" report with prioritized gaps

**Duration:** 1-2 weeks

**Brain updates:** None (read-only audit)

---

[Rest of the file follows the same comprehensive pattern with Phase 0-7, examples, error handling, self-improvement loop, etc.]

---

*Part of the PMM Go-to-Market collection.*  
*Orchestrates all hs- skills + pmm-toolkit skills.*  
*Reads from brain, writes back to brain.*  
*Produces master program documents for complete GTM programs.*
