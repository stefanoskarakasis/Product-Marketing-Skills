# Brain Template
## For `product-marketing-context/templates/brain-template.md`

Use this template file in your repo. The `product-marketing-context` skill will populate all `{{variable}}` placeholders when a user completes the wizard.

---

```markdown
# PMM Brain — {{product_name}}

**Generated:** {{generated_date}}
**Version:** 3.4.0
**Owner:** {{brain_owner}}

---

## Section 1: Product Context

**Product Name:** 
{{product_name}}

**Product Description:**
{{product_description}}

**Stage:** 
{{product_stage}}

**Target Market:**
{{target_market}}

**Value Proposition:**
{{value_proposition}}

**Offerings (what we sell, packaged):**
{{offerings}}

**Approved Terminology (we say X, not Y):**
{{glossary}}

**Permitted Claims (may be made without further approval):**
{{permitted_claims}}

**Business Model (how you charge, what the price scales with, self-serve or sales-led):**
{{business_model}}

---

## Section 2: ICP Definition

**Company Size:**
{{icp_company_size}}

**Industry/Vertical:**
{{icp_industry}}

**Geography:**
{{icp_geography}}

**Primary Persona:**
{{icp_primary_persona}}

**Economic Buyer:**
{{icp_economic_buyer}}

**Champion Profile:**
{{icp_champion}}

**Top 3 Pain Points:**
1. {{icp_pain_points_1}}
2. {{icp_pain_points_2}}
3. {{icp_pain_points_3}}

**Buying Triggers:**
{{icp_buying_triggers}}

**Jobs to Be Done (When __, I want to __, so I can __):**
{{jobs_to_be_done}}

**Cost of the Problem (time, money or risk, with a number and its source):**
{{cost_of_problem}}

**Anti-Persona (who is NOT a fit, and why):**
{{anti_persona}}

**Buying Committee (standing roles, what each cares about, what makes each block):**
{{committee_roles}}

---

## Section 3: Alternatives & Positioning

**Named Alternatives (Top 3):**
1. {{alternatives_primary_1}}
2. {{alternatives_primary_2}}
3. {{alternatives_primary_3}}

**Status Quo (If they don't buy anything):**
{{alternatives_status_quo}}

**Why They Leave Alternatives:**
{{alternatives_why_leaving}}

**Unique Capabilities:**
{{unique_capabilities}}

**Category:**
{{category}}

**Market Type:**
{{market_type}}

**Where Each Alternative Falls Short (for this ICP):**
{{alt_shortfalls}}

**Switching Forces (push, pull, habit, anxiety):**
{{switching_forces}}

**Objections (who raises it, approved response):**
{{objections}}

---

## Section 4: Voice & Tone

**Brand Voice Attributes:**
{{voice_attributes}}

**Tone Shifts by Persona:**
{{tone_shifts}}

**Language Preferences:**
{{language_preferences}}

**Forbidden Phrases:**
{{forbidden_phrases}}

**Tone Example (Copy that captures our voice):**
> {{tone_example}}

**Customer Language (exact words, each with who said it and where):**
{{customer_phrases}}

---

## Section 5: Market Context

**Market Maturity:**
{{market_maturity}}

**Macro Forces Making Our Solution Relevant:**
{{macro_forces}}

**Why Now:**
{{why_now}}

**Market Narrative (The bigger story):**
{{market_narrative}}

---

## Section 6: Proof Points Registry

**Approved Metrics (With sources):**
{{approved_metrics}}

**Customer Quotes & Case Study Results:**
{{proof_points_quotes}}

**Forbidden Claims (Never say this):**
{{forbidden_claims}}

---

## Section 7: Strategy

**Top Priorities This Quarter (max 3):**
{{priorities}}

**Launches (name, date, tier T1-T4):**
{{launches}}

**Quarterly Goals (metric, baseline, target, date):**
{{quarter_goals}}

**Active Bets:**
{{active_bets}}

**Explicitly Not Doing:**
{{not_doing}}

**Conversion Action (the one thing the funnel drives):**
{{conversion_action}}

---

## Section 8: Execution

**Stakeholders (role, what they care about, stance):**
{{stakeholders}}

**Approvals (what needs sign-off, from whom, how long it takes):**
{{approvals}}

**Prohibited (topics, claims or competitor mentions legal or leadership ruled out):**
{{prohibited}}

**Channels (where you publish and who owns each):**
{{channels}}

**Cadence (recurring reviews, launches, reporting):**
{{cadence}}

---

## Quick Reference

**Your Brain in One Sentence:**
[User: complete after all sections filled]

**ICP Quick ID:**
- **Company:** {{icp_company_size}} {{icp_industry}} {{icp_geography}}
- **Primary Persona:** {{icp_primary_persona}}
- **Pain Points:** [top 1]
- **Buying Trigger:** [top trigger]

**Positioning Quick ID:**
- **Category:** {{category}}
- **Unique Capability:** [top 1]
- **vs. Status Quo:** [quick contrast]
- **vs. Top Alternative:** [quick contrast]

**Voice Quick ID:**
- **Attributes:** {{voice_attributes}}
- **Tone:** {{tone_shifts}} (describe primary persona)
- **Forbidden:** {{forbidden_phrases}} (top 3)

---

## How Other Skills Use This Brain

Which skill reads or writes which section, and how long each section stays fresh: see `references/brain-schema.md`.

---

## Maintenance

**Last Updated:** {{last_updated}}

Each section has its own freshness limit (see `references/brain-schema.md`). Fields may carry a source tag: `[src: <where> | <date> | <stated/pulled/inferred> | <draft/confirmed/stale>]`. An untagged field is read as stated by you and confirmed on the last-updated date.

**Update this brain when:**
- Your ICP changes (new target segment)
- Market dynamics shift (new macro forces, new category)
- Positioning is challenged (new competitor, loss patterns)
- Voice changes (brand refresh, new CEO, new tone)
- A quarter turns over (Section 7)
- A new call, interview or win/loss review changes what customers say or object to (Sections 2, 3, 4)
- An approval path, owner or channel changes (Section 8)

**How to update:**
1. Run `product-marketing-context` skill
2. Choose [Edit a section]
3. Select the section that changed
4. Re-answer those questions
5. Confirm the before/after; the file is updated

You may also edit this file by hand. Run the health audit afterwards so tags and dates stay accurate.

**Do NOT:**
- Delete old sections (keep history)
- Present an unconfirmed value as confirmed

Sections 1 to 6 make a complete brain. The ten deal-reality fields (see `references/brain-schema.md`) are recommended too: a brain without them stays complete, and the audit reports how many are captured. Sections 7 (Strategy) and 8 (Execution) are recommended: an existing brain without them stays complete, and the audit reports each as "not built" rather than as a gap.

---

Generated by: `product-marketing-context`
```

---

## Notes on Variables

**Template variable naming convention:**

```
{{product_name}}              ← Simple field
{{icp_pain_points_1}}         ← Array item 1
{{alternatives_primary_1}}    ← Array item 1
{{voice_attributes}}          ← String list (comma-separated)
{{generated_date}}            ← Current date (auto-filled)
{{brain_owner}}               ← User's name or email
{{last_updated}}              ← Date of last edit
```

When populating the template in the skill:
1. Replace all `{{variable}}` with actual values from wizard answers
2. Remove blank `{{variable}}` lines (don't leave empty lines)
3. If a user skipped a section, note it: "*(Skipped during setup)*"
4. Always include the `{{brain_owner}}` and `{{generated_date}}`

---

## Example: Populated Brain (Reference)

A complete, filled-in brain for a fictional company lives at [`examples/example-brain.md`](../../examples/example-brain.md). It shows the level of detail each field needs: a specific ICP (not "small/medium/large"), named alternatives, a tone example written as a paragraph, and proof points with a source and an approval status.

Every name, number and quote in that file is invented. Use it to see the shape, not to copy claims.
