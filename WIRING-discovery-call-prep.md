# Wiring: discovery-call-prep (one-line changes to existing files)

Draft only. I could not read your live files, so each change gives the line to add or replace; confirm the surrounding text on `main` before pasting. Counts below say "+1" because I do not know whether `objection-handling` has landed.

## A. New files (visible names only)

- `pmm-sales/skills/discovery-call-prep/SKILL.md`
- `pmm-sales/skills/discovery-call-prep/references/` (method, questions, modes, formats, rules, connectors, feed-forward)
- `pmm-sales/skills/discovery-call-prep/evals/discovery-call-prep.eval.md`
- `pmm-sales/commands/discovery-call-prep.md`

## B. The `prep` takeover from `deal-review`

| File | Change |
|---|---|
| `pmm-sales/skills/deal-review/SKILL.md` | Description: remove `"prep me for my call with [deal]"`; add `call prep (discovery-call-prep)` to the Not-for list. Trigger section, Args: delete mode `prep`. Add to Not for: `Call prep → discovery-call-prep`. Example list: delete the `prep` example |
| `pmm-sales/skills/deal-review/references/modes.md` | Replace the `## prep` section with one line: `## prep. Moved to discovery-call-prep, which reads this skill's last record and _gaps.md for the open-deal short form.` |
| `pmm-sales/skills/deal-review/references/feed-forward.md` | Row "A discovery question that unlocked missing evidence": change receiver to `produced by discovery-call-prep; hand off`. Reads: add `discovery-call-prep` `_outcomes.md` for the account |
| `pmm-sales/skills/deal-review/evals/deal-review.eval.md` | Repoint the `prep` case: "Prep me for Marlow at 3pm" routes to `discovery-call-prep`. Update the case count in the frontmatter |
| `pmm-sales/commands/deal-review.md` | Remove the `Prep me for my Marlow call` invocation line and the word "pre-call prep" from the description and Workflow |

## C. Sibling skills

| File | One-line change |
|---|---|
| `prospect-research/SKILL.md` | Hand-off line: `Next: discovery-call-prep for the call plan once a meeting is booked.` Reads: its record is read by `discovery-call-prep` |
| `prospect-research/references/feed-forward.md` | Add `discovery-call-prep` `_outcomes.md` as a source for signal hit and miss |
| `customer-context/SKILL.md` | Not-for: `a discovery call plan → discovery-call-prep` |
| `objection-handling/SKILL.md` | Examples: `prep me for objections` stays; add Not-for: `a discovery call plan → discovery-call-prep`. Feed: objections raised in discovery arrive as a hand-off |
| `competitive-battlecard/SKILL.md` | Step 2: for stage Discovery, read `/context/discovery/<slug>` (one line) |
| `sales-research-digest/references/sources.md` | Add `/context/discovery/_outcomes.md` and `_questions.md`; new "Discovery" section (see feed-forward section 6) |
| `meta-synthesis` `/context/learning-sources.md` | One row for `/context/discovery/` ledgers (adoption-only flag if the file supports it; otherwise keep proposals owned by this skill) |
| `product-messaging-playbook/SKILL.md` | Not-for: `a call plan for one buyer → discovery-call-prep` |

## D. Repo-level

| File | Change |
|---|---|
| `product-marketing-context/.claude-plugin/next-skill-map.md` | `After prospect-research: discovery-call-prep`; `After a meeting is booked: discovery-call-prep`; `After a discovery call: deal-review` |
| `docs/routing-checks.md` | Add six prompts (below) |
| `tests/test_triggers.py` | Add the six prompts and assert the sales skills name each other in Not for |
| `pmm-sales/README.md` | Skill list, command list, Start-here line |
| `pmm-sales/CONNECTORS.md` | No new rows; add `discovery-call-prep` to the "Used in" wording |
| `pmm-sales/.claude-plugin/plugin.json` and the Cursor manifest | Keywords: `discovery`, `call prep`, `first call` |
| `README.md`, `QUICK-START.md`, `AGENTS.md` | Skill and command counts +1 |
| `SKILL-SPEC.md` | T2 row for the new skill's Quality Gate |
| `CHANGELOG.md` | Entry: new skill `discovery-call-prep`; `prep` moved from `deal-review` |

### Six routing prompts

| Prompt | Should route to |
|---|---|
| "Prep my discovery call with the VP Finance at Tidewell Foods" | `discovery-call-prep` |
| "What should I ask a head of RevOps in a 30-minute intro?" | `discovery-call-prep` |
| "Prep me for my call with Marlow at 3pm" | `discovery-call-prep` (open-deal short form) |
| "Is there a reason to contact Tidewell Foods now?" | `prospect-research` |
| "Is the Marlow deal real?" | `deal-review` |
| "They said it is too expensive" | `objection-handling` |

## E. Open checks before landing

1. The brain field names in the contract (`anti_persona`, `committee_roles`, `context_owners`) are copied from `deal-review` and `objection-handling`. Confirm them against the brain schema.
2. Whether `learning-sources.md` supports an adoption-only flag (still open from batch 127).
3. Description budget: this description is 797 characters; check the 20,000 total after adding it.
4. The `deal-review` `prep` removal and the new skill must land in the same release, or the trigger has no owner.
5. Run the six routing prompts in fresh chats and record the result in `docs/eval-results.md`.
