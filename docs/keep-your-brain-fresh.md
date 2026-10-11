# Keep your brain fresh

Your brain is only useful while it is true. This page explains how the repo helps you notice when it is not, and what it will and will not do on its own.

## What this is: assisted refresh

Nothing here changes your brain by itself. The skills **find** what is old or missing and **ask** you. Every change is shown as an exact before/after and written only after you say yes. That is deliberate: your brain feeds launch plans and customer-facing claims, so you stay in charge.

## The three ways it stays current

1. **Each section has a freshness limit.** The limits live in `product-marketing-context/references/brain-schema.md`: Strategy and Market Context 90 days, ICP, Alternatives, Product and Execution 180 days, Voice 365 days, proof points per claim 12 months.
2. **Refresh.** Run `/product-marketing-context:refresh-brain`. It lists only the fields past their limit and asks, one at a time: still true, changed, or drop. "Still true" answers are bumped together after one confirmation.
3. **Gaps.** When another skill needs a fact the brain does not have, it asks you one question in the moment. If you skip it, the question is saved to `/foundation/gaps.md`. Run `/product-marketing-context:brain-gaps` to answer the saved ones, one at a time. A skipped question stays quiet for 30 days.

## A weekly check (optional)

You can ask Claude to run a read-only check on a schedule, for example every Monday morning:

> Create a scheduled task that runs every Monday at 9:00. It should open my brain at /foundation/brain.md, list every field past its freshness limit and how many open gaps are in /foundation/gaps.md, and save that list to /context/brain-health.md. It must not change the brain or the gaps file.

You then read the list and run refresh or gaps when you have ten minutes. Scheduled tasks run in a fresh session, so the task needs access to the same folder as your brain.

## What it will not do

- It will not edit your brain without your confirmation.
- It will not replace a value you confirmed with newer material. If newer material disagrees, it shows you both and asks.
- It will not call itself self-healing. It reminds you; you decide.

## A weekly look outward (optional)

The checks above look at your brain. `signal-monitor` looks at the world and compares it with your brain. See [the AI marketer loop](ai-marketer-loop.md) for how to schedule it. It is read-only, like the brain check.
