---
name: interview-summary
version: 2.3.0
description: >
  Customer interview synthesis engine for PMMs, Product Managers, and UX Researchers.
  Transforms raw transcripts into structured discovery outputs anchored in JTBD theory,
  with signal-level pattern detection and confidence scoring.
  Trigger on: "summarize interview", "process transcript", "interview summary", "what did customers say", 
  "synthesize discovery", "interview debrief", "JTBD analysis", "customer insight", "research synthesis", 
  or any request to process, structure, or extract meaning from a customer or prospect interview.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-21
---
# interview-summary — Customer Discovery Synthesis Engine

Transforms raw interview transcripts into structured intelligence.
Not a transcription service. A synthesis engine that extracts Jobs, surfaces patterns,
and flags contradictions with your positioning or ICP.
Built on JTBD theory. Sharpened for B2B product and GTM contexts.

---
## Trigger
- **When:** Any customer or prospect interview needs synthesis into structured discovery output.
  This includes: discovery calls, win/loss debriefs, churn interviews, competitive research interviews,
  onboarding feedback, feature validation calls, or any call where you need to extract Jobs, map solutions,
  and flag contradictions with your positioning or ICP.
- **Not for:**
  - **interview-summary** is not a transcription tool — use Otter.ai or Fireflies for that.
  - **interview-summary** is not for analyzing *your own* positioning or messaging in isolation.
    If you need to check whether your messaging lands with buyers, route to `positioning-messaging` or `gaccs-brief`.
  - **interview-summary** is not for building buyer personas from scratch without interviews.
    No dedicated persona-building skill exists yet; this skill synthesizes existing transcript data only.
- **Example prompts:**
  - "Summarize this customer discovery call and flag which Jobs matter most"
  - "I have a win/loss interview — help me extract what we lost and why"
  - "Process this transcript. Flag any positioning signal that contradicts our current narrative"
  - "Churn interview debrief — what Job did we fail to deliver on?"
---
## Inputs
- **Args:** Path to a transcript file (`.txt`, `.md`, `.pdf`), pasted plain text,
  structured note dump, or Otter/Fireflies/Rev transcription output.
  Optional: interview context (interviewee role, company, interview purpose).
  Free format — transcript alone is sufficient; context makes synthesis sharper.
- **Defaults:** If no context provided, skill asks three orientation questions.
  If interviewee segment unknown, default to "Unclassified" in ICP match.
  If no interview type specified, default to "Discovery".
- **Context keys:**
  - `/foundation/brain.md` (ICP, Positioning, Beachhead Segment sections) — optional, if exists: load for validation
  - `/context/meta-patterns.md` — optional; recurring patterns the user has logged from prior interviews
---
## Pre-flight
- If `/context/meta-patterns.md` exists in the user's workspace, check for recurring patterns they've logged from prior interviews. If one applies, surface a guardrail prompt before Step 1. Skip silently if the file doesn't exist.
- Load `/foundation/brain.md` if it exists. Extract: ICP Prioritisation, Positioning, Beachhead Segment, Revenue Levers.
  If missing, surface non-blocking notice: "No brain context. Synthesis will be transcript-isolated."
- Accept transcript in any format: pasted text, uploaded file (`.txt`, `.md`, `.pdf`),
  or structured notes. Read the full file before producing output.
- Identify interview type (Discovery / Validation / Win-loss / Churn / Competitive / Other)
  from context or ask in intake step.
---
## Steps
**Step 1: Orientation & Context Load**
- If no context provided, ask: "Who is this? (role, company, segment) | What was the purpose? | What are you trying to learn?"
- Load `/foundation/brain.md` and extract ICP, Positioning, Beachhead Segment for validation.
- Declare interview type and confidence upfront.
**Step 2: Intake & Pre-Synthesis Audit**
- Read transcript in full.
- Run silent pre-synthesis audit: Does it have ≥1 identifiable Job? Current solution? Satisfaction signals? Verbatim quotes?
- If too sparse, surface: "Coverage too thin. What I can extract: [list]. Proceed with caveats or follow up?"
- If adequate: proceed to synthesis.
**Step 3: JTBD Synthesis & Pattern Matching**
- Extract Jobs (functional, emotional, social).
- For each Job: Desired outcome, Importance, Satisfaction level, Verbatim signal.
- If `/context/meta-patterns.md` exists, check whether any cross-skill pattern logged there applies.
- Flag any new signal worth tracking: is this a new Job type or pattern the user hasn't seen before?
**Step 4: Validation Against Context**
- ICP match: Does this interviewee match the ICP? Flag if not.
- Anti-ICP discovery: Does this interview surface a signal that suggests this segment is a poor fit? (e.g., "Long procurement cycles are a blocker").
- Positioning signal: Does what they said validate or contradict current positioning?
- Beachhead alignment: Does this person represent the beachhead or an adjacent segment?
- Objection discovery: Any new objection or anti-persona signal?
**Step 5: Generate Structured Summary**
- Produce markdown summary with template structure.
- All Metadata fields on separate lines; all Job fields on separate lines; separate Key Insights (analysis only) from Signal Quotes (verbatim only).
- Include Action Items table with named owners and dates.
- Include Flags section (contradictions with positioning or ICP) or explicitly mark "None detected".
**Step 6: Surface Learnings**
- If a strategic signal surfaced (an ICP change, a positioning contradiction, a new pattern worth tracking),
  name it explicitly and ask the user if and where they'd like it saved — their own notes, a
  brain-adjacent doc, or `/context/meta-patterns.md` if they maintain one. This skill does not
  write to any file on its own.
- If an anti-ICP signal was discovered, flag it and ask if the user wants to update
  `/foundation/brain.md` Section 2 themselves — offer to draft the wording, but don't write it.
**Step 7: Learning Close**
- Ask: "What surprised you most? Wish I'd flagged anything else?"
- Ask: "Does this change your view of the most important Job?"
- Ask: "Does this change how you want to describe the problem?"
---
## Outputs
- **Chat output format:** Structured markdown summary with Metadata, Background, Current Solution, What they like, Problems (JTBD blocks),
  Key Insights, Action Items table, Flags, Signal Quotes, Pattern Signal.
  All output in markdown, copy-paste ready for Notion, GitHub, or email.
- **External side effects:** None. This skill does not write to any file on its own — any
  saves happen only if the user asks and confirms where.
---
## Verification
- [ ] Guardrails checked if `/context/meta-patterns.md` exists
- [ ] Every summary includes Metadata with Date, Participants, Interview Type, Confidence, ICP Match.
- [ ] Every Job block has: Job name, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
- [ ] Key Insights contain only analysis — no verbatim quotes (those go in Signal Quotes section).
- [ ] Signal Quotes are verbatim, not paraphrased. Include speaker name and context.
- [ ] Action Items table has named owners (not placeholders) and real dates (YYYY-MM-DD format).
- [ ] Flags section is populated with contradictions, or explicitly states "None detected".
- [ ] ICP match is assessed (not defaulted to "Yes") — reasoning included if "Partial" or "No".
- [ ] Anti-ICP signals are flagged and surfaced to the user, not silently dropped.
- [ ] Positioning signals are noted in Key Insights or Flags, not omitted.
- [ ] If sparse transcript: confidence is 🔴 Low and warning prepended.
---
## Do Not Use For
- **Transcription** — use Otter.ai, Fireflies, or Rev. This skill synthesizes, not transcribes.
- **Building personas from scratch** — no dedicated skill exists yet. This skill processes existing interviews.
- **Analyzing your own positioning in isolation** — use `positioning-messaging` or `gaccs-brief`.
  Route: `positioning-messaging` for positioning audit, `gaccs-brief` for campaign messaging.
---
## Operating Rules
1. **Context-first synthesis** — Load `/foundation/brain.md` before synthesis, if it exists.
   If missing, surface non-blocking notice. Synthesis is transcript-isolated if context missing.
2. **Full transcript read** — Never summarize from a partial read. Read the complete file before output.
3. **Confidence calibration** — Score (🟢 High / 🟡 Medium / 🔴 Low) based on transcript quality and completeness.
   For 🔴 summaries, prepend explicit warning. Confidence must match input quality, not optimism.
4. **Every Job gets all five fields** — Job, Desired outcome, Importance + evidence, Satisfaction + evidence, Verbatim signal.
   No blank fields. No block text. Each on its own line.
5. **Verbatim quotes are sacred** — Signal Quotes are exact verbatim. Key Insights are pure analysis, no quotes.
   Never paraphrase a quote as verbatim. Never bury a quote in an insight.
6. **ICP match is assessed, not defaulted** — If interviewee matches ICP: state "Yes". If partial match: state "Partial" with reason.
   If doesn't match: state "No" with reason. Never default to "Yes" for convenience.
7. **Anti-ICP discovery is actionable** — If interview surfaces a signal like "long procurement cycles", flag it explicitly.
   Offer to draft an update for the user to make themselves. Don't suppress it.
8. **Positioning signals are explicit** — If interview validates positioning, state it. If contradicts, flag it.
   If neutral, mark as such. Don't suppress contradictions.
9. **Interview type shapes the synthesis** — Win/loss emphasizes what we lost and why.
   Churn emphasizes Job delivery failure. Discovery emphasizes new Jobs. Validation emphasizes confirmation or contradiction.
   Weighting differs by type; synthesis logic adapts.
---
## Quality Gate
| Check | Standard | Pass = |
|---|---|---|
| Guardrails surfaced | `/context/meta-patterns.md` checked if it exists | Yes |
| Frontmatter complete | name, version, description, metadata present | Yes |
| All required sections | Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For, Operating Rules, Quality Gate | Yes |
| Steps named and imperative | Steps in imperative form | Yes |
| Outputs specify all sub-fields | Chat format, side effects | Yes |
| Verification is concrete | Checkable checks | Yes |
---
## Summary Output Template
````markdown
---
# Interview Summary
interview-summary v2.3.0
---
## 📋 Metadata
**Date:** [Date and time]
**Participants:** [Interviewer name + role] | [Interviewee name + role + company]
**Interview type:** [Discovery / Validation / Win-loss / Churn / Competitive / Other]
**Confidence:** [🟢 High / 🟡 Medium / 🔴 Low]
**ICP match:** [Yes / Partial / No — one-line reason if not Yes]
**Anti-ICP signals:** [List if any, else "None detected"]
---
## 🏢 Background
[Role, company, team size, and context about their situation.]
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
**New signal for tracking:** [Yes / No]
**Anti-ICP signal detected:** [Yes / No — specific signal]
````
---
## Related Skills
Cross-reference when findings trigger downstream work:
- **product-marketing-context** → Always load first. Use to validate ICP, Positioning, Beachhead.
- **gaccs-brief** → Messaging hypothesis surfaced → route here for campaign brief.
- **pre-mortem** → Risk or failure mode surfaced by customer → route here.
- **pmm-okrs** → Success metric gap surfaces → route here for KR signal.
---
## Commands
| Command | What it does |
|---------|-------------|
| `/summarize [transcript or file]` | Run the full synthesis flow on a transcript |
| `/summarize-quick [transcript or file]` | Output only: skips intake questions, produces summary immediately |
| `/close` | Run the Learning Close for the current session |
| `/help` | Show available commands |
