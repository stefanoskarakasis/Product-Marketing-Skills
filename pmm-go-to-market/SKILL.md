---
name: go-to-market-strategy
description: "Assigns launch tier (T1-T4) and generates GTM strategy briefs with messaging, channels, and success metrics. Reads brain for self-learning from past launches. Use when planning product launches, features, pricing changes, or market expansion. Chains with positioning-messaging and workflow-orchestrator."
---

# Go-to-Market Strategy

Assign tier to any GTM initiative (T1-T4), generate strategic briefs, and self-learn from launch history stored in your brain.

## When to Use This Skill

- Planning a product or feature launch
- Pricing change or increase
- Market expansion or new segment entry
- Any GTM initiative that needs scope + strategy

## How It Works

**Step 1: You provide context**
- Product/feature being launched
- Target audience
- Success metrics
- Timeline/constraints

**Step 2: Skill assigns tier**
- T1: Company bet (6-12 week campaign, high budget)
- T2: Major initiative (2-4 weeks, medium investment)
- T3: Routine launch (1 week, standard process)
- T4: Minimal lift (internal only, <1 day)

**Step 3: Skill generates brief**
- Strategic rationale for tier
- Positioning angles (from brain Section 3)
- Channel strategy by tier
- Success metrics framework
- Competitive context (from brain Section 4)
- Timeline estimate

**Step 4: Skill updates brain Section 7**
- Captures launch in your history
- Self-learns from actuals (after launch/retro)
- Future launches get smarter recommendations

## Example Prompts

**"Help me scope this launch"**

We're launching SSO integration for enterprise customers.
Currently doing $2M ARR, trying to reach $5M by EOY.
Our main competitors (Okta, Entra) have this.
What tier is this? What's the GTM strategy?

**"Run GTM strategy with full workflow"**

/workflow-orchestrator "Full launch workflow for analytics dashboard"
DRI: me
Timeline: 8 weeks
Target: mid-market product teams

## What This Skill Reads

- Brain Section 2 (ICP & personas)
- Brain Section 3 (positioning)
- Brain Section 4 (competitive landscape)
- Brain Section 5 (proof points)
- Brain Section 7 (launch history for self-learning)

## What This Skill Writes

- Brain Section 7: Adds launched product/feature with actual results (after retro)

## Tier Framework

| Tier | Scope | Timeline | Budget | Use Case |
|------|-------|----------|--------|----------|
| T1 | Company bet | 6-12 weeks | High | Major product, market entry, pricing |
| T2 | Major init | 2-4 weeks | Medium | New segment, significant feature |
| T3 | Routine | 1 week | Standard | Regular feature, minor expansion |
| T4 | Minimal | <1 day | Low | Internal, bug fix, small tweak |

## Next Steps

After strategy is assigned:
1. Run `positioning-messaging` to build positioning for your audience
2. Run `competitive-battlecard` for competitive context
3. Run `workflow-orchestrator` to chain all execution skills
4. After launch, run `retro` to capture learnings → updates brain
