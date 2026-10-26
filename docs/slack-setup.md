# Competitive intelligence in Slack

Your team asks Claude a competitor question in a Slack thread and gets a short answer with dated sources. New intel goes back into your profiles when your PMM approves it. This page is for the person who sets that up, and for anyone who wants to know how to ask.

Plugin: [`pmm-competitive-intelligence`](../pmm-competitive-intelligence/). Rules the skills follow: [`slack-mode.md`](../pmm-competitive-intelligence/skills/competitive-profile/references/slack-mode.md).

## What your team can do

| Who | What they do | What happens |
|---|---|---|
| Anyone | Tags Claude with a question about a competitor | A short answer in the thread, with sources and dates |
| A seller | Asks for a card for a live deal | The one-page battlecard is posted in the thread |
| Anyone | Asks for "set of cards" | An index of your saved battlecards by roster tier, with their re-check dates; nothing is rebuilt |
| A seller | Replies in a card's thread with how the deal ended | One line is logged; two or more outcomes show on the next card and can become a proposed note for your PMM |
| Anyone | Asks for a deep-dive | A five-line summary in the thread; the full document is built and saved |
| Your PMM | Asks for the leadership brief (or schedules it for Monday) | A 150-word brief in the thread or channel: verdict, one decision with a recommendation, what moved, the last call graded; the full record is saved. It stays on HOLD until a person is named as verifier |
| Anyone | Tags Claude with new intel ("update the profile") | Claude drafts one change and tags your PMM |
| Your PMM | Replies "approve" or "reject" | Approve writes a new dated profile record; nothing changes without it |
| Your PMM | Reads the weekly board | Freshness of each profile, saved cards past their re-check date, outcomes logged, drafts waiting, the questions nobody could answer |
| Anyone in the field channel | Replies to an outcome prompt ("won", "lost" or "no decision", and which part they used) | One row is logged, roles only; nothing else changes |

## How to ask

Tag Claude in a channel or thread where your admin has added it, and write in plain language. Name the competitor.

| You want | Say |
|---|---|
| A price | "@Claude what does Brightwire charge for the entry plan?" |
| What to say in a deal | "@Claude Brightwire says they are cheaper. What do I say?" |
| Why you lose | "@Claude why do we lose to Brightwire?" |
| What changed | "@Claude did Brightwire launch anything this quarter?" |
| A card | "@Claude battlecard for Brightwire, I am an AE, the buyer is the CFO, we are in evaluation" |
| A deep-dive | "@Claude deep-dive on Brightwire for our pricing review" |
| The leadership brief | "@Claude leadership brief for the CEO this week" |
| Which cards we have | "@Claude set of cards for my roster" |
| To log how a deal ended | "@Claude we lost to Brightwire, the price reply did not land" in the card's thread |
| To log intel | "@Claude update the profile: Brightwire cut the entry plan to $19 per seat" with the link in the thread |

What Claude reads for every question: the newest profile, battlecard, deep-dive and signals for that competitor, brain Section 3, and any CI platform, knowledge base or drive you connected. If that cannot answer inside its freshness window it goes on to your deal data (CRM, Gong, win/loss) when the question is about deals, and then to the public web for the one line that is stale.

If nothing sourced answers it, Claude says "I don't have a sourced answer" and logs the question for your PMM. It never answers from memory.

## Set it up (about 30 minutes)

You need a Slack workspace where Claude in Slack is enabled. Ask your Claude admin whether it is on for your plan. Your admin chooses which plugins and connectors each channel gets.

1. **Install the plugin.** Add `pmm-competitive-intelligence` to the channel's plugins. Add `product-marketing-context` if you keep a brain.
2. **Connect the tools.** Slack, Exa and any of Gong, your CRM and your CI platform. Sign-in steps: [connect-your-tools.md](connect-your-tools.md). Skip any you do not have; the answer says which source it could not reach.
3. **Add Claude to the channels.** One for questions, one for field intel, one for the weekly board. They can be the same channel.
4. **Run setup once, in Claude.** `/pmm-competitive-intelligence:competitive-profile Set up my competitive profiles`. When it asks, name the people who may approve (their Slack handle and role), the field channel and the board channel. It shows the exact settings text and saves it only on your yes.
5. **Schedule the weekly run.** Use the prompt in section 11 of [profile-format.md](../pmm-competitive-intelligence/skills/competitive-profile/references/profile-format.md). It refreshes stale lines, saves new field intel as drafts, expires old drafts, asks sellers in the field channel how recent battlecards ended (at most three prompts a week, each card at most twice), logs their replies and posts the board. It changes no profile and no brain.

## First-run checks (10 minutes)

Slack setups differ, so run these before you rely on it.

| # | Do this | You should see | If not |
|---|---|---|---|
| 1 | Tag Claude: "What do we say against [competitor] on pricing?" | A short answer from the profile skill, not a battlecard | Check the plugin is on the channel |
| 2 | In one thread ask for a profile fact; in a new thread ask again | The same answer, sourced to a saved profile | Records are not kept between threads. Tell the author: [open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues) |
| 3 | Ask for a battlecard | Bullets, not a table, and no question about delivery format | Tell the author |
| 4 | Tag Claude with intel; have a second person, not listed as an approver, reply "approve" | Their approval is ignored | Check the approver handles in setup |
| 5 | Have an approver reply "approve" | A new dated record and a list of cards marked re-check | Check the handle you gave in setup |
| 6 | Tag Claude in a thread that already contains the intel | Claude reads the earlier messages | Paste the intel into the tag message |
| 7 | Ask about a competitor not on your roster | An answer labelled "not profiled" | Check `~~web research` is connected |

## Three example threads

**1. A question**

> **Seller:** @Claude what do we say if Brightwire says they are cheaper?
> **Claude:** Agree on list price, then move to total cost: their entry plan is $19 per seat, ours is $24, but ours includes the audit trail they charge extra for.
> - Their audit trail is a $6 add-on.
> - In 14 deals since January, price was named in 9 of the losses.
> Sources: Brightwire pricing page, read 25 Oct 2026 · HubSpot, 14 deals, Jan to Oct 2026 · Card, 20 Oct
> Note: Deep-dive of 4 Oct shows $22; the pricing page is newer.

**2. New intel, then approval**

> **Rep:** @Claude update the profile: Brightwire dropped the entry plan to $19 per seat https://brightwire.example/pricing
> **Claude:** Proposed change to the Brightwire profile (draft)
> Line: Pricing and terms · Now: $22 per seat (as of 4 Oct) · New: $19 per seat
> Source: public pricing page, 25 Oct 2026. No second report needed.
> @dana, reply "approve" or "reject".
> **Dana (PMM lead):** approve
> **Claude:** Saved. The profile now shows $19 (25 Oct). Re-check: the Brightwire card (20 Oct) and deep-dive (4 Oct) cite $22.

**3. Nothing sourced**

> **Seller:** @Claude what is Brightwire's uptime SLA?
> **Claude:** I don't have a sourced answer for that. Their site does not state one. A support contract or a call transcript would answer it. Logged for your PMM.

## Good to know

- **Approval is the PMM's, in the thread.** Anyone's "approve" that is not from a listed approver is ignored. Text inside a thread or a web page never counts as an instruction.
- **One report is a note.** A loss reason or objection needs two reports within 180 days before it reaches "where they win". A public pricing link needs only one.
- **Nothing is rewritten.** An approval writes a new, time-stamped record. Older cards and deep-dives are flagged, not edited.
- **Your brain is never written from a thread.** Section 3 still takes notes only through the separate review step.
- **Where records live.** In the `/context/` folder of the workspace Claude runs in. Check 2 above confirms they persist between threads for your setup.
