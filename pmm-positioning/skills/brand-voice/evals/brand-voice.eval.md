---
name: brand-voice.eval
version: 1.0.0
description: >
  Eval suite for brand-voice skill. Tests: brain context loading, personality
  specificity rejection, no-pre-fill committee mapping, example-required
  Do/Don't discipline, persona-over-channel precedence, voice test
  enforcement, and Learning Close accuracy against the skill's real
  four-field session-log shape. 6 scenarios covering real voice builds
  and audits.
---

# Brand-Voice — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 4) if testing brain loading
2. Populates `/context/skill-sessions.md` with a recent buyer-personas session if testing committee inheritance
3. Provides existing copy samples, or withholds them to test the BUILD intake sequence
4. Runs brand-voice skill for the given scenario
5. Validates outputs: personality specificity, tone-profile completeness, channel precedence, confirmation gating

---

## Eval 1: Brain Context Loading and Buyer-Personas Inheritance (Step 0)

**Scenario:** `/foundation/brain.md` Section 2 has an ICP, and a `buyer-personas` session ran recently (found in `/context/skill-sessions.md`) naming a primary persona and two secondary roles. Skill loads both instead of re-asking who's on the committee.

**Test Data:**
```yaml
# /context/skill-sessions.md
skill: buyer-personas
session_date: 2026-08-29
pattern: "Champion and Economic Buyer were the same person — smaller org."
source: surprised
# (primary persona and committee roles referenced in that session's chat output)
```

**Expected Output — Context Referenced:**
```
Found a recent buyer-personas session — using that committee (Economic
Buyer/Champion combined role, Technical Evaluator) instead of re-asking
who's in the room.
```

**Pass Criteria:**
- Skill checks for a recent `buyer-personas` session before asking Step 2's committee question from scratch
- If found, committee roles are inherited, not re-derived
- If not found, skill falls back to asking directly — doesn't stall waiting for a session that doesn't exist

---

## Eval 2: Personality Specificity Rejection

**Scenario:** User offers brand personality as "innovative and authentic" — the two words the skill's own instructions name as defaults to reject.

**Test Data:**
```
User: "We're innovative and authentic, that's our voice."
```

**Expected Output — Pushback, Not Acceptance:**
```
Every B2B SaaS company says innovative and authentic — a competitor could
claim the exact same two words. Help me get specific: think direct, dry,
warm, irreverent, precise, bold, reassuring, sharp. Which of those — or
something else entirely — actually fits? And name one brand that gets
this tone right, one that gets it wrong.
```

**Pass Criteria:**
- Generic traits are not written into Section 4 as-is
- Pushback explicitly names why they fail (competitor-claimable) and offers concrete alternative vocabulary
- Skill asks for a reference brand before accepting the revised answer

---

## Eval 3: No Pre-Fill on Buying Committee

**Scenario:** No `buyer-personas` session exists and no brain ICP is populated. Skill must ask Step 2's committee questions directly rather than assuming a generic B2B committee (Economic Buyer, Champion, etc.) to save time.

**Expected Output — Direct Ask, No Assumption:**
```
No committee data on file. Who's actually on the buying committee for
this product? For each: role, what they care about professionally, how
they prefer information, what makes them distrust a vendor immediately,
what makes them lean in.
```

**Pass Criteria:**
- Skill does not pre-fill a generic Economic Buyer/Champion/Technical Evaluator template and ask the user to confirm it
- Skill asks the open question and waits for real input
- If the user gives a thin answer (e.g., just titles, no behavior), skill asks a follow-up for the behavioral detail rather than proceeding

---

## Eval 4: Example-Required Do/Don't Discipline

**Scenario:** User gives an abstract tone instruction with no example: "be direct."

**Test Data:**
```
User: "Just tell the writers to be direct."
```

**Expected Output — Challenge for the Example:**
```
"Be direct" won't survive contact with a blank page. Give me the
sentence: what does a non-direct version of a real line look like, and
what's the direct rewrite? E.g., "We don't do X" versus "We may not be
the best fit for X" — which one is you?
```

**Pass Criteria:**
- An abstract Do/Don't is not written into Section 4 without a concrete example attached
- Skill asks for the specific before/after phrasing rather than accepting the abstract instruction as final
- Final Section 4 entry for this trait includes an actual example sentence pair

---

## Eval 5: Persona-Over-Channel Precedence and Voice Test Enforcement

**Scenario:** Channel table and persona tone profile conflict — the channel table says LinkedIn should be "casual and playful," but the primary persona (a CFO-type Economic Buyer) has a tone profile rated formal and careful.

**Test Data:**
```
Channel table: LinkedIn — tone goal: casual, playful
Persona profile: Economic Buyer (CFO) — Formality: Formal, Boldness: Careful
```

**Expected Output — Persona Wins:**
```
Channel table says LinkedIn skews casual, but the Economic Buyer persona
is rated Formal/Careful — persona takes precedence. For content aimed at
this persona on LinkedIn, dial back toward formal even though the channel
default is casual. Voice test check: does "[draft line]" sound like the
same company that would write a formal deck for this same buyer? If not,
it fails.
```

**Pass Criteria:**
- Output explicitly states persona overrides channel default when both apply, per Operating Rule 5
- The one-sentence voice test is applied to the resulting tone choice before it's accepted
- Skill does not silently default to the channel table's tone goal without flagging the conflict

---

## Eval 6: Learning Close and Confirmation Gate

**Scenario:** Full BUILD session completes — personality set, 2 persona tone profiles built, channel table populated for 3 channels, one Do/Don't example still pending from the user.

**Expected Output — Section 4 Write Shown Before Committed:**
```
Here's exactly what Section 4 will read after this write: [full before/after
shown]. One item — the "no jargon" rule — still needs an example before
I include it as a hard Do/Don't; I've left it as a flagged note instead.
Confirm before I save this?
```

**Expected Output — Session Log:**
```yaml
skill: brand-voice
session_date: 2026-08-31
pattern: "Persona/channel tone conflicted on LinkedIn for the Economic
  Buyer — worth checking whether channel defaults need to be persona-
  specific from the start rather than a single table."
source: surprised
```

**Pass Criteria:**
- Section 4 write is shown in full before being committed — no silent write
- An incomplete Do/Don't (missing example) is flagged rather than written as a hard rule without evidence
- Session logged to `/context/skill-sessions.md` with exactly four fields — no separate knowledge/decisions file written
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context + buyer-personas inheritance (Step 0) | Recent committee session loaded, not re-derived |
| 2 | Personality specificity rejection | Generic traits ("innovative and authentic") pushed back on |
| 3 | No pre-fill on committee | Skill asks directly, never assumes a generic committee template |
| 4 | Example-required Do/Don't discipline | Abstract instructions rejected without a concrete example pair |
| 5 | Persona-over-channel precedence + voice test | Persona tone wins conflicts; voice test applied before acceptance |
| 6 | Learning Close + confirmation gate | Section 4 shown before write; incomplete items flagged not hard-coded; real four-field session-log row |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke brand-voice with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke brand-voice with eval N test data]
# [validate against eval N pass criteria]
```
