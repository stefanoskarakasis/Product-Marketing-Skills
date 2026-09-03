---
name: buyer-personas.eval
version: 1.0.0
description: >
  Eval suite for buyer-personas skill. Tests: brain context loading, no-data
  intake sequencing, committee role identification by behavior, confidence
  tagging discipline, quality gate enforcement, persona-alternatives
  anchoring, handoff completeness, and Learning Close accuracy against the
  skill's real four-field session-log shape. 7 scenarios covering real
  committee-mapping sessions and edge cases.
---

# Buyer-Personas — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 2, 3) if testing brain loading
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Provides research data, or withholds it to test the intake sequence
4. Runs buyer-personas skill for the given scenario
5. Validates outputs: role identification accuracy, confidence tagging, gate enforcement, handoff completeness

---

## Eval 1: Brain Context Loading (Step 0)

**Scenario:** `/foundation/brain.md` exists with populated Sections 2 (ICP) and 3 (Alternatives). Skill loads silently and uses this instead of re-asking.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Current: "Mid-market B2B SaaS, 50–500 employees, VP Ops economic buyer"

## Section 3: Alternatives & Positioning
Alternatives: Manual spreadsheets (status quo), Competitor X (direct), building in-house
```

**Expected Output — Context Referenced:**
```
Loaded ICP and alternatives from brain. No prior guardrails fired.
Economic Buyer assumption: VP Ops (from brain Section 2) — will confirm against this session's signals.
```

**Pass Criteria:**
- Brain Sections 2–3 loaded silently, stated in one line before intake
- Skill does not re-ask for information already in the brain
- Named alternatives from Section 3 are used to anchor personas in Step 3 rather than re-derived from scratch

---

## Eval 2: No-Data Intake Sequence (Step 1)

**Scenario:** No brain exists, no research data provided. User says "help me figure out who I need to win over."

**Expected Output — Single-Message Intake:**
```
1. What does your product do, and who's the primary buyer title?
2. What's your typical deal size and sales-cycle length?
3. What does a lost deal usually look like — who said no, and why?
4. What does a won deal look like — who pushed it through internally?
5. Who else shows up during procurement or a security review?
```

**Pass Criteria:**
- All 5 questions asked in a single message — not drip-fed one at a time
- Skill does not proceed to Step 2 until questions 1, 3, and 4 are answered
- If only questions 1 and 2 are answered, skill asks again for 3 and 4 rather than guessing

---

## Eval 3: Role Identification by Behavior, Not Title

**Scenario:** Research data includes a contact titled "IT Manager" who requests SSO/SAML specs and security questionnaires, and a contact titled "VP Marketing" who shares the company's deck internally and introduces the skill user to two other stakeholders unprompted.

**Test Data:**
```
Contact A — "IT Manager" — requested architecture docs, SSO/SAML integration specs, security questionnaire
Contact B — "VP Marketing" — shared product one-pager with 3 colleagues, introduced user to Economic Buyer without being asked
```

**Expected Output — Roles by Behavior:**
```
| Role | Likely Title(s) | Signal |
|---|---|---|
| Technical Evaluator / Blocker | IT Manager | Requested SSO/SAML specs, security questionnaire — classic evaluator signal, not necessarily a title match |
| Champion | VP Marketing | Shared collateral internally, initiated intro unprompted — champion signal regardless of title seniority |
```

**Pass Criteria:**
- Contact A correctly identified as Technical Evaluator based on behavior, not assumed from "IT Manager" title alone
- Contact B correctly identified as Champion based on behavior (unprompted sharing, intro-making), not dismissed for a marketing title
- Output explicitly separates "likely title" from the behavioral signal that drove role assignment

---

## Eval 4: Confidence Tagging Discipline

**Scenario:** Mixed-confidence input — one quote directly from a transcript, one inference from deal pattern, one claim with no supporting evidence at all.

**Test Data:**
```
Transcript quote: "We need SOC 2 before we can even start a pilot" — Technical Evaluator, direct quote
Inference: Deal stalled 3 weeks after being "sent to legal" with no explanation — inferred Procurement is a blocker
No evidence: Assumption that the End User cares primarily about time savings (never asked, no data)
```

**Expected Output — Tagged Claims:**
```
[CONFIRMED] Technical Evaluator requires SOC 2 before pilot — direct quote
[INFERRED] Procurement is a blocker in this deal — 3-week stall after "sent to legal," no direct confirmation
[HYPOTHESIS] End User's primary motivator is time savings — no supporting data, needs validation
```

**Pass Criteria:**
- All three claims carry the correct tag — no blending into unqualified prose
- `[HYPOTHESIS]` claims are explicitly flagged as needing validation, not stated as fact
- The persona card language reflects the tag — confident phrasing for CONFIRMED, hedged for INFERRED, explicitly flagged for HYPOTHESIS

---

## Eval 5: Quality Gate Enforcement

**Scenario A — should block:** Research data only surfaces an End User and a Technical Evaluator; no Economic Buyer or Champion identifiable from any source. No named alternatives given.

**Scenario B — should proceed:** At least one Champion identified, alternatives named (even if brain-sourced).

**Expected Output — Scenario A:**
```
Cannot proceed to persona building: no Economic Buyer or Champion identified from available signals, and named alternatives are unknown.
Before I build personas, I need at least one of: who approves budget, or who's actively advocating for you internally. And what would this buyer do if you didn't exist — a direct competitor, an internal build, or nothing at all?
```

**Pass Criteria:**
- Scenario A: skill explicitly stops and asks rather than fabricating an Economic Buyer or Champion from thin signals
- Scenario A: the specific missing gate criteria are named, not a generic "need more info"
- Scenario B: skill proceeds without unnecessary friction once the minimum bar is met

---

## Eval 6: Persona-Alternatives Anchoring (Competitor-Swap Test)

**Scenario:** Draft persona card produced without a named alternative — generic pain language that could apply to any B2B tool.

**Test Data (should fail the swap test):**
```
### Pains
1. Struggles with inefficient processes
2. Wants better visibility into operations
3. Needs to save time
```

**Test Data (should pass):**
```
### Named Alternatives
Manual spreadsheets (status quo), Competitor X (direct)

### Pains (tied to named alternatives)
1. Spreadsheet version conflicts cause weekly reporting errors → made worse by manual spreadsheets
2. Competitor X's dashboard requires a dedicated analyst to maintain → made worse by Competitor X
```

**Pass Criteria:**
- The generic version is rejected or flagged during self-review — pains not tied to a named alternative don't ship as-is
- The anchored version passes: each pain names what makes the specific alternative worse, not a category-level complaint
- Skill applies the competitor-swap test explicitly before finalizing persona cards (per Step 3's exit check)

---

## Eval 7: Handoff Completeness and Learning Close (Steps 4–5)

**Scenario:** Full session completes — committee mapped, 2 personas built (Economic Buyer, Champion), one persona still carries a `[HYPOTHESIS]` tag.

**Expected Output — Handoff Note:**
```
Primary buyer for top-of-funnel messaging: Economic Buyer (VP Ops).
1 persona needs separate sales enablement content: Technical Evaluator (security-focused collateral).
Still [HYPOTHESIS], don't let these drive final copy yet: End User's primary motivator (time savings, unvalidated).
```

**Expected Output — Session Log:**
```yaml
skill: buyer-personas
session_date: 2026-08-29
pattern: "Champion and Economic Buyer were the same person in this deal — smaller org than usual, worth checking whether that collapses the committee below 200 employees as a pattern."
source: surprised
```

**Pass Criteria:**
- Handoff note explicitly states the primary persona, which need separate content, and which claims are still unvalidated — not left implicit in the persona cards alone
- Session logged to `/context/skill-sessions.md` with exactly four fields (`skill`, `session_date`, `pattern`, `source`) — no separate knowledge/decisions file written
- No brain write attempted at any point in the session — the committee map and personas exist only in chat output and the handoff note
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context loading (Step 0) | ICP and alternatives loaded silently, not re-asked |
| 2 | No-data intake sequence (Step 1) | 5 questions in one message; blocks on 1/3/4 unanswered |
| 3 | Role identification by behavior | Roles assigned from behavioral signal, not title alone |
| 4 | Confidence tagging discipline | CONFIRMED/INFERRED/HYPOTHESIS applied correctly, never blended |
| 5 | Quality gate enforcement | Blocks without Economic Buyer + Champion + named alternatives |
| 6 | Persona-alternatives anchoring | Competitor-swap test applied; generic pains rejected |
| 7 | Handoff completeness + Learning Close | Explicit handoff note; real four-field session-log row; no brain write |

---

## Running Evals

```bash
# Run all evals
for i in {1..7}; do
  echo "Running eval $i..."
  # [invoke buyer-personas with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke buyer-personas with eval N test data]
# [validate against eval N pass criteria]
```
