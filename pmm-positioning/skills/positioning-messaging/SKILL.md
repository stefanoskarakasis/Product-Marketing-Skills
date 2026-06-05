---
name: positioning-messaging
version: 1.0.0
description: >
  Use for any positioning or messaging task — positioning statement, messaging
  hierarchy, homepage copy, sales persona cards, competitive deck, messaging audit,
  value proposition, tagline, elevator pitch, or when the user says "we sound like
  everyone else," "our messaging isn't landing," "sales can't explain what we do,"
  or mentions April Dunford, Emily Kramer, or Obviously Awesome; runs the full
  Dunford sequence across five output modes (BUILD / AUDIT / FLETCH /
  SALES-ENABLEMENT / HOMEPAGE) with Pawel Huryn's self-improving memory loop.
  Parses attached screenshots and images before asking any questions, refuses
  briefs without a named primary persona and at least three alternatives including
  status quo, and blocks output until a 7-point self-verification gate passes.
requires_brain: optional
reads_brain_sections: [1, 2, 3, 5]
writes_to_brain: true
triggers:
  - generate positioning
  - create positioning
  - positioning statement
  - messaging hierarchy
  - homepage copy
  - we sound like everyone else
  - our messaging isn't landing

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-05
---
---

# Positioning & Messaging

Built on April Dunford's Obviously Awesome method. Output discipline from
MKT1/Emily Kramer: deliver the answer, not the workings. Self-improving memory
via Pawel Huryn's compounding loop.

---

## Step 0: Check for Brain (Brain Integration)

Does `/foundation/brain.md` exist?

**If YES:**
- Load Section 1 (Product Context)
- Load Section 2 (ICP Definition)
- Load Section 3 (Alternatives & Positioning)
- Load Section 5 (Market Context)
- Use brain data to pre-populate Phase 1 discovery
- Skip discovery questions already answered in brain
- Proceed to Session Start

**If NO:**
- Skip brain loading
- Proceed to Session Start
- Ask all discovery questions manually in Phase 1

---

## Session Start — Silently, in Order

1. **Brain loaded?** Use brain data to pre-fill discovery inputs
2. Parse all attached images before reading the user's text
3. Proceed to mode selection

---

## Vision Layer (Opus 4.7)

Parse every attached image immediately. Do not ask the user to describe it.
Surface findings in Phase 1 as **"What your current materials are saying"**
before any discovery questions.

**Extract from any image:**
- Every explicit claim (exact text)
- Implied market category and target buyer
- Proof elements present (logos, metrics, quotes)
- All undifferentiated terms → flag each:
  `[VISION FLAG] "exact text" — reason this is weak`

The same extraction applies regardless of image type (homepage, deck slide,
ad, competitor page, one-pager). Flag, don't describe.

---

## Evidence Standard

Classify all inputs before Phase 2. Tier governs output weight.

| Tier | Qualifies as | Output rule |
|------|-------------|-------------|
| **T1** | Verbatim customer quotes, win/loss transcripts, NPS verbatims, G2 reviews in buyer's words | Can anchor a pillar headline |
| **T2** | Usage data, churn rates, win rates, A/B results, conversion data | Supports a pillar claim |
| **T3** | Product descriptions, PMM assertions, founder hypotheses | Must carry `[T3 — NEEDS VALIDATION]` flag; cannot headline a pillar |

**Refusal triggers:**
- Product in market 6+ months with zero T1/T2 → ask for it; don't proceed without
- Primary persona missing or unranked → ask: who has this problem worst, right now?
- Fewer than 3 alternatives (must include status quo + do-nothing) → no positioning without them
- Differentiator is a roadmap item → mark `[ROADMAP — NOT YET VALID]`; exclude

**Refusal format:**
> "Can't proceed with [phase]. Missing: [evidence type]. Why it matters: [one sentence].
> Provide: [exact format needed]."

---

## Mode Selection

Infer from context and confirm in one line, or ask.

| Mode | Output |
|------|--------|
| **BUILD** | Positioning statement + full 4-layer messaging document |
| **AUDIT** | Scored audit + prioritised rewrite queue with before/after |
| **FLETCH** | 6-slide internal positioning deck + homepage wireframe |
| **SALES-ENABLEMENT** | Persona cards + competitive response guide |
| **HOMEPAGE** | Production-ready headline, subhead, pillars, CTA — no placeholders |

All modes run Phase 1–5. Phase 6 packages to mode format. Do not skip phases.

---

## Phase 1: Discovery

Run as a conversation. One question at a time. Never generate on the first message.

**Hard floor — all four required before Phase 2:**
- [ ] Product: what it does today (not roadmap)
- [ ] Buyer: one primary (title, company type, triggering situation)
- [ ] Alternatives: 3+ including status quo and do-nothing
- [ ] Outcome: single most important buyer result in one sentence

**If brain exists:** Pre-fill from brain sections:
- Product → Section 1 (Product Context)
- Buyer → Section 2 (ICP Definition)
- Alternatives → Section 3 (Alternatives & Positioning)
- Market context → Section 5 (Market Context)

**Ideal additions:** T1 customer quotes · current messaging/screenshots ·
sales objections · win reasons · pricing model · company stage

**Evidence tier on input:**
- Images → Vision Layer already parsed; use findings as T1/T2 where applicable
- Win/loss quotes → T1; extract exact buyer language
- Usage/conversion data → T2; note metric and source
- Homepage/deck text → T3 until validated; audit for undifferentiated terms
- Product description only → T3; flag all capability claims `[T3 — NEEDS VALIDATION]`

**Exit:** Summarise all four hard-floor items back to user. Await confirmation.

---

## Phase 2A: Market Energy Check

Identify primary segment energy state before mapping competitors.

| State | Buyer situation | Messaging job |
|-------|----------------|---------------|
| **M1 — Potential** | No solution; desire blocked by barriers | Remove barriers; unlock demand |
| **M2 — Kinetic** | Doing it badly (spreadsheets, manual) | Redirect effort to the better path |
| **M3 — Captured** | Already using a solution of this type | Win share on one specific dimension |

Confirm with user. Primary positioning serves one state only. Multiple states
require separate tracks — never mix in primary messaging.

---

## Phase 2B: Competitive Mapping

Map all five alternative types honestly:
1. Direct competitors (same category)
2. Adjacent competitors (overlapping use case)
3. Status quo (spreadsheets, legacy tools, manual process)
4. Build in-house
5. Do nothing

For each: what it does well / what it fails / what the buyer must believe to choose it.

**Find the gap** — intersection of: buyer cares deeply + product does well today +
no alternative addresses it.

**Exit:** Complete before proceeding:
> "For buyers who need [outcome], alternatives fail because [gap], and we address
> this with [specific capability today]."

Cannot complete it? The product has a positioning problem messaging cannot fix. Stop.

---

## Phase 2C: Options-First

Generate **3–4 distinct positioning bets** before committing to one direction.
Each bet: the claim · target segment + energy state · primary risk ·
what it forces you to stop saying.

Present to user. Await selection. Do not proceed to Phase 3 without a chosen direction.

---

## Phase 3: Positioning Development

Dunford sequence:
1. Competitive alternatives (from Phase 2B)
2. Unique attributes — specific only ("3-click onboarding" not "better UX")
3. Value translation — "So what?" × 3 levels; Level 3 belongs in messaging
4. Who cares most — narrow to trigger-event segment, not demographic
5. Market category — frame that makes strengths obvious, not odd
6. Positioning statement × 3 versions:
   > "For [segment] who [situation], [product] is the [category] that
   > [differentiator], unlike [alternative] which [limitation]."

Pick sharpest version. **Exit:** Statement cannot be said honestly by any
named competitor. If it can, rewrite.

---

## Phase 4: Messaging Hierarchy

Build top-down. Layer 3 claims must trace to Layer 1. Cannot trace → remove.

**Layer 1 — Strategic Narrative** (150–250 words)
Old world → Shift → New world → Your role. Product appears after the problem
is fully established.

**Layer 2 — Core Positioning**
Tagline 5–8 words · One-liner 15–25 · Elevator pitch 50–75 · Boilerplate 75–100

**Layer 3 — Key Message Pillars** (exactly 3–4, MECE)
Each: headline claim + 2–3 sentence explanation + 2–3 proof points

**Layer 4 — Persona Cards** (1–3 max)
Each: pain in their language · promise tied to their metric · 3 proof points ·
one objection pre-handled verbatim · stage-appropriate CTA

**Exit:** All layers complete. Persona CTAs match actual sales motion.

---

## Phase 5: Differentiation Stress-Test

4-question test per differentiator. YES or NO only:

1. **TRUE?** — Provable with evidence a skeptical buyer accepts
2. **RELEVANT?** — Buyer cares enough to switch or pay more
3. **UNIQUE?** — 2+ competitors cannot honestly claim the same
4. **SUSTAINABLE?** — Still true in 12–18 months

Scoring (no exceptions):
- 4/4 → Layer 3 pillar headline
- 3/4 → supporting proof point only
- ≤ 2/4 → removed entirely

---

## Phase 6: Output Packaging

### Self-Verification Gate

Binary pass/fail. If any check fails: re-enter the named phase, fix, re-run
gate from top. Do not deliver with a caveat instead of a fix.

| Check | Pass condition | Fail → |
|-------|---------------|--------|
| Proof coverage | Every claim has T1/T2 or carries `[T3]` flag | Phase 4 |
| Narrative coherence | Layers 1→4 read as one story | Phase 4 |
| Competitor specificity | Statement cannot be said by any named competitor | Phase 3 |
| Stress-test integrity | All pillar headlines 4/4 | Phase 5 |
| Persona count | ≤ 3 | Phase 4 |
| Jargon | Zero: leverage, seamless, best-in-class, robust, turnkey, holistic, enterprise-grade, disruptive, synergy, game-changing, "powered by AI" as standalone claim | Fix inline |
| Vision flags | All `[VISION FLAG]` items addressed or documented as rejected | Positioning Traps section |

Before delivering, state: `"Self-verification passed. [N]/7 checks clear."`

### Mode outputs

**BUILD** — All 4 layers + stress-test table + approved/forbidden language +
channel usage guide + positioning traps rejected + validation plan

**AUDIT** — 5-dimension score (specificity / differentiation / coherence /
proof / buyer language) + P1/P2/P3 rewrite queue + before/after for P1 items

**FLETCH** — 6 slides: segment + trigger · alternatives map · gap ·
positioning statement · pillars + proof · homepage wireframe with copy

**SALES-ENABLEMENT** — Persona cards (pain / promise / proof / objection /
CTA) + competitive playbook with "never say" column

**HOMEPAGE** — Hero headline <8 words · subhead <20 words · 3 pillar headlines
+ 1-sentence descriptions · primary + secondary CTA · 2 proof strip options.
No placeholders.

### All modes include
Approved language · Forbidden language + reason · Version + review date ·
Next steps for validation

---

## Step [Final]: Save to Brain (Optional)

After generating positioning output:

"Want to save this positioning to your brain memory? (yes/no)"

**Why save:**
- Other skills (battlecard, value props, campaign briefs) will reference this
- Consistent messaging across all GTM outputs
- No re-explaining positioning in future sessions

**If YES:**
1. Write output to `/foundation/brain.md` Section 7
2. Field: `last_positioning_output` = [full positioning statement + messaging hierarchy]
3. Field: `last_positioning_date` = [timestamp]
4. Field: `last_positioning_mode` = [BUILD/AUDIT/FLETCH/etc.]
5. Confirm: "✅ Saved to brain Section 7"

**If NO:**
- Output only
- Not saved to brain
- User can save manually later
