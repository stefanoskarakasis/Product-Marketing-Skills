---
name: meta-verify
version: 1.0.0
description: >
  Second-pass quality check on T1 skill output. Reads output cold — without the
  context of how it was produced — and checks it against the originating skill's
  operating rules and quality gate criteria. The difference between a skill
  self-grading and an independent evaluator. Start with T1 skills: pre-mortem,
  go-to-market-strategy, positioning-messaging. Trigger on: "verify this output",
  "check this brief", "is this pre-mortem complete", "second opinion on this",
  "quality check this", or any request to independently validate a skill output
  before acting on it.

metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-06-06
---

# meta-verify

Independent quality check for T1 skill output. Reads output cold — no session
context, no knowledge of how it was produced — and checks it against the
originating skill's operating rules and quality gate.

The skill that produced the output is the worst judge of whether it's good.
This skill is the second opinion that catches what self-grading misses.

---

## Trigger

- **When:** Any T1 skill output before the user acts on it — especially before
  a launch commits resources, a pre-mortem is presented to stakeholders, or
  positioning is handed off to copy or sales.
- **Not for:** Checking skill *file* structure → use `meta-review`. Capturing
  session learnings → use `meta-learn`. Reviewing brain file health → use
  `product-marketing-context` audit mode.
- **Example prompts:**
  - "Verify this GTM brief before I share it with my VP"
  - "Second opinion on this pre-mortem"
  - "Is this positioning output complete?"
  - "/verify gtm [paste output]"
  - "Quality check this before we commit to the launch plan"

---

## Inputs

- **Args:** Skill name + output to verify. Paste the full output directly.
- **Defaults:** If skill name not stated, infer from output structure before asking.
  If output not provided, ask for it — never verify without the content.
- **Context keys:**
  - Originating skill's `SKILL.md` — required. Load the operating rules and
    quality gate of the skill that produced the output.
  - n.v.t. — no brain file. Context-agnostic by design. Verification must be
    objective and independent of company context.

---

## Pre-flight

- Identify the originating skill from the output structure or user statement.
- Load the originating skill's `SKILL.md` — specifically its `## Operating Rules`
  and `## Quality Gate` sections. These are the standards to verify against.
- If the originating skill's SKILL.md cannot be found: ask the user to confirm
  which skill produced the output before proceeding.
- Do not load `/foundation/brain.md`. Verification must be independent of the
  company context that generated the output — otherwise the same bias that
  produced the output will evaluate it.
- Read the output in full before running any checks. No partial verification.

---

## Steps

### Step 1: Load Verification Standard

Load the originating skill's operating rules and quality gate. State them
explicitly before checking — this makes the standard visible and auditable.

> "Verifying against [skill-name] operating rules and quality gate.
> [N] operating rules. [N] quality gate checks. Reading output now."

---

### Step 2: Run Independent Quality Gate

Check each quality gate item from the originating skill as binary pass/fail.
Read the output cold — as if you did not produce it.

For every ❌:
- Name the specific check that failed
- Quote the exact part of the output that failed it (or note the omission)
- State the specific fix required — not a direction, the actual content needed

Format each failure:

```
❌ [Check name]
Found: [exact quote from output, or "missing"]
Required: [what the check demands]
Fix: [specific content to add or change]
```

---

### Step 3: Check Operating Rules

Beyond the quality gate, scan output against the originating skill's operating rules.
These catch behavioural failures the quality gate doesn't test — things like
"tier rationale must be grounded in four signals" or "no Tiger without a mitigation."

Flag any operating rule violation in the same format as quality gate failures.

---

### Step 4: Produce Verification Report

```markdown
## Verification Report — [skill-name] output
**Verified against:** [skill-name] v[version] operating rules + quality gate
**Date:** [YYYY-MM-DD]
**Verifier:** meta-verify v1.0.0

---

### Result: ✅ PASS / ❌ FAIL / ⚠️ CONDITIONAL PASS

**Quality gate:** [X/N checks passed]
**Operating rules:** [X/N rules satisfied]

---

### Failures (must fix before acting on this output)

[Failure blocks in format from Step 2]

---

### Warnings (should fix before sharing externally)

[Any ⚠️ items — present but weak, not absent]

---

### Passing checks

[List of ✅ checks — confirms what's correct]

---

### Recommendation

[One sentence: safe to act on / fix these items first / do not use without revision]
```

---

### Step 5: Offer Fix Mode

After report, offer:
> "Want me to fix the failures and produce a corrected version of the output?
> Use `/verify-fix` to apply the fixes automatically."

---

## Outputs

- **Files written:** n.v.t. — verification is read-only. No writes.
- **Chat output format:** Verification report in the structure above. Markdown
  formatted for copy-paste into a review comment, Notion, or GitHub issue.
- **External side effects:** n.v.t.

---

## Verification

- Originating skill's SKILL.md loaded before checking begins.
- Standard stated explicitly before checks run.
- Output read in full — no partial verification.
- Every ❌ includes exact quote from output and specific fix.
- Result clearly states Pass / Fail / Conditional Pass.
- No brain file loaded — verification is context-agnostic.
- No writes made — read-only throughout.

---

## Do Not Use For

- **meta-review** — for checking whether a skill *file* is built correctly.
  `meta-verify` checks whether a skill *output* is correct. Different inputs,
  different purpose.
- **meta-learn** — for capturing what was learned from a session. Run `meta-verify`
  first to check output quality, then `meta-learn` to capture patterns.
- **Rewriting output** — `meta-verify` identifies failures. Use `/verify-fix`
  to produce corrections, or return to the originating skill with the failures listed.

---

## Commands

### /verify [skill-name]
Run full verification on a pasted output. Loads the originating skill's standards
and checks the output cold.

```
/verify pre-mortem
/verify go-to-market-strategy
/verify positioning-messaging
```

Paste the output immediately after the command.

---

### /verify-fix [skill-name]
After a verification report, apply the identified fixes and produce a corrected
version of the output.

```
/verify-fix pre-mortem
```

Applies all ❌ fixes from the most recent verification report. Outputs corrected
version. Does not change ⚠️ warnings — those are flagged but left to the user.

---

### /verify-standard [skill-name]
Show the verification standard for a named skill — its operating rules and quality
gate — without running a verification. Useful for understanding what will be checked
before submitting output.

```
/verify-standard pre-mortem
/verify-standard go-to-market-strategy
```

Output:
```
Verification standard — [skill-name] v[version]

Operating rules ([N]):
1. [Rule]
2. [Rule]
...

Quality gate checks ([N]):
| Check | Standard | Pass = |
|---|---|---|
| [Check] | [Standard] | [Condition] |
```

---

### /verify-scope
List which skills are currently in scope for `meta-verify`. Starts with T1 skills
and expands as the meta skill matures.

```
/verify-scope
```

Output:
```
meta-verify scope — v1.0.0

✅ In scope (T1 skills):
- pre-mortem — 17 quality gate checks, 14 operating rules
- go-to-market-strategy — 10 quality gate checks, 10 operating rules
- positioning-messaging — 7 quality gate checks

🔜 Planned (T2 skills):
- retro
- stakeholder-maps
- beachhead-segment

Not in scope: T3/T4 skills, utility skills
```

---

## T1 Skill Verification Standards

### pre-mortem
Key operating rules to verify against:
- Every Tiger has a mitigation and named owner — no Tiger without a plan
- Every Elephant has: what to find out / investigator / due date / upgrade condition
- PMM Recommendation present and explicit (Go / Conditional Go / No-Go)
- No-Go framed as validation sprint if politically complex
- All five lenses represented with at least one risk each
- Launch-Blocking Tigers: 🔴 mitigation confidence → recommendation cannot be 🟢

### go-to-market-strategy
Key operating rules to verify against:
- All four tier signals applied — tier not assigned on single signal
- Tier rationale stated in one sentence before brief
- Leading indicator present alongside primary metric
- Channel recommendations ICP-specific — not generic lists
- Competitive context: primary alternative named with attack and defend angle
- Brain Section 7 write offered (not auto-executed)

### positioning-messaging
Key operating rules to verify against:
- Positioning statement cannot be said honestly by any named competitor
- All pillar headlines pass 4/4 differentiation stress-test
- Zero jargon: leverage, seamless, best-in-class, robust, enterprise-grade, etc.
- Every claim has T1/T2 evidence or carries `[T3 — NEEDS VALIDATION]` flag
- Persona count ≤ 3
- All Vision Flags addressed or documented as rejected

---

## Operating Rules

- **Load the standard before the output.** Always load the originating skill's
  operating rules and quality gate before reading the output. Standard-first
  prevents anchoring on what's there rather than what's required.
- **Read the output in full before checking.** Partial reads produce false passes.
- **Context-agnostic by design.** Never load brain file. The same company context
  that generated the output will bias its evaluation.
- **Every failure needs a specific fix.** "The tier rationale is weak" is not a fix.
  "Tier rationale must cite all four signals — Market Impact, Revenue Potential,
  Competitive Urgency, Resource Requirement — currently only Revenue is cited" is.
- **Quotes, not summaries.** For every failure, quote the exact text or note the
  exact omission. Never paraphrase a failure.
- **Read-only always.** No writes under any circumstance. Verification produces
  a report — it does not produce a fixed output unless `/verify-fix` is called.
- **Pass threshold is the skill's own gate.** Do not apply a lower standard than
  the originating skill's quality gate. The standard is the standard.
- **Conditional Pass for minor gaps.** If the output passes all hard gates but
  has ⚠️ warnings, issue a Conditional Pass — safe to use internally but not
  yet ready for external sharing.
- **Expand scope deliberately.** Start with T1 skills only. Add T2 skills when
  T1 verification patterns are stable and the checklist is confirmed accurate.
- **Surface scope gaps.** If a skill is not yet in scope for verification, say
  so explicitly rather than running an informal check. Informal checks without
  loaded standards are less reliable than no check.

---

## Quality Gate

Runs after verification report is generated, before delivery.

| Check | Standard | Pass = |
|---|---|---|
| Standard loaded | Originating skill's SKILL.md read before output checked | Yes |
| Full output read | No partial verification | Yes |
| Brain not loaded | Verification is context-agnostic | Yes |
| Every ❌ has quote | Exact text or omission cited for each failure | Yes |
| Every ❌ has fix | Specific content required stated, not direction | Yes |
| Result stated | Pass / Fail / Conditional Pass clearly declared | Yes |
| Recommendation present | One sentence on whether output is safe to act on | Yes |
| No writes made | Verification produced no file changes | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Check `knowledge/meta/rules.md` — apply any confirmed patterns about what
   T1 skills most commonly fail on.
2. Check `knowledge/meta/hypotheses.md` — note any open hypothesis about
   verification accuracy this session could test.
3. Load `pmm-meta/skills/[originating-skill]/SKILL.md` — fresh load every
   session. Never use a cached standard.

### After every session:
1. Note which check most commonly failed in this verification.
   Log to `knowledge/meta/hypotheses.md`.
2. If the same check fails across 3+ verifications of the same skill →
   propose to `knowledge/meta/rules.md`: "Check [X] in [skill] is the most
   common failure — flag proactively before running full verification."
3. If a failure was found that the originating skill's quality gate doesn't
   currently test → propose addition to that skill's quality gate via
   Self-Improvement Trigger, routed to the originating skill's SKILL.md.

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed across verifications]
Proposed update: [exact wording]
Location: [file path — either meta-verify or originating skill]
Awaiting approval before encoding.
```

---

## Changelog

### v1.0.0 — 2026-06-06
Initial build. Third skill in `pmm-meta` plugin.

Architecture decisions:
- Context-agnostic: no brain file. Verification must be independent of the
  context that generated the output being checked.
- Standard-first: originating skill's SKILL.md loaded before output is read.
  Prevents anchoring on what's present rather than what's required.
- T1 scope only at launch: pre-mortem, go-to-market-strategy,
  positioning-messaging. Expand to T2 once T1 patterns are stable.
- Read-only by design. Verification produces a report. `/verify-fix` produces
  corrections. They are deliberately separate commands.
- Conditional Pass for ⚠️ warnings: output safe for internal use, not external.
- Four commands: /verify, /verify-fix, /verify-standard, /verify-scope.
- T1 verification standards documented inline — reduces dependency on reading
  individual skill files for the most common verification scenarios.
