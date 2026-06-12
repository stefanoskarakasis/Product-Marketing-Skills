---
skill: product-marketing-context
version: 2.3.0
eval_version: 1.0.0
last_updated: 2026-06-12
author: Stefanos Karakasis
---

# Evals — product-marketing-context

Scenario-based eval file for `product-marketing-context` v2.3.0. Each scenario
states a starting condition, an input, and the exact behaviour the skill must
produce to pass.

**How to use this file:**
1. Set up the starting condition (file state, prior messages) as described.
2. Send the input to a Claude session with this skill active.
3. Check the output against the Pass criteria. Every criterion must be met.
4. Mark ✅ PASS or ❌ FAIL. Log failures with the observed output.

**Scoring threshold:** 32/37 scenarios must pass (86%) for the skill to be
considered production-ready. Below that, identify the failing category and fix
the operating rule or step that governs it.

**Update cadence:** Add new scenarios whenever a user reports unexpected behaviour.
Promote edge cases to core scenarios after they appear twice.

---

## Category A — Routing and Trigger Detection (6 scenarios)

These confirm the skill fires for the right prompts and routes away correctly
for prompts that belong to other skills.

---

### A1 — First-run trigger: no brain present
**ID:** `routing-brain-missing-first-run`
**Starting condition:** `/foundation/brain.md` does not exist. No `.agents/` legacy files.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] First-run hook message appears BEFORE any wizard question
- [ ] Message explains what brain.md does for downstream skills
- [ ] At least two downstream skills named (e.g. `hs-positioning-messaging`, `go-to-market-strategy`)
- [ ] Three options offered: [Yes, let's build it] [Not now] [I have old files to migrate]
- [ ] No wizard question (Q1: What's your product called?) appears in this first response

---

### A2 — Brain-exists routing: no wizard auto-launch
**ID:** `routing-brain-exists-no-wizard`
**Starting condition:** `/foundation/brain.md` exists and is populated.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Skill offers [View current] [Edit sections] [Rebuild from scratch]
- [ ] First-run hook does NOT appear
- [ ] Wizard does NOT auto-launch
- [ ] No wizard question asked in this response

---

### A3 — Audit trigger routes correctly
**ID:** `routing-audit-trigger`
**Starting condition:** `/foundation/brain.md` exists.
**Input:** `"Check brain health"`
**Pass criteria:**
- [ ] Skill loads brain silently
- [ ] Offers current state summary or health check options
- [ ] Does NOT restart the wizard
- [ ] Does NOT show the first-run hook

---

### A4 — Single-section update routes directly
**ID:** `routing-single-section-update`
**Starting condition:** `/foundation/brain.md` exists.
**Input:** `"Update my ICP"`
**Pass criteria:**
- [ ] Skill goes directly to Section 2 (ICP) questions
- [ ] Does NOT re-run Section 1 questions first
- [ ] Does NOT re-run Sections 3–6

---

### A5 — Wrong-skill routing: battlecard request
**ID:** `routing-wrong-skill-battlecard`
**Starting condition:** Any state.
**Input:** `"Help me build a competitive battlecard"`
**Pass criteria:**
- [ ] Skill routes to `hs-competitive-battlecard`
- [ ] Brain wizard does NOT start
- [ ] Explanation given for why this is the correct skill

---

### A6 — Wrong-skill routing: positioning copy request
**ID:** `routing-wrong-skill-positioning`
**Starting condition:** Any state.
**Input:** `"Write me positioning copy for our homepage"`
**Pass criteria:**
- [ ] Skill routes to `hs-positioning-messaging`
- [ ] Brain wizard does NOT start
- [ ] Note that positioning skill reads from brain (creating urgency to build brain first if missing)

---

## Category B — First-Run Hook / Ramp Glass Pattern (3 scenarios)

These confirm the Glass principle: show value before asking for effort.

---

### B1 — Value shown before wizard starts
**ID:** `hook-value-before-effort`
**Starting condition:** No brain exists. First time this skill is triggered.
**Input:** `"Set up my GTM foundation"`
**Pass criteria:**
- [ ] Response explains WHAT brain.md does — not just THAT it exists
- [ ] At least two specific downstream skills named with what they use the brain for
- [ ] The phrase "15 minutes" or equivalent time estimate appears
- [ ] "You do it once" or equivalent permanence signal appears
- [ ] Zero wizard questions in this first response

---

### B2 — Three options always offered on first run
**ID:** `hook-three-options-offered`
**Starting condition:** No brain exists.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Option 1 present: start wizard / yes / let's build it (any equivalent)
- [ ] Option 2 present: not now / remind me later / decline (any equivalent)
- [ ] Option 3 present: I have old files / migrate (any equivalent)
- [ ] No option forces the user to start if they don't want to

---

### B3 — Hook suppressed when brain already exists
**ID:** `hook-suppressed-on-return`
**Starting condition:** `/foundation/brain.md` exists from a prior session.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] First-run hook message absent
- [ ] Skill immediately acknowledges the existing brain
- [ ] Offers [View / Edit / Rebuild] in the same response

---

## Category C — Wizard Flow and Validation (8 scenarios)

These confirm section-by-section flow, confirmation gates, and specificity enforcement.

---

### C1 — Section confirmation gate
**ID:** `wizard-section-confirm-before-next`
**Starting condition:** No brain. User has started wizard and answered all 5 Section 1 questions.
**Input:** User provides `product_name`, `product_description`, `product_stage`, `target_market`, `value_proposition`.
**Pass criteria:**
- [ ] Skill shows all 5 answers back in a summary
- [ ] Asks "Look good? (yes / edit / skip for now)" or equivalent
- [ ] Does NOT proceed to Section 2 until user confirms
- [ ] Section 2 Q1 does NOT appear in the same response as the confirmation

---

### C2 — Vague ICP answer rejected
**ID:** `wizard-vague-icp-rejected`
**Starting condition:** Wizard is on Section 2, Q1 (company size).
**Input:** `"Small to medium businesses"`
**Pass criteria:**
- [ ] Skill does NOT accept this answer and write it to brain
- [ ] Skill pushes back asking for specific numbers (employee count or ARR range)
- [ ] Provides an example of an acceptable answer (e.g. "50–500 employees" or "$5M–$50M ARR")
- [ ] Does not move to Q2 until a specific answer is given

---

### C3 — Vague value proposition rejected
**ID:** `wizard-vague-value-prop-rejected`
**Starting condition:** Wizard is on Section 1, Q5 (value proposition).
**Input:** `"We help companies grow faster"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Prompts user to fill in the template structure: "[Product] helps [target market] to _____ so they can _____"
- [ ] Explains why specificity matters (links output quality)
- [ ] Does not advance until structure is followed

---

### C4 — Skip accepted without force
**ID:** `wizard-skip-accepted`
**Starting condition:** Wizard is on Section 4 (Voice & Tone) confirmation.
**Input:** `"Skip for now"`
**Pass criteria:**
- [ ] Skill accepts the skip without pushback
- [ ] Section marked as incomplete (not as Placeholder or error state)
- [ ] Skill continues to Section 5
- [ ] Skill does NOT re-ask the section or guilt the user

---

### C5 — Edit mid-wizard re-runs only that section
**ID:** `wizard-edit-single-section`
**Starting condition:** Wizard has shown Section 2 confirmation summary.
**Input:** `"Edit"`
**Pass criteria:**
- [ ] Skill returns to Section 2, Q1
- [ ] Does NOT restart from Section 1
- [ ] Does NOT jump to Section 3

---

### C6 — Partial state saved on quit
**ID:** `wizard-partial-state-save`
**Starting condition:** Wizard running. User has confirmed Sections 1 and 2.
**Input:** `"Stop for now, I'll come back later"` (or equivalent quit signal)
**Pass criteria:**
- [ ] Skill acknowledges the pause and confirms progress is saved
- [ ] Mentions `/foundation/.brain-draft.md` or equivalent save location
- [ ] Tells user how to resume (run skill again)
- [ ] Does NOT write `/foundation/brain.md` from incomplete answers

---

### C7 — Resume from draft on restart
**ID:** `wizard-resume-from-draft`
**Starting condition:** `/foundation/.brain-draft.md` exists with Sections 1–2 completed, stopped at Section 3 Q1.
**Input:** `"Build my brain"` (new session)
**Pass criteria:**
- [ ] Skill detects the draft file
- [ ] Offers to resume from where the user left off (not restart)
- [ ] Names the section and question number where they stopped
- [ ] Does NOT start from Section 1 Q1

---

### C8 — Brain written only after all confirmations
**ID:** `wizard-brain-written-after-confirm`
**Starting condition:** Wizard running. User has just confirmed Section 6 (Proof Points).
**Input:** `"Yes, that looks good"` (Section 6 confirmation)
**Pass criteria:**
- [ ] `/foundation/brain.md` written with all 31 variables populated
- [ ] `/foundation/.brain-draft.md` deleted (or noted as deleted)
- [ ] Success confirmation message shown (includes brain file path)
- [ ] Step 9 routing question asked in the same or immediately following response
- [ ] No blank or TBD values in the written brain file

---

## Category D — Legacy Migration (3 scenarios)

---

### D1 — Legacy files detected and offered for migration
**ID:** `legacy-detection-prompt`
**Starting condition:** No `/foundation/brain.md`. `.agents/icp.md` and `.agents/alternatives-map.md` exist.
**Input:** `"Build my brain"`
**Pass criteria:**
- [ ] Skill detects legacy files and names them
- [ ] Offers [Yes, migrate] [No, start fresh] — not auto-migrating
- [ ] First-run hook still shown (value statement), migration offer follows
- [ ] Wizard does NOT start before user chooses an option

---

### D2 — Migration confirms field-by-field
**ID:** `legacy-migration-field-confirm`
**Starting condition:** User has chosen "Yes, migrate" from D1.
**Input:** `"Yes, migrate the old files"`
**Pass criteria:**
- [ ] Skill extracts fields from old files and shows them one section at a time
- [ ] User is asked to confirm each extracted value before it's accepted
- [ ] Skill does NOT write brain.md until all confirmations are received
- [ ] User can correct any extracted value before it's written

---

### D3 — Legacy files not deleted after migration
**ID:** `legacy-files-preserved`
**Starting condition:** Migration completed successfully. brain.md written.
**Input:** (Check output state after migration completes)
**Pass criteria:**
- [ ] `.agents/` legacy files still exist — not deleted
- [ ] Skill confirms or notes that old files are preserved
- [ ] No instruction to delete old files is given

---

## Category E — Post-Setup Routing / Step 9 (9 scenarios)

These confirm the skill always routes after setup and maps focus to the correct skills.

---

### E1 — Routing always runs after full setup
**ID:** `routing-always-after-setup`
**Starting condition:** User has just completed a full brain build (all 6 sections).
**Input:** Brain confirmation accepted (`"Yes"`)
**Pass criteria:**
- [ ] Step 9 routing question asked in the same response or immediately after
- [ ] Question offers the 6 focus options
- [ ] Not skipped even if brain was already partly populated

---

### E2 — Path 1: Launch
**ID:** `routing-path-launch`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Launching a product or feature"` (or option 1)
**Pass criteria:**
- [ ] `go-to-market-strategy` surfaced with description
- [ ] `hs-pre-mortem` surfaced with description
- [ ] `hs-gaccs-brief` surfaced with description
- [ ] No unrelated skills added (e.g. not hs-brainstorm-okrs)

---

### E3 — Path 2: Positioning
**ID:** `routing-path-positioning`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Fixing or refreshing our positioning"` (or option 2)
**Pass criteria:**
- [ ] `hs-positioning-messaging` surfaced
- [ ] `hs-alternatives-map` surfaced
- [ ] `hs-value-prop-statements` surfaced

---

### E4 — Path 3: Competitive
**ID:** `routing-path-competitive`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Building competitive intelligence"` (or option 3)
**Pass criteria:**
- [ ] `hs-competitive-battlecard` surfaced
- [ ] `hs-ci-stakeholder-briefing` surfaced
- [ ] `hs-alternatives-map` surfaced

---

### E5 — Path 4: Buyers
**ID:** `routing-path-buyers`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Understanding our buyers better"` (or option 4)
**Pass criteria:**
- [ ] `hs-buyer-personas` surfaced
- [ ] `hs-icp` surfaced
- [ ] `hs-interview-summary` surfaced

---

### E6 — Path 5: Sales enablement
**ID:** `routing-path-sales`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Enabling the sales team"` (or option 5)
**Pass criteria:**
- [ ] `hs-value-prop-statements` surfaced
- [ ] `hs-competitive-battlecard` surfaced
- [ ] `hs-stakeholder-maps` surfaced

---

### E7 — Path 6: Quarterly planning
**ID:** `routing-path-quarterly`
**Starting condition:** Step 9 question has been shown.
**Input:** `"Planning the quarter"` (or option 6)
**Pass criteria:**
- [ ] `hs-brainstorm-okrs` surfaced
- [ ] `workflow-orchestrator` surfaced
- [ ] `hs-prioritization-frameworks` surfaced

---

### E8 — Senior/VP uplift
**ID:** `routing-senior-uplift`
**Starting condition:** Step 9 question shown. User has indicated VP or team-lead context earlier in session.
**Input:** Any path choice (e.g. option 1)
**Pass criteria:**
- [ ] `workflow-orchestrator` surfaced in addition to path skills
- [ ] `hs-ci-stakeholder-briefing` surfaced in addition to path skills
- [ ] Path-specific skills still listed (not replaced by senior additions)

---

### E9 — Routing also runs after single-section edit
**ID:** `routing-after-edit`
**Starting condition:** User edited only Section 2 ICP (not a full rebuild).
**Input:** Section 2 confirmation accepted
**Pass criteria:**
- [ ] Step 9 routing question asked after the edit completes
- [ ] Not skipped just because it was an edit, not a full build

---

## Category F — Brain File Quality (5 scenarios)

---

### F1 — No placeholders in written brain
**ID:** `quality-no-placeholders`
**Starting condition:** Full wizard completed with all sections confirmed.
**Input:** (Check brain.md after write)
**Pass criteria:**
- [ ] brain.md contains no empty fields
- [ ] brain.md contains no "TBD", "Placeholder", or "[fill in]" text
- [ ] All 31 variables have non-empty values

---

### F2 — Alternatives stored as named products
**ID:** `quality-alternatives-named`
**Starting condition:** Wizard on Section 3 Q1 (alternatives).
**Input:** `"Salesforce, HubSpot, and manual spreadsheets"`
**Pass criteria:**
- [ ] Stored as-is: Salesforce, HubSpot, manual spreadsheets
- [ ] Not normalised to "enterprise CRM" or "legacy tools"
- [ ] Status quo (manual spreadsheets) recorded separately as `alternatives_status_quo`

---

### F3 — Vague alternatives rejected
**ID:** `quality-vague-alternatives-rejected`
**Starting condition:** Wizard on Section 3 Q1 (alternatives).
**Input:** `"The big CRMs and some spreadsheets"`
**Pass criteria:**
- [ ] Skill rejects this answer
- [ ] Asks for named products buyers actually compare you to
- [ ] Provides example of acceptable format (e.g. "Salesforce, HubSpot, Pipedrive")

---

### F4 — Unquantified proof point rejected
**ID:** `quality-proof-point-quantified`
**Starting condition:** Wizard on Section 6 Q1 (metrics).
**Input:** `"High customer retention rate"`
**Pass criteria:**
- [ ] Skill rejects "high" as non-specific
- [ ] Asks for a number with a source (e.g. "89% retention rate, internal dashboard Q4 2025")
- [ ] Does not proceed until a number is provided

---

### F5 — Direct edit attempt redirected
**ID:** `quality-no-direct-edit`
**Starting condition:** Brain exists. User asks about editing directly.
**Input:** `"Can I just edit brain.md directly in my text editor?"`
**Pass criteria:**
- [ ] Skill does NOT say "yes, go ahead"
- [ ] Redirects to `--edit-section [1-6]` wizard flow or equivalent
- [ ] Explains why direct edits bypass validation

---

## Category G — Edge Cases (3 scenarios)

---

### G1 — Foundation directory created if missing
**ID:** `edge-foundation-dir-missing`
**Starting condition:** No `/foundation/` directory exists at all.
**Input:** User completes full wizard and confirms all sections.
**Pass criteria:**
- [ ] Skill creates `/foundation/` directory before writing brain.md
- [ ] No error thrown about missing directory
- [ ] brain.md written successfully

---

### G2 — Placeholder section flagged before skill runs
**ID:** `edge-placeholder-section-flagged`
**Starting condition:** brain.md exists. Section 3 (Alternatives) is marked as Placeholder or empty.
**Input:** Another skill (e.g. hs-competitive-battlecard) triggers and reads brain.
**Pass criteria:**
- [ ] Skill flags Section 3 as incomplete before the dependent skill runs
- [ ] Warning includes which skill is affected and why
- [ ] Dependent skill is not blocked — user can proceed but is warned

---

### G3 — "Not now" exits gracefully
**ID:** `edge-not-now-graceful-exit`
**Starting condition:** No brain exists. First-run hook shown with three options.
**Input:** `"Not now — remind me later"` (or option 2)
**Pass criteria:**
- [ ] Skill exits cleanly without starting the wizard
- [ ] No guilt message or repeated prompt
- [ ] Simple acknowledgement: how to restart when ready
- [ ] Session ends without /foundation/brain.md being written

---

## Eval Log

Use this table to track runs. Update after each eval session.

| Run date | Version | Scenarios passed | Scenarios failed | Failed IDs | Notes |
|---|---|---|---|---|---|
| 2026-06-12 | v2.3.0 | — | — | — | Initial eval file created — not yet run |

---

## Known Gaps (add as discovered)

| Gap ID | Description | Scenario to add | Priority |
|---|---|---|---|
| — | — | — | — |

---

## Changelog

### v1.0.0 — 2026-06-12
Initial eval file. 37 scenarios across 7 categories: Routing (6), First-Run Hook (3),
Wizard Flow (8), Legacy Migration (3), Post-Setup Routing (9), Brain File Quality (5),
Edge Cases (3). Threshold set at 32/37 (86%).
