---
name: privacy-policy
version: 3.0.0
description: Draft a jurisdiction-aware privacy policy for any digital product — use this skill whenever a PMM or Product Manager needs to create, update, audit, or review data protection documentation, asks about GDPR, CCPA, or UK GDPR obligations, mentions "privacy policy", "cookie policy", "data retention", "right to be forgotten", "data processing agreement", or asks what their product needs to comply with applicable privacy law.
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: false
last_updated: 2026-08-24
---

# privacy-policy

A drafting engine for PMMs and Product Managers who need a rigorous, jurisdiction-aware
privacy policy ready for legal review — not a generic template.

**The contract of this skill:** this skill drafts. It does not certify.
Every output is a structured first draft requiring qualified legal review before publication.
High-risk clauses are marked `[⚠️ LEGAL REVIEW REQUIRED]` throughout — always.

---

## Trigger

- **When:** Creating, updating, auditing, or reviewing a privacy policy or other data protection documentation, or answering what a product needs to comply with applicable privacy law.
- **Not for:** n.v.t. — this skill has no overlap with another skill in this stack; overlap was considered and there is none.
- **Example prompts:**
  - "Draft a privacy policy"
  - "Are we GDPR compliant?"
  - "Update our cookie policy"
  - "Review our data retention policy"
  - "What does our product need for CCPA compliance?"

---

## Inputs

- **Args:** Product name, company legal name and address, privacy contact, user location(s), data types collected, third-party tools in use, and optionally an existing policy to refresh. Free format — Step 1 (Intake) fills gaps conversationally.
- **Defaults:** If the user skips intake, default to broadest jurisdiction coverage and flag all inferred inputs.
- **Context keys:**
  - `/foundation/brain.md` — optional. Product name/description, company name/address, primary market, data types, and ICP can all be inferred from it.
  - **Brain contract:** Reads brain content opportunistically (no fixed section numbers — this skill infers from whatever's present). Writes: none.

---

## Pre-flight

Read `/foundation/brain.md` if available. Extract silently:
- Product name and description
- Company name and registered address
- Primary market / geographic focus → infer likely jurisdiction(s)
- Data types mentioned in the product description
- ICP → infer B2C vs B2B exposure

If missing, proceed without it and collect everything through Intake instead.

Even with brain context loaded, surface what was inferred and require explicit
confirmation in Step 1. Legal documents cannot be built on silent assumptions.

---

## Steps

### Step 1: Intake

Present as a single message — not a question drip.

> "I've loaded your product context. Before I draft, verify or correct these — legal
> documents can't rely on inferences.
>
> **Which product is this policy for?** [Pre-fill or blank]
> **Company legal name and registered address:** [Pre-fill or blank]
> **Privacy contact email** (e.g. privacy@company.com):
>
> **Who are your users?** Consumers (B2C), businesses (B2B), or both?
> [Pre-fill from ICP if found — flagged as inferred]
>
> **Where are your users located?** (determines which laws apply)
> EU/EEA → GDPR · UK → UK GDPR + PECR · California → CCPA/CPRA · Multiple → all applicable
> [Pre-fill from market context — flagged as inferred, not confirmed]
>
> **What data does your product collect?** Check all that apply:
> Names and emails · Passwords / credentials · Usage behaviour and analytics ·
> Device identifiers and IP addresses · Location data · Payment information ·
> Health or biometric data `[⚠️ special category]` · Children's data `[⚠️ COPPA/GDPR-K]`
> Anything else?
> [Pre-fill from product description where inferrable — flagged as inferred]
>
> **Third-party tools in use?** Analytics, payments, CRM, email, ads, SSO — list them.
> These determine your processor obligations.
>
> **Existing policy?** Paste it or describe what changed — I'll diff rather than start over."

If the user provides an existing policy → **REFRESH mode**.
If the user provides a brain dump → **DRAFT mode** from their inputs.
If the user skips intake → default to broadest jurisdiction coverage; flag all inferred inputs.

---

### Step 2: Jurisdiction Baseline

Derive applicable laws from confirmed inputs — never assume. Apply the relevant
baseline below. These are the core obligations to draft from; treat every specific
period, threshold, or right listed as a candidate to confirm or correct with the
user, not a fact to state unflagged in the final policy.

| User location | Primary law | Core obligations to reflect |
|---|---|---|
| EU / EEA | GDPR | Lawful basis for each processing activity; data subject rights (access, rectification, erasure, portability, restriction, objection); DPO required above certain processing thresholds (Art. 37); breach notification to the supervisory authority within 72 hours; cross-border transfer mechanism (SCCs or adequacy) for any non-EEA processor. |
| UK | UK GDPR + PECR | Same core rights as GDPR, enforced by the ICO; PECR governs cookies and direct electronic marketing consent separately from the general lawful-basis regime; UK IDTA or the UK Addendum to SCCs for cross-border transfers. |
| California | CCPA / CPRA | Right to know, delete, correct, and opt out of sale/sharing of personal information; "Do Not Sell or Share My Personal Information" link required if applicable; look-back disclosure of categories collected in the past 12 months; opt-out for sensitive personal information processing. |
| US (other states) | VCDPA, CPA, TDPSA, CTDPA, and similar | Broadly CCPA-adjacent: access, deletion, correction, opt-out of targeted advertising/sale, and (in several states) opt-out of profiling with legal effect. Thresholds and exact rights vary by state — flag as `[⚠️ LEGAL REVIEW REQUIRED]` rather than asserting exact scope. |
| Canada | PIPEDA / Law 25 (QC) | Consent-based collection, meaningful purpose limitation, breach reporting to the Privacy Commissioner where real risk of significant harm exists; Law 25 adds Quebec-specific consent and cross-border transfer assessment requirements. |
| Australia | Privacy Act + APPs | 13 Australian Privacy Principles covering collection, use, disclosure, access, and correction; notifiable data breach scheme for eligible breaches. |
| Global / Multi | All above | Use GDPR as the floor (it is the strictest baseline) and layer jurisdiction-specific rights (e.g. CCPA's "sale/share" opt-out) as additional sections rather than separate policies where feasible. |

**Industry overlays** — apply silently when relevant:

| Product type | Additional obligations |
|---|---|
| FinTech / Payments | PSD2 data obligations, PCI-DSS, FCA breach notification (UK) |
| Health data | HIPAA (US), GDPR Article 9 special category, NHS DSPT (UK) |
| Children | COPPA (US), GDPR Article 8 age of consent (13–16 by member state), UK Children's Code |
| HR / employee data | Additional GDPR lawful basis requirements |
| B2B only | Reduced consumer-rights exposure; processor obligations remain |

Every obligation in these tables is a drafting starting point, not confirmed law for
the user's specific situation — tag any clause built from this baseline `[M]` (model
knowledge, not a loaded authoritative source) and mark it `[⚠️ LEGAL REVIEW REQUIRED]`.

---

### Step 3: Select Operating Mode

| Mode | Trigger | Output |
|---|---|---|
| **DRAFT** | New policy from scratch | Full three-part output |
| **REFRESH** | Existing policy provided | Diff: legal changes + redlined clauses |
| **AUDIT** | "Review our policy" / "are we compliant" | Gap analysis + prioritised fix list |
| **CLAUSE** | "Write the cookie section" / "draft our retention policy" | Single section with alternatives |
| **LEARN** | "Our lawyer flagged X" / "legal said we need Y" | Legal feedback surfaced back to the user for their own records |

Default: **DRAFT**.

---

### Step 4: Draft the Twelve-Section Policy Architecture

Draft every DRAFT and REFRESH policy in this order. This is the baseline structure —
adapt section depth to what Step 1 and Step 2 actually surfaced, and drop a section
only if it is genuinely inapplicable (state why, briefly, rather than deleting silently).

1. **Overview and scope** — who this policy covers, what product/service it applies to.
2. **Data we collect** — every data type from Intake, organized by collection method
   (provided directly, collected automatically, received from third parties).
3. **How we use your data** — purpose for each data type, tied to a lawful basis
   (GDPR) or business purpose (CCPA).
4. **Legal basis for processing** (GDPR/UK GDPR jurisdictions only) — consent,
   contract, legitimate interest, legal obligation, vital interest, or public task,
   named per processing activity.
5. **Cookies and tracking technologies** — categories used (strictly necessary,
   functional, analytics, advertising), consent mechanism, link to cookie settings.
6. **Third-party sharing and processors** — every named third party from Intake,
   what data they receive, and why. Never describe processors generically.
7. **International data transfers** — named transfer mechanism (SCCs, UK IDTA,
   adequacy decision) for every processor outside the user's primary jurisdiction.
8. **Data retention** — a stated period or deletion trigger per data type. Every
   period gets `[⚠️ LEGAL REVIEW REQUIRED]` — no exceptions.
9. **Your rights** — the specific rights from the Step 2 baseline for the user's
   confirmed jurisdiction(s), plus how to exercise each one.
10. **Security measures** — a general, honest description of safeguards in place.
    Never overstate; never make an unverifiable claim (e.g. "military-grade").
11. **Children's data** — state whether the product is directed at children; if
    special-category handling applies, flag it explicitly.
12. **Changes to this policy and contact information** — how updates are
    communicated, plus the confirmed privacy contact from Intake.

---

### Step 5: Follow the Drafting Protocol

Follow this sequence — it prevents confident-sounding errors.

1. Confirm all inputs are verified, not inferred.
2. Apply the Step 2 jurisdiction baseline for every confirmed location.
3. Identify special categories and industry overlays.
4. List every named third-party processor before drafting Section 6 of the policy.
5. Draft all twelve sections from Step 4, in order.
6. Run self-audit (Step 8) — all four layers must pass before output.
7. Deliver three-part output (Step 6).
8. Run the legal feedback check (Step 9).

**The specificity rule** — apply to every clause:

❌ `"We use your data to improve our services."`
✅ `"We analyse session recordings and feature usage logs to identify friction in onboarding
     flows and prioritise product improvements. This is based on our legitimate interest in
     improving the product experience. [⚠️ LEGAL REVIEW REQUIRED]"`

If a clause could appear in any product's privacy policy unchanged, rewrite it.

---

### Step 6: Deliver Output Format

Deliver in three parts every session, every mode.

**Part 1 — Intake Confirmation**
```
PRODUCT:             [name — confirmed]
COMPANY:             [legal name — confirmed]
JURISDICTIONS:       [list — confirmed vs ⚠️ inferred]
DATA TYPES:          [confirmed list]
THIRD PARTIES:       [named list]
SPECIAL CATEGORIES:  [Yes — type / No]
INFERRED INPUTS:     [anything not explicitly confirmed — flagged]
MODE:                [DRAFT / REFRESH / AUDIT / CLAUSE / LEARN]
```

**Part 2 — Full Policy Document**

Complete, ready-to-send-to-legal policy using the twelve-section architecture in
Step 4. Write in plain English. No legalese. Define technical terms on first use.
Every `[⚠️ LEGAL REVIEW REQUIRED]` marker visible inline.

**Part 3 — Compliance Notes and Next Steps**
- Summary of every `[⚠️ LEGAL REVIEW REQUIRED]` clause and why it needs legal attention
- Jurisdiction-specific obligations that require action, not just documentation
- Third-party DPA checklist
- Technical tasks: consent management, deletion flows, breach notification procedure
- Pre-publish checklist:
  - [ ] Qualified data privacy attorney has reviewed the policy
  - [ ] Policy matches actual data collection and processing in the product
  - [ ] Consent management platform configured for cookie consent
  - [ ] Data subject rights request process is operational
  - [ ] DPA signed with every named third-party processor
  - [ ] Legal basis documented internally for every processing activity
  - [ ] DPO appointed if required (GDPR Article 37)
  - [ ] Breach notification procedure documented and tested
  - [ ] Retention deletion workflows are technically implemented

---

### Step 7: Apply Hard Rules

**Never present output as a finished legal document.**
The disclaimer is mandatory. Remove or soften it at user request: not permitted.

**Never draft without confirmed product identity.**
The user must name the specific product before any clause is written.

**Never auto-populate jurisdiction silently.**
Pre-fill and flag. A policy written for the wrong jurisdiction is worse than no policy.

**Never state a retention period without flagging it for legal review.**
Retention periods are a primary enforcement target. Every stated period gets
`[⚠️ LEGAL REVIEW REQUIRED]` — no exceptions.

**Never describe third-party processors generically.**
Name them, or state "processors are listed at [URL]" with a maintained live list.

**Never present the Step 2 baseline as confirmed law for the user's situation.**
It is model knowledge (`[M]`), not a verified legal source. Flag every clause drawn
from it.

---

### Step 8: Run Self-Audit

Run internally before producing any output. All four layers must pass.

**Layer 1 — Input integrity**
Any inputs still inferred rather than confirmed? Disclosed in Part 1?

**Layer 2 — Jurisdiction coverage**
All applicable laws covered? Cross-border transfers addressed for every named processor?
Every relevant user right included per confirmed jurisdiction?

**Layer 3 — Specificity**
Every clause product-specific? Retention periods concrete? All processors named?

**Layer 4 — Legal flag completeness**
Every high-risk clause marked `[⚠️ LEGAL REVIEW REQUIRED]`?
All special category clauses flagged?

Only after all four layers pass: produce output.

---

### Step 9: Legal Feedback Check

Run at end of every session, after output delivered and audit passed. This is
a bespoke feedback loop for this skill only — distinct from the repo's
standard Learning Close (Section 5.1 of `SKILL-SPEC.md`), which does not
apply here since this is a T3 skill with `quality_gate: false`. This step
never writes to `/context/skill-sessions.md` or any other file on its own.

**Why this matters**

A clause that reads well can still get flagged by a data protection authority.
The skill cannot infer legal quality from silence — learning only fires when the
user explicitly reports legal outcomes.

**Prompt the user before closing:**
> "Before I close — did your lawyer flag anything in a previous policy review,
> or do you have feedback from a legal or compliance review?
> Even a quick note helps me apply the right pattern next time."

**If the user reports feedback**, treat it as a signal for this session and any
future one you draft for them — but do not write it to any file on your own. If they
want it saved, ask where (their own notes, or a brain-adjacent doc they maintain)
and let them confirm the destination.

| User input | How to use it this session |
|---|---|
| "Our lawyer flagged [clause]" | Treat as a known risk area — apply extra scrutiny to that clause type for the rest of this draft and any future one. |
| "Legal said [X] needed to be added / removed / reworded" | Apply the correction now; note it back to the user as a pattern worth remembering. |
| "This draft got approved unchanged" | Good signal — keep using the same structure for that clause type. |
| "We were fined / audited about [X]" | Highest priority — treat that clause area as `[⚠️ LEGAL REVIEW REQUIRED]` even where it wouldn't otherwise be flagged, for the rest of this engagement. |

---

### Step 10: Ecosystem Integration

| Upstream | This skill | Downstream |
|---|---|---|
| `product-marketing-context` → product, market, ICP | `privacy-policy` | Legal review → published policy |
| User confirms data types and jurisdiction | | `gaccs-brief` if policy change triggers comms |

If product context changes — new market, new data type, new feature:
→ Re-run in **REFRESH** mode.

---

## Outputs

- **Files written:** None — this skill does not write to `/context/skill-sessions.md`
  or any other file on its own. If the user wants a policy or its notes saved
  anywhere, ask where.
- **Chat output format:** Three-part output every session — Intake
  Confirmation, Full Policy Document, and Compliance Notes and Next Steps
  (Step 6).
- **External side effects:** None.

---

## Verification

- All inputs confirmed or explicitly flagged as inferred (Part 1 of output).
- Jurisdiction baseline applied for every confirmed location, with `[M]` and `[⚠️ LEGAL REVIEW REQUIRED]` tags on every clause drawn from it.
- Self-Audit (Step 8) passed on all four layers before output was produced.
- Every retention period and high-risk clause carries `[⚠️ LEGAL REVIEW REQUIRED]`.
- Disclaimer present and not softened or removed at user request.

---

## Do Not Use For

- n.v.t. — this skill has no overlap with another skill in this stack; overlap was considered and there is none.
