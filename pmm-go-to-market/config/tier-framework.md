# Launch Tier Framework

This framework assigns launch tier (T1/T2/T3/T4) based on business impact, audience, competitive dynamics, and organizational sponsorship.

**Source:** Adapted from Product Launch Playbook + Intercom's launch tiering methodology.

---

## Decision Logic

**If ANY criterion in a tier is met, that tier applies.**

**If criteria span multiple tiers, assign the HIGHER tier.**

---

## Tier 1: Major Launch (Dedicated Campaign)

### Criteria (ANY = T1)
- **Product scope:** New product line, new platform, or complete redesign
- **Audience:** Enters a new market segment or persona
- **Revenue:** New revenue stream or new pricing model
- **Competitive:** First-to-market or major differentiation
- **Executive visibility:** Board/investor narrative, CEO involvement
- **External comms:** Press release, analyst briefing, event keynote

### What Tier 1 Means

**Timeline:** 12 weeks pre-launch (minimum)

**Budget:** $50K-$150K
- Includes: PR/media, paid campaigns, video production, events, analyst relations

**Team Size:** 15-20 people
- PMM (lead), PM, Content Marketing, Demand Gen, Design, PR/Comms, Sales Enablement, Sales Leadership, Customer Success, Support, Engineering, Executive Sponsor, RevOps, Legal (if needed)

**Channel Investment:**
- ALL channels active (press, blog, email, paid, social, events, enablement, analyst relations)
- Multiple customer segments
- Extensive sales enablement (live training, decks, battlecards, talk tracks)
- Customer webinar or event
- Video/demo production

**Success Metrics:**
- Revenue impact: $500K+ ARR in first year
- Adoption: 40% of target segment in 90 days
- Win rate: +10pp improvement
- Brand/market lift: Press mentions, analyst awareness
- NPS impact: +5-10 points

**Examples:**
- Launching an entirely new product line
- Entering a new market (e.g., healthcare when you've only done fintech)
- New business model (e.g., launching a marketplace when you've been SaaS-only)
- First-to-market capability that redefines category

---

## Tier 2: Moderate Launch (Integrated Campaign)

### Criteria (ANY = T2)
- **Product scope:** Major feature, significant bundle, or new integration
- **Audience:** Expands value for existing segment (not new market)
- **Revenue:** Expansion or upsell enabler
- **Competitive:** Parity or leapfrog on specific capability
- **Executive visibility:** VP-level sponsorship
- **External comms:** Blog, email, social (no press)

### What Tier 2 Means

**Timeline:** 8 weeks pre-launch (standard)

**Budget:** $10K-$30K
- Includes: Limited paid campaigns, webinar (optional), organic social

**Team Size:** 8-10 people
- PMM (lead), PM, Design, Sales Enablement, Customer Success, Support, Content Marketing, Demand Gen (optional)

**Channel Investment:**
- Targeted channels (email to segment, not full base)
- Blog post + organic social
- Sales enablement (training + deck + talk tracks)
- In-product announcement
- Help docs update
- Webinar (optional, if high-value segment)
- Paid social (optional, budget-dependent)

**Success Metrics:**
- Revenue impact: $100K-$500K ARR (if expansion play)
- Adoption: 25% of target segment in 90 days
- Feature engagement: 60% weekly usage
- Win rate: +5pp (if competitive feature)
- NPS impact: neutral or positive

**Examples:**
- Major feature that's been heavily requested (#1-3 on roadmap)
- Integration with a major platform (Salesforce, Slack, etc.)
- Competitive catch-up feature (competitor has it, you need parity)
- Significant expansion of existing capability

---

## Tier 3: Minor Launch (Lightweight Campaign)

### Criteria
- **Product scope:** Enhancement, minor feature, UX improvement
- **Audience:** Existing users only (no new segment)
- **Revenue:** Retention or satisfaction play (no direct revenue)
- **Competitive:** Table stakes or catch-up (not strategic)
- **Executive visibility:** Director-level or below
- **External comms:** Release notes, in-app, changelog

### What Tier 3 Means

**Timeline:** 3 weeks pre-launch (or less)

**Budget:** $0-$5K
- Mostly internal resources, minimal external spend

**Team Size:** 3-4 people
- PMM, PM, Design (optional), Support

**Channel Investment:**
- Email to affected segment only (not full customer base)
- In-product banner (not modal)
- Blog post (300-500 words)
- Changelog entry
- Help center update
- Social post (maybe 1, organic only)
- Sales/CS email update (no training)

**Success Metrics:**
- Adoption: 20% in 30 days
- Support tickets: <10 per 100 users
- CSAT: >4.0 for the feature
- NPS impact: neutral (don't hurt it)

**Examples:**
- Keyboard shortcuts for power users
- Dark mode
- CSV export improvements
- Performance optimization (faster load times)
- UI polish or minor workflow improvement

---

## Tier 4: Maintenance (No Campaign)

### Criteria
- **Product scope:** Bug fix, minor improvement, maintenance
- **Audience:** Existing users (passive discovery)
- **Revenue:** None
- **Competitive:** N/A
- **External comms:** Changelog only

### What Tier 4 Means

**Timeline:** 1 week (or concurrent with development)

**Budget:** $0

**Team Size:** 1-2 people
- PMM (changelog writer), Support (help doc update if needed)

**Channel Investment:**
- Changelog entry only
- Help doc update (if relevant)
- Internal Slack announcement (optional)
- No marketing campaign, no sales enablement, no customer email

**Success Metrics:**
- Changelog views
- Support ticket reduction (if bug fix)
- No formal tracking needed

**Examples:**
- Bug fixes
- Security patches
- Behind-the-scenes infrastructure work
- Minor copy changes
- Small UI tweaks

---

## Edge Cases & Tie-Breakers

### "This feels like a T2 but has T1 characteristics"

**Rule:** Round UP.

**Example:** Major feature (T2) that also has CEO visibility (T1) → Assign T1.

**Why:** Under-tiering burns goodwill. If leadership treats it as T1, resource it as T1.

---

### "Competitor launched this 6 months ago, we're catching up"

**Evaluation:**
- Is this feature parity (T2) or strategic catch-up that unlocks a market (T1)?
- If it's blocking deals → likely T2 minimum
- If it's "nice to have" → T3

**Past launch data (Section 7):** Check if similar catch-up features drove revenue. If yes, tier higher.

---

### "Small feature, but our CEO wants to talk about it"

**CEO involvement = T1 by definition.**

**But:** Have a conversation with leadership first:
- "This meets T3 criteria on product scope. You're asking for T1 resourcing. That means 12 weeks, $100K budget, cross-functional team. Are you sure?"

If they confirm → T1. If they back down → T2 or T3 with exec comms add-on.

---

### "We're bundling 5 small features into one announcement"

**Evaluate the bundle:**
- Does the bundle create a new capability? → Possibly T2
- Are the features unrelated? → Still T3 (just one announcement for convenience)

**Example:** 
- ✅ "Real-time collaboration bundle" (live cursors + comments + sharing) → T2
- ❌ "Q2 quality improvements" (5 unrelated bug fixes) → T3

---

## Tier Calibration (Self-Learning)

After each launch, record actual results in brain Section 7.

If pattern emerges (e.g., "Last 3 T2 launches underperformed"), adjust:

**Option 1: Tighten T2 criteria**
- Raise the bar: "Expansion revenue must be $200K+ (not $100K+) to qualify as T2"

**Option 2: Add product-type modifier**
- "Infrastructure products take 2x longer to show ROI → reduce ARR target by 30% for these launches"

**Option 3: Adjust channel tactics**
- "Paid social hasn't worked for any enterprise T2 launch → remove from standard T2 playbook"

**Update this file** as you learn. The framework should evolve.

---

## Quick Reference Table

| Dimension | T1 | T2 | T3 | T4 |
|-----------|-------|-------|-------|-------|
| **Product Scope** | New product line, platform | Major feature, integration | Enhancement, minor feature | Bug fix, maintenance |
| **Audience** | New segment/market | Expand existing segment | Existing users only | Existing users (passive) |
| **Revenue** | New revenue stream | Expansion/upsell | Retention/satisfaction | None |
| **Competitive** | First-to-market | Parity/leapfrog | Table stakes | N/A |
| **Exec Sponsor** | CEO/Board | VP | Director | None |
| **Timeline** | 12 weeks | 8 weeks | 3 weeks | 1 week |
| **Budget** | $50K-$150K | $10K-$30K | $0-$5K | $0 |
| **Team** | 15-20 people | 8-10 people | 3-4 people | 1-2 people |
| **External Comms** | Press, analysts, event | Blog, email, social | Changelog, in-app | Changelog only |
| **Success Metric** | $500K+ ARR, 40% adoption | $100K-$500K ARR, 25% adoption | 20% adoption, CSAT >4.0 | Changelog views |

---

*This framework is a starting point. Adjust based on your company's stage, market, and past launch performance.*
