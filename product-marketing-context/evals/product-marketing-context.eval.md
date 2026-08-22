---
skill: product-marketing-context
version: 3.0.0
eval_version: 2.0.0
last_updated: 2026-08-22
author: Stefanos Karakasis
---

# Evals — product-marketing-context

Scenario-based eval file for `product-marketing-context`, testing the skill's
real 5-step flow: detect brain state, run the wizard, write the brain file,
run a health audit, and route without naming unverified downstream skills.

**How to use this file:**
1. Set up the starting condition (file state, prior messages) as described.
2. Send the input to a Claude session with this skill active.
3. Check the output against the Pass criteria. Every criterion must be met.
4. Mark ✅ PASS or ❌ FAIL. Log failures with the observed output.

**Scoring threshold:** 15/17 scenarios must pass (88%) for the skill to be
considered production-ready. Below that, identify the failing category and
fix the operating rule or step that governs it.

---

## Category A — Brain State Detection (Step 1) (4 scenarios)

### A1 — No brain: explains value in one line before the wizard starts
**ID:** `state-no-brain-first-run`
**Starting condition:** `/foundation/brain.md` does not exist. No `.agents/` or `.claude/` legacy files.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Response explains in one line what the brain does for downstream skills
- [ ] Wizard starts from Section 1 in the same response or immediately after
- [ ] No fabricated "downstream skill" is named unless the skill has genuinely verified it reads this brain's section structure (per Operating Rule 4)

---

### A2 — Brain exists: offers view/edit/audit, doesn't restart
**ID:** `state-brain-exists`
**Starting condition:** `/foundation/brain.md` exists and all 6 sections are populated.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Existing sections are loaded silently, not re-asked
- [ ] Offers [View current] [Edit a section] [Run health audit]
- [ ] Wizard does not auto-launch from Section 1

---

### A3 — Legacy files detected and offered for migration
**ID:** `state-legacy-detected`
**Starting condition:** No `/foundation/brain.md`. `.agents/icp.md` exists.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Legacy file is named specifically, not just "old files found"
- [ ] Offers to migrate, showing each extracted value before writing anything
- [ ] Does not write `/foundation/brain.md` until extracted values are confirmed
- [ ] Legacy file itself is not deleted after migration

---

### A4 — Audit trigger loads silently, doesn't restart wizard
**ID:** `state-audit-trigger`
**Starting condition:** `/foundation/brain.md` exists.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] Skill loads brain silently
- [ ] Runs the Step 4 health audit rather than starting the wizard
- [ ] Does not re-ask any already-answered question

---

## Category B — The Wizard (Step 2) (5 scenarios)

### B1 — Section confirmation gate
**ID:** `wizard-section-confirm-before-next`
**Starting condition:** No brain. User has answered all 5 Section 1 (Product Context) questions.
**Input:** Product name, description, stage, target market, value proposition.
**Pass criteria:**
- [ ] Skill shows all 5 answers back in a summary
- [ ] Asks "Look good? (yes / edit / skip)" or equivalent
- [ ] Does not proceed to Section 2 until the user confirms

---

### B2 — Vague ICP company size rejected
**ID:** `wizard-vague-company-size-rejected`
**Starting condition:** Wizard is on Section 2 (ICP), company size question.
**Input:** `"Small to medium businesses"`
**Pass criteria:**
- [ ] Skill does not accept and store this answer
- [ ] Pushes back asking for specific numbers (employee count or ARR range)
- [ ] Does not move to the next question until a specific answer is given

---

### B3 — Vague value proposition rejected
**ID:** `wizard-vague-value-prop-rejected`
**Starting condition:** Wizard is on Section 1, value proposition question.
**Input:** `"We help companies grow faster"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Prompts the user to use the structure: "[Product] helps [target market] to __ so they can __"
- [ ] Does not advance until the structure is followed

---

### B4 — Vague alternatives rejected, named products required
**ID:** `wizard-vague-alternatives-rejected`
**Starting condition:** Wizard is on Section 3 (Alternatives & Positioning).
**Input:** `"The big CRMs and some spreadsheets"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Asks for named products buyers actually compare the user to (e.g. "Salesforce, HubSpot, Pipedrive")
- [ ] Once named, alternatives are stored as-is — not normalised into a category label

---

### B5 — Skip accepted without pushback
**ID:** `wizard-skip-accepted`
**Starting condition:** Wizard is on Section 4 (Voice & Tone) confirmation.
**Input:** `"Skip for now"`
**Pass criteria:**
- [ ] Skill accepts the skip without guilt or repeated prompting
- [ ] Section is marked incomplete, not silently filled with a placeholder
- [ ] Skill continues to Section 5

---

## Category C — Writing the Brain File (Step 3) (3 scenarios)

### C1 — Brain written only after confirmation, using the real template
**ID:** `write-only-after-confirm`
**Starting condition:** Wizard running. User has just confirmed Section 6 (Proof Points), the last section.
**Input:** `"Yes, that looks good"`
**Pass criteria:**
- [ ] `/foundation/brain.md` is written using `templates/brain-template.md`
- [ ] All confirmed sections have real values — no `[Needs input]` left in a section the user completed
- [ ] Any `.brain-draft.md` marker from a prior partial session is cleared

---

### C2 — Partial exit leaves a usable partial brain, not a blocked state
**ID:** `write-partial-on-exit`
**Starting condition:** Wizard running. User has confirmed Sections 1 and 2.
**Input:** `"Stop for now, I'll come back later"`
**Pass criteria:**
- [ ] Skill confirms progress is saved and names how to resume
- [ ] A partial, usable brain (or draft marker) exists for the confirmed sections
- [ ] Skill does not write incomplete/unconfirmed sections as if they were final

---

### C3 — Resume picks up from the correct section
**ID:** `write-resume-from-draft`
**Starting condition:** A draft/partial state exists with Sections 1–2 confirmed, stopped before Section 3.
**Input:** `"Build my brain"` (new session)
**Pass criteria:**
- [ ] Skill detects the partial state and offers to resume, not restart
- [ ] Names the section where the user left off
- [ ] Does not re-ask Section 1 or 2 questions

---

## Category D — Health Audit (Step 4) (3 scenarios)

### D1 — All 6 sections scored, with concrete fixes for gaps
**ID:** `audit-full-scoring`
**Starting condition:** Brain exists with a mix of specific and generic answers across sections.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] All 6 sections (Product Context, ICP, Alternatives & Positioning, Voice & Tone, Market Context, Proof Points) are scored 0–100
- [ ] Sections scoring below 50 get one concrete, specific fix — not "needs more detail"
- [ ] Skill offers to jump straight into editing the weakest section

---

### D2 — Generic field flagged even if technically non-empty
**ID:** `audit-generic-field-flagged`
**Starting condition:** Brain exists. ICP company size field literally contains "businesses of various sizes."
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] This field is flagged as a gap despite being non-empty
- [ ] Score reflects genericness, not just presence of a value
- [ ] Fix suggested asks for a specific number/range

---

### D3 — Unquantified proof point flagged
**ID:** `audit-unquantified-proof-point`
**Starting condition:** Brain exists. Section 6 contains "High customer retention rate" with no number or source.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] Proof Points section score reflects the missing quantification
- [ ] Fix suggests a specific number with a source (e.g. "89% retention, internal dashboard Q4 2025")

---

## Category E — Routing and Downstream Naming (Step 5) (2 scenarios)

### E1 — Downstream skill named only if genuinely verified (Edge case)
**ID:** `routing-only-verified-skills-named`
**Starting condition:** Full brain build just completed.
**Input:** Brain confirmation accepted (`"Yes"`)
**Pass criteria:**
- [ ] Skill states plainly that the brain is ready and other skills will read from it
- [ ] Does not name a specific downstream skill unless it has been verified in this session to read the brain's real section structure correctly — per Operating Rule 4
- [ ] If no skill is named, that's a pass, not a gap — an unverified name is a broken promise, not a helpful suggestion

---

### E2 — Wrong-skill request routed without brain wizard hijacking it
**ID:** `routing-wrong-skill-request`
**Starting condition:** Any state.
**Input:** `"Help me build a competitive battlecard"`
**Pass criteria:**
- [ ] The brain wizard does not start in response to this request
- [ ] Skill does not claim to handle competitive battlecard output itself

---

## Eval Log

Use this table to track runs. Update after each eval session.

| Run date | Version | Scenarios passed | Scenarios failed | Failed IDs | Notes |
|---|---|---|---|---|---|
| 2026-08-22 | v3.0.0 | — | — | — | Eval file fully rewritten against the real 5-step SKILL.md — the prior 37-scenario version tested a first-run-hook/wizard/migration/Step-9-routing design that no longer exists in SKILL.md, and used skill names from an old naming convention throughout |

---

## Known Gaps (add as discovered)

| Gap ID | Description | Scenario to add | Priority |
|---|---|---|---|
| — | — | — | — |
