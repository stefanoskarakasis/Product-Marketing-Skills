# Weekly Mode

Read when the request says "weekly", "Friday sweep" or "what did we learn this week", or when a scheduled task runs this skill. Same gate as the normal run; nothing is written to the brain without a yes.

## Steps

1. Load the sources in `learning-sources.md`. Say in one line which were found and which were missing.
2. Count sessions per skill for the last 7 days from `/context/skill-sessions.md`. Show the table below. A skill with zero sessions this week is listed under "quiet", so the owner can see what is not being used.
3. Find patterns across sessions and ledgers by the counting rules. Turn each into one numbered item: the exact text, the target file or brain section, the receiving skill, its evidence and n, and its confidence.
4. Show the promotion queue in one message. The user answers: approve all, approve some, or reject. A rejected item is logged with its reason and is not proposed again without new evidence.
5. Write only the approved items. Update `last_synthesis` in `/context/meta-patterns.md`. Log the session.
6. Add one line from `hygiene.md`: live, watch and retired guardrails, and how many are due for review. Propose retirements in the same queue.

## Adoption table

| Skill | Sessions this week | vs last week | Surprised / wrong / missing |
|---|---|---|---|

## Promotion queue

```
1. [Pattern] · n=[count] [sessions | accounts | outcomes] · [high | watch]
   Proposed: [guardrail in /context/meta-patterns.md | brain Section N]
   "[exact text]"
   Evidence: [ledger, dates]
```

## Unattended runs

A scheduled run builds the adoption table and the queue and saves the queue to `/context/promotion-queue.md`. It writes no guardrail and no brain edit. The next interactive run opens with "A queue from [date] is waiting" and asks for the answer.

## Keeping it running

End every interactive run with one offer: "Want this every Friday?" On yes, create a scheduled task with this prompt: "Run meta-synthesis in weekly mode on the shared context folder. Build the adoption table and the promotion queue and save it to /context/promotion-queue.md. Write nothing else." Also tell the user the manual fallback: say "run the weekly learning sweep". If no scheduling tool is available, say so and give the manual line.
