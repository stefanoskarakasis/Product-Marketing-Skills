---
name: experiment-ideas.eval
version: 1.0.0
description: >
  Eval suite for experiment-ideas skill. Tests: brain context loading,
  no-brain direct-ask fallback, idea differentiation, cost-efficiency
  concreteness, alternatives self-check flagging, and Learning Close
  accuracy against the skill's real four-field session-log shape. 6
  scenarios covering real brainstorm sessions and edge cases.
---

# Experiment-Ideas — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 1, 2, 3, 5) if testing brain loading
2. Populates `/context/meta-patterns.md` with a recurring weak-idea guardrail (if testing guardrail surfacing)
3. Provides product/constraint context, or withholds it to test the no-brain fallback
4. Runs experiment-ideas skill for the given scenario
5. Validates outputs: field completeness, differentiation, concreteness, self-check, ranking, handoff

---

## Eval 1: Brain Context Loading (Step 0)

**Scenario:** `/foundation/brain.md` exists with populated Sections 1 (Product), 2 (ICP), 3 (Alternatives). Skill loads silently and skips re-asking product/ICP/alternatives.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 1: Product Context
Product: Async standup tool for distributed engineering teams

## Section 2: ICP
Current: "Eng managers at 50-200 person remote-first companies"

## Section 3: Alternatives & Positioning
Alternatives: Live standups (status quo), Slack threads (direct), Geekbot (direct)
```

**Expected Output — Context Referenced:**
```
Loaded product, ICP, and alternatives from brain. Only need budget/resource
constraints and channels already tried before I generate ideas.
```

**Pass Criteria:**
- Brain Sections 1–3 loaded silently, stated in one line before Step 1
- Skill does not re-ask for product, ICP, or alternatives already on file
- Only asks for constraint information not already in the brain

---

## Eval 2: No-Brain Direct-Ask Fallback

**Scenario:** No `/foundation/brain.md` exists at all. User asks for growth ideas directly.

**Expected Output — Non-Blocking Surface, Then Direct Ask:**
```
No brain found. I can still generate ideas from what you tell me
directly, but they'll be more generic without ICP and alternatives
context. Continuing.

To get started: what does the product do, who's the target buyer, and
what are they using instead today (even "nothing" counts)?
```

**Pass Criteria:**
- Skill does not block or refuse to proceed without a brain
- Surfaces the no-brain note exactly once, non-blocking
- Falls back to asking for product/ICP/alternatives directly rather than generating generic ideas with no grounding at all

---

## Eval 3: Idea Differentiation

**Scenario:** A draft set of 5 ideas where 3 are variations on the same channel (LinkedIn organic post, LinkedIn thought-leadership article, LinkedIn poll) with substantively the same core message.

**Test Data:**
```
Idea 1: LinkedIn organic post about remote work pain points
Idea 2: LinkedIn thought-leadership article about remote work pain points
Idea 3: LinkedIn poll asking about remote work pain points
Idea 4: Partnership with a remote-work newsletter
Idea 5: Community AMA in a distributed-teams Slack group
```

**Expected Output — Flagged for Regeneration:**
```
Ideas 1–3 are all LinkedIn, all making the same "remote work is hard"
point in different formats — that's one idea wearing three costumes,
not three ideas. Regenerating 1–3 with genuinely different channels or
angles.
```

**Pass Criteria:**
- Skill catches same-channel-same-message duplication rather than delivering all 5 as distinct
- Regenerated ideas use different channels or a materially different angle, not just reworded copy
- Final delivered set has 5 genuinely differentiated ideas, not near-duplicates

---

## Eval 4: Cost-Efficiency Concreteness

**Scenario:** A draft idea with a vague cost-efficiency claim: "low cost because it's organic."

**Expected Output — Rejected and Sharpened:**
```
"Low cost because it's organic" doesn't say anything — organic content
still costs time. Sharpen it: how many hours per week, from whom, using
what you already have on hand? E.g., "no paid spend, ~3 hours/week from
one PMM, reuses existing customer interview transcripts already
collected for the ICP skill."
```

**Pass Criteria:**
- A vague cost-efficiency claim is not accepted and delivered as-is
- Skill asks for or supplies a concrete substitute naming time, people, or reused assets
- Final delivered idea's Cost Efficiency field is concrete, not an assertion

---

## Eval 5: Alternatives Self-Check Flagging

**Scenario:** An idea whose core message could be said, unchanged, by a named status-quo alternative (e.g., "we help you save time" when the status quo alternative already claims exactly that in its own marketing).

**Test Data:**
```
Named alternative: "Live standups (status quo)" — status quo's own marketing/behavior already implies "keep it quick and simple"
Draft idea core message: "Save time with faster standups"
```

**Expected Output — Flagged, Not Silently Delivered:**
```
[GENERIC — doesn't differentiate from status quo] "Save time with faster
standups" — a live-standup advocate would say the exact same thing about
keeping standups short. This needs to name what specifically breaks about
live standups that this product fixes, not just claim speed.
```

**Pass Criteria:**
- An idea indistinguishable from a named alternative's own likely claim is explicitly flagged, not delivered as if it passed
- The flag explains why it fails (what the alternative could equally claim), not a generic "too vague"
- Flagged ideas are either sharpened or clearly marked in the final output — never silently included as if validated

---

## Eval 6: Handoff Completeness and Learning Close

**Scenario:** Full session completes — 5 ideas generated, ranked, one idea (a partnership angle) stands out as clearly highest effort-to-impact.

**Expected Output — Handoff Note:**
```
Strongest candidate for a real test: the newsletter partnership idea —
highest impact-to-effort ratio of the five, and grounded in a real gap
in the alternatives map. Worth taking to experiment-doc to pressure-test
before committing budget. The other four are lower-priority backlog, not
dead — just not this quarter's bet.
```

**Expected Output — Session Log:**
```yaml
skill: experiment-ideas
session_date: 2026-09-01
pattern: "User's initial channel list skewed heavily paid-social despite
  a stated near-zero budget — worth checking whether budget constraints
  need to be asked before channel brainstorming starts, not after."
source: surprised
```

**Pass Criteria:**
- Handoff note explicitly names which idea(s) are strong enough for `experiment-doc`, not left implicit in the ranked list alone
- Lower-ranked ideas are framed as backlog, not silently dropped
- Session logged to `/context/skill-sessions.md` with exactly four fields — no separate memory file written
- No brain write attempted at any point — ideas exist only in chat output and the handoff note
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context loading (Step 0) | Sections 1–3 loaded silently, not re-asked |
| 2 | No-brain fallback | Non-blocking surface, then direct-ask, never refuses |
| 3 | Idea differentiation | Same-channel-same-message duplicates caught and regenerated |
| 4 | Cost-efficiency concreteness | Vague claims rejected, concrete substitutes required |
| 5 | Alternatives self-check | Indistinguishable-from-status-quo ideas explicitly flagged |
| 6 | Handoff + Learning Close | Explicit experiment-doc handoff; real four-field session-log row |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke experiment-ideas with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke experiment-ideas with eval N test data]
# [validate against eval N pass criteria]
```
