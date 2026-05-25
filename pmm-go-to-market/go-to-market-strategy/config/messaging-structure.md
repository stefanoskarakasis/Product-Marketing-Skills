# Messaging Structure Template

Framework for developing launch messaging — pulled from your GTM Brief template + April Dunford positioning + Fletch PMM methodology.

**Use this structure when generating the "Messaging & Positioning" section of GTM strategy docs.**

---

## Core Positioning Statement (Required)

**Template:**

```
For [target audience]
who [pain point or need],
[product/feature name] is a [category]
that [key benefit or outcome].

Unlike [primary alternative],
it [key differentiator].
```

**How to populate:**

1. **[target audience]:** Pull from brain Section 2 (ICP) → primary persona title + segment
   - Example: "VP of Data at mid-market SaaS companies"

2. **[pain point or need]:** Pull from brain Section 2 (ICP) → top pain point
   - Example: "need real-time visibility into pipeline health"

3. **[product/feature name]:** The thing being launched
   - Example: "CloudSync Real-Time Collaboration"

4. **[category]:** How you want buyers to frame this (from brain Section 3)
   - Example: "collaborative data workspace" (not "file sharing tool")
   - Tip: Choose a category where you can be #1 or differentiated

5. **[key benefit]:** The outcome, not the feature (from brain Section 3)
   - Example: "enables teams to work together without losing control"
   - Not: "allows multiple users to edit simultaneously"

6. **[primary alternative]:** What buyers use today (from brain Section 4)
   - Example: "spreadsheets and email threads" or "CompetitorA"
   - Use status quo if first-to-market, competitor if playing catch-up

7. **[key differentiator]:** The thing that makes you different (from brain Section 4)
   - Example: "offers granular permissions that enterprise teams require"
   - Must be provable and tied to a real capability

**Bad example (feature-focused, no alternative anchoring):**
```
CloudSync Real-Time Collaboration lets teams edit documents together.
```

**Good example (outcome-focused, alternative-anchored):**
```
For data teams at mid-market SaaS companies who need to collaborate without losing control, CloudSync is a real-time workspace that enables multiple users to work together with enterprise-grade permissions. Unlike spreadsheets passed via email or tools like CompetitorA that treat everything as public, CloudSync gives teams granular control over who can view, edit, and manage each section.
```

---

## Key Messages (3 Required)

**Structure:**

Each message has:
1. **Benefit headline** (5-7 words, outcome-focused)
2. **Explanation** (1-2 sentences, how it works)
3. **Proof point** (metric, testimonial, or case study from brain Section 5)

**Template:**

```markdown
### Message 1: [Benefit Headline]

[One sentence explaining how it works]

**Proof:** [Metric or quote from brain Section 5, or note "TBD"]

---

### Message 2: [Benefit Headline]

[One sentence explaining how it works]

**Proof:** [Metric or quote, or "TBD"]

---

### Message 3: [Benefit Headline]

[One sentence explaining how it works]

**Proof:** [Metric or quote, or "TBD"]
```

**How to choose the 3 messages:**

1. **Message 1:** The primary benefit (what most buyers care about most)
   - Usually: solves the biggest pain from ICP (brain Section 2)
   - Example: "Collaborate without chaos"

2. **Message 2:** The usage benefit (what the experience is like)
   - Usually: adoption or time-to-value story
   - Example: "Your team is already here — now they can work here"

3. **Message 3:** The trust/risk mitigation benefit (why it's safe to choose you)
   - Usually: security, compliance, or differentiation vs. alternatives
   - Example: "Enterprise-grade collaboration, not consumer-grade sharing"

**Example:**

```markdown
### Message 1: Collaborate Without Chaos

Real-time editing with granular permissions means your team can work together without anyone accidentally breaking your setup. Section-level controls (viewer/editor/admin) ensure the right people have the right access.

**Proof:** Beta customer Acme Corp reduced workspace duplication by 73% — teams now work in one shared space instead of creating copies.

---

### Message 2: No Migration, No Training

Your team is already using CloudSync. Now they can work together in the exact same workspace they know. Invite teammates, they see your structure, and they start contributing immediately.

**Proof:** Average time from invite to first edit: 4 minutes (beta data, n=287 users)

---

### Message 3: Built for Enterprise Security, Not Consumer Sharing

Unlike tools that treat everything as public, CloudSync is built for teams that need audit trails, SSO, and admin controls — not another tool IT has to fight.

**Proof:** SOC2 compliant from day one. Full audit log for every change. Admin can set default permissions at workspace, folder, or section level.
```

---

## Competitive Differentiation (Required for T1/T2)

**Template:**

```markdown
Unlike [primary competitor or alternative],
[your product] [specific differentiator with proof].
```

**How to populate:**

1. **[primary competitor or alternative]:** From brain Section 4 (Alternatives Map)
   - Use: The thing buyers compare you to most often in sales calls
   - Could be: direct competitor, status quo, DIY solution, adjacent category

2. **[specific differentiator]:** The capability they lack (from brain Section 4)
   - Must be: Provable, matters to buyers, hard for them to copy quickly
   - Not: Vague ("better UX") or subjective ("more intuitive")

**Examples:**

**Direct competitor:**
```
Unlike CompetitorA's "everything is open" sharing model, CloudSync offers section-level permissions (viewer/editor/admin) — critical for regulated industries where not everyone should see everything.
```

**Status quo:**
```
Unlike spreadsheets passed via email, CloudSync gives you a real-time workspace with version history, conflict resolution, and granular access controls — so your team collaborates without creating 14 versions of the same file.
```

**Adjacent category:**
```
Unlike project management tools that force you into their workflow, CloudSync adapts to how your team already works — you structure your workspace your way, then invite teammates to collaborate.
```

**If brain Section 4 is missing:**
```
⚠️ Competitive differentiation TBD — run `hs-competitive-battlecard` for top competitors.
```

---

## Objection Handling (Top 3)

**Template:**

| Objection | Response |
|-----------|----------|
| "[Likely objection from buyer]" | [Talk track that reframes or addresses] |
| "[Likely objection from buyer]" | [Talk track] |
| "[Likely objection from buyer]" | [Talk track] |

**How to identify objections:**

1. Pull from brain Section 4 (Alternatives Map) → "Why buyers choose alternatives"
2. Pull from past sales calls (if win/loss data available)
3. Infer from ICP pain points (brain Section 2) → what would make them hesitate?

**How to write responses:**

- **Don't:** Dismiss the objection ("that's not actually a problem")
- **Do:** Reframe or address with proof
- Structure: Acknowledge + Reframe + Proof

**Examples:**

| Objection | Response |
|-----------|----------|
| "This sounds complicated — we don't have time to onboard our team." | Onboarding is instant. Your team already uses CloudSync individually — collaboration just means inviting them into your existing workspace. Average time to first edit: 4 minutes. No training needed. |
| "We already use [Competitor] for collaboration — why switch?" | If [Competitor] is working, stick with it. Where we see teams switch is when they need granular permissions — [Competitor] treats everything as fully open, which doesn't work for regulated industries or teams with contractors. If that's not your situation, [Competitor] is fine. |
| "Our IT team won't approve another collaboration tool." | CloudSync is already approved if your team is using it for individual work. Collaboration is an add-on to your existing instance — same SSO, same security controls, same compliance certifications. We're not asking IT to approve a new tool; we're activating a feature in a tool they already approved. |

**If you lack objection data:**
- Note: "⚠️ Objections TBD — run competitive analysis and sales interview to surface common hesitations"
- Proceed with educated guesses based on ICP and alternatives

---

## Message Hierarchy (How Messages Nest)

```
Positioning Statement (the anchor)
    ↓
Key Message 1 (primary benefit)
    ↓
Key Message 2 (usage benefit)
    ↓
Key Message 3 (trust/risk mitigation)
    ↓
Competitive Differentiation (anchors against alternatives)
    ↓
Objection Handling (addresses specific hesitations)
```

**Every asset flows from positioning:**
- Homepage hero: Positioning statement (simplified)
- Email subject line: Key Message 1 (benefit headline)
- Blog post: Positioning + 3 messages + differentiation
- Sales deck: Positioning on slide 1, one slide per message
- Battlecard: Differentiation + objections front and center

**Consistency rule:**
- Same positioning across all channels
- Same 3 messages (phrasing can adapt, core idea stays)
- Same differentiator (word-for-word in high-stakes contexts like sales)

---

## Voice & Tone Application (If Available)

If brain Section 6 has Voice & Tone guidelines:

1. **Apply tone to messaging:**
   - If brand voice is "confident but approachable" → don't say "industry-leading" (too corporate)
   - If brand voice is "technical and precise" → don't say "magical" (too fluffy)

2. **Adapt examples to voice:**
   - Developer audience + casual tone → "Unlike spreadsheet hell, CloudSync gives you..."
   - Enterprise audience + formal tone → "Unlike traditional spreadsheet workflows, CloudSync provides..."

3. **Keep positioning structure, change words:**
   - Positioning framework (for/who/pain, product/category/benefit, unlike/differentiator) stays
   - Word choice reflects brand voice

**If brain Section 6 missing:**
- Use neutral, clear B2B SaaS voice (professional but not stuffy)
- Avoid: jargon, hype, vague claims
- Prioritize: clarity, specificity, proof

---

## When to Flag Messaging Gaps

**During strategy doc generation, flag if:**

1. **Positioning >6 months old (brain Section 3):**
   ```
   ⚠️ Your positioning was last updated 8 months ago.
   Market may have shifted. Recommend refresh before launch.
   → Run `hs-positioning-messaging` (30 min)
   ```

2. **No proof points (brain Section 5 empty):**
   ```
   ⚠️ No approved proof points found.
   Key messages need metrics or testimonials for credibility.
   → Run `hs-proof-points-claims` to audit claims (15 min)
   ```

3. **Competitive intel missing (brain Section 4 incomplete):**
   ```
   ⚠️ Differentiation vs. [Competitor] is unclear.
   Sales needs this for competitive deals.
   → Run `hs-competitive-battlecard` for [Competitor] (20 min)
   ```

4. **ICP unclear (brain Section 2 missing primary persona):**
   ```
   ⚠️ Target audience not defined.
   Can't write effective messaging without knowing who we're talking to.
   → Run `hs-buyer-personas` (25 min)
   ```

**Don't block strategy generation**, but clearly flag gaps in output.

---

## Self-Learning: What Messaging Worked

After launch, capture messaging performance in brain Section 7:

```markdown
**Messaging Performance:**

**What resonated:**
- "Collaborate without chaos" (Message 1) → highest email click-through (8.2%)
- Granular permissions angle → cited in 67% of win calls
- "Unlike spreadsheets" positioning → strong social engagement

**What fell flat:**
- "Enterprise-grade" messaging → felt too corporate for SMB segment
- Speed claims ("4 minutes to first edit") → buyers didn't care about speed, cared about control

**Lesson for next launch:**
- Lead with control/permissions angle (not speed)
- Avoid "enterprise-grade" unless selling to literal enterprise
- Spreadsheet comparison works across segments
```

Next launch → skill reads this, adjusts messaging recommendations.

---

*This structure is baked into the GTM strategy skill. Every strategy doc includes a Messaging & Positioning section built with this framework.*
