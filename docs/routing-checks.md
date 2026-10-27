# Routing checks

Claude chooses a skill from its name and description. This page is how you check, by hand, that the right competitive skill answers the right request. Run it after installing or updating the plugin, and whenever you add a skill that shares words with another.

`tests/test_triggers.py` catches the collisions a script can catch (duplicate or hidden phrases, a missing "Not for" clause). It cannot tell you how Claude actually routes. This battery can.

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

**Pass:** 16 of 18, and prompts 12 to 14 never build a leadership brief or a newsletter without asking.

## If two sets of skills are installed

If you also run another set of competitive skills in the same project (for example another vendor's battlecard or briefing skill), natural-language prompts can go to either. The slash command always goes to this plugin:

| You want | Use |
|---|---|
| The weekly leadership brief | `/pmm-competitive-intelligence:competitive-briefing` |
| The weekly industry newsletter | `/pmm-competitive-intelligence:industry-newsletter` |
| A battlecard for a live deal | `/pmm-competitive-intelligence:competitive-battlecard` |
| A deep-dive on one competitor | `/pmm-competitive-intelligence:competitor-deep-dive` |
| Profiles, roster, a competitor question | `/pmm-competitive-intelligence:competitive-profile` |

Better still, keep one set of competitive skills per project.

## Recording results

Add one row per run to [`docs/eval-results.md`](eval-results.md): date, plugin version, prompts passed out of 15, and each failure with its exact prompt. A failure is a trigger-wording bug: report it as an issue and the description is changed, not the prompt.
