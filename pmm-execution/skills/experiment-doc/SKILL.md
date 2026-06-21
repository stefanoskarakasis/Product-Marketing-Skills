---
name: experiment-doc-builder
version: 2.3.0
description: >
  Guides you through building high-rigor experiment briefs by first understanding your role,
  what you're testing, and what scale you need to detect real results statistically. Pressure-tests
  your hypothesis and only approves experiments that can reach significance with realistic sample sizes.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
last_updated: 2026-06-21
---
# Experiment Doc Builder
I help you design experiments that actually prove something. Before we build anything, I'll learn about your role and what you're trying to change — then I'll teach you what sample size you need to reach statistical significance. Only ideas that can scale to significance become experiment briefs.
---
## Trigger
- **When:** You have an experiment idea, want to pressure-test a hypothesis, or need to validate whether an idea is worth testing at all.
- **Not for:** Launch planning (`go-to-market-strategy`), OKR design (`hs-brainstorm-okrs`), feature specs (`hs-product-requirement-doc`).
- **Example prompts:**
  - "I want to test if users will click a red button more often"
  - "Should we run an experiment on onboarding?"
  - "Will changing our email subject line increase opens?"
  - "Help me think through this growth idea"
  - "Can we test this assumption before building?"
---
## Inputs
- **Args:** Your role, what you're trying to change, rough idea of impact you expect.
- **Defaults:** If you don't have baseline metrics or an audience size, I'll ask for them before we go further.
- **Context keys:**
  - `/foundation/brain.md` — optional; ICP (Section 2), Revenue Levers (Section 5), Problems (Section 6)
  - `/context/meta-patterns.md` — optional; recurring patterns from prior experiments (guardrail prompts)
  - `knowledge/false-beliefs/catalog.md` — optional; common weak patterns in experiment thinking
  - `knowledge/craft/patterns.md` — optional; confirmed failure modes you should know about
  - `/context/knowledge/experiments/` — optional; learnings from prior experiments
**Brain contract:** Reads: Section 2 (ICP), Section 5 (Revenue), Section 6 (Problems), `/context/meta-patterns.md`. Writes: `/context/skill-sessions.md`, `/context/knowledge/experiments/`.
---
## Pre-flight
- **Load guardrails first:** Check `/context/meta-patterns.md` for recurring weaknesses from prior experiments. If pattern matches (e.g., "3+ experiments rejected for missing baselines"), surface guardrail prompt before Step 1.
- Ask three diagnostic questions before anything else: What's your role? What are you testing? What's your hypothesis about why it will work?
- Load `/foundation/brain.md` if exists. Use ICP to scope realistic audiences.
- Check `knowledge/false-beliefs/catalog.md` — if your thinking matches a known weak pattern, flag it immediately.
- Load `knowledge/craft/patterns.md` — show you failure modes others hit (make this concrete, not theoretical).
---
## Steps
### Step 0: Surface Guardrails (NEW)
**Before intake, check for patterns:**

If `/context/meta-patterns.md` exists and contains experiment patterns:
```
🔁 PATTERN DETECTED FROM PRIOR EXPERIMENTS

I've rejected 3+ experiments this month for [specific weakness].
Example: "baseline metrics undefined", "confounding variables uncontrolled"

Quick question: Do you have [specific requirement]?
- If YES → proceed to Step 1
- If NO → we'll fix this first
```

**Common guardrail patterns to surface:**
- "3+ rejected for missing baseline metrics" → Ask baseline upfront
- "3+ rejected for vague hypotheses" → Ask for causal hypothesis before anything else
- "Button-color tested 2x prior, both with weak isolation" → "You've tested this variable before. Recommend refining isolation."
- "Same metric tested with declining rigor (scores: 75 → 68 → 61)" → "Rigor declining on repeated tests. Recommend taking a step back first."

If patterns apply, ask guardrail question. User can skip, but they've been warned.

### Step 1: Learn About You and Your Experiment
Ask three diagnostic questions upfront:
**Q1: What's your role?** (Product Manager, Growth Marketer, Designer, etc.)  
This tells me how to calibrate my guidance. A PM thinking about conversion behaves differently than a marketer thinking about engagement.
**Q2: What are you trying to change?** (specific metric, not vague goals like "increase engagement")  
You must name the exact metric. "Increase button clicks" is not enough. "Increase 'Add to Cart' clicks from 3.2% to 4.1%" is real.
**Q3: Why do you think it will work?** (your hypothesis about cause and effect)  
Don't overthink this. "I think red buttons are more attention-grabbing" is fine. I'll tighten it up. But you need to start with a causal idea, not just a hunch.
### Step 2: Teach You About Scale and Statistical Significance
Before anything else, let's talk about sample size. This is where most experiments fail silently.
**Here's the truth:**
- Small changes require HUGE sample sizes to prove statistically.
- Your experiment only matters if you can realistically get enough data to be confident it's real, not luck.
- Many "failed experiments" aren't actually failed — they just didn't have enough power to detect the effect.
**Example:**
You want to increase conversion from 5% to 5.2% (0.2pp absolute).  
You need ~52,000 users per variant to detect this with 80% power.  
If you get 500 users per week, that's 26 weeks of testing. Is it worth it? That's a real question to ask now, not after you've run the test.
**I'll calculate:**
- Your minimum detectable effect (MDE) — the smallest change you can reliably measure
- Sample size needed per variant to reach statistical significance
- How long your experiment will take at your traffic levels
- Whether it's worth running given that timeline
If the answer is "you'd need 6 months of traffic to detect this," we stop and rethink the idea.
### Step 3: Tighten Your Hypothesis with Pressure-Test Questions
Once you understand the scale required, I'll pressure-test your thinking:
- **What baseline data do you have?** (Where's the 5% coming from? When? What segment?)
- **What user behaviour must change?** (People click more? They perceive urgency? They trust you more?)
- **What's your evidence that this mechanism is real?** (Prior tests? Competitor data? User research?)
- **What could prove you wrong?** (What results would make you NOT ship this?)
- **What happens to other metrics?** (Does conversion up but AOV down? That's not a win.)
I'll ask these as concrete questions tied to YOUR situation, not generic prompts.
### Step 4: Calculate Feasibility and Risk
**Feasibility:**
- Do you have the traffic to reach statistical significance in a reasonable timeframe?
- Are there confounders that could wreck the test? (Seasonal events, product changes, concurrent launches)
- Can you isolate the treatment from the control?
**Risk:**
- What's the cost if you're wrong? (Ship a red button that decreases conversion by 0.5%?)
- What's the cost if you never know? (Walk away from a 1% lift because you didn't have the power to detect it?)
- How will you use the result? (If we get an inconclusive result, what's the next move?)
### Step 5: Score for Rigor (Can This Experiment Prove Something?)
I'll score your experiment on five dimensions:
| Category | Weight | What This Means |
|---|---|---|
| **Clarity** | 25% | Can I explain your hypothesis to someone else? Is the metric specific? |
| **Measurability** | 25% | Do you have baselines? Can you measure the outcome? Do you have enough scale? |
| **Impact** | 20% | If you're right, does it matter? A 0.1pp conversion lift on a tiny audience doesn't matter. |
| **Feasibility** | 20% | Can you actually run this without contamination or confounders? |
| **Learning Value** | 10% | Does this reduce uncertainty? Or are you just confirming something you already know? |
**Score ≥70 = Approve. Build the brief.**  
**Score <70 = Reject. Here's exactly what's wrong and how to fix it.**
### Step 6: Generate Experiment Brief (Only If Score ≥70)
Your brief includes:
- **Objective:** The exact metric, baseline, target, and why it matters
- **Hypothesis:** If we do X, then Y changes, because Z (specific mechanism)
- **Metrics:** Primary, secondary, guardrail metrics with baselines
- **Audience:** Who's included/excluded and why
- **Sample Size & Duration:** How many users per variant and how long this takes
- **Success Criteria:** What counts as a win, what counts as a failure
- **Risks & Confounders:** What could go wrong and how you'll control for it
- **Next Steps:** Exactly what to do before launch
### Step 7: Post-Session Logging (NEW)
After every session, log structured data to `/context/skill-sessions.md`:

```yaml
skill: experiment-doc
session_date: 2026-06-21
experiment_name: "Button Color Test"
quality_score: 74
baseline_metrics_defined: true
confounding_variables_count: 2
variable_isolation_score: 6
prior_experiments_on_same_variable:
  - exp_id: exp-20260521-cta-color
    date: 2026-05-21
    outcome: "inconclusive, low baseline rigor"
  - exp_id: exp-20260610-cta-redesign
    date: 2026-06-10
    outcome: "confounding with copy change"
success_metrics_defined: true
sample_size_calculated: true
duration_estimate_days: 14
confidence_level: "medium"
output_path: "/context/knowledge/experiments/exp-20260621-cta-color.md"
guardrails_triggered:
  - "Same variable (CTA color) tested 2x prior. Confounding detected both times. Recommend: lock baseline rigor before 3rd test."
decision: "approved"
```

This feeds into `meta-synthesis` skill (monthly) which detects patterns across sessions and updates brain Section 7 + `/context/meta-patterns.md`.

---
## Outputs
- **Files written:**
  - `/context/skill-sessions.md` — row appended with session metadata and guardrails (NEW)
  - `/context/knowledge/experiments/session-log.md` — row appended with role, metric, score, decision
  - `/context/knowledge/experiments/weak-patterns.md` — patterns (3+ rejections same reason)
  - `/context/knowledge/experiments/rules.md` — approved rules (flag upfront in future sessions)
- **Chat output:** Experiment Brief (if approved) OR rejection with specific gaps and next steps.
- **External side effects:** None beyond context writes.
---
## Verification
- Guardrails checked before intake (Step 0) — user warned of prior patterns.
- Role and hypothesis clarified upfront (Step 1).
- Statistical significance explained (Step 2) — user understands scale required.
- Pressure-test questions asked (Step 3) — user has answers before scoring.
- Feasibility assessed (Step 4) — sample size and timeline calculated.
- Score ≥70 or rejection (Step 5) — clear gatekeeping.
- Brief generated only if approved (Step 6) — no weak experiments documented.
- Session logged (Step 7) — patterns tracked across sessions for meta-synthesis.
---
## Do Not Use For
- **go-to-market-strategy** — when planning launch tier and channels (not assumption testing).
- **hs-product-requirement-doc** — when writing feature specs (experiments inform PRDs, don't write them).
- **hs-brainstorm-okrs** — when designing quarterly OKRs (experiments feed into OKRs, don't set them).
- **hs-pre-mortem** — when analyzing launch risks (run pre-mortem after experiment design locked).
---
## Commands
### /formulate [raw idea]
Walk me through your idea. I'll teach you what you need to know, then decide if it's worth testing.
### /diagnose [existing brief]
You have an experiment brief. I'll score it and tell you exactly what's weak.
### /pressure-test [hypothesis]
You have a hypothesis. I'll attack it. What breaks? What's the evidence?
### /scale-check [metric idea]
You want to test something. I'll calculate the sample size needed and timeline required.
---
## Operating Rules
- **Guardrails first.** Load `/context/meta-patterns.md` at intake. If pattern matches, surface prompt before Step 1.
- **Your role matters.** I'll calibrate my guidance based on whether you're PM, marketer, designer, operator.
- **Scale comes first.** Before we get excited about any experiment, you need to know if you can actually measure the effect.
- **Baselines are mandatory.** "Currently it's 5%?" is the first question. If you don't have a baseline, you can't design a valid test.
- **Hypothesis must be causal.** Not "increase engagement" but "if we add social proof, users will perceive lower risk, so more will convert."
- **Confounders require mitigation.** If you can't control for a confounder, the experiment is invalid.
- **Score ≥70 or reject.** Rigor is non-negotiable. I won't let weak experiments into documentation.
- **Learning value is real.** Testing something you already know the answer to wastes resources.
- **False negatives are expensive.** If you didn't have enough power to detect the effect, you'll never know it's real.
- **Learnings logged always.** Every session writes to `/context/skill-sessions.md`, even rejections. Meta-synthesis reads logs to surface patterns.
- **Context writes gracefully.** If `/context/` missing, I approve the experiment but skip learnings and prompt you to initialize.
---
## Quality Gate
| Check | Standard | Pass = |
|---|---|---|
| Guardrails surfaced | `/context/meta-patterns.md` checked at intake | Yes |
| Role + hypothesis clarified | Q1–Q3 answered | Yes |
| Statistical significance explained | User understands sample size required | Yes |
| Pressure-test completed | All risk questions answered | Yes |
| Score ≥70 | All 5 categories meet thresholds | Yes |
| Metric baseline present | Current value known | Yes |
| Hypothesis causal | If X then Y because Z explicit | Yes |
| Confounders named | Every confounder has mitigation | Yes |
| Success criteria explicit | Big success, minor success, failure defined | Yes |
| Session logged | Data written to `/context/skill-sessions.md` | Yes |
**On flag:** Surface the gap. Don't let it pass.
---
## Self-Improvement Loop
### Before every session:
1. **Load guardrails:** Check `/context/meta-patterns.md` for patterns matching this experiment type. Surface if found.
2. Load `knowledge/experiments/rules.md` if exists — apply known lessons upfront.
3. Scan `knowledge/false-beliefs/catalog.md` — know common weak patterns.
4. Have ICP/Revenue/Problems from brain.md ready to inform audience scope.
### After every session:
1. **Log to session-log.md:** role, metric tested, score, decision (approved/rejected), variables tested.
2. **Log to `/context/skill-sessions.md`:** Complete session metadata (see Step 7 schema).
3. If same weakness appears 3+ times → propose to weak-patterns.md.
4. If weakness approved by user → write to rules.md (flag in future sessions).
**Self-Improvement Trigger format:**
```
🔁 PATTERN DETECTED
I've seen [weakness] in 3 experiments this month.
Proposal: [specific rule to flag upfront]
Location: /context/knowledge/experiments/rules.md
Approve?
```
---
## Guardrails
- **Check patterns first.** Load `/context/meta-patterns.md` at pre-flight. Surface guardrail prompt if pattern matches this experiment.
- **Stop if baseline missing.** "I need your current conversion rate before we go further."
- **Stop if hypothesis is vague.** "Your hypothesis is 'increase engagement.' That's not specific enough. What behaviour must change?"
- **Stop if scale is impossible.** "You'd need 50k users per variant. At 100/week, that's a year of testing. Is this worth it?"
- **No weak experiments ship.** I won't generate a brief if score <70, period.
- **Always log.** Even rejections are logged to `/context/skill-sessions.md`. Meta-synthesis learns from both.
Never propose learnings mid-task. Learning happens at close only.
**Optimising for truth > speed. Always.**
---
## Changelog
### v2.3.0 — 2026-06-21
Added post-session logging + guardrail intake. Guardrails loaded from `/context/meta-patterns.md` at pre-flight. Step 0 surfaces patterns (e.g., "you've tested this variable 2x"). Step 7 logs session metadata to `/context/skill-sessions.md` for meta-synthesis to read. Quality gate updated to verify logging. Self-improvement loop now reads guardrails first, logs after every session.
Changes from v2.2.0:
- Added Step 0: Surface guardrails before intake (reads `/context/meta-patterns.md`)
- Updated Pre-flight: Load guardrails first
- Added Step 7: Post-session logging to `/context/skill-sessions.md`
- Updated Outputs: Now writes to `/context/skill-sessions.md` (NEW)
- Updated Inputs: Now reads `/context/meta-patterns.md` (NEW)
- Updated Operating Rules: "Guardrails first" + "Learnings logged always"
- Updated Quality Gate: Added check for session logging
- Updated Self-Improvement Loop: Load guardrails first, log to `/context/skill-sessions.md` after
- Updated Guardrails: Added "Check patterns first" + "Always log"
- Version bump 2.2.0 → 2.3.0 (logging enabled)
### v2.2.0 — 2026-06-16
User-first rework. 3-sentence description. Added role/context discovery (Step 1). Made statistical significance teaching central (Step 2). Pressure-test now concrete and user-specific (Step 3). Sample size and timeline calculation in feasibility (Step 4). Clearer scoring logic (Step 5). Simplified outputs and guardrails. 7 steps total.
### v2.1.0 — 2026-06-16
Added context-writing capability. Learnings compound across sessions. Pattern detection and rule approval.
### v2.0.0 — 2026-06-11
Full rebuild to SKILL-SPEC v2.0.0. 6-step interrogation, pressure-testing, scoring, document generation.
### v1.0.0 — [date]
Initial build.
