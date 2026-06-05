---
name: product-marketing-context
skill: product-marketing-context
version: 2.1.0
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
description: The PMM Brain - setup wizard + health audit. Create your brain once, use it everywhere. Zero repetition.
triggers:
  - setup brain
  - create brain
  - configure foundation
  - pmm foundation
  - brain wizard
  - initialize context
  - check brain health
  - audit brain
  - brain health score
last_updated: 2026-06-05
---

# PMM Brain Setup Wizard

This skill creates `/foundation/brain.md` — the central context file that all other PMM skills read first.

## What This Does

Guides you through building your PMM brain in ONE session:
1. Product Context (5 questions)
2. ICP Definition (8 questions)
3. Alternatives & Positioning (6 questions)
4. Voice & Tone (5 questions)
5. Market Context (4 questions)
6. Proof Points Registry (3 questions)

**Time to complete:** 15-20 minutes

**Output:** `/foundation/brain.md` (your GTM operating system)

---

## Execution Logic

### Step 1: Check for Existing Brain

```
Does /foundation/brain.md exist?
```

**If YES:**
- "I see you already have a brain file. What would you like to do?"
  - [ ] View current brain
  - [ ] Edit specific sections
  - [ ] Rebuild from scratch
  - [ ] Cancel

**If NO:**
- Check for legacy v1.x foundation files:
  - `.agents/product-marketing-context.md`
  - `.claude/product-marketing-context.md`
  - `.agents/icp.md`
  - `.agents/alternatives-map.md`
  - `.agents/voice-tone.md`
  - `.agents/market-context.md`
  - `.agents/proof-points.md`

**If legacy files found:**
- "I found old foundation files from v1.x. Want to migrate them automatically?"
  - [Yes] → Parse old files, pre-fill wizard answers
  - [No] → Start fresh wizard

**If no brain and no legacy:**
- "Let's build your PMM brain. This takes 15-20 minutes but you'll only do it once. Ready?"
  - [Yes] → Start wizard
  - [Not now] → Exit

---

### Step 2: Run the Wizard

**Tone:** Conversational, encouraging, specific. Ask ONE question at a time. After each answer, confirm understanding before moving to next question.

---

## Section 1: Product Context (5 questions)

**Q1.1 — Product Name**
"What's your product called?"

*Example: "HubSpot", "Notion", "our AI meeting assistant"*

→ Store as `product_name`

---

**Q1.2 — Product Description**
"In 2-3 sentences, what does [product_name] do? Focus on the problem it solves, not features."

*Example: "HubSpot is a CRM platform that helps growing companies manage their entire customer journey. We solve the problem of disconnected sales, marketing, and service tools that create blind spots and slow down growth."*

→ Store as `product_description`

---

**Q1.3 — Stage**
"What stage is [product_name] at?"
- [ ] Pre-launch (idea/validation stage)
- [ ] Launch (first customers, PMF search)
- [ ] Growth (PMF found, scaling)
- [ ] Scale (market leader, optimization)

→ Store as `product_stage`

---

**Q1.4 — Target Market**
"Who is your primary target market? Be specific about company size, industry, role, or use case."

*Example: "Mid-market B2B SaaS companies (50-500 employees) in the sales, marketing, or customer success space. Our sweet spot is companies that just crossed $5M ARR and need to professionalize their GTM motion."*

→ Store as `target_market`

---

**Q1.5 — Core Value Proposition**
"Complete this sentence: [product_name] helps [target_market] to _____ so they can _____."

*Example: "HubSpot helps growing B2B companies unify their GTM data so they can make faster decisions and grow revenue predictably."*

→ Store as `value_proposition`

---

**Confirm Section 1:**
"Here's your Product Context:
- Product: [product_name]
- Stage: [product_stage]
- Target: [target_market]
- Value Prop: [value_proposition]

Look good? (yes/edit/skip for now)"

---

## Section 2: ICP Definition (8 questions)

**Q2.1 — Company Size**
"What company size (employee count or revenue) is your ideal customer?"

*Example: "50-500 employees OR $5M-$50M ARR"*

→ Store as `icp_company_size`

---

**Q2.2 — Industry / Vertical**
"Any specific industries or verticals? Or horizontal across all industries?"

*Example: "Horizontal — any B2B SaaS company" OR "Vertical — FinTech, HealthTech, and EdTech companies"*

→ Store as `icp_industry`

---

**Q2.3 — Geography**
"Primary geographic market(s)?"

*Example: "North America (US + Canada)" OR "Global, English-speaking"*

→ Store as `icp_geography`

---

**Q2.4 — Primary Persona**
"Who is the primary buyer or user? (Title + role description)"

*Example: "VP of Marketing — responsible for demand gen, owns the marketing tech stack, reports to CMO or CEO"*

→ Store as `icp_primary_persona`

---

**Q2.5 — Economic Buyer**
"Who actually signs the contract? (If different from primary persona)"

*Example: "CFO for deals over $50k/year" OR "Same as primary persona"*

→ Store as `icp_economic_buyer`

---

**Q2.6 — Champion Profile**
"Who becomes your internal champion? What do they care about?"

*Example: "Mid-level marketing ops managers who are frustrated with manual reporting. They care about looking good to their VP by saving time and increasing data accuracy."*

→ Store as `icp_champion`

---

**Q2.7 — Pain Points (Top 3)**
"What are the top 3 pain points your ICP has that your product solves?"

*Example:*
*1. Disconnected data across 8 different tools*
*2. Spending 10+ hours/week on manual reporting*
*3. Can't prove marketing ROI to leadership*

→ Store as `icp_pain_points` (array)

---

**Q2.8 — Buying Triggers**
"What event triggers your ICP to start looking for a solution like yours?"

*Example: "Just raised Series A and need to professionalize their GTM motion" OR "CMO got fired because they couldn't prove marketing ROI"*

→ Store as `icp_buying_triggers`

---

**Confirm Section 2:**
"Here's your ICP:
- Company: [icp_company_size], [icp_industry], [icp_geography]
- Buyer: [icp_primary_persona]
- Economic Buyer: [icp_economic_buyer]
- Champion: [icp_champion]
- Pain Points: [list]
- Buying Triggers: [icp_buying_triggers]

Look good? (yes/edit/skip for now)"

---

## Section 3: Alternatives & Positioning (6 questions)

**Context:** This section uses April Dunford's positioning framework. We're identifying your named alternatives (not just competitors) and how you're different.

---

**Q3.1 — Named Alternatives (Primary)**
"What are the top 3 products buyers compare you to? (Not 'our competitors' — what do BUYERS actually consider?)"

*Example: "Salesforce, HubSpot, Pipedrive"*

→ Store as `alternatives_primary` (array)

---

**Q3.2 — Status Quo**
"What do buyers do TODAY if they don't buy any tool (including yours)? What's the status quo?"

*Example: "Manual spreadsheets + Gmail + Slack to track deals" OR "Keep using their legacy CRM they hate"*

→ Store as `alternatives_status_quo`

---

**Q3.3 — Why They're Leaving Alternatives**
"Why do buyers leave those alternatives and consider you instead?"

*Example: "Salesforce is too expensive and complex for their team size. HubSpot lacks the specific automation they need for their workflow. Pipedrive doesn't integrate with their existing stack."*

→ Store as `alternatives_why_leaving`

---

**Q3.4 — Your Unique Capabilities**
"What can you do that NO alternative can do? (Features, approach, delivery model, etc.)"

*Example: "We're the only platform that combines CRM + customer data platform + revenue intelligence in one tool, specifically built for PLG companies."*

→ Store as `unique_capabilities`

---

**Q3.5 — Category**
"What category do you compete in? (If you're creating a new category, what do you call it?)"

*Example: "Revenue Intelligence Platform" OR "All-in-one CRM for growing SaaS companies" OR "We're creating the 'Unified GTM Platform' category"*

→ Store as `category`

---

**Q3.6 — Market Type (Dunford)**
"Are you in an existing market, a new market, or resegmenting an existing market?"
- [ ] Existing market (competing with established players)
- [ ] New market (creating a new category)
- [ ] Resegmented market (same category, new segment)

→ Store as `market_type`

---

**Confirm Section 3:**
"Here's your Positioning:
- Alternatives: [alternatives_primary]
- Status Quo: [alternatives_status_quo]
- Why They Leave: [alternatives_why_leaving]
- Unique Capabilities: [unique_capabilities]
- Category: [category]
- Market Type: [market_type]

Look good? (yes/edit/skip for now)"

---

## Section 4: Voice & Tone (5 questions)

**Q4.1 — Brand Voice Attributes**
"Pick 3-5 words that describe your brand voice. (Examples: authoritative, playful, technical, empathetic, bold, straightforward)"

*Example: "Authoritative, straightforward, data-driven, human"*

→ Store as `voice_attributes` (array)

---

**Q4.2 — Tone Shifts by Persona**
"Does your tone shift when talking to different personas? If yes, describe the shifts."

*Example:*
*- VP of Marketing → strategic, ROI-focused, executive tone*
*- Marketing Ops → technical, specific, practitioner tone*
*- CEO → high-level, business outcomes, boardroom tone*

→ Store as `tone_shifts`

---

**Q4.3 — Language Preferences**
"Any language preferences? (e.g., 'we say X, not Y')"

*Example: "We say 'revenue team' not 'sales team'. We say 'GTM motion' not 'sales process'."*

→ Store as `language_preferences`

---

**Q4.4 — Forbidden Phrases**
"Any words or phrases you NEVER use? (Jargon, clichés, competitor language)"

*Example: "Never say 'game-changer', 'revolutionary', 'one-stop-shop', or 'synergy'. Avoid 'AI-powered' unless it's genuinely a core differentiator."*

→ Store as `forbidden_phrases`

---

**Q4.5 — Tone Example**
"Paste a paragraph of copy that perfectly captures your voice. (Homepage hero, recent blog post, email, anything)"

*[User pastes example]*

→ Store as `tone_example`

---

**Confirm Section 4:**
"Here's your Voice & Tone:
- Voice: [voice_attributes]
- Tone Shifts: [tone_shifts]
- Language: [language_preferences]
- Forbidden: [forbidden_phrases]

Look good? (yes/edit/skip for now)"

---

## Section 5: Market Context (4 questions)

**Q5.1 — Market Maturity**
"How mature is your market?"
- [ ] Nascent (category doesn't exist yet)
- [ ] Emerging (category exists, few players)
- [ ] Growing (multiple players, buyers aware)
- [ ] Mature (crowded, commoditized)

→ Store as `market_maturity`

---

**Q5.2 — Macro Forces**
"What macro trends or forces make your solution more relevant NOW? (Tech shifts, regulatory changes, buyer behavior changes, etc.)"

*Example: "Remote work explosion → need for async collaboration tools. Privacy regulations → need for compliant data handling. AI adoption → need for AI-native workflows."*

→ Store as `macro_forces`

---

**Q5.3 — Why Now?**
"Complete this: 'Buyers need [your product] NOW because _____'"

*Example: "Buyers need unified GTM platforms NOW because the old model of disconnected sales, marketing, and CS tools is breaking down as teams need to move faster and make decisions with real-time data."*

→ Store as `why_now`

---

**Q5.4 — Market Narrative**
"What's the bigger story you're telling about where the market is going? (2-3 sentences)"

*Example: "The future of GTM is unified, data-driven, and AI-augmented. Companies that stick with legacy point solutions will lose to those with integrated platforms that give every team member real-time intelligence. We're building the operating system for this new era."*

→ Store as `market_narrative`

---

**Confirm Section 5:**
"Here's your Market Context:
- Maturity: [market_maturity]
- Macro Forces: [macro_forces]
- Why Now: [why_now]
- Narrative: [market_narrative]

Look good? (yes/edit/skip for now)"

---

## Section 6: Proof Points Registry (3 questions)

**Q6.1 — Approved Metrics**
"What metrics can your team confidently cite? (With sources if possible)"

*Example:*
*- 89% customer retention rate (from Salesforce, Q4 2025)*
*- $50M ARR (public announcement, Jan 2026)*
*- 2,500+ customers (internal dashboard, updated weekly)*

→ Store as `approved_metrics` (array)

---

**Q6.2 — Customer Quotes & Case Studies**
"Any customer quotes, testimonials, or case study results you can reference?"

*Example:*
*- "HubSpot reduced our sales cycle by 40%" — Sarah Chen, VP Sales at Acme Corp*
*- Case study: Acme Corp increased pipeline by 3x in 6 months*

→ Store as `proof_points_quotes`

---

**Q6.3 — Forbidden Claims**
"Any claims your team is NOT allowed to make? (Unverified, exaggerated, or legally risky)"

*Example: "Don't claim 'industry-leading' without data. Don't cite customer names without written approval. Don't promise specific ROI numbers."*

→ Store as `forbidden_claims`

---

**Confirm Section 6:**
"Here's your Proof Points:
- Metrics: [list]
- Quotes: [list]
- Forbidden: [forbidden_claims]

Look good? (yes/edit/skip for now)"

---

## Step 3: Generate the Brain File

Once all 6 sections are confirmed, generate `/foundation/brain.md` using the brain template structure.

**Template path:** `pmm-foundation/templates/brain-template.md`

**Populate all variables:**
- Replace `{{product_name}}` with actual value
- Replace `{{product_description}}` with actual value
- etc. for all 31 variables

---

## Step 4: Save and Confirm

```bash
# Create foundation directory if it doesn't exist
mkdir -p /foundation

# Write brain file
cat > /foundation/brain.md << 'EOF'
[populated template content]
EOF
```

**Confirmation message:**
"✅ Your brain is set up at `/foundation/brain.md`

All PMM skills will now read from this file. You'll never have to re-enter your ICP, positioning, or voice again.

**Next steps:**
- Run `/positioning` to test it
- Run `/value-prop` to generate value prop statements
- Run `/battlecard` to build a competitive battlecard

Want to view your brain file now? (yes/no)"

**If yes:** Display the full brain.md content

**If no:** "You can always view it by opening `/foundation/brain.md` or running `/setup-brain` again."

---

## Step 5: Post-Setup Guidance

After brain is created, offer:

"Your brain is live. Here's what changed:

**Before v2.0 (painful):**
- Every skill asked for ICP → you re-typed it 10 times
- Positioning wasn't consistent across battlecards and messaging
- Voice & tone were in your head, not in the system

**After v2.0 (brain-powered):**
- Skills auto-load your context
- Messaging is consistent across all outputs
- Your team can use the same brain for alignment

**Free tier vs Paid tier:**
- Free: No brain → manual context every time
- Paid: Brain exists → zero repetition, 10x faster

Want to run your first brain-powered skill? Try `/positioning`"

---

## Edge Cases & Error Handling

### If user quits mid-wizard:
"Wizard paused. Your progress is saved. Run `/setup-brain` again to continue from Section [X]."

### If brain file is corrupted:
"I found a brain file but couldn't parse it. Want to rebuild it? (yes/no)"

### If user wants to edit one section later:
"/setup-brain → [Edit specific sections] → Choose section → Re-run questions for that section only"

### If user has v1.x files and skips migration:
"No problem. Your old files are still in `.agents/` if you need them. But I recommend migrating — it'll save you time."

---

## Success Metrics

After brain setup, track:
- Time to complete wizard (target: <20 min)
- Sections completed vs skipped
- Whether user ran a brain-powered skill afterward
- Whether user came back to edit sections

**Goal:** 80%+ completion rate, 60%+ run a skill immediately after

---

## Related Skills

This skill powers the entire PMM ecosystem:
- `hs-positioning-messaging` — reads brain Sections 1, 2, 3, 4
- `hs-value-prop-statements` — reads brain Sections 1, 2, 3
- `hs-competitive-battlecard` — reads brain Sections 1, 2, 3, 5
- `hs-buyer-personas` — reads brain Section 2
- `hs-gaccs-brief` — reads brain Sections 1, 2, 4, 6
- [All other execution skills] — check for brain first

---

## Technical Notes

**File path convention:**
- Brain file: `/foundation/brain.md`
- Legacy check: `.agents/*.md`, `.claude/*.md`
- Template: `pmm-foundation/templates/brain-template.md`

**Variable naming:**
- Use snake_case for all variables
- Prefix section numbers: `q1_1`, `q2_3`, etc.
- Arrays for multi-item answers: `icp_pain_points[]`

**State management:**
- If wizard is interrupted, save partial state to `/foundation/.brain-draft.md`
- On restart, check for draft and offer to resume

---

## Maintenance

**When to update this skill:**
- New section added to brain template
- New question needed for better context
- User feedback suggests confusing questions
- Brain-powered skills need additional context

**Version history:**
- v2.0.0 (2026-05-20) — Initial brain wizard release
---
skill: brain-audit
version: 2.1.0
author: Stefanos
description: Analyze your PMM brain file and get a health score + actionable improvement recommendations
triggers:
  - audit brain
  - brain health
  - check brain
  - brain quality
  - brain score
  - diagnose brain
last_updated: 2026-05-20
---

# Brain Audit Skill

Analyzes `/foundation/brain.md` and provides a health score (0-100) plus actionable recommendations.

## What This Does

Checks your brain against 50+ quality criteria across 6 sections:
- Is your ICP specific or vague?
- Are alternatives properly defined (Dunford framework)?
- Is your voice example provided?
- Are proof points quantified?
- Are critical fields populated?

**Output:** Health score + recommendations prioritized by impact

---

## Execution Logic

### Step 1: Check for Brain File

```
Does /foundation/brain.md exist?
```

**If NO:**
- "You don't have a brain file yet. Want to create one?"
  - [Yes] → Launch `/setup-brain`
  - [No] → Exit

**If YES:**
- "Found your brain file. Running diagnostics..."
- Proceed to audit

---

### Step 2: Load and Parse Brain

Read `/foundation/brain.md` and extract all fields:

**Section 1: Product Context**
- product_name
- product_description
- product_stage
- target_market
- value_proposition

**Section 2: ICP Definition**
- icp_company_size
- icp_industry
- icp_geography
- icp_primary_persona
- icp_economic_buyer
- icp_champion
- icp_pain_points (array)
- icp_buying_triggers

**Section 3: Alternatives & Positioning**
- alternatives_primary (array)
- alternatives_status_quo
- alternatives_why_leaving
- unique_capabilities
- category
- market_type

**Section 4: Voice & Tone**
- voice_attributes (array)
- tone_shifts
- language_preferences
- forbidden_phrases (array)
- tone_example

**Section 5: Market Context**
- market_maturity
- macro_forces
- why_now
- market_narrative

**Section 6: Proof Points**
- approved_metrics (array)
- proof_points_quotes
- forbidden_claims (array)

---

### Step 3: Score Each Section

## Section 1: Product Context (Score: 0-100)

### product_name (20 points)
- **Exists:** +10
- **Is specific (not "our app", "my product"):** +10

### product_description (20 points)
- **Exists:** +5
- **Is 2+ sentences:** +5
- **Contains problem statement (keywords: "helps", "solves", "fixes"):** +10

### product_stage (20 points)
- **Is defined:** +20

### target_market (20 points)
- **Exists:** +5
- **Is specific (mentions size/industry/role):** +10
- **Is not too broad ("businesses", "companies"):** +5

### value_proposition (20 points)
- **Exists:** +5
- **Follows "[Product] helps [audience] to X so they can Y" structure:** +15

**Section 1 Total: max 100 points**

---

## Section 2: ICP Definition (Score: 0-100)

### icp_company_size (12.5 points)
- **Exists:** +6
- **Is specific (numbers, not "small/medium/large"):** +6.5

### icp_industry (12.5 points)
- **Exists:** +6
- **Is clear (specific industries OR "horizontal"):** +6.5

### icp_geography (12.5 points)
- **Exists:** +6
- **Is specific (regions/countries):** +6.5

### icp_primary_persona (12.5 points)
- **Exists:** +6
- **Includes title + responsibility:** +6.5

### icp_economic_buyer (12.5 points)
- **Exists:** +12.5

### icp_champion (12.5 points)
- **Exists:** +6
- **Describes who + what they care about:** +6.5

### icp_pain_points (12.5 points)
- **Has 1+ pain points:** +4
- **Has 3+ pain points:** +4
- **Pain points are specific (not generic):** +4.5

### icp_buying_triggers (12.5 points)
- **Exists:** +6
- **Describes specific event (not "need a tool"):** +6.5

**Section 2 Total: max 100 points**

---

## Section 3: Alternatives & Positioning (Score: 0-100)

### alternatives_primary (20 points)
- **Has 1+ alternatives:** +7
- **Has 2+ alternatives:** +7
- **Alternatives are product names (not categories):** +6

### alternatives_status_quo (15 points)
- **Exists:** +7
- **Is specific (not "nothing"):** +8

### alternatives_why_leaving (15 points)
- **Exists:** +7
- **Explains reasons for each alternative:** +8

### unique_capabilities (25 points)
- **Exists:** +10
- **Is specific (not "easy to use", "AI-powered"):** +15

### category (15 points)
- **Exists:** +15

### market_type (10 points)
- **Is defined:** +10

**Section 3 Total: max 100 points**

---

## Section 4: Voice & Tone (Score: 0-100)

### voice_attributes (25 points)
- **Has 1+ attributes:** +8
- **Has 3+ attributes:** +8
- **Attributes are specific (not "professional", "friendly"):** +9

### tone_shifts (20 points)
- **Exists:** +10
- **Describes persona-specific shifts:** +10

### language_preferences (15 points)
- **Exists:** +15

### forbidden_phrases (15 points)
- **Exists:** +15

### tone_example (25 points)
- **Exists:** +25

**Section 4 Total: max 100 points**

---

## Section 5: Market Context (Score: 0-100)

### market_maturity (25 points)
- **Is defined:** +25

### macro_forces (25 points)
- **Exists:** +10
- **Lists 1+ external trends:** +15

### why_now (25 points)
- **Exists:** +10
- **Connects to macro forces:** +15

### market_narrative (25 points)
- **Exists:** +10
- **Is 2+ sentences:** +10
- **Describes future state:** +5

**Section 5 Total: max 100 points**

---

## Section 6: Proof Points (Score: 0-100)

### approved_metrics (40 points)
- **Has 1+ metrics:** +15
- **Has 3+ metrics:** +10
- **Metrics are quantified (not "high", "lots"):** +15

### proof_points_quotes (30 points)
- **Has 1+ quotes/case studies:** +30

### forbidden_claims (30 points)
- **Exists:** +30

**Section 6 Total: max 100 points**

---

### Step 4: Calculate Overall Score

**Formula:**
```
Overall Score = (S1 + S2 + S3 + S4 + S5 + S6) / 6
```

**Example:**
```
Section 1 (Product Context): 85/100
Section 2 (ICP): 70/100
Section 3 (Alternatives): 90/100
Section 4 (Voice): 50/100
Section 5 (Market): 60/100
Section 6 (Proof Points): 40/100

Overall: (85+70+90+50+60+40)/6 = 65.8/100
```

---

### Step 5: Generate Recommendations

**Priority levels:**
- **CRITICAL (score <50):** Major gaps that break brain-powered skills
- **IMPORTANT (score 50-79):** Weaknesses that reduce effectiveness
- **MINOR (score 80+):** Polish opportunities

**Recommendation format:**
```
[Section Name] — [Score]/100 — [Priority Level]

**Issue:** [What's wrong]
**Impact:** [How this hurts execution skills]
**Fix:** [Specific action to take]
```

---

## Output Format

```
🧠 Brain Health Report
Generated: [timestamp]
Overall Score: [X]/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SECTION SCORES

✅ Strengths (80+)
- [Section Name]: [Score]/100

⚠️ Needs Improvement (50-79)
- [Section Name]: [Score]/100

❌ Critical Gaps (<50)
- [Section Name]: [Score]/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PRIORITY RECOMMENDATIONS

1. [CRITICAL] [Section] — [Score]/100
   Issue: [What's wrong]
   Impact: [How this hurts]
   Fix: [Action]

2. [IMPORTANT] [Section] — [Score]/100
   Issue: [What's wrong]
   Impact: [How this hurts]
   Fix: [Action]

3. [IMPORTANT] [Section] — [Score]/100
   Issue: [What's wrong]
   Impact: [How this hurts]
   Fix: [Action]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 QUICK WINS

These are easy fixes that will boost your score:
- [Quick action 1]
- [Quick action 2]
- [Quick action 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Want to fix the critical gaps now? (yes/no)
```

---

## Example Output

```
🧠 Brain Health Report
Generated: 2026-05-20 15:30:00
Overall Score: 68/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SECTION SCORES

✅ Strengths (80+)
- Product Context: 85/100
- Alternatives & Positioning: 90/100

⚠️ Needs Improvement (50-79)
- ICP Definition: 70/100
- Market Context: 60/100

❌ Critical Gaps (<50)
- Voice & Tone: 45/100
- Proof Points: 35/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PRIORITY RECOMMENDATIONS

1. [CRITICAL] Voice & Tone — 45/100
   Issue: No tone example provided
   Impact: Writing assistant can't match your voice accurately
   Fix: Run /setup-brain → Edit Section 4 → Add a tone example

2. [CRITICAL] Proof Points — 35/100
   Issue: Metrics are not quantified ("high retention" vs "89% retention")
   Impact: Battlecards and sales materials lack credibility
   Fix: Run /setup-brain → Edit Section 6 → Add specific numbers + sources

3. [IMPORTANT] ICP Definition — 70/100
   Issue: Company size is too broad ("small to medium businesses")
   Impact: Positioning and personas will be too generic
   Fix: Run /setup-brain → Edit Section 2 → Specify "50-500 employees"

4. [IMPORTANT] Market Context — 60/100
   Issue: "Why now" doesn't connect to macro forces
   Impact: Launch messaging won't have urgency
   Fix: Run /setup-brain → Edit Section 5 → Connect to macro trends

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 QUICK WINS

These are easy fixes that will boost your score:
- Add 1 customer quote to Proof Points (+30 points)
- Add a tone example to Voice & Tone (+25 points)
- Specify company size in ICP (+13 points)

Estimated score after quick wins: 68 → 89/100

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Want to fix the critical gaps now? (yes/no)
```

---

## Step 6: Offer to Fix

**If user says "yes":**
```
Which section do you want to fix first?
1. Voice & Tone (45/100) ← Biggest impact
2. Proof Points (35/100)
3. ICP Definition (70/100)
4. Market Context (60/100)
5. Edit brain file manually

[User selects]
```

**If user selects 1-4:**
- Launch `/setup-brain` → Edit specific sections

**If user selects 5:**
- "Your brain file is at /foundation/brain.md — edit it in any text editor, then run /brain-audit again to see your new score."

---

## Related Commands

- `/setup-brain` — Fix sections interactively
- `/positioning` — Test brain-powered skill after improvements
- `/brain-audit` — Re-run audit after fixes

---

## Technical Notes

**Audit logic location:** This skill

**Validation rules:** Read from `validation-rules.md`

**Scoring weights:** Sections are equally weighted (100 points each)

**Recommendation prioritization:**
1. Critical gaps (<50) — breaks functionality
2. Important (50-79) — reduces effectiveness
3. Minor (80+) — polish only

---

## Success Metrics

**Good brain:** 80+ overall score
**Functional brain:** 60-79 overall score
**Needs work:** <60 overall score

**Target:** 90% of users should achieve 70+ score after running wizard once

---

## Maintenance

**When to update scoring:**
- New brain sections added
- Execution skills require additional fields
- User feedback suggests scoring is too harsh/lenient

**When to update recommendations:**
- New quick wins discovered
- Better fix instructions available
- Common user mistakes identified

Add product-marketing-context skill
