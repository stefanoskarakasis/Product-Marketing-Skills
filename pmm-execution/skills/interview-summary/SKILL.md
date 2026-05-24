---
name: hs-interview-summary
version: 2.0.0
description: >
  A self-improving customer interview synthesis engine for PMMs, Product Managers, and
  UX Researchers. Transforms raw transcripts into structured discovery outputs anchored
  in JTBD theory, with signal-level pattern detection, confidence scoring, and a
  compounding learning loop. Trigger on: "summarize interview", "process transcript",
  "interview summary", "what did customers say", "synthesize discovery", "interview
  debrief", "JTBD analysis", "customer insight", "research synthesis", or any request
  to process, structure, or extract meaning from a customer or prospect interview.
---

# hs-interview-summary — Customer Discovery Synthesis Engine

Transforms raw interview transcripts into structured intelligence.
Not a transcription service. A synthesis engine that extracts Jobs, surfaces patterns,
flags contradictions, and compounds learning across every session.

Built on JTBD theory. Sharpened for B2B product and GTM contexts.

---

## ⓪ PMM CONTEXT — LOAD FIRST

Before intake, check `.agents/product-marketing-context.md`.

**If it exists — load silently. Extract:**

- `## ICP Prioritisation` → does this interviewee match the ICP? Flag if they don't.
- `## Positioning` → does what they said validate or challenge current positioning?
- `## Objections & Anti-Personas` → flag any new objections or anti-persona signals in the transcript.
- `## Revenue Levers` → which lever does the discovered Job connect to?
- `## Beachhead Segment` → does this interviewee represent the beachhead or an adjacent segment?

**If context file is missing:**

Surface once, non-blocking:
> "No PMM context found. Run `hs-product-marketing-context BUILD` first to make
> pattern detection significantly sharper. Continuing — but insights will be
> transcript-isolated, not connected to your positioning or ICP."

---

## RELATED SKILLS

Cross-reference when findings trigger downstream work:

- **hs-product-marketing-context** → positioning signal from interview → update here
- **hs-competitive-battlecard** → competitor mentioned as current solution → LEARN mode
- **hs-value-prop-statements** → strong Job discovered → pressure-test value prop against it
- **hs-gaccs-brief** → messaging hypothesis surfaced → route here for campaign brief
- **hs-pre-mortem** → risk or failure mode surfaced by customer → route here
- **hs-brainstorm-okrs** → success metric gap surfaces → route here

---

## ① INTAKE — ORIENT BEFORE SYNTHESIZING

> ⚠️ Never summarize a transcript cold. Always establish context first.
> A context-blind summary misses what matters.

If the user pastes a transcript or file with no context, ask in one message:

> "Before I synthesize this, give me three things:
>
> 1. **Who is this?** Role, company, segment — and does this person match your ICP?
> 2. **What was the purpose of this interview?** (Discovery / Validation / Win-loss /
>    Churn / Competitive / Onboarding / Other)
> 3. **Is there anything specific you're trying to learn or confirm?**
>    (If yes, I'll weight those areas. If no, I'll surface what's most surprising.)"

If context is already provided, proceed directly. Don't ask questions whose answers are visible.

---

## ② TRANSCRIPT INTAKE

Accept transcripts in any of the following formats:
- Pasted plain text
- Uploaded `.txt`, `.md`, or `.pdf` file
- Audio transcription output (Otter.ai, Fireflies, Rev, etc.)
- Structured note dump (bullet points, rough notes)

For uploaded files: read the full file before producing any output.

For rough notes or partial transcripts:
> "This looks like abbreviated notes rather than a verbatim transcript.
> I'll synthesize from what's here — flag anything you want me to treat with
> more precision before I continue."

---

## ③ PRE-SYNTHESIS AUDIT

Before generating the summary, run a silent internal check:

**Coverage audit:**
- [ ] Does the transcript cover enough to identify at least one Job?
- [ ] Is the interviewee's current solution identifiable?
- [ ] Are there satisfaction signals — even implicit ones?
- [ ] Are there any verbatim quotes worth preserving exactly?

**Signal scan:**
- [ ] Any mention of a competitor by name?
- [ ] Any language that matches or contradicts current positioning?
- [ ] Any Job or outcome that contradicts existing ICP assumptions?
- [ ] Any emotional signal (frustration, surprise, delight)?

If coverage is too thin to produce a reliable summary:
> "This transcript is too sparse to synthesize with confidence.
> Here's what I can extract: [list]. What I'd flag as missing: [list].
> Proceed with caveats, or go back for a follow-up?"

---

## ④ SUMMARY OUTPUT — STRUCTURED TEMPLATE

````
---
# Interview summary
hs-interview-summary v2.0.0
---

## 📋 Metadata

**Date:** [Date and time]

**Participants:** [Interviewer name + role] | [Interviewee name + role + company]

**Interview type:** [Discovery / Validation / Win-loss / Churn / Competitive / Other]

**Confidence:** [🟢 High — full transcript / 🟡 Medium — partial / 🔴 Low — rough notes]

**ICP match:** [Yes / Partial / No — one-line reason if not Yes]

---

## 🏢 Background

[Role, company, team size, and any relevant context about their situation.]

---

## 🛠️ Current solution

[What they use today — tool, process, or workaround.]

---

## ✅ What they like about their current solution

- **[Strength label]:** [What Job it satisfies and how.]

---

## 🔴 Problems with their current solution

**Job:** [The functional task they're trying to get done]

**Desired outcome:** [What success looks like for them]

**Importance:** [Critical / High / Medium / Low] — [one-line evidence]

**Satisfaction:** [Not satisfied / Partially / Satisfied] — [one-line evidence]

**Verbatim signal:** *"[Exact quote if available]"*

[Repeat block per Job. Separate each with a line break.]

---

## 💡 Key insights

- [Unexpected finding or analytical observation — no quotes here, pure interpretation.]

---

## 📋 Action items

| Date | Owner | Action |
|------|-------|--------|
| YYYY-MM-DD | [Name] | [Specific action] |

---

## ⚠️ Flags

- **[Flag label]:** [What it contradicts and why it matters.]

---

## 🗣️ Signal quotes

> *"[Quote]"* — [Speaker, context. What makes this one irreplaceable.]

---

## 📊 Pattern signal

**Matches existing pattern:** [Yes / No / Partial]

**New signal for tracking:** [Yes / No]

**Hypothesis triggered:** [State it, or "None"]
````

---

## ⑤ CONFIDENCE SCORING

Apply a three-level confidence score to the whole summary:

**🟢 High** — Full verbatim transcript, clear interviewee context, identifiable Jobs
**🟡 Medium** — Partial transcript, rough notes, or ambiguous signals
**🔴 Low** — Very sparse notes, single-source claim, no verbatim quotes

For 🔴 summaries, prepend a warning block:
> "⚠️ Low-confidence summary. Findings below are based on thin input.
> Do not route downstream without a follow-up or validation pass."

---

## ⑥ KNOWLEDGE ARCHITECTURE — LEARNING LOOP

> This is what turns a transcript processor into a discovery intelligence system.

**Before generating the summary**, check:
- `knowledge/interviews/patterns.md` — confirmed patterns across sessions
- `knowledge/interviews/hypotheses.md` — active hypotheses being tracked
- `knowledge/interviews/rules.md` — rules derived from 3+ confirmed hypotheses

Apply confirmed rules by default. Check if any hypothesis can be tested against today's transcript.

**After generating the summary**, extract and store:

```
knowledge/interviews/
  patterns.md   — recurring Jobs, pain patterns, vocabulary across interviews
  hypotheses.md — signals worth tracking but not yet confirmed
  rules.md      — confirmed patterns (3+ instances) — apply to future syntheses
  INDEX.md      — router to all knowledge domains
```

**Hypothesis promotion rule:**
When a pattern appears in 3 or more interviews, promote it from `hypotheses.md` to `rules.md`.
Propose the promotion to the user. Apply only with explicit approval.

**Rule demotion rule:**
If a confirmed rule is contradicted by a new interview, flag it:
> "⚠️ This interview contradicts Rule [X]: '[rule]'. Recommend demoting to hypothesis.
> Confirm demotion?"

---

## ⑦ DECISION JOURNAL

When a summary produces a significant strategic decision (repositioning signal, ICP update,
Jobs model revision, messaging change), log it:

File: `decisions/YYYY-MM-DD-{topic}.md`

```
## Decision: [what was decided]
## Context: [what interview finding triggered this]
## Alternatives considered: [what else was on the table]
## Reasoning: [why this interpretation won]
## Trade-offs accepted: [what uncertainty you're accepting]
## Supersedes: [prior decision, if replacing one]
```

Before logging a new decision, check `decisions/` for prior decisions in the same area.
Follow existing decisions unless this interview provides contradicting evidence.

---

## ⑧ QUALITY GATE

Before delivering the summary, run this internal check. Do not show the checklist to the user.
If the summary fails, fix it before output. Report only if a critical failure can't be resolved.

**Structure:**
- [ ] Every Job block has all five fields populated — no blanks
- [ ] Each Job field starts on its own line — no block text
- [ ] Key insights contain only analysis — no verbatim quotes (those go in Signal quotes)
- [ ] Signal quotes are verbatim — not paraphrased
- [ ] Action items have named owners and real dates — no placeholders
- [ ] Flags section is populated, or explicitly marked "None detected"

**Signal integrity:**
- [ ] No insight is stated as fact if it's based on a single, unverified quote
- [ ] Confidence score matches the quality of the transcript input
- [ ] Any new signal that contradicts existing rules is flagged, not suppressed

**PMM context check (if loaded):**
- [ ] ICP match is assessed — not defaulted to "Yes"
- [ ] Positioning signals are noted in Key Insights or Contradictions, not omitted

**Hard block — do not output if:**
- The transcript is too thin to produce even one credible Job
- The interviewee context is unknown and cannot be inferred

---

## ⑨ LEARNING CLOSE

At the end of every synthesis session, run this close.

First, an open prompt:
> "Before we wrap — what surprised you most about this interview, or what do you
> wish I'd flagged that I didn't?"

Then three structured questions:

1. **Pattern check:** "Does this change what you believe is the most important Job
   for [ICP segment / product area]?"
2. **Positioning check:** "Did anything in this transcript make you want to change
   how you describe the problem or the solution?"
3. **Skill check:** "Anything in the summary format or depth that should work
   differently next time?"

After the user responds:
- If patterns shift → update `knowledge/interviews/hypotheses.md`
- If positioning changes → flag for `hs-product-marketing-context` update
- If skill improvement identified → propose a SKILL.md patch with exact change

> "Want me to update the skill with that change? I'll show you the diff before applying."

Only apply updates with explicit user approval.

---

## SESSION METADATA

Every summary saved to `sessions/` carries:

```
_Interviewee: [role + company]_
_Interview type: [type]_
_Session date: YYYY-MM-DD_
_ICP match: Yes / Partial / No_
_Confidence: 🟢 / 🟡 / 🔴_
_QG: Pass / Fail_
_New hypothesis triggered: Yes / No_
_Version: 2.0.0_
```

---

## INTEGRATION MAP

| Skill | When to cross-reference |
|---|---|
| `hs-product-marketing-context` | Always — load before synthesis |
| `hs-competitive-battlecard` | Competitor named as current solution |
| `hs-value-prop-statements` | Strong Job discovered — pressure-test messaging |
| `hs-gaccs-brief` | Messaging hypothesis surfaced in interview |
| `hs-pre-mortem` | Customer surfaced a failure mode or risk |
| `hs-brainstorm-okrs` | Success metric gap or KR signal discovered |

---

## KNOWLEDGE INDEX

`knowledge/interviews/INDEX.md` routes to:

```
patterns.md   — recurring Jobs and pain signals across all interviews
hypotheses.md — active hypotheses (< 3 confirmations)
rules.md      — confirmed patterns (3+ confirmations) — applied automatically
decisions/    — strategic decisions derived from interview synthesis
sessions/     — archived summaries with full metadata
```

---

## COMMANDS

Run these at any point in a session.

| Command | What it does |
|---------|-------------|
| `/summarize [transcript or file]` | Run the full synthesis flow on a transcript |
| `/summarize-quick [transcript or file]` | Output only: skips intake questions, runs pre-synthesis audit silently, produces summary immediately |
| `/patterns` | Show all active patterns, hypotheses, and rules from the knowledge base |
| `/hypotheses` | Show active hypotheses and their current confirmation count |
| `/promote [hypothesis name]` | Propose promotion of a hypothesis to a confirmed rule |
| `/flags` | List all flags across sessions — contradictions with positioning or ICP assumptions |
| `/decisions` | Show all logged strategic decisions from prior sessions |
| `/close` | Run the Learning Close for the current session |
| `/save` | Save the current summary to `sessions/` with full metadata |
| `/help` | Show available commands and current knowledge base status |

---

## SAMPLE PROMPTS

**Basic — paste transcript**
```
/summarize
[paste transcript]
```

**Basic — with file**
```
/summarize
[attach transcript file]
```

**With context upfront — skip intake questions**
```
/summarize
Interviewee: Head of RevOps, ~200-person SaaS. Matches ICP.
Purpose: Discovery — understand current reporting pain and switching triggers.
[paste transcript]
```

**Win/loss**
```
/summarize
This is a win/loss interview with a customer who chose [Competitor] over us.
Focus on which Job we lost and why.
[paste transcript]
```

**Churn debrief**
```
/summarize
Churn interview. Focus on the Jobs they hired us for vs. what broke down.
Flag any signal that should update our ICP.
[paste transcript]
```

**Quick output — no intake, straight to summary**
```
/summarize-quick
[paste transcript]
```

**Check knowledge base after multiple sessions**
```
/patterns
```

**Run the learning close after a session**
```
/close
```

---

## CHANGELOG

### v2.0.1 — 2026-04-20
Formatting and structure patch from review session.

- Output template updated: all Metadata fields now on separate lines
- Output template updated: all Problems with their current solution fields now on separate lines
- Section order confirmed: Pawel's six core sections first, extensions (Flags, Signal quotes, Pattern signal) after
- Key insights and Signal quotes split: Key insights = analysis only, Signal quotes = verbatim only
- Action items table simplified: Priority column removed from default template
- Background and Current solution separated into distinct sections (matching Pawel's original structure)
- Commands block added
- Sample prompts updated with `/summarize`, `/summarize-quick`, `/close`, `/patterns`
- Quality Gate updated to reflect new section names and formatting rules

### v2.0.0 — 2026-04-20
Full rebuild from v1.0.0. Breaking changes throughout.

**Architecture upgrades:**
- PMM context loading block added (Section ⓪)
- Related Skills cross-references added
- Intake orientation step added (Section ①) — prevents cold synthesis
- Pre-synthesis audit added (Section ③) — coverage and signal scan before output
- Confidence scoring system added (Section ⑤)
- Knowledge Architecture / Learning Loop added (Section ⑥) — patterns, hypotheses, rules
- Decision Journal added (Section ⑦)
- Quality Gate added (Section ⑧)
- Learning Close added (Section ⑨)
- Session metadata block added
- Integration Map added

**Output template upgrades:**
- ICP match + Confidence added to Metadata
- JTBD block restructured per Job: five fields, each on its own line
- Signal quotes section added — verbatim only, separate from Key insights
- Flags section added — contradictions with positioning and ICP
- Pattern signal block added — connects to knowledge layer
- Action items converted to table with named owner and date

**Removed:**
- Author credit removed
- Static "further reading" links removed — replaced by Related Skills routing

### v1.0.0 — original
Simple transcript-to-template. JTBD template, action items, further reading.
