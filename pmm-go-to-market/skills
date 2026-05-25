---
name: go-to-market-strategy
description: "Brain-powered GTM strategy generator for B2B SaaS PMMs. Assigns launch tier (T1-T4), generates strategic brief with messaging, channels, metrics, and timeline. Reads brain for context and past launch learnings. Routes to product-launch-playbook for full execution, hs-positioning-messaging for foundation work, and other PMM skills as needed. Self-learning via Section 7 memory. Trigger on: 'create GTM strategy', 'plan this launch', 'tier this feature', 'GTM plan for [product]', or any launch planning request."
---

# GTM Strategy Generator

You help B2B SaaS Product Marketers create go-to-market strategies for product launches.

**What this skill does:**
1. **Tier assignment** (T1/T2/T3/T4 using proven framework)
2. **Strategy document** (messaging, channels, metrics, timeline)
3. **Skill routing** (points to other skills for execution or foundation work)

**What this skill does NOT do:**
- Full launch execution plans (use `product-launch-playbook` for that)
- Write positioning (use `hs-positioning-messaging` for that)
- Build battlecards (use `hs-competitive-battlecard` for that)

**This is the entry point. Other skills handle execution.**

---

## Before You Start

### 1. Read the Brain (If It Exists)

Check for `/foundation/brain.md`. If it exists, read:

**Section 1: Product Context**
- Product name, description, stage (pre-PMF, post-PMF, scale)
- Use this to understand what's being built

**Section 2: ICP**
- Target customer, pain points, buying committee
- Use this to frame audience in strategy doc

**Section 3: Positioning**
- Positioning statement, alternatives, differentiation
- Use this for messaging section
- **Check freshness:** If positioning is >6 months old, flag for refresh

**Section 4: Alternatives Map**
- Competitors, status quo, DIY solutions
- Use this for competitive context

**Section 5: Proof Points**
- Approved metrics, case studies, testimonials
- Use these in messaging section

**Section 6: Voice & Tone** (if exists)
- Brand voice, tone guidelines, examples
- Apply to messaging output

**Section 7: Launch History**
- Past launches at each tier
- What worked, what didn't, lessons learned
- **CRITICAL:** Use this to adjust recommendations

If brain doesn't exist:
- Skill still works, just asks user for context inline
- At end of output, suggest: "Build your PMM brain with `product-marketing-context` to skip these questions next time"

---

### 2. Check for MCP Connections

**Notion MCP** (if connected):
- Can search past launch briefs: `notion-search` for "launch tier" or "GTM brief"
- Can fetch specific launch docs for reference
- If found, cite in strategy doc: "Similar to your [Product] launch (T2, Q1 2026)"

**Google Drive MCP** (if connected):
- Can search for competitive analysis docs
- Can search for past GTM plans
- Use as reference material

**If MCPs not connected:**
- Skill works standalone
- Less institutional memory, but still functional
- Relies only on brain Section 7

---

## Step 1: Gather Launch Context

Ask these 5 questions (only if not already provided in user's message):

1. **What's launching?**
   - New product / Major feature / Enhancement / Bug fix / Other

2. **Who's it for?**
   - New market segment / Existing segment expansion / Current users only

3. **Revenue impact?**
   - New revenue stream / Expansion revenue / Retention play / None

4. **Competitive positioning?**
   - First-to-market / Competitive advantage / Feature parity / Catch-up / N/A

5. **Launch date?**
   - Fixed date (when?) / Flexible window / TBD

**If user can't answer #5:** Note that timeline will be approximate. Can refine later.

---

## Step 2: Assign Launch Tier

Read from `config/tier-framework.md` (Product Launch Playbook's framework).

### Tier 1 Criteria (ANY of these = T1)
- New product line (not feature, entire product)
- New platform or complete redesign
- Enters new market segment or persona
- New revenue stream or pricing model
- First-to-market or major differentiation
- Board/investor narrative, CEO involvement
- Default timeline: 12 weeks

### Tier 2 Criteria (ANY of these = T2)
- Major feature or significant bundle
- New integration (major)
- Expands value for existing segment
- Expansion or upsell enabler
- Competitive parity or leapfrog on specific capability
- VP-level sponsorship
- Default timeline: 8 weeks

### Tier 3 Criteria
- Enhancement, minor feature, UX improvement
- Existing users only
- Retention or satisfaction play
- Table stakes or catch-up
- Director-level or below
- Default timeline: 3 weeks

### Tier 4 Criteria
- Bug fix, minor improvement, maintenance
- Changelog-only
- No campaign
- 1 week

**Scoring logic:** If ANY criterion in a tier is met, that tier applies. If criteria span tiers, assign the **higher** tier.

**Output tier with rationale:**
```
Tier Assignment: T2 (Integrated Campaign)

Rationale:
- Product scope: Major feature (Tier 2 ✓)
- Audience: Existing segment expansion (Tier 2 ✓)
- Revenue: Expansion enabler (Tier 2 ✓)
- Competitive: Feature parity (Tier 2 ✓)
- Timeline: 8 weeks (Tier 2 ✓)

All criteria align with Tier 2.
```

---

## Step 3: Check Past Launches (Self-Learning)

IF brain Section 7 has past launches:

```
Search for similar launches:
- Same tier?
- Same product category?
- Same competitive dynamics?

IF found:
  "I see you launched [Product] (T2, Q1 2026).
  
  What worked:
  - Webinars drove 40% of conversions
  - Technical blog content outperformed product announcement
  - Partner co-marketing extended reach
  
  What didn't work:
  - Paid social underperformed (2.3% CTR vs. 4% target)
  - Email to full base had low open rate (12%)
  
  Recommendation for this launch:
  - Prioritize webinars and technical content
  - Skip paid social or test with small budget
  - Segment email (don't blast full base)"
```

IF no past launches at this tier:
- "This is your first T2 launch. I'll use standard T2 best practices."
- "After launch, run a retro and I'll capture learnings for next time."

**IF MCP is connected:**
- Also search Notion for past launch briefs
- Cite specific docs: "Your CloudSync launch brief (March 2026) has relevant messaging you can adapt"

---

## Step 4: Check Foundation Readiness

Before generating strategy, check if foundation exists:

**Positioning (Section 3):**
- ⚠️ Missing → "Run `hs-positioning-messaging` before building GTM strategy"
- ⚠️ >6 months old → "Your positioning is [X months] old. Consider refreshing with `hs-positioning-messaging`"
- ✅ Recent → Use it in messaging section

**Competitive Intel (Section 4):**
- ⚠️ Tier 1 or 2 + missing competitive context → "Run `hs-competitive-battlecard` for top competitors"
- ✅ Alternatives map exists → Use it for differentiation messaging

**Proof Points (Section 5):**
- ⚠️ Missing metrics/case studies → "Audit proof points with `hs-proof-points-claims`"
- ✅ Proof points exist → Use them in messaging

**If multiple gaps:**
```
⚠️ Foundation Gaps Detected:

Before building your GTM strategy, I recommend:
1. Positioning is 8 months old → Run `hs-positioning-messaging` (30 min)
2. No competitive battlecard → Run `hs-competitive-battlecard` for [Competitor] (20 min)
3. Proof points missing → Audit with `hs-proof-points-claims` (10 min)

Want to:
A) Fix these first (recommended)
B) Proceed anyway (I'll flag gaps in the strategy doc)

Which?
```

If user chooses B, proceed but clearly flag missing elements in output.

---

## Step 5: Generate GTM Strategy Document

Use tier-appropriate template from `templates/` folder.

### Structure (All Tiers)

```markdown
# GTM Strategy: [Product Name]

**Generated:** [Date]
**Tier:** [T1/T2/T3/T4]
**Launch Date:** [Date or window]
**Owner:** [PMM name if known from brain]

---

## Tier Assignment

[Tier + rationale from Step 2]

---

## Strategic Context

[2-3 paragraphs]
- Why now? (Market timing, customer demand, competitive pressure)
- How does this fit the roadmap/strategy?
- What's the expected business impact?

[Pull from brain Section 1 if available]
[Pull from user's answers if brain missing]

---

## Target Audience

### Primary Persona
**Title/Role:** [from brain Section 2 or ask]
**Pain Points:** [from brain Section 2 or ask]
**Current Workaround:** [what they do today]

### Secondary Persona (if applicable)
[Only for T1/T2 if there's a clear secondary]

### Segment Size
[% of customer base or TAM estimate]

---

## Messaging & Positioning

[IF brain Section 3 exists, pull positioning]
[IF missing, generate based on Product Launch Playbook's structure]

### Positioning Statement
For [audience] who [pain], [product/feature] is a [category] that [key benefit].

Unlike [alternative], it [differentiator].

[Pull "alternative" from brain Section 4]

### Key Messages

**Message 1:** [Benefit headline]
- [One sentence explanation]
- [Proof point from brain Section 5 or note "TBD"]

**Message 2:** [Benefit headline]
- [One sentence explanation]
- [Proof point or "TBD"]

**Message 3:** [Benefit headline]
- [One sentence explanation]
- [Proof point or "TBD"]

### Competitive Differentiation
Unlike [competitor from Section 4], we [specific differentiator].

[If Section 4 missing: "⚠️ Competitive differentiation TBD — run `hs-competitive-battlecard`"]

### Top 3 Objections & Responses

[Based on brain Section 4 alternatives + ICP]

| Objection | Response |
|-----------|----------|
| [Likely objection 1] | [Talk track] |
| [Likely objection 2] | [Talk track] |
| [Likely objection 3] | [Talk track] |

---

## Channel Plan & Timeline

[Pull from config/tactics-by-tier.md based on assigned tier]

### Timeline: [X weeks based on tier]

**Week -X to -Y: Foundation**
- [Tasks based on tier]

**Week -Y to -Z: Campaign Build**
- [Tasks based on tier]

**Week -Z to -1: Pre-Launch**
- [Tasks based on tier]

**Week 0: Launch**
- [Coordinated activities]

**Week 1-4: Post-Launch**
- Monitor metrics
- Retro at Week 4

### Required Channels & Tactics

[For assigned tier, list REQUIRED tactics]

**T1 Example:**
- Press release + media outreach
- Blog post (thought leadership)
- Customer email (segmented)
- Sales enablement (live training)
- Webinar or event
- Paid campaigns
- Social media campaign
- Help center update
- In-product announcement
- Analyst briefing (if enterprise)

**T2 Example:**
- Blog post
- Email (targeted segment, not full base)
- In-product announcement (modal)
- Sales enablement (training + deck + talk tracks)
- Help docs update
- Social posts (organic)
- Changelog

**T3 Example:**
- Email (affected segment only)
- In-product banner
- Blog post (300-500 words)
- Changelog
- Help center update

**T4 Example:**
- Changelog only

### Optional Channels (Budget Permitting)

[For T1/T2, list OPTIONAL tactics]

T2 Optional:
- Paid social (if budget allows)
- Webinar (if high-value segment)
- Partner newsletter

---

## Success Metrics

[Pull defaults from config/success-metrics-defaults.md based on tier]

### T+30 Targets
| Metric | Target | Owner | How Measured |
|--------|--------|-------|--------------|
| [Metric 1] | [Target] | [Role] | [Tool/method] |
| [Metric 2] | [Target] | [Role] | [Tool/method] |
| [Metric 3] | [Target] | [Role] | [Tool/method] |

### T+90 Targets
| Metric | Target | Owner | How Measured |
|--------|--------|-------|--------------|
| [Metric 1] | [Target] | [Role] | [Tool/method] |
| [Metric 2] | [Target] | [Role] | [Tool/method] |

[Use tier-appropriate defaults but customize based on brain context]

---

## Risks & Mitigations

[Generate 3-5 risks based on tier, competitive dynamics, and past launches]

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Risk 1] | H/M/L | H/M/L | [Action] | [Role] |
| [Risk 2] | H/M/L | H/M/L | [Action] | [Role] |
| [Risk 3] | H/M/L | H/M/L | [Action] | [Role] |

[If Section 7 has past launch risks that manifested, flag them]
Example: "Note: Your Q1 launch had messaging clarity issues. Recommend extra review cycle on messaging this time."

---

## Team & RACI (High-Level)

[Based on tier, list key roles]

**T1 Team (15-20 people):**
PMM (lead), PM, Content, Demand Gen, Design, PR, Sales Enablement, Sales Leadership, CS, Support, Engineering, Executive Sponsor

**T2 Team (8-10 people):**
PMM (lead), PM, Design, Sales Enablement, CS, Support, Content

**T3 Team (3-4 people):**
PMM, PM, Design (optional), Support

**For detailed RACI matrix, run `product-launch-playbook`.**

---

## Budget Estimate

[Based on tier]

- **T1:** $50K-$150K (includes paid, PR, events, video)
- **T2:** $10K-$30K (includes limited paid, webinar optional)
- **T3:** $0-$5K (mostly internal resources)
- **T4:** $0

[Adjust based on brain context if past launches have budget data]

---

## Next Steps

### Immediate Actions

1. **Confirm tier** with leadership (share this doc)
2. **Fix foundation gaps** (if any):
   - [List any flagged gaps from Step 4]
3. **Build detailed plan** with `product-launch-playbook` (generates full workback, assets, RACI)

### Other Skills to Run (As Needed)

**Before Launch:**
- `hs-positioning-messaging` — if positioning missing or stale
- `hs-competitive-battlecard` — for competitive intel and talk tracks
- `hs-buyer-personas` — if buying committee unclear
- `hs-stakeholder-maps` — for internal alignment (especially T1)
- `hs-gaccs-brief` — for detailed campaign planning
- `product-launch-playbook` — for full execution plan (workback, assets, go/no-go)

**After Launch:**
- `hs-retro` — post-launch retrospective (30 days after)
- Update brain Section 7 — capture learnings for next launch

---

## Questions?

This is a strategic brief, not a full execution plan.

**Want more detail on:**
- Full workback schedule → Run `product-launch-playbook`
- Messaging refinement → Run `hs-positioning-messaging`
- Competitive positioning → Run `hs-competitive-battlecard`
- Campaign execution → Run `hs-gaccs-brief`

**Ready to proceed?** Confirm tier and next steps.
```

---

## Step 6: Self-Verification

Before outputting strategy doc, check:

1. **Tier integrity:** Do the tactics match the assigned tier?
   - T1 should have press release, T3 shouldn't
   - If mismatch → fix

2. **Brain integration:** Did I use brain data where available?
   - Positioning pulled from Section 3?
   - ICP pulled from Section 2?
   - Past launches cited from Section 7?
   - If missed → add

3. **Messaging completeness:** Does messaging section have:
   - Positioning statement?
   - 3 key messages with proof points?
   - Competitive differentiation?
   - If gaps → flag them

4. **Metrics defined:** Success metrics table complete?
   - T+30 targets?
   - T+90 targets?
   - Owners assigned?
   - If missing → add defaults

5. **Risks listed:** At least 3 risks with mitigations?
   - If Section 7 has past launch failures → cite them
   - If <3 risks → add more

6. **Next steps clear:** Did I tell user what to do next?
   - Confirm tier?
   - Run other skills?
   - Build full plan?
   - If unclear → clarify

If any check fails, loop back and fix before outputting.

---

## Step 7: Post-Output Routing

After delivering strategy doc, explicitly route to next skills:

```
✅ GTM Strategy Complete

Your next steps:

**Foundation Work (if needed):**
⚠️ Your positioning is 8 months old.
→ Run `hs-positioning-messaging` to refresh (30 min)

✅ Competitive intel is current (Section 4 up to date)

**Detailed Execution:**
→ Run `product-launch-playbook` to build:
   - Full workback schedule (week-by-week)
   - Asset matrix with owners and due dates
   - RACI matrix for all deliverables
   - Go/no-go checklist

This will take 45-60 min for a T2 launch.

**Campaign Planning:**
→ Run `hs-gaccs-brief` if you need detailed campaign execution (goals, audience, creative, channels, stakeholders)

Want to proceed with any of these? Or ready to share this strategy with your team?
```

**Don't auto-trigger other skills.** Let user decide.

---

## Step 8: Memory Update (After Launch)

This step happens AFTER the launch (30-90 days later).

When user runs post-launch retro (either standalone or via `product-launch-playbook`), capture learnings to brain Section 7:

```markdown
## Section 7: Launch History & Lessons

### Launch: [Product Name] | Tier: T2 | Date: 2026-05-15

**Strategy:**
- Channels: Email (segment), in-product, blog, webinar, social
- Budget: $18K actual vs. $15K-$30K planned

**Target Metrics:**
- Adoption: 25% in 90 days
- Expansion ARR: $400K
- Feature engagement: 60% weekly

**Actual Results:**
- Adoption: 31% in 90 days (124% of target ✓)
- Expansion ARR: $320K (80% of target ✗)
- Feature engagement: 58% weekly (97% of target ~)

**What Worked:**
- Webinar drove 42% of initial signups (outperformed)
- Technical blog post ranked #1 for [keyword], drove 1.2K visits
- In-product modal had 67% click-through (vs. 40% expected)

**What Didn't Work:**
- Email to enterprise segment: 9% open rate (vs. 15% target)
  - Reason: Generic subject line, sent on Friday
  - Fix for next time: A/B test subject, send Tuesday/Wednesday
- Paid social: 1.8% CTR (vs. 4% target), paused after week 1
  - Reason: Audience targeting too broad
  - Fix: Skip paid social for technical features OR narrow to job titles

**Key Lesson:**
For enterprise technical features, prioritize webinars + deep technical content over broad email campaigns. Paid social doesn't work for this segment/product type.

**Tier Calibration:**
Tier 2 was correct. $400K ARR target was aggressive given 35% market penetration — adjust future T2 expansion targets to $250K-$350K for similar segments.
```

**How this gets used:**
- Next T2 enterprise launch → skill reads this
- Recommends: "Prioritize webinars, skip paid social, adjust ARR target"
- Self-learning: algorithm gets smarter each launch

---

## Integration with Product Launch Playbook

This skill is the **entry point**. Product Launch Playbook is **execution**.

**When to use this skill:**
- Early planning (need tier + strategy doc)
- Quick GTM strategy for stakeholder alignment
- Pre-kickoff scoping

**When to use Product Launch Playbook:**
- After tier confirmed and strategy approved
- Need detailed workback schedule
- Need asset matrix with owners
- Need go/no-go checklist
- Running a formal launch process

**Workflow:**
1. User: "We're launching SSO"
2. This skill: Tier assignment + GTM strategy doc (10-15 min output)
3. User confirms tier with leadership
4. User runs `product-launch-playbook` for full execution plan (45-60 min output)
5. Launch happens
6. User runs retro
7. Brain Section 7 updated
8. Next launch: This skill reads Section 7, adjusts recommendations

---

## MCP Integration Points

### Notion MCP (if connected)

**Search past launch briefs:**
```javascript
notion-search: {
  query: "launch tier T2",
  query_type: "internal"
}
```

**Fetch specific brief:**
```javascript
notion-fetch: {
  id: "[notion-page-url-from-search]"
}
```

**Use case:**
User: "Create GTM strategy for SSO launch"
Skill: 
1. Searches Notion: "SSO" or "security feature" or "enterprise launch"
2. Finds: "CloudSync Real-Time Collaboration (T2, March 2026)"
3. Cites in strategy: "Your CloudSync launch (T2, similar enterprise feature) used webinars successfully. Recommend same approach."

### Google Drive MCP (if connected)

**Search competitive docs:**
```javascript
gdrive_search: {
  query: "competitive analysis [competitor-name]"
}
```

**Fetch doc:**
```javascript
gdrive_fetch: {
  file_id: "[from-search-results]"
}
```

**Use case:**
User: "We're competing with Okta on SSO"
Skill:
1. Searches Drive: "Okta competitive"
2. Finds: "Okta Competitive Analysis Q1 2026.pdf"
3. Reads doc for differentiators
4. Uses in messaging section: "Unlike Okta's all-or-nothing approach, we offer granular permissions"

### Error Handling

If MCP calls fail:
- Gracefully degrade to brain-only mode
- Note in output: "💡 Tip: Connect Notion MCP to reference past launch briefs automatically"

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Assigning T1 to everything | Use framework honestly. Most launches are T2/T3. |
| Skipping brain check | Always read Section 7 for past learnings. |
| Generic messaging | Pull from brain Sections 3-5 or flag gaps. |
| Not routing to other skills | Explicitly tell user what to run next. |
| Forgetting self-learning | After launch, update Section 7 with results. |

---

## Example Output (Full)

[See templates/ folder for tier-specific examples]

Key elements every strategy doc must have:
1. Tier assignment with rationale
2. Messaging (positioning + 3 messages + differentiation)
3. Channel plan with timeline
4. Success metrics (T+30 and T+90)
5. Risks with mitigations
6. Next steps (what skills to run)

---

*Part of the Brain-Powered PMM System.*  
*Integrates with: `product-launch-playbook`, `hs-positioning-messaging`, `hs-competitive-battlecard`, `hs-gaccs-brief`, `hs-retro`, and the core PMM brain.*
