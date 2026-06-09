# meta-verify — Eval Suite
**Skill version:** 1.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: GTM brief passes cleanly

**Input:**
```
/verify go-to-market-strategy

[Paste of a complete GTM brief with:
- T2 assigned with four-signal rationale stated
- Leading indicator present alongside primary metric
- Channels with ICP-specific rationale (not generic)
- Competitive context with primary alternative, attack and defend angles
- Proof points from brain Section 5
- Timeline with tier-appropriate milestones
- Next steps including retro trigger]
```

**Expected output includes:**
- Originating skill's operating rules and quality gate loaded and stated before checking
- Brain NOT loaded — context-agnostic confirmed
- All 10 quality gate checks pass ✅
- Result: ✅ PASS
- Passing checks listed explicitly
- Recommendation: "Safe to act on"
- Offer to run `/verify-fix` (even on pass — for future fixes)

**Expected output excludes:**
- Any brain context loaded or referenced
- False failures on a complete, well-formed brief
- Partial read of the output

**Pass condition:**
10/10 quality gate checks pass, result is ✅ PASS, brain not referenced.

---

## Test Case 2: Pre-mortem fails — Tiger without mitigation

**Input:**
```
/verify pre-mortem

[Paste of a pre-mortem output where:
- Tiger R-03 "Competitive response from Salesforce" is listed as Launch-Blocking
- No mitigation plan, no owner, no due date assigned to R-03
- PMM Recommendation is 🟢 Go despite the unresolved Launch-Blocking Tiger]
```

**Expected output includes:**
- pre-mortem operating rules loaded first
- Two failures identified:
  1. ❌ "No Tiger without a mitigation" — R-03 has no mitigation, owner, or due date.
     Quote: "R-03: Competitive response from Salesforce — [no mitigation block present]"
     Fix: "Add full action plan block: What breaks / Why it's real / Mitigation / Owner / Due date / Confidence"
  2. ❌ QG escalation rule — Launch-Blocking Tiger with no mitigation means
     PMM Recommendation cannot be 🟢 Go.
     Quote: "PMM Recommendation: 🟢 Go"
     Fix: "Change to 🟡 Conditional Go or 🔴 No-Go until R-03 mitigation is assigned"
- Result: ❌ FAIL
- Recommendation: "Do not present to stakeholders until both failures are resolved"

**Expected output excludes:**
- Passing R-03 because it's listed as a Tiger (existence ≠ completeness)
- Accepting 🟢 Go with an unresolved Launch-Blocking Tiger
- Generic fix directions without specific content

**Pass condition:**
Both failures identified with exact quotes, specific fixes stated, result is ❌ FAIL.

---

## Test Case 3: Positioning output — Conditional Pass with jargon warning

**Input:**
```
/verify positioning-messaging

[Paste of a positioning output where:
- Positioning statement is differentiated and competitor-specific ✅
- All pillar headlines pass 4/4 stress-test ✅
- Evidence tiers correct ✅
- One headline contains "seamless integration" — jargon on the forbidden list
- Persona count is 2 ✅]
```

**Expected output includes:**
- positioning-messaging operating rules and quality gate loaded
- One failure or warning identified:
  ⚠️ Jargon check — "seamless integration" in pillar headline
  Quote: "[exact headline containing 'seamless integration']"
  Fix: "Replace 'seamless' — remove entirely or rewrite with specific claim:
       e.g. 'connects to Salesforce in 4 clicks' not 'seamless integration'"
- All other checks pass ✅
- Result: ⚠️ CONDITIONAL PASS
- Recommendation: "Safe for internal use. Fix jargon before external sharing."

**Expected output excludes:**
- Full ✅ PASS ignoring the jargon violation
- Full ❌ FAIL — jargon is a warning, not a hard gate failure
- Vague fix: "remove jargon from this headline"

**Pass condition:**
Conditional Pass issued correctly, jargon flagged as ⚠️ with specific replacement suggested.

---

## Test Case 4: /verify-standard — shows standard without verifying

**Input:**
```
/verify-standard pre-mortem
```

**Expected output includes:**
- pre-mortem SKILL.md loaded
- Operating rules listed (all 14+) — numbered, exact text from SKILL.md
- Quality gate table shown — all 17 checks with Standard and Pass condition columns
- No verification run — no output checked
- Offer: "Ready to verify a pre-mortem output? Use `/verify pre-mortem` and paste the output."

**Expected output excludes:**
- Any verification happening without output being provided
- Partial list of rules (must be complete)
- Generic description of what pre-mortem does (that's the skill description, not the standard)

**Pass condition:**
Complete operating rules and quality gate shown, no verification attempted without output.

---

## Test Case 5: Unknown skill — asks before proceeding

**Input:**
```
/verify

[Paste of output that doesn't match any known T1 skill format —
e.g. a resume review output from pmm-resume]
```

**Expected output includes:**
- Skill not identified from output structure
- Asks before proceeding:
  > "I can't identify which skill produced this output. Which skill should I verify
  > against? (pre-mortem / go-to-market-strategy / positioning-messaging)"
- If user names a skill not in current scope:
  > "pmm-resume is not currently in meta-verify scope (T3 utility skill). In-scope
  > skills: pre-mortem, go-to-market-strategy, positioning-messaging.
  > Use `/verify-scope` to see the full list."
- Does not run an informal check without a loaded standard

**Expected output excludes:**
- Running verification without identifying the originating skill
- Running an informal check ("let me do my best") without a loaded standard
- Treating the resume output as a positioning output

**Pass condition:**
Skill not assumed, user asked to clarify, out-of-scope skill gracefully declined.

---

## Test Case 6: /verify-scope — correct scope listing

**Input:**
```
/verify-scope
```

**Expected output includes:**
- T1 skills listed as in-scope with check counts:
  - pre-mortem: 17 quality gate checks
  - go-to-market-strategy: 10 quality gate checks
  - positioning-messaging: 7 quality gate checks
- T2 skills listed as planned (retro, stakeholder-maps, beachhead-segment)
- Clear statement: T3/T4 and utility skills not in scope
- Offer: "/verify-standard [skill] to see the full standard before submitting output"

**Expected output excludes:**
- T2 skills listed as in-scope
- No differentiation between in-scope and planned
- No mention of how to expand scope

**Pass condition:**
Exactly three T1 skills listed as in-scope with accurate check counts.

---

## Test Case 7: /verify-fix — corrects identified failures

**Input:**
```
/verify-fix go-to-market-strategy

[Context: previous /verify run identified two failures:
1. Tier rationale only cited Revenue Potential — missing three other signals
2. Channel list has no ICP-specific rationale — generic "LinkedIn, email, events"]
```

**Expected output includes:**
- Both failures from the verification report addressed
- Corrected tier rationale: all four signals cited (Market Impact, Revenue Potential,
  Competitive Urgency, Resource Requirement) with one-sentence synthesis
- Corrected channel list: each channel has ICP-specific reason tied to motion type
  and buying trigger from the brief context
- ⚠️ warnings (if any) noted but left unchanged — only ❌ failures fixed
- Offer to re-run `/verify go-to-market-strategy` on the corrected output

**Expected output excludes:**
- Fixing items that weren't in the failure list
- Rewriting the entire brief rather than fixing specific failures
- Fixing ⚠️ warnings without noting they were left to the user's discretion

**Pass condition:**
Exactly the two failures fixed with ICP-specific content, ⚠️ warnings preserved unchanged.
