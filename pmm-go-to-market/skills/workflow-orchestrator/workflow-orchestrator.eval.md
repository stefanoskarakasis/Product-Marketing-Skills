# workflow-orchestrator — Eval Suite
**Skill version:** 2.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: Program Charter confirmation — full launch workflow

**Input:**
```
/run full-launch
Initiative: Analytics Dashboard for mid-market product teams.
DRI: me.
Goal: 30% feature adoption in 90 days.
Launch in 8 weeks.
```

**Expected output includes:**
- Brain pre-flight runs silently — staleness of Sections 3 and 4 assessed
- Program Charter produced before any skill runs:
  - Initiative name, workflow type, DRI, primary metric, timeline
  - Brain status summary (which sections are current vs. stale)
  - Ordered skill sequence with one-line rationale per skill
  - Skills to skip (if any brain sections are current) with reason stated
- Charter ends with explicit confirmation prompt: "Confirm to start? [Y/N]"
- No skill runs before confirmation

**Expected output excludes:**
- Any skill output before charter is confirmed
- Silent brain reads without surfacing staleness to user
- Charter produced without DRI named

**Pass condition:**
Program Charter is complete, all required fields present, explicit confirmation
requested, and zero skill outputs produced before user confirms.

---

## Test Case 2: Brain missing — orchestrator blocks

**Input:**
```
Run a full positioning refresh for our B2B SaaS product.
```

**Expected output includes:**
- Pre-flight detects missing brain
- Blocking message surfaced — not a soft warning:
  > "Brain file not found at `/foundation/brain.md`. Run `product-marketing-context`
  > first..."
- Explicit instruction to run `product-marketing-context` before proceeding
- No workflow starts, no skills run
- Contrast with individual skill behaviour — orchestrator does not degrade gracefully

**Expected output excludes:**
- Soft warning that continues into the workflow anyway
- Any skill invoked without brain present
- Generic "I'll do my best without context" response

**Pass condition:**
Orchestrator fully blocks execution and routes to `product-marketing-context`
with a clear reason. No skill runs.

---

## Test Case 3: /skip command — downstream impact disclosed

**Input:**
```
/run quarterly-cycle

[Charter confirmed]

/skip positioning-messaging — we just did a full positioning refresh 6 weeks ago
```

**Expected output includes:**
- Skip acknowledged with the user's reason
- Downstream impact explicitly stated before confirmation:
  - What the next skill (e.g. `hs-competitive-battlecard`) loses by not having
    fresh positioning output
  - Whether the 6-week-old positioning is likely still coherent with upcoming
    competitive work
- Explicit confirmation request before skip is locked in: "Confirm skip? [Y/N]"
- If confirmed: orchestrator proceeds to next skill in sequence without re-running
  positioning
- Skip logged in program state for master document

**Expected output excludes:**
- Skip executed without downstream impact disclosure
- Silent skip with no confirmation
- Downstream skill run as if positioning was just refreshed (inaccurate state)

**Pass condition:**
Downstream impact is named specifically before confirmation, user confirms,
and skip is logged in program state.

---

## Test Case 4: /coherence — conflict detected and surfaced

**Input:**
```
/coherence

[Context: positioning-messaging has run and positioned the product for VP of Sales
at enterprise companies. go-to-market-strategy ran next and recommended SMB-focused
channels — LinkedIn ads to startup founders, Product Hunt launch.]
```

**Expected output includes:**
- Coherence check structured output with ✅ / ⚠️ / ❌ per pairing
- ❌ flagged for Positioning ↔ GTM strategy conflict:
  positioning targets VP of Sales / enterprise, GTM channels target SMB founders
- Specific conflict description — not generic "there may be a mismatch"
- Recommended action: re-run `go-to-market-strategy` with enterprise ICP explicitly
  passed, or confirm if SMB is the intended expansion target
- No downstream skill proceeds until conflict is resolved

**Expected output excludes:**
- ✅ across all pairings when a clear conflict exists
- Vague "you may want to review alignment" without naming the specific conflict
- Orchestrator proceeding to next skill with an unresolved ❌

**Pass condition:**
Coherence check catches the positioning/GTM segment conflict, names it specifically,
and blocks progression until user resolves it.

---

## Test Case 5: /status command mid-program

**Input:**
```
/status

[Context: quarterly-cycle workflow started 3 days ago. retro and positioning-messaging
have been completed. hs-competitive-battlecard is pending.]
```

**Expected output includes:**
- Program name and workflow type
- Skills completed with dates: `retro` (date), `positioning-messaging` (date)
- Skills pending: `hs-competitive-battlecard`, `hs-proof-points-claims`, `hs-brainstorm-okrs`
- Next skill clearly named: `hs-competitive-battlecard` — what it reads from prior
  outputs and what it will produce
- Brain updates made so far: Section 3 updated (date), Section 7 retros completed (date)
- Open items if any surfaced during completed skills
- No new skills triggered by /status

**Expected output excludes:**
- /status triggering any skill execution
- Missing or incomplete program state
- Open items without named owner

**Pass condition:**
/status returns complete program state without triggering execution, correctly
shows completed vs. pending skills and brain updates made.

---

## Test Case 6: Full PMM Onboarding / Audit — read-only enforcement

**Input:**
```
/run audit

I just joined as Head of PMM at this company and want to understand what's in place.
DRI: me.
```

**Expected output includes:**
- Charter produced: workflow type = "Full PMM Onboarding / Audit", read-only noted
- Brain sections 1–7 audited: completeness, staleness, gaps named per section
- `positioning-messaging` run in AUDIT mode only — no new positioning generated
- `hs-proof-points-claims` run in AUDIT mode only — no new claims added
- Current State Report produced with prioritised gaps
- Explicit statement at close: "No brain writes made — this was a read-only audit"
- Recommended next step: which skill to run first based on highest-priority gap

**Expected output excludes:**
- Any write to brain sections during the audit
- Full positioning BUILD run instead of AUDIT
- New proof points added to Section 5
- Gaps identified without priority order

**Pass condition:**
Zero brain writes made. Current State Report produced with prioritised gaps.
Read-only confirmation stated explicitly at close.

---

## Test Case 7: Competitive Response (Fast) — expedited workflow

**Input:**
```
/run competitive-response Salesforce

Salesforce just announced Einstein AI deeply integrated into their CRM at the same
price point as us. This is urgent — we have a sales call with a prospect tomorrow
who will definitely bring this up.
```

**Expected output includes:**
- Fast workflow confirmed — 3-skill sequence: battlecard → value props → exec briefing
- Urgency acknowledged — orchestrator notes "expedited mode" in charter
- Charter produced but lightweight — does not require full charter confirmation
  given stated urgency (offers "Confirm in 30 seconds or I start immediately")
- `hs-competitive-battlecard` runs for Salesforce specifically — not all competitors
- Output includes immediate talk tracks usable in tomorrow's sales call
- `hs-ci-stakeholder-briefing` produces a short exec alert, not a full newsletter
- Brain Section 4 update offered after completion
- Timeline: entire program estimated < 1 hour

**Expected output excludes:**
- Full heavyweight charter process that takes longer than the urgency warrants
- All competitors updated, not just Salesforce
- Full quarterly competitive program run instead of targeted response
- No acknowledgement of the tomorrow timeline

**Pass condition:**
Expedited mode activated, 3-skill sequence runs for Salesforce specifically,
output contains immediately usable talk tracks, and program completes within
the urgency timeline.
