---
name: experiment-doc
version: "1.1.0"
author: "JET Growth — Prosus Portfolio"
description: >
  Use this skill to build, audit, score, and pressure-test growth and product experiment
  documents for Just Eat Takeaway.com and Prosus portfolio companies. It auto-localises
  every experiment to the right market (NL, UK, DE, AU, CA, IL, NO and more), pulls live
  context from any connected source (Drive, Confluence, Slack, Calendar, Jira), applies
  ICE scoring and Reforge growth frameworks before interrogation, enforces guardrail
  metrics and named stakeholders as hard requirements, and compounds learnings into a
  self-updating knowledge base across sessions. Markets explicitly covered include NL,
  UK (Just Eat), DE (Lieferando), AU (Menulog), CA (SkipTheDishes), IL, NO, DK and more.
  Trigger on: experiment, test, hypothesis, A/B, feature flag, rollout, experiment brief,
  experiment review, conversion optimisation — or any of: "does this make sense to test?",
  "write me an experiment doc", "localise this for [market]", "pressure-test this idea",
  "what did we learn from X?", "score my brief", "diagnose this experiment".
---

# Experiment-doc

**Version:** 1.1.0
**Maintainer:** JET Growth / Prosus Portfolio
**Brain:** See `CLAUDE.md` for identity, routing, voice, hard rules, and session close protocol.
**Scope:** JET markets (NL · UK · DE · AU · CA · IL · NO · DK · BE · AT · CH · PL · SK
· BG · RO) + extensible to any Prosus portfolio company

---

## What This Skill Does

Experiment-doc is a structured thinking partner for growth and product experimentation
at JET and across the Prosus portfolio. It does four things a standard doc template
cannot:

1. **Stops bad experiments before they start.** It interrogates the idea, not the prose.
   If the hypothesis has no causal mechanism, the metrics have no guardrail, or the
   stakeholders aren't named, it blocks document generation and tells you exactly why.

2. **Localises automatically.** Every experiment runs inside a specific market with
   specific regulatory constraints, consumer behaviour patterns, and competitive
   dynamics. This skill loads that context before asking a single question — so a DE
   experiment doesn't get built on NL assumptions.

3. **Applies proven growth frameworks as lenses, not lessons.** ICE scoring, Reforge
   growth loop analysis, and lifecycle fit are applied to every idea before interrogation
   begins. You get a structured view of impact, confidence, ease, and strategic fit —
   not a lecture about methodology.

4. **Gets smarter with use.** Learnings from experiments are stored in a structured
   knowledge base — organised by market. Confirmed patterns become rules applied by
   default. Unconfirmed patterns sit as hypotheses surfaced when relevant. The more it
   gets used across your team, the sharper it becomes.

---

## Onboarding — Your First Session

If this is the first time you're using Experiment-doc, start here. This section shows
you exactly what to expect and how to get the most out of it from the first prompt.

### The most important thing to know upfront

This skill is not a document writer. It is a thinking partner that interrogates your
idea before helping you document it. The first few exchanges will feel like questions,
not outputs. That is by design — the interrogation is where the value is.

### The fastest path to a great experiment

**Step 1 — State your idea in one sentence and name the market.**
You don't need a full brief to start. The skill will ask for what it needs. But naming
the market upfront saves at least one round of questions.

Good first message:
```
I want to test [what] in [market]. I think it will [expected outcome] because [rough
reason]. I own this experiment and [name] is the approver.
```

**Step 2 — Let the skill score the idea before you say anything else.**
After your first message, the skill will apply an ICE score and tell you whether this
looks like a growth loop intervention or a funnel step optimisation. Read this before
responding. It tells you where the interrogation will push hardest.

**Step 3 — Answer interrogation questions with numbers, not directions.**
"CVR will improve" gets challenged. "CVR baseline is 32.4% (Amplitude, April 2026) and
we expect 2pp absolute lift" passes. The single most common reason an experiment gets
blocked is missing baselines with sources.

**Step 4 — Name all four stakeholder roles before being asked.**
Owner · Approver · Informed · Instrumentation owner. Having these ready skips a full
interrogation round.

**Step 5 — Define failure, not just success.**
The skill will always ask: "If this fails, what's the threshold and what's the
decision?" Having a kill threshold ready ("below 1pp absolute we don't ship") closes
this gap immediately.

### What a first session looks like end-to-end

```
You:    NL market. I want to test a progress indicator on the onboarding flow.
        I think it'll lift step completion because users don't know how many
        steps are left. Owner: me. Approver: NL Product Lead.

Skill:  [ICE score: Impact 6 / Confidence 4 / Ease 7 = ICE 5.7]
        [Identifies as funnel step optimisation, not loop]
        [Surfaces Hypothesis 002 from knowledge base: prior NL signal +11%]
        Gaps remaining: primary metric + baseline, guardrail metric,
        Instrumentation owner, success/failure thresholds.
        → What is the baseline step completion rate and where is it measured?

You:    61% at step 3, Amplitude. Instrumentation: Data team.

Skill:  → What is the guardrail metric — what would make you stop the test
          even if the primary metric lifts?

You:    Step 1 drop-off must not increase by more than 3pp.

Skill:  → Define your three success levels with numeric thresholds.

You:    Big success: >4pp lift. Minor: 2–4pp. Failure: <2pp, kill.

Skill:  [Score: 78/100 — APPROVED]
        [Generates full experiment document]
        [Adversarial checks inline on Hypothesis and Metrics sections]
        → Confirm Drive write and Slack post to #experiment-learnings?
```

Total exchanges to a fully approved document: 3–5 rounds for a prepared brief.
8–12 rounds for a raw idea. The interrogation is the shortcut, not the obstacle.

### Common first-session mistakes to avoid

| Mistake | What happens | Fix |
|---|---|---|
| No market stated | Skill asks before doing anything else | State market in first message |
| "CVR will improve" as primary metric | Challenged — not specific enough | "Checkout CVR, baseline 34.2%, Amplitude" |
| No guardrail metric | Blocks document generation | Name one thing that stops the test if it degrades |
| "We'll see how the data looks" as success criterion | Rejected | Three threshold levels with numbers |
| Submitting a brief without a because-clause | Hypothesis rejected | "...because [the exact behaviour that must change]" |

### Nudged prompt to copy for your first experiment

If you're not sure where to start, copy this and fill in the brackets:

```
[Market] experiment.

I want to test [specific intervention — what changes for the user].
I think [primary metric] will [increase/decrease] by approximately [magnitude]
because [the exact user behaviour that must change and why].

Baseline: [metric value] ([source], [date])
Owner: [name]
Approver: [name]
Instrumentation: [name/team]

Mode: Formulate
```

### Need a hand?

If anything is unclear — whether it's the skill itself, how to frame your hypothesis,
what metric to use, or whether your experiment idea makes sense — you can always reach
out directly on Slack: **@stefanos**. He built this skill and knows the JET and Prosus
context. No question is too small. Getting the experiment right before you run it is
always worth the conversation.

---

## Methodologies Applied

### ICE Scoring — Sean Ellis / GrowthHackers
Every idea is scored on three axes (1–10 each) before interrogation begins:
- **Impact** — if it works at the expected magnitude, how significant is the outcome in
  this market?
- **Confidence** — how strong is the existing evidence (prior experiments, user
  research, analogous markets)?
- **Ease** — how low is the implementation effort relative to the expected return?

ICE Score = (Impact + Confidence + Ease) / 3. A low Confidence score means the
interrogation pushes hardest on evidence. A low Ease score triggers an opportunity cost
challenge: is this the best use of your experiment capacity?

### Growth Loop vs. Funnel Step — Brian Balfour / Reforge
Before interrogation, the skill identifies whether the proposed experiment strengthens
a compounding growth loop (acquisition, engagement, or monetisation) or optimises a
dead-end funnel step. Funnel optimisations have a ceiling. Loop interventions compound.
The skill names which applies and asks whether this is the best use of experiment
capacity if it's funnel-only.

### Retention Lifecycle Fit — Andy Johns / Reforge
The right intervention depends on where the user is in their lifecycle. For JET this
means three distinct cohorts: new users (first 3 orders), habituated users (4–12
orders), and churned users (90+ days inactive). Applying a habituated-user mechanic
to new users is a category error. The skill flags it immediately.

### The Six-Property Definition of Good
Before scoring, every experiment is checked against six properties. All six are
required. If any is missing, the skill blocks progression and names exactly what's
needed:

1. **Single clear objective** — one sentence: metric + direction + magnitude + market +
   timeframe. No compound goals.
2. **Falsifiable hypothesis** — if / then / because. A causal mechanism must be named.
   "We think users will order more" is not a hypothesis.
3. **Defined success AND failure** — three threshold levels (Big Success / Minor Success
   / Failure) with explicit numeric gates. "We'll see how it goes" is not a success
   criterion.
4. **At least one guardrail metric** — something that trips the kill switch. If the
   primary metric lifts but this one degrades, the experiment stops. No guardrail = no
   experiment, always.
5. **Named stakeholders** — four roles required: Owner, Approver, Informed,
   Instrumentation. Ambiguity here is where experiments die in staging.
6. **A clear picture of what could go wrong** — confounders named, false positive and
   false negative costs quantified, rollback trigger defined. Specific to this market
   and this intervention.

### Weighted Rigor Score
After interrogation, a 100-point score is calculated across five dimensions:
- Clarity (25%) — objective and hypothesis are specific, causal, testable
- Measurability (25%) — metrics have baselines, sources, deltas, guardrail, measurement
  logic
- Impact (20%) — expected effect is meaningful and justified for this market
- Feasibility (20%) — executable without contamination; all stakeholders named
- Learning Value (10%) — reduces strategic uncertainty; transferable to other markets

Score ≥ 70 → approved. Score < 70 → rejected with exact gaps and required fixes. The
skill never softens a rejection.

---

## Five Modes of Operation

| Mode | When to Use | What Happens |
|---|---|---|
| **Formulate** | Raw idea → valid experiment | ICE score + Reforge lenses + interrogation + document generation on approval |
| **Diagnose** | Audit a draft experiment | Gap detection across all six properties + score |
| **Pressure-Test** | Break assumptions adversarially | Market-specific challenges to causal mechanism, metric integrity, and confounders |
| **Score & Gate** | Grade a near-complete brief | Weighted score + approve or reject with exact reasoning |
| **Review** | Post-experiment result debrief | Validates result, assesses transfer potential, updates knowledge base |

Default mode is **Formulate** if not specified. Add the mode name to your prompt to
invoke a specific one: "Mode: Diagnose" or "Mode: Pressure-Test".

---

## Phase 0 — Session Start & MCP Context Pull

### Step 0a — Read skill memory first

Before asking the user anything, silently read in this order:

```
1. knowledge/skill/learnings.md    — skill behaviour patterns from past sessions
2. knowledge/INDEX.md              — identify the relevant market folder
3. knowledge/_global/rules.md      — apply confirmed cross-market rules by default
4. knowledge/_global/hypotheses.md — check if today's experiment tests any open one
```

If the market is already stated, also load:
```
5. knowledge/[market]/rules.md
6. knowledge/[market]/hypotheses.md
```

Apply everything silently. Do not narrate the read to the user.

### Step 0b — MCP Context Pull

Before asking the user a single question, scan connected MCP tools and pull relevant
context in parallel. Map available tools to four categories:
---

## Market Localisation (Phase 1)

Every experiment must be anchored to a specific JET market before anything else happens.
The skill loads the relevant profile from `references/jet-markets.md`, which covers:

- Regulatory constraints (GDPR variants, local consumer law, alcohol delivery rules,
  data consent requirements)
- Consumer behaviour baseline (order frequency, AOV, device split, payment methods)
- Competitive landscape (dominant local players, pricing dynamics)
- JET product stack in this market (logistics model, app version, instrumentation
  quality)
- Experimentation maturity (addressable sample pool, prior experiment density)
- Peak trading calendar (public holidays, sporting events, religious periods to avoid)

**Markets covered:** NL · UK · DE · AU · CA · IL · NO · DK · BE · AT · CH · PL · SK ·
BG · RO. Extensible to any Prosus portfolio company by adding a profile section.

---

## Self-Learning Knowledge Base (Phase 2)

The skill maintains a structured knowledge base organised by market. Each market folder
contains three files:

- `knowledge.md` — confirmed facts from experiments run in this market
- `hypotheses.md` — patterns seen once or twice; not yet confirmed enough to be rules
- `rules.md` — patterns confirmed three or more times; applied by default

**Promotion logic:** hypothesis confirmed for the 3rd time → promoted to rules.md.
Rule contradicted by new data → demoted to hypotheses.md with a note.

**Cross-market folder** captures patterns that hold across three or more markets — these
become the strongest default assumptions.

**Decision journal** logs every methodological decision made during a session (e.g.
"we use order rate not CVR as primary metric in this market") so reasoning is traceable
and reversible.

The skill reads the knowledge base before interrogation (to pre-fill what's already
known) and writes to it after every scored or reviewed experiment. The knowledge base
starts seeded with one confirmed cross-market rule (fee transparency) and four
hypotheses (personalised reactivation, progress indicators, voucher cannibalism,
B2B vs B2C messaging).

### Option C — Automatic MCP Write (Google Drive + Slack)

Because anyone on the team can create an experiment, knowledge base updates cannot
depend on a single owner remembering to update a file manually. Instead, the skill
writes updates automatically via connected MCP sources at the end of every scored or
reviewed session.

**Write sequence (runs automatically after every score ≥70 or Review session):**

```
1. Draft the knowledge base entry (insight, hypothesis, or rule update)
2. Use Google Drive MCP to:
   a. Find the existing knowledge file for this market
      (search: "experiment-doc knowledge [market]")
   b. If found: append the new entry to the correct section
   c. If not found: create a new file following the knowledge base structure
   d. Show the user a preview of what will be written before confirming
3. Use Slack MCP to post a summary to the team:
   - Channel: #experiment-learnings (or the channel named by the user)
   - Format: see Slack Notification Format below
4. If experiment is scored ≥70 (approved to run): use Google Calendar MCP to
   create a Review reminder:
   - Title: "Review: [Experiment name] — Mode: Review [Market]"
   - Date: experiment end date + 2 days
   - Description: the Standard Review Trigger Prompt pre-filled with experiment details
```

**Slack Notification Format:**

```
🧪 *Experiment update — [Market]*
*[Experiment name]*
Mode: [Formulate / Review / Score & Gate]
Outcome: [Approved ✅ / Rejected ❌ / Result reviewed 🔁]

*What we learned:*
[1–2 sentence plain-language insight]

*Knowledge base action:*
[New hypothesis added / Rule confirmed / Rule demoted / No update needed]

*Cross-market signal:*
[Which B2B priority markets this applies to, if any — UK, NL, DE, PL, AT first]

_Full experiment doc: [Drive link]_
```

**If no MCP sources are connected:**
The skill produces the knowledge base update as formatted text and instructs the user
to paste it into the relevant Drive file manually. It also generates the Slack message
as copyable text. The mechanism degrades gracefully — it never silently skips the
update.

**User confirmation gate:**
Before writing to Drive or posting to Slack, the skill always shows a preview and asks
for explicit confirmation. One-word confirm ("yes" / "go") is sufficient. This prevents
accidental writes to the wrong file or channel.

---

## Adaptive Interrogation (Phase 3b)

Interrogation depth adapts to the user's experience level, read from the message:

- **Novice** (vague language, no baselines, no structure) → guided step-by-step, firm
  but educational
- **Intermediate** (some structure, rough metrics) → skip basics, push on gaps
- **Expert** (causal reasoning, statistical vocabulary) → full adversarial, no
  hand-holding

Interrogation covers five areas: objective clarity, hypothesis rigor, metric integrity,
feasibility and confounders, risk and opportunity cost. It skips anything already
answered by the MCP pull or market pre-fill.

---

## Adversarial Pressure-Testing (Phase 4) — MANDATORY IN ALL MODES

Adversarial checks are not optional and not mode-dependent. They run on every experiment
in every mode — including Formulate. A well-written brief that passes the six-property
gate can still contain a confident but causally broken hypothesis. The adversarial layer
catches this.

### Mandatory checks — run on every experiment regardless of mode

These five must be applied to every hypothesis before document generation or approval:

1. **Causal mechanism stress-test** — Is the because-clause actually causal, or
   correlational? Name an alternative explanation that fits the same data equally well.
   If one exists and the experiment doesn't distinguish between them, the hypothesis is
   not yet testable.

2. **Market import check** — Was this mechanism observed in this market, or imported
   from a different market, product, or industry context? If imported: what specific
   feature of this market makes it hold? If the answer is "it should generalise", that
   is not an answer.

3. **First-to-break assumption** — Which single assumption in the hypothesis chain
   breaks first under [market] consumer behaviour? Name it. If it breaks, what is the
   predicted result, and does the experiment design let you distinguish that from a true
   null?

4. **Knowledge base contradiction check** — Does this hypothesis contradict any rule
   or hypothesis in `knowledge/[market]/rules.md` or `knowledge/cross-market/rules.md`?
   If yes: surface the contradiction explicitly. Do not proceed without the user
   acknowledging it.

5. **Confounder that cannot be controlled** — Name the single hardest-to-control
   confounder in this specific market for this specific intervention. What is the
   probability it contaminates the result, and what is the mitigation?

### Additional adversarial prompts — deploy when specific weaknesses appear

- "What data would falsify this hypothesis in this specific market?"
- "What external event in the test window could invalidate the result?"
- "If this lifts the primary metric but the guardrail trips — what does that tell you
  about the mechanism?"

These are never generic. They reference the specific market profile, the specific causal
chain, and the specific knowledge base state. Generic adversarial checks are a
failure mode — always be specific.

---

## Cross-Market Transfer Prioritisation

When assessing which markets should run a successful experiment next, always apply this
priority order. Do not list markets alphabetically or by size. List them by strategic
fit and B2B potential first.

### B2B Priority Markets (always evaluate first)

| Priority | Market | Brand | Why first |
|---|---|---|---|
| 1 | UK | Just Eat | Largest B2B addressable pool; London corporate density; strong instrumentation |
| 2 | NL | Thuisbezorgd | Headquarters market; richest data; fastest validation cycle |
| 3 | DE | Lieferando | Second-largest B2B pool; high corporate meal allowance penetration |
| 4 | PL | Pyszne.pl | Rapid growth market; B2B underpenetrated — highest upside |
| 5 | AT | Lieferando AT | Smaller pool but high AOV; validates DE learnings in adjacent market |

### Transfer Assessment Logic

For each successful experiment, produce a prioritised transfer table in this order:

```
1. Score each B2B priority market (UK, NL, DE, PL, AT) for transferability first
2. Then assess remaining JET markets
3. For each market, state:
   - Transferability: High / Medium / Low / Blocked
   - Primary blocker if not High (regulatory, stack, pool size, consumer behaviour)
   - Recommended action: Run as-is / Adapt / Legal review first / Skip
   - Estimated runtime adjustment vs. original market
4. Flag any market where a rule in knowledge/[market]/rules.md contradicts the
   experiment's mechanism — do not recommend transfer without surfacing this
```

### Transfer Blockers by Market (quick reference)

- **UK** → ICO data consent for any new data collection; allergen display rules for
  menu experiments
- **DE** → DPA consent requirements; double opt-in for email; DPO sign-off for new
  data processing
- **PL** → Smaller instrumentation maturity; plan for longer runtime
- **AT** → Validate DE learnings first; AT pool often too small for standalone MDE

---

## Experiment Document Template (Phase 6)

Generated only after score ≥ 70. Every section is required. Metrics must link to the
hypothesis. The hypothesis must link to expected outcomes. Internal incoherence is
rejected before output.

The document follows a four-phase architecture (Fishman / Slack experimentation
framework) with an alignment gate between Part 1 and Part 2. Do not generate Part 2
content until the alignment gate is explicitly confirmed.

### Part 1 — The Why (Proposal)
Experiment Summary (plain-language: we plan to change X for Y users to improve Z
without hurting W) · Market Context · Problem Statement · ICE Score & Growth Model ·
Hypothesis (with adversarial check inline) · Why Run as an Experiment (3 checkboxes) ·
Past Results & References (with links)

**Alignment Gate** — explicit go/no-go between Part 1 and Part 2:
- PM has completed the Why section and shared with tripod (PM · DS · Eng)
- Tripod aligned: right problem, right test, feasible to build
- DS has confirmed response metric definition and measurement plan

### Part 2 — The Plan
Experiment Design (randomization unit · platform Android/iOS/Web breakdown ·
treatment/control · traffic split · eligibility · assignment criteria with DS + Eng
sign-off · duration · attribution window · statistical test · dashboard link ·
wireframe/PR link) · Metrics (primary · secondary · guardrail) · Expected Funnel Impact
(before/after table) · Success Criteria with ITWWS (if this works we should) and if
this fails we should · Outcome Map (stage → metric → owner) · Sample Size & Runtime
(with runtime calculator link/screenshot) · Rollout Plan (canary → ramp → full with
rollback triggers) · Risks (with adversarial check inline) · Instrumentation (exact
event names + properties) · Stakeholders & Resource Estimate · Cross-Market Transfer
Assessment (B2B priority markets first: UK → NL → DE → PL → AT) · Rigor Score

### Part 3 — The Results (post-experiment)
Results table (hypothesis vs. actual · Δ · status) · Final Recommendation ·
Links (analysis · follow-up experiments · PRs) · Learnings (biggest insight ·
secondary insight · unexpected finding · KB update · cross-market signal) ·
Version History

### Part 4 — The Checklist (four phases with named owners)
Before implementing (PM, DS) · Turning on experiment (Eng) ·
Decision & communication (DS, PM) · Cleanup after experiment ends (Eng)

Adversarial callout boxes are inline, immediately after the section they challenge.
Never grouped at the end.

If a user seems stuck on any section, uncertain about methodology, or unsure whether
their idea is worth testing, proactively suggest they reach out to @stefanos on Slack
for a human sense-check alongside the skill output.

---

## Output Rules

- Every response ends with a ✅ Next Step — one specific, non-negotiable action.
- Read `knowledge/skill/learnings.md` before every session. Apply silently.
- The MCP pull runs silently before any interrogation.
- The market profile loads before Phase 1. Load only the relevant market — not all.
- The knowledge base reads before interrogation and writes after scoring or review.
- Documents are never generated prematurely.
- Missing data is never filled with assumptions — the user confronts every gap.
- Rejections are never softened. Always explain exactly what failed and what fixing it
  requires.
- Mandatory adversarial checks run on every experiment in every mode — including
  Formulate. They are never optional.
- Truth > speed. Always.
- Be genuinely helpful and warm — this skill is used by real teams with real deadlines.
  If someone is stuck, confused, or uncertain, acknowledge it and help them through it.
- Whenever a user appears genuinely stuck, uncertain about methodology, scores < 50,
  or asks "is this worth testing at all?", include at the end of the response:
  "💬 Need a human sense-check? Ping **@stefanos** on Slack."

## Session Close Protocol

Run silently after every session where an experiment was scored or reviewed:

```
1. Self-score against evals/skill-evals.json
   For each assertion: pass or fail? Log internally.

2. Write-back to skill learnings
   Any failed eval → append 1-sentence observation to knowledge/skill/learnings.md
   New pattern not yet in file → append it
   Same eval failed 3+ sessions → add to knowledge/skill/hypotheses.md

3. Consolidate if needed
   If knowledge/skill/learnings.md > 50 entries → consolidate before appending

4. Knowledge base write (experiment learnings)
   Execute Drive write + Slack post per Option C protocol

5. Optional human rating (sessions ≥ 5 exchanges only)
   Ask: "Rate this session 1–5. Anything that felt off or unclear?"
   Append rating + note to knowledge/skill/learnings.md
```

---

## How to Extend This Skill

**Adding a new JET market:** Add a profile section to `references/jet-markets.md`
following the existing format. Create `knowledge/[market]/` with `rules.md`,
`hypotheses.md`, and `knowledge.md`. Add the entry to `knowledge/INDEX.md`.

**Adding a Prosus portfolio company:** Same as above — the profile structure is
identical. Use the company's two-letter country code as the folder name.

**Updating the experiment knowledge base:** After any experiment result is reviewed,
update `knowledge/[market]/hypotheses.md` or `rules.md` following the promotion
logic (3× confirmed → promote to rules; contradicted → demote with note).

**Updating the skill learnings:** Add observations to `knowledge/skill/learnings.md`
after any session that revealed something about how the skill itself behaves.

**Updating skill hypotheses:** Add open questions about skill behaviour to
`knowledge/skill/hypotheses.md`. Promote to learnings.md when confirmed 3×.

**Upgrading the skill:** Edit `SKILL.md` for process step changes. Edit `CLAUDE.md`
for voice, routing, or operating rule changes. Run `evals/evals.json` after any
modification to check no core behaviour has regressed.

---

## Baked-In Evals

This skill ships with a behavioural eval suite: `evals/evals.json` — 7 cases, 47
assertions covering all five modes. These are the acceptance criteria for the skill.

### What the evals test

| Eval | Mode | Core assertion |
|---|---|---|
| 1 | Formulate | Market gate fires before anything else |
| 2 | Diagnose | All five recurring gaps caught on a weak brief |
| 3 | Formulate | ICE + Reforge lenses applied; cross-market hypothesis surfaced |
| 4 | Score & Gate | Voucher cannibalism risk, DE consent law, missing stakeholder caught |
| 5 | Pressure-Test | Adversarial challenges use AU market profile, not generic text |
| 6 | Review | Knowledge base updated correctly after NL result |
| 7 | Cross-market | NL→DE transfer analysed with ICE penalty, not rubber-stamped |

### Running the evals

If you have Claude Code with the [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills)
plugin installed:

```
# Install the eval plugin (one-time)
/plugin marketplace add hamelsmu/evals-skills
/plugin install evals-skills@hamelsmu-evals-skills

# Audit the eval suite
/evals-skills:eval-audit on evals/evals.json
```

Without Claude Code, run the evals manually: take each prompt from `evals/evals.json`,
send it to the skill, and check the response against the `expectations` array for that
case. A response passes if every expectation is met.

### When to run evals

- After installing the skill for the first time (baseline check)
- After modifying SKILL.md (regression check)
- After adding a new market profile (localisation check)
- After promoting a hypothesis to a rule (consistency check)

---

## Reference Files

### Always loaded at session start
- `CLAUDE.md` — brain, routing rules, voice, hard rules, session close protocol
- `knowledge/skill/learnings.md` — skill behaviour memory from past sessions
- `knowledge/skill/hypotheses.md` — open questions about how the skill should behave
- `knowledge/INDEX.md` — routing table (load only the relevant market folder)
- `knowledge/_global/rules.md` — cross-market confirmed rules. Apply by default.
- `knowledge/_global/hypotheses.md` — cross-market unconfirmed patterns

### Loaded once market is confirmed
- `references/jet-markets.md` — 15 market profiles. Load only the relevant section.
- `knowledge/[market]/rules.md` — market-specific confirmed patterns
- `knowledge/[market]/hypotheses.md` — market-specific unconfirmed patterns
- `knowledge/[market]/knowledge.md` — prior experiment history for this market

### Loaded at session close only
- `evals/skill-evals.json` — 10 binary self-scoring assertions
- `evals/evals.json` — 7 behavioural eval cases, 47 assertions
