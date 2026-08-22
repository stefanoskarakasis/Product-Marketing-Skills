---
name: product-marketing-context
description: Build and maintain the shared GTM brain — product context, ICP, positioning, voice, market context, and proof points — that every other skill in this stack reads before producing output. Works standalone with your own answers, supercharged when you connect docs or a CRM. Trigger with "build my brain", "set up my GTM foundation", "audit my brain", "update my ICP", or "check brain health".
---

# Product Marketing Context (The Brain)

Stop re-explaining your company, your buyer, and your competitors to every tool you use. Answer these questions once, in about 15 minutes, and every other skill in this stack reads the answers automatically instead of asking again.

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRODUCT MARKETING CONTEXT                     │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone)                                       │
│  ✓ You tell me: product, ICP, alternatives, voice, market,      │
│    proof points — one section at a time                         │
│  ✓ Output: /foundation/brain.md, confirmed section by section   │
│  ✓ Pushes back on vague answers before storing them             │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Docs/Drive: pulls company overview and product facts          │
│  + CRM: pulls win/loss reasons and deal data to sharpen ICP      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

When you run this skill, I'll check for an existing brain first:

**No brain yet:**
- I'll ask for what I need, one section at a time — product, ICP, alternatives, voice, market, proof points
- You confirm each section before I save it

**Brain exists:**
- I load it silently and skip anything already answered
- Choose: [View current] [Edit a section] [Run health audit]

**Helpful if you have it:**
- A pitch deck, pricing page, or win/loss doc you can paste in
- Prior positioning or ICP notes, even rough ones

---

## Connectors (Optional)

Connect your tools to supercharge this skill:

| Connector | What It Adds |
|-----------|--------------|
| **Docs/Drive** | Company overview, pricing, and product docs — instead of typing them in |
| **CRM** (e.g. HubSpot, Salesforce) | Win/loss reasons and deal velocity to sharpen ICP and buying triggers |

> **No connectors?** No problem. Paste what you have — a deck excerpt, a pricing page, a win/loss doc — and I'll work from that.

---

## Output Format

```markdown
# Brain Update: [Section Name]

## What Changed
[Old value → New value, or "New — first time this section is filled"]

## Section Status
[Confirmed / Needs another pass — specific gap noted]

## Health Score (if audit was run)
| Section | Score | Status |
|---------|-------|--------|
| Product Context | X/100 | ... |
| ICP | X/100 | ... |
| Alternatives & Positioning | X/100 | ... |
| Voice & Tone | X/100 | ... |
| Market Context | X/100 | ... |
| Proof Points | X/100 | ... |

## Next Step
[One sentence — what to run or fix next]

---
_Brain update proposed: [Yes — exact section and field / No — audit or view only]_
```

---

## Execution Flow

### Step 1: Detect Brain State

Check for `/foundation/brain.md`.

- **Missing:** Explain in one line what the brain does, then start the wizard from Section 1.
- **Exists:** Load all sections silently. Offer: [View current] [Edit a section] [Run health audit].
- **Legacy files found** (`.agents/*.md`, `.claude/*.md`): offer to migrate, showing each extracted value before writing anything.

### Step 2: Run the Wizard

Ask one question at a time. After each section, show the collected answers and ask "Look good? (yes / edit / skip)." Push back on vague answers before storing them — "small businesses" is not a company size, "everyone" is not an ICP.

1. **Product Context** — product name; 2-3 sentence description (problem, not features); stage (pre-launch/launch/growth/scale); target market; value proposition ("[Product] helps [market] to __ so they can __")
2. **ICP Definition** — company size; industry/vertical; geography; primary persona (title + role); economic buyer; champion profile; top 3 pain points; buying trigger
3. **Alternatives & Positioning** — top 3 named alternatives (products buyers actually compare you to, not "competitors" in the abstract); status quo if they buy nothing; why they leave alternatives for you; your unique capabilities; category; market type (existing/new/resegmented)
4. **Voice & Tone** — 3-5 voice attributes; tone shifts by persona; language preferences ("we say X not Y"); forbidden phrases; one paragraph of copy that sounds like you
5. **Market Context** — market maturity; macro forces making this relevant now; "buyers need this now because __"; the 2-3 sentence market narrative
6. **Proof Points Registry** — approved metrics with sources; customer quotes/case study results; forbidden claims

### Step 3: Write the Brain File

Once a section is confirmed, write it to `/foundation/brain.md` using the template at `templates/brain-template.md`. Write section by section, not in one batch — a mid-wizard exit should still leave a partial, usable brain plus a `.brain-draft.md` marker noting which section to resume from.

### Step 4: Health Audit (Run Standalone or After Edits)

Score each of the 6 sections 0-100 on: does the field exist, and is it specific rather than generic (named alternatives not "competitors," numbers not "high," a real persona not "businesses"). Report strengths (80+), needs improvement (50-79), and critical gaps (<50), with one concrete fix per gap. Offer to jump straight into editing the weakest section.

### Step 5: Route to What's Next

After any completed setup, edit, or audit, tell the user plainly that the brain is ready and other skills in the stack will read from it automatically. Do not name a specific downstream skill unless you have verified, in this session, that it reads this brain's real section structure correctly — an unverified skill name is a broken promise.

---

## Quality Gate

| Check                                          | Pass =                          |
|-------------------------------------------------|----------------------------------|
| Brain state checked before any question asked  | Yes                              |
| No section written without user confirmation   | Yes                              |
| Vague answers challenged, not silently stored  | Yes                              |
| Alternatives are named products, not categories| Yes                              |
| Proof points are quantified with a source      | Yes                              |
| Output format fully populated                  | No `[Needs input]` left blank    |
| Downstream skill names only used if verified   | Yes, or none named               |

---

## Operating Rules

1. **Never write to brain.md without user confirmation.** Every write is shown as an exact before/after and requires a yes.
2. **Never re-ask what the brain already knows.** Load existing sections silently and skip any question already answered.
3. **Push back on vague answers inline.** "We sell to businesses" gets "what size, industry, role?" before it's accepted, not after.
4. **Don't name a downstream skill unless its write-back is verified correct.** A routing suggestion that writes to the wrong section is worse than no suggestion.

---

This skill is upstream of everything else in this stack — it doesn't need a
Related Skills section pointing out to its dependents. Every other skill that
reads or writes `/foundation/brain.md` should name this skill and its exact
section numbers in its own file instead.
