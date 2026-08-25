# pmm-okrs Evals

## Eval 1: Guardrails surface before intake
**Scenario:** User starts `/build` for Q3. `/context/meta-patterns.md` contains "confidence too high 2x, external dependencies blocked 1x"
**Expected:** Guardrail prompt surfaces before Step 1 intake
**Input:** `/build Q3 2026 for 3-person PMM team`
**Output check:** 
- Does guardrail appear? YES/NO
- Does guardrail match pattern from meta-patterns? YES/NO
- Can user skip guardrail? YES/NO

## Eval 2: Confidence calibration recommended
**Scenario:** `/context/skill-sessions.md` shows Q2: predicted 75%, achieved 78%
**Expected:** Step 1 surfaces recommendation for Q3 confidence range (72-78%)
**Input:** `/build Q3 2026`
**Output check:**
- Confidence reasoning section present? YES/NO
- References Q2 calibration? YES/NO
- Recommends 72-78% range? YES/NO

## Eval 3: Three options delivered with Quality Gates
**Scenario:** User runs `/build` without prior OKRs
**Expected:** Three OKR options, each with 5-gate results (✅/❌ table)
**Input:** `/build Q3 OKRs for SMB focus`
**Output check:**
- Three options present? YES/NO
- Quality Gate table in each option? YES/NO
- Gate results binary (✅/❌)? YES/NO
- No narrative substitutions? YES/NO

## Eval 4: Learning Close accuracy (Step 8)
**Scenario:** User completes `/build` and `/scorecard`
**Expected:** Entry written to `/context/skill-sessions.md` per Step 8's real Learning Close template — exactly four fields, matching `SKILL.md` verbatim
**Input:** `/build` + `/scorecard`
**Output check:**
- Session logged? YES/NO
- Row contains exactly these four fields: `skill`, `session_date`, `pattern`, `source`? YES/NO — no additional fields (no `quarter`, `objectives_count`, `guardrails_triggered`, or similar; those are chat-output details from `/build` and `/scorecard`, not part of the log row)
- `pattern` is a single falsifiable statement about this session, or the literal `"none"`? YES/NO
- `source` is one of `surprised / wrong / missing / n.v.t.`? YES/NO
- Row written directly, without asking the user for permission? YES/NO

## Eval 5: Adversarial callouts surface inline
**Scenario:** User submits OKRs with vague KR ("improve adoption")
**Expected:** Callout surfaces during `/review` with rewrite before delivery
**Input:** `/review` with vague KR
**Output check:**
- Callout appears? YES/NO
- Format: ⚠️ ADVERSARIAL CALLOUT: [Issue]? YES/NO
- Rewrite provided? YES/NO
- Rewrite is specific? YES/NO

## Eval 6: Scorecard Weight confirmed at 100%
**Scenario:** User runs `/scorecard` with weights that don't total 100%
**Expected:** Discrepancy surfaced, scorecard not delivered
**Input:** `/scorecard` with 4 metrics weighted 30%, 30%, 20%, 15%
**Output check:**
- Discrepancy detected? YES/NO
- Totals 95% mentioned? YES/NO
- Scorecard held from delivery? YES/NO
- Prompt to rebalance given? YES/NO

## Eval 7: Prior quarter dependency risks flagged in `/map`
**Scenario:** `/context/skill-sessions.md` shows "external dependencies blocked in Q2"
**Expected:** `/map` output flags this risk for current KRs
**Input:** `/map` with 3 KRs containing external dependencies
**Output check:**
- Guardrail about prior quarter blockers? YES/NO
- Specific to external dependencies? YES/NO
- Asks user to accept risk? YES/NO

## Eval 8: Option selection reflected in Learning Close
**Scenario:** User selects Option B from `/build` (not Option A)
**Expected:** Per `SKILL.md`'s real `Outputs` section, this skill writes nothing beyond the Step 8 session-log row — there is no separate `decisions/` file. The choice of Option B over Option A should be reflected, if notable, in that row's `pattern` field.
**Input:** User selects Option B
**Output check:**
- No file created at any `decisions/` path — that mechanism does not exist in this skill? YES/NO
- If the Option B choice was a genuine surprise or worth remembering, `pattern` in the Step 8 row names it (e.g. "User picked the higher-risk option over the calibration-recommended one")? YES/NO
- If not notable, `pattern: none` is still written — the row is never skipped? YES/NO
