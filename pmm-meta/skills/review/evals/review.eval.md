# review — Eval Suite
**Skill version:** 1.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: Well-built T1 skill passes with 19/19

**Input:**
```
/review pre-mortem
```

**Context:** `pre-mortem` SKILL.md is fully built — all 7 required sections,
operating rules with 10+ items, quality gate with 17 checks, self-improvement loop,
changelog at v2.0.1, frontmatter complete with `context: brain-dependent`,
`quality_gate: true`, description ~400 chars with trigger phrases, under 500 lines.

**Expected output includes:**
- SKILL-SPEC loaded before skill is read — stated explicitly
- Tier identified as T1 before scoring begins
- Score of 18/19 or 19/19 (Q3 evals check flagged as "cannot verify from file")
- Status: PASS
- Q3 specifically noted as "cannot verify — confirm evals/ folder exists in repo"
- No false failures on sections that genuinely exist and are complete
- Fix order section present — noting only Q3 as unverifiable

**Expected output excludes:**
- False failures on sections that exist and are complete
- Score below 17/19 for a well-built T1 skill
- Q3 marked as ✅ Pass without caveat

**Pass condition:**
Score ≥ 17/19, PASS status, Q3 flagged as unverifiable rather than passed
or failed without evidence.

---

## Test Case 2: README-grade skill produces specific fixes

**Input:**
```
/review go-to-market-strategy
```

**Context:** Old `go-to-market-strategy` v1.0.0 — 93 lines, no Trigger section,
no Inputs section, no Pre-flight, no Steps with named steps, no Outputs section,
no Verification, no Do Not Use For, no Operating Rules, no Quality Gate,
no Self-Improvement Loop, no Changelog. Frontmatter has `name`, `description`
but no `metadata.context`, no `version`, no `last_updated`.

**Expected output includes:**
- Tier identified — likely T1 or T2 from context clues despite missing sections
- Score in range 4–7/19
- Status: FAIL — well below 17/19 threshold
- Every ❌ has a specific fix, not "add a Trigger section" — the actual sub-fields
  required (When, Not for, Example prompts) must be stated
- Recommended fix order starts with frontmatter (F4, F5 missing) then missing
  required sections (S1–S7)
- Estimated fix time: L (45+ min) given the scope of gaps
- Offer to run `/fix go-to-market-strategy [check-id]` for copy-paste content

**Expected output excludes:**
- Vague fixes ("add more sections")
- Score above 10/19 for a 93-line README-grade file
- Fix order starting with quality checks before required sections

**Pass condition:**
Score ≤ 10/19, every failure has a specific fix with exact content or format
required, fix order prioritises frontmatter then required sections.

---

## Test Case 3: Tier detection — T3 skill not penalised for missing T1 sections

**Input:**
```
/review writing-assistant
```

**Context:** `writing-assistant` is a T3 utility skill — `quality_gate: false`,
no self-improvement loop, no operating rules. Has all 7 required sections plus
changelog. Frontmatter complete.

**Expected output includes:**
- Tier identified as T3 before scoring begins
- T3 (Self-Improvement Loop) check marked as n/a — not ❌ Fail
- T1 (Operating Rules) check marked as n/a for T3 — not ❌ Fail
- T2 (Quality Gate) check — since `quality_gate: false`, this passes or is n/a
- Score reflects only the checks applicable to T3
- Status: PASS if all T3-applicable checks pass

**Expected output excludes:**
- Operating Rules marked as ❌ Fail for a T3 skill
- Self-Improvement Loop marked as ❌ Fail for a T3 skill
- Score penalised for deliberately omitted T1-only sections

**Pass condition:**
Tier correctly identified as T3, tier-inappropriate checks excluded from scoring,
skill passes on T3-applicable checks.

---

## Test Case 4: /review-all produces summary table

**Input:**
```
/review-all pmm-go-to-market
```

**Context:** `pmm-go-to-market` contains `go-to-market-strategy` (v2.0.0, rebuilt),
`workflow-orchestrator` (v2.0.0, rebuilt), `beachhead-segment` (v1.0.0, new).

**Expected output includes:**
- Summary table with all three skills: name, score, status, top failure
- Each skill scored independently
- Skills sorted by score ascending (lowest first) in recommended fix order
- Count of passing vs failing skills
- "Lowest score" and "recommended first fix" named explicitly
- Q3 flagged as unverifiable for all three (evals folders not verifiable from file)

**Expected output excludes:**
- Missing any of the three skills in the table
- Alphabetical sort instead of score-ascending
- Individual full reports (summary mode only — offer to drill down per skill)

**Pass condition:**
All three skills appear in table, sorted by score ascending, with top failure
per skill and recommended first fix identified.

---

## Test Case 5: /fix generates copy-paste content

**Input:**
```
/fix writing-assistant S1
```

**Context:** `writing-assistant` is missing the `## Trigger` section — S1 fails.
Skill is a T3 writing coach for B2B tech teams.

**Expected output includes:**
- Exact markdown to paste into `writing-assistant` SKILL.md
- Content is skill-specific — not a generic template filled with placeholders
  like "[condition]". It should include actual When, Not for, and Example prompts
  appropriate for a writing assistant skill.
- Location stated: "Add after the H1 opening paragraph, before ## Inputs"
- Instruction to re-run `/review writing-assistant` after adding

**Expected output excludes:**
- Generic template with placeholder text like "When: [condition that fires this skill]"
- Fix that doesn't match the writing-assistant's actual purpose
- Missing location instruction

**Pass condition:**
Fix content is specific to `writing-assistant`, not a generic template, and
includes exact location in the file.

---

## Test Case 6: /diff confirms upgrade landed

**Input:**
```
/diff go-to-market-strategy v1.0.0 v2.0.0
```

**Context:** v1.0.0 was 93 lines, README-grade. v2.0.0 is the rebuilt file
with all sections, commands, quality gate, etc.

**Expected output includes:**
- Checks gained: all 7 required sections (S1–S7), operating rules (T1),
  quality gate (T2), self-improvement loop (T3), changelog (T4), frontmatter
  fields (F1–F5) — listed explicitly
- Checks lost: none (no regression)
- Net change: positive (+N checks)
- New score stated
- No regression flagged

**Expected output excludes:**
- Checks lost listed when there are none (no fabrication)
- New score that doesn't match what a full /review would produce

**Pass condition:**
Checks gained match the actual structural additions between v1 and v2,
no false regressions listed, net change is positive.

---

## Test Case 7: n.v.t. Pre-flight passes correctly

**Input:**
```
/review prioritization-frameworks
```

**Context:** `prioritization-frameworks` is a T3 utility skill. Pre-flight
section exists and contains exactly: `- n.v.t.`

**Expected output includes:**
- S3 (Pre-flight) marked as ✅ Pass — `n.v.t.` is a valid answer
- Not marked as ❌ Fail because it "doesn't have content"
- Operating rule applied: n.v.t. is a deliberate declaration, not an empty section

**Expected output excludes:**
- S3 marked as ❌ Fail because Pre-flight "has no dependency checks"
- S3 marked as ⚠️ Partial because it only says n.v.t.

**Pass condition:**
`n.v.t.` in Pre-flight is treated as a passing answer for S3.
