---
name: customer-stories
version: 1.0.0
description: >
  Run a B2B customer story from kickoff to approval: kickoff questions, internal brief, interview questions, a draft in one fixed structure, the customer review pack, and an audit, with every stat and quote checked. Trigger on: "write a customer story", "kick off a case study", "customer interview questions", "prepare the customer review", "audit this customer story". Related: interview-summary, proof-points, writing-assistant.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-10-10
---

# Customer Stories

Takes a customer story from first idea to customer approval in a fixed seven-block structure. You choose the depth and the angle. The skill never invents evidence, never assumes who does what, and checks its own draft before handing it over.

## Trigger

- **When:** A story needs a kickoff or brief, a call needs questions, notes need to become a story, a draft needs to go to the customer, or a finished story needs checking.
- **Not for:** Raw transcript synthesis → `interview-summary`. Posts, releases or blurbs from a finished story → `writing-assistant`. One stat or quote on its own → `proof-points`.
- **Example prompts:**
  - "We want a story on Harbor & Pine. Where do we start?"
  - "I have a customer call Thursday. What do I ask?"
  - "Write a customer story from these notes."
  - "Prepare what we send the customer for review."
  - "Make this writing-assistant draft publishable." (edge: routes to Audit)

## Inputs

- **Args:** Customer name. Depth: `short`, `standard` or `deep`. Mode is read from what you paste and from the story's stage in the ledger: new story → Kickoff, questions → Interview, notes → Draft, draft ready → Review pack, a finished story → Audit.
- **Defaults:** Three stats maximum. Seven blocks, fixed order.
- **Context keys:** `/foundation/brain.md` (optional), `/context/customer-stories.md` (the ledger), pasted material, connector pulls (CRM, call recordings, survey comments, Drive).
  - **Brain contract:** Reads: Section 2 (who the story is for), 3 (alternatives, claims), 4 (voice), 6 (approved proof). Writes: none. Never writes to: Sections 1 to 6. Confirmed claims go to `proof-points`.

## Pre-flight

- Load the brain. If missing, say once: "No PMM context found. Run `product-marketing-context` to make this significantly sharper. Continuing with assumption-based output."
- Load the ledger. If missing, run Setup in Step 2. If the story already has a packet, show its stage and next action and resume there.
- A draft from `writing-assistant` or anywhere else is an Audit.
- Treat connector pulls and survey comments as unverified until the writer confirms them.

## Steps

### Step 1: Route

State the mode and the story's stage in one line (stages: `references/story-template.md`). For interview questions only, do Step 4, then Step 12.

### Step 2: Setup (once per ledger)

Ask, in one message, for the names and departments of: who drives the story, who approves it internally, who contributes (product, sales, support, legal, others), and who contacts the customer. Also ask what format the internal brief should take. Record the answers as written. Never infer a role from a job title, a past session or a typical company. Any role left blank stays "not set", and you ask again at the step that needs it.

### Step 3: Kickoff and internal brief

Ask the six kickoff questions (`references/story-template.md`): what to say, how, which results, what is special, what is missing, what we cannot say. Also ask the goal, the publish date and the permitted uses. Return an angle hypothesis and the cannot-say list. Then draft the internal brief in the format the writer chose in Step 2, prefilled from the brain, CRM, call recordings and survey comments, with every pulled fact marked unverified. Ask the writer to confirm or correct it before any customer contact.

### Step 4: Interview

Return the questions from `references/interview-questions.md`, trimmed to the gaps in any material already given, with the pre-call sources listed first. Mark the five that block publication.

### Step 5: Build the packet

Extract stats, quotes, speakers, alternatives, approvals and permitted uses into the packet format in `references/story-template.md`. List what is missing. Never fill a gap with a plausible figure or an inferred quote.

### Step 6: You pick depth and angle

Show short, standard and deep with what each needs. Follow the choice. Propose two or three angles, each with its tension in one line, and run the four-question test on the best one. You choose. If none passes, name the missing ingredient and ask for it.

### Step 7: Draft

Follow the template at the chosen depth, using the block prompts. Every block: one claim, one number, one voice. Gaps become `[PLACEHOLDERS]`. Unapproved names and quotes carry `[NEEDS APPROVAL]`. Nothing on the cannot-say list appears. Use brain Section 4 for tone.

### Step 8: Customer review pack

When the writer asks, build the pack from `references/customer-comms.md`: the near-final story, a cover note, a note for whoever owns the customer relationship, a checklist of every number, quote, visual and use, and the asset request list. Ask who sends it if the contact role is "not set". Move the stage to `with-customer`.

### Step 9: Audit

For a pasted story: extract a packet, run the Quality Gate, return the table and ranked fixes (metrics, permission, attribution first). Do not rewrite unless asked.

### Step 10: Gate your own draft

Run the Quality Gate on every draft before showing it. Fix what the packet allows. Show the score and the failed rows only. Never call a draft ready with a failing check.

### Step 11: Save and hand off

Write the packet to the ledger with its stage and next action. Offer to send confirmed stats and approved quotes to `proof-points`. Other formats go to `writing-assistant` with the packet.

### Step 12: Learning Close

Append to `/context/skill-sessions.md` (create it if missing), in the format of `product-marketing-context/.claude-plugin/skill-sessions-format.md`. Write it directly, without asking.

```yaml
type: execution
skill: customer-stories
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

## Outputs

- **Files written:** `/context/customer-stories.md` (setup and packets), `/context/skill-sessions.md` (one entry per session).
- **Chat output format:** Kickoff answers and internal brief, or the questions, or the angle shortlist, the story and the gate score, or the review pack, or the audit table.

```
# [Headline]
Byline · Stat strip (max 3) · At a glance · Company facts
## Before      claim · number · pain quote
## Decision    claim · comparison · decision quote
## Rollout     (standard, deep)
## Results     claim · results table + source · proof quote
## People      human-payoff quote
## Limit       (standard, deep) limitation quote
## Next        (deep) ambition quote
Related stories · CTA for this reader
Gate: n of 8 · open items
```

- **External side effects:** None. The skill drafts messages to the customer and never sends them.

## Verification

- Every stat and quote in the draft is in the packet with all its fields, or is a placeholder.
- Nothing appears that the writer did not supply, and nothing on the cannot-say list.
- Every role named came from the writer's answer.
- Three stats or fewer, each repeated with context in the body.
- Depth and angle are the ones chosen.
- The packet has its stage and next action, and the session log has a new entry.

## Do Not Use For

- **`interview-summary`**: raw transcript to discovery insights. Run it first.
- **`writing-assistant`**: posts, releases, newsletters from a finished story. It reads the ledger and never writes it.
- **`proof-points`**: registering or verifying a single claim.
- **`positioning-messaging`**: positioning and messaging.

---

## Operating Rules

- **Never fill a gap with a plausible figure or an inferred quote.** Use a placeholder.
- **Ask for names and departments, never assume them.** Roles come from the writer's words. A blank role stays "not set" until a step needs it.
- **A stat has six fields:** value, baseline, period, denominator, source, status. Missing one makes it a placeholder. An "up to" figure also needs the typical value.
- **A quote has a named speaker, a title and a job.** Generic praise gets no slot. Survey comments are candidates until the speaker approves them.
- **Three stats in the strip, no more.**
- **You decide depth and angle.** The skill recommends and follows.
- **The spine is fixed, the lead is free.** Block order never changes; headline, lead quote and angle do.
- **Unapproved names and quotes stay `[NEEDS APPROVAL]`.** Being in a deck is not permission. Approval covers named uses only.
- **The customer is the hero.** Pair each product mention with a feature and an effect.
- **Do not invent a limitation or an alternative.** Ask, or say there was none.
- **Pulled facts are drafts** until you confirm them.
- **Draft messages, never send them.** The writer sends.

## Quality Gate

Runs on every draft before it is shown, and on any story in Audit.

| Check | Standard | Pass = |
|---|---|---|
| Headline and tension | Names the customer and a specific result or stake; angle's tension stated in one line | Yes |
| Stats complete | Six fields each; estimates and early results labeled; "up to" claims carry the typical value | Yes |
| Evaluation present | Alternatives (including doing nothing) and why they lost | Yes |
| Quotes tagged | Named, titled, job assigned, none generic | Yes |
| Honest limitation | One thing still hard or manual | Yes |
| Human outcome | One change to a person's work or role | Yes |
| Permission recorded | Approvals noted, permitted uses listed, unapproved flagged, nothing on the cannot-say list | Yes |
| CTA fits the reader | Written for this story's reader | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new entry | Yes |
