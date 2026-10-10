# Story template

The spine is fixed. The lead is free. Read this file in Steps 1, 3 and 5 to 7.

## Stages

Every story sits in one stage. The ledger holds the stage and the next action.

| Stage | Means | Next action |
|---|---|---|
| selected | The customer is chosen | Run kickoff |
| briefed | Kickoff answers are recorded | Draft the internal brief |
| internal-draft | Internal brief is confirmed | Book and run the interview |
| interviewed | Call done, packet built, story drafted | Gate it, then build the review pack |
| with-customer | Review pack sent by the named sender | Collect feedback and approvals |
| approved | Customer and internal approvers confirmed | Publish, then register proof |
| published | Live, with date and place | None |

A story pasted from elsewhere enters at `audited` and moves to `with-customer` after its fixes. Never skip a stage silently; say which one you are in.

## Kickoff questions

Ask all six, then the goal, the publish date and the permitted uses.

| # | Ask | Feeds |
|---|---|---|
| 1 | What do we want to say with this story? | Angle hypothesis |
| 2 | How do we want to say it? (tone, length, where it runs) | Depth, format |
| 3 | Which results do we expect to show? | Stat shortlist |
| 4 | What is special about this customer? | Tension |
| 5 | What is missing today? (data, quotes, contacts) | Open items |
| 6 | What can we not say? (competitor names, unreleased features, numbers) | Cannot-say list |

The cannot-say list is binding: nothing on it appears in any draft or message.

## Internal brief

Drafted before any customer contact, in the format the writer chose in Setup. It holds: the goal, why this customer, publish date, the angle hypothesis, the cannot-say list, what we already know (from the brain, CRM, call recordings, survey comments, all marked unverified), the gaps, and the contact. The writer confirms it before the stage moves to `internal-draft`.

## Header zone

| Piece | Rule |
|---|---|
| Headline | One of the five formulas below. Names the customer and a result or a stake. |
| Byline | The champion plus one more speaker, with titles. |
| Stat strip | At most three stats. Prefer three different kinds (time, money, quality, scale, risk, satisfaction). Each has a context line with the denominator and period. |
| At a glance | Three sentences: who they are, what they chose, what happened. |
| Company facts | Industry, region, size, features used. Use the customer's industry words only here. |

## Headline formulas

| Formula | Shape | Use when |
|---|---|---|
| Outcome-led | How [customer] [verb] [specific result] | There is one clean number |
| Crisis-led | How a [event] led [customer] to [big move] | A real event forced the decision |
| Attitude-colon | [Customer's stance]: How [customer] [outcome] | The customer has a point of view |
| Number-in-time | [Customer] [verb] [number] in [timeframe] | Speed is the story |
| Capability-led | How [customer] is building [outcome] through [capability] | No strong number yet (weakest) |

## The seven blocks

Every block follows **claim, number, voice**: one sentence stating what the block shows, one number that proves it, one named person saying it.

| # | Block | Holds | Anchor | Quote job |
|---|---|---|---|---|
| 1 | Before | Stakes and friction in the customer's terms | Baseline stat | Pain |
| 2 | Decision | Alternatives considered, how they were tested, why they lost | Comparison table | Decision |
| 3 | Rollout | Phases, timeline, effort | Phases or timeline | Optional |
| 4 | Results | What changed, with baseline and source | Results table | Proof |
| 5 | People | How someone's work or role changed | None | Human payoff |
| 6 | Limit | What is still hard or manual | None | Limitation |
| 7 | Next | What the customer wants next | None | Ambition |

Block prompts, to draw out detail the customer rarely volunteers:

| Block | Also ask |
|---|---|
| Before | Who felt it most, and what did it cost them? |
| Decision | Why us over the others, in their words? |
| Rollout | Which teams use it now, and for what? |
| Results | Which parts of the product gave the value? |
| Next | Why do they keep choosing us, and what would they expand? |

Name headings for what the block says ("When spreadsheets stopped scaling"), never for the slot ("Challenge").

## Depth

| Depth | Blocks | Length | Needs from the packet |
|---|---|---|---|
| Short | 1, 2, 4, 5 (1 and 2 may merge; subheads optional) | ~500 to 700 words | Baseline, result, one alternative, one person |
| Standard | 1 to 6 | ~1,000 words | Adds rollout and a limitation |
| Deep | 1 to 7, two speakers per block where available | ~1,500 and up | Adds the test method, a second speaker, a forward ambition |

## Stat record

| Field | Example |
|---|---|
| value | 6.8% → 1.9% |
| baseline | Q4 2025 |
| period | month 6 after go-live |
| denominator | of ~14,000 invoices a month |
| source | customer finance dashboard |
| status | measured / estimated / early |

Missing any field: the stat becomes a placeholder, for example `[BASELINE]`.

## Quote record

| Field | Rule |
|---|---|
| text | Verbatim, as the customer said it |
| speaker | Name |
| title | Job title |
| job | pain / decision / proof / human payoff / limitation / ambition / second voice / leadership view |
| approval | confirmed / `[NEEDS APPROVAL]` |

At least two speakers where the customer has them. If only one person is available, say so in the gate notes.

## Angles

Pick from the packet, not from this list alone.

| Angle | Tension |
|---|---|
| Speed | They needed it in weeks, the alternative needed months |
| Crisis | An event broke the old way, with a date |
| Contrarian | They did the opposite of what their industry does |
| Scale | Volume outgrew the team |
| Trust | Being wrong costs more here than anywhere else |
| Role change | A person's job became something new |

## Compelling test

1. Who is the reader, and what do they fear?
2. What is the surprise, or the stake beyond the metric?
3. Would a reader repeat one sentence from it?
4. Is there a before they recognize and an after they want?

If none passes, name the missing ingredient and ask for it.

## Permitted uses

Approval is per use. Record which of these the customer agreed to: phone reference, events or panels, written case study, media, blog, all. A use not listed is not approved.

## Assets

Ask for: desktop and mobile screenshots, GIFs, logo, headshots for each quoted person, and any approved visuals. Record each as received, requested or not available.

## Close

Related stories (two or three) and a CTA written for the reader this story is for. A generic CTA fails the gate.

## Ledger packet format

`/context/customer-stories.md` opens with a Setup header, then one packet per story, newest last.

```
# Customer Stories Ledger

Setup:
  driver: [name, department] · internal approver: [name, department]
  contributors: [name, department, ...] · customer contact owner: [name, department]
  internal brief format: [as the writer chose]
  approvers: [customer, legal, ...] · naming rules: [...]
  (any role not given: "not set")

## [Customer name]
stage: selected | briefed | internal-draft | interviewed | audited | with-customer | approved | published
next action: [one line]
goal: [..] · why this customer: [..]
publish: [date and place, or "not set"]
contact: [name, title]
depth: short | standard | deep
angle: [name] · tension: [one line]
cannot say: [..]
permitted uses: [phone reference / events / written case study / media / blog / all / none yet]
approvals: [person ✓ / person [NEEDS APPROVAL] / legal ...]
stats:
  - [value] · baseline [..] · period [..] · denominator [..] · source [..] · status [..] (up to: typical [..])
quotes:
  - "[text]" · [speaker], [title] · job [..] · approval [..]
alternatives: [..]
assets: [item: received / requested / not available]
open: [gaps still to fill]
updated: [YYYY-MM-DD]
```

Update a packet in place; never duplicate a customer. `writing-assistant` may read this file but must not write to it.
