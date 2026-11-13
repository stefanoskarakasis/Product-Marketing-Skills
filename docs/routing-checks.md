# Routing checks

Claude chooses a skill from its name and description. This page is how you check, by hand, that the right competitive skill answers the right request. Run it after installing or updating the plugin, and whenever you add a skill that shares words with another.

`evals/triggers/prompts.json` holds three prompts for every skill, to run the same way. `tests/test_triggers.py` catches the collisions a script can catch (duplicate or hidden phrases, a missing "Not for" clause). It cannot tell you how Claude actually routes. This battery can.

## How to run it

1. Open a fresh session with the plugins installed. One session per prompt, so earlier answers do not steer the next.
2. Type the prompt exactly as written. Note which skill answers, or whether it asks a question first.
3. Mark Pass if the result matches. Write failures down with the exact prompt and what happened.

## The battery

| # | Prompt | Should route to |
|---|---|---|
| 1 | Build me a battlecard for Acme, I am an AE | `competitive-battlecard` |
| 2 | Brief the CEO on competitors | `competitive-briefing` |
| 3 | Weekly leadership brief | `competitive-briefing` |
| 4 | Board update on competitors | `competitive-briefing` |
| 5 | Brief my CRO on win and loss against competitors | `competitive-briefing` |
| 6 | Summarise what changed this week with competitors for leadership | `competitive-briefing` |
| 7 | Grade last week's call | `competitive-briefing` |
| 8 | What changed this week | `signal-monitor` |
| 9 | What do we say against Acme on pricing? | `competitive-profile` |
| 10 | Deep-dive on Acme for our pricing review | `competitor-deep-dive` |
| 11 | Keep my competitor profiles current | `competitive-profile` |
| 12 | Competitive update | One question (leadership brief, or refresh the profiles). No build |
| 13 | What are our competitors doing | One question, or `competitive-profile`. Never a leadership brief |
| 14 | Competitive newsletter | One question. No leadership brief without an audience |
| 15 | Who are we competing with | `alternatives-map` |
| 16 | Write this week's industry newsletter | `industry-newsletter` |
| 17 | Weekly market and pricing watch for our GTM leaders | `industry-newsletter` |
| 18 | Brief the CEO on competitors, with the euro at risk | `competitive-briefing` |
| 19 | Set up media monitoring for our five competitors | `media-monitoring` |
| 20 | Run the weekly competitor sweep | `media-monitoring` |
| 21 | What did the monitoring catch this week | `media-monitoring` |
| 22 | Rank this week's sweep findings against our quarterly priorities | `signal-monitor` |
| 23 | Competitor news | One question (sweep, opportunities or leadership brief). No build |
| 24 | Build our vs page against Northgate AP | `comparison-page-brief` |
| 25 | Write a best alternatives to Paystream page | `comparison-page-brief` |
| 26 | Competitive page | One question (page type and rival, or seller card). No build |
| 27 | Research Acme before I reach out | `prospect-research` |
| 28 | Is there a reason to contact Acme now? | `prospect-research` |
| 29 | Catch me up on Acme (Acme is a customer in the CRM) | `customer-context` |
| 30 | Catch me up on Acme (no CRM match) | One question: is this a customer? |
| 31 | Research the CFO at Acme (Acme is in Germany) | `prospect-research`, then the EMEA role-only question |
| 32 | What do we say against Acme on pricing? | `competitive-profile`, not `prospect-research` |
| 33 | Run the weekly learning sweep | `meta-synthesis` (weekly mode) |
| 34 | Weekly sales digest | `sales-research-digest` |
| 35 | How is the sales team using the research briefs? | `sales-research-digest` |
| 36 | Which skills did we use this week across everything? | `meta-synthesis` (weekly mode), not `sales-research-digest` |
| 37 | Review the Acme deal before Friday's call | `deal-review` |
| 38 | Is the Acme deal real or are we kidding ourselves? | `deal-review` |
| 39 | What changed on the Acme deal since last week? | `deal-review` (`since`) |
| 40 | Which of my deals need attention today? | `deal-review` (`queue`, deals only) |
| 41 | Research Acme before we reach out (no deal yet) | `prospect-research`, not `deal-review` |
| 42 | Build a battlecard for the Acme deal against Rival | `competitive-battlecard`, not `deal-review` |
| 43 | Run the weekly competitive updates | `weekly-competitive-updates` |
| 44 | Weekly competitor update for the C-suite, Germany only | `weekly-competitive-updates` |
| 45 | Executive competitor news this week | `weekly-competitive-updates`, not `industry-newsletter` |
| 46 | Weekly competitor update for the C-suite with the euro at risk | `competitive-briefing`, not `weekly-competitive-updates` |

**Pass:** 43 of 46, and prompts 12 to 14, 23 and 26 never build a leadership brief or a newsletter without asking.

## If two sets of skills are installed

If you also run another set of competitive skills in the same project (for example another vendor's battlecard or briefing skill), natural-language prompts can go to either. The slash command always goes to this plugin:

| You want | Use |
|---|---|
| The weekly leadership brief | `/pmm-competitive-intelligence:competitive-briefing` |
| The weekly C-suite update from public sources | `/pmm-competitive-intelligence:weekly-competitive-updates` |
| The weekly industry newsletter | `/pmm-competitive-intelligence:industry-newsletter` |
| A battlecard for a live deal | `/pmm-competitive-intelligence:competitive-battlecard` |
| A deep-dive on one competitor | `/pmm-competitive-intelligence:competitor-deep-dive` |
| Profiles, roster, a competitor question | `/pmm-competitive-intelligence:competitive-profile` |

Better still, keep one set of competitive skills per project.

## Recording results

Add one row per run to [`docs/eval-results.md`](eval-results.md): date, plugin version, prompts passed out of 46, and each failure with its exact prompt. A failure is a trigger-wording bug: report it as an issue and the description is changed, not the prompt.


The full run sheet for this battery and the held-out set is [`evals/triggers/run-sheet.md`](../evals/triggers/run-sheet.md). How to record a run: [`routing-runs.md`](routing-runs.md).
