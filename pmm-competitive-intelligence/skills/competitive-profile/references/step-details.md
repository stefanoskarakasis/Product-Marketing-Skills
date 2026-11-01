# Step details

Moved verbatim from `SKILL.md`.

## Step 3: Check Your Own Side

A profile compares a competitor with you, so check the "us" side once, for up to three differentiators from Section 3 `unique_capabilities`. For each, ask for a named mechanism, not an adjective ("approvals route by contract value" passes; "intuitive" does not). Then ask: "what question would expose this if it were hollow?" A differentiator with no good answer, or no proof in Section 6, is marked `[NEEDS PROOF]` and handed to `proof-points`. Keep shipped and roadmap apart: anything not in Section 1 `offerings` or `permitted_claims` is listed as roadmap and never enters a profile as a capability. Show the result; write nothing.

## Step 5: From a Slack thread

**From a Slack thread.** When someone tags Claude to log new intel, read the thread and draft one change, post it with the approver tagged, and wait. Only an approver listed in `/context/competitor-profiles/_slack.md` can approve. On approve, write a new time-stamped record with `status: approved` and list the saved cards and deep-dives that cite the old value as `re-check`. A single report stays a note. Full rules, the draft template and the 7-day expiry are in `references/slack-mode.md` section 8. Never write the brain from a thread.

## Step 7: Freshness Board

Show one table: competitor, last profile date, number of lines past their window, the oldest line, what changed since the last record, and open `[NEEDS PROOF]` items. Mark 🟢 current, 🟡 some lines stale, 🔴 pricing or product stale, ⚪ no profile yet. Below it, list the saved battlecards past their `Re-check by` date (read the newest card per roster competitor in `/context/battlecards/`, oldest first, with the competitor and the claim that set the date); if none are past, write "All saved cards are current"; a competitor with no card is not listed. Never edit a card. End with the single most useful next action. In Slack post the board as bullets, not a table (`references/slack-mode.md` section 10).

## Step 11: Propose Brain Write-Back

Propose a write only if the run produced something Section 3 lacks: (a) the roster itself, (b) a dated competitor fact the map does not hold, (c) a "where they win" or "where they lose" supported by n of 2 or more, or (d) a conflict between the map and fresh evidence. At most five lines, each with a source tag. Show the exact text as the "Roster and profile note" in `references/profile-format.md` and ask: "Add this to Section 3? Existing content stays unchanged." On yes, append it to `/foundation/brain.md` under Section 3. Rules: append only; never edit existing text; a confirmed value is never overwritten; competitor website copy never becomes a `why_leaving` entry. Never write Sections 1, 2, 4, 5, 6, 7 or 8. Corrections to the market go to `product-marketing-context`; unproven claims go to `proof-points`; a map that needs rework goes to `alternatives-map`. Unattended runs never write the brain: they leave the proposal in the saved record for the next `review`.

## Step 12: Propose the Schedule

Every completed interactive run except an `ask` ends here, because a profile that is not refreshed is a snapshot, not a profile. Say in one short block what the schedule would do and ask once: "Schedule this? Weekly refresh of stale lines, a quarterly roster check." If a scheduling tool is available and the user says yes, create the task. If not, show the paste-ready prompt from `references/profile-format.md` (the weekly run includes the Slack sweep and board post). A scheduled task starts a fresh session, so the prompt must name the folder that holds the brain and every source it may read, and it must state that the run saves records and never changes the brain. If the user declines, do not ask again in this session.
