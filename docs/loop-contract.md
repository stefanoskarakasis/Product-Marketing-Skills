# The run contract for scheduled skills

A skill that runs on a schedule, or when something triggers it, is a loop. Nobody is watching a loop, so it must be written to do nothing most weeks and to stop safely. This page is the shape every scheduled skill follows. The idea of nine parts comes from the `marketing-loops` skill in coreyhaines31/marketingskills (MIT).

## The nine parts

1. **Cadence.** How often it looks. Match the speed of the signal: competitor pages weekly, a roster monthly. A loop that runs more often than its signal changes becomes busywork and gets ignored.
2. **Acts when.** The condition that makes the run do anything. Most runs end with nothing to do, and the skill says so in one line.
3. **Purpose.** The one outcome it exists to move. If you cannot name it, delete the loop.
4. **Skills used.** Which other skills it calls, so a change in one is visible in the other.
5. **Loop body.** The ordered steps of one run. They are the same whether a person or a schedule starts it.
6. **Self-check.** What it verifies before acting, so it does not react to noise, a one-off spike or a broken source.
7. **State.** What it remembers between runs: last-run date, what it already reported, what it is waiting on. A rerun on the same day must not repeat itself or contact anyone twice.
8. **Stop.** When it halts, hands over to a person, or turns itself off, including when a source cannot be read.
9. **Output.** Where the result goes: a saved file, a draft, a Slack post. Name the place.

## Two rules that do not bend

- **A person approves anything that sends, spends, publishes or touches personal data.** An unattended run saves records and proposals. It does not change the brain.
- **A loop nobody acts on is deleted.** The weekly learning sweep (`meta-synthesis`, weekly mode) shows adoption per skill; a quiet skill is a question, not a success.

## Where the scheduled skills stand today

Found by searching each skill and its references for the words below, not by reading every line. Treat "not found" as a prompt to read the skill, not as proof.

| Skill | Quiet-run rule | Keeps state | Stop rule |
|---|---|---|---|
| media-monitoring | found | found (`_state.md`) | found (schema mismatch) |
| weekly-competitive-updates | found | found (edition archive, threat ledger) | found (no sources) |
| industry-newsletter | found | found (carry-forward items) | found (prohibited competitor only) |
| competitive-briefing | found | found (prediction ledger) | found (prohibited competitor only) |
| competitive-profile | found (refresh only stale lines) | found (dated records) | found (prohibited competitor only) |
| sales-research-digest | found (unattended rules) | found (last run) | found |
| meta-synthesis | found (unattended rules) | found (`last_synthesis`) | found |
| signal-monitor | not found | not found | not found |

## Adding a scheduled skill

State parts 2, 7, 8 and 9 in the skill or its `references/`. Say in the skill what a quiet run looks like. Offer the schedule once and never schedule without a yes.
