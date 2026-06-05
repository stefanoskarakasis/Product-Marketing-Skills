---
name: hs-privacy-policy
version: 2.0.0
description: Draft a jurisdiction-aware privacy policy for any digital product — use this skill whenever a PMM or Product Manager needs to create, update, audit, or review data protection documentation, asks about GDPR, CCPA, or UK GDPR obligations, mentions "privacy policy", "cookie policy", "data retention", "right to be forgotten", "data processing agreement", or asks what their product needs to comply with applicable privacy law.

metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: false
last_updated: 2026-06-05
---

# hs-privacy-policy

A drafting engine for PMMs and Product Managers who need a rigorous, jurisdiction-aware
privacy policy ready for legal review — not a generic template.

**The contract of this skill:** this skill drafts. It does not certify.
Every output is a structured first draft requiring qualified legal review before publication.
High-risk clauses are marked `[⚠️ LEGAL REVIEW REQUIRED]` throughout — always.

---

## ⓪ On Load — Read Before Anything Else

**1. Load apex context**

Check `.agents/product-marketing-context.md`. If found, extract silently:
- Product name and description
- Company name and registered address
- Primary market / geographic focus → infer likely jurisdiction(s)
- Data types mentioned in the product description
- ICP → infer B2C vs B2B exposure

**2. Load skill knowledge**

Check `knowledge/INDEX.md`. If it exists:
- Load applicable `knowledge/jurisdiction/` files
- Load applicable `knowledge/clauses/` files
- Apply confirmed 🟢 rules by default
- Note any 🟡 hypotheses testable with today's session

**3. Challenge the user — never auto-populate silently**

Even with full context loaded, surface what was inferred and require explicit confirmation.
Legal documents cannot be built on silent assumptions. Present the intake block in Section ①.

---

## ① Intake

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

## ② Jurisdiction Detection

Derive applicable laws from confirmed inputs — never assume.

| User location | Primary law | Load |
|---|---|---|
| EU / EEA | GDPR | `knowledge/jurisdiction/gdpr.md` |
| UK | UK GDPR + PECR | `knowledge/jurisdiction/uk-gdpr.md` |
| California | CCPA / CPRA | `knowledge/jurisdiction/ccpa.md` |
| US (other states) | VCDPA, CPA, TDPSA, CTDPA patchwork | `knowledge/jurisdiction/us-states.md` |
| Canada | PIPEDA / Law 25 (QC) | `knowledge/jurisdiction/canada.md` |
| Australia | Privacy Act + APPs | `knowledge/jurisdiction/australia.md` |
| Global / Multi | All above — GDPR as floor, layer others | All files |

**Industry overlays** — apply silently when relevant:

| Product type | Additional obligations |
|---|---|
| FinTech / Payments | PSD2 data obligations, PCI-DSS, FCA breach notification (UK) |
| Health data | HIPAA (US), GDPR Article 9 special category, NHS DSPT (UK) |
| Children | COPPA (US), GDPR Article 8 age of consent (13–16 by member state), UK Children's Code |
| HR / employee data | Additional GDPR lawful basis requirements |
| B2B only | Reduced consumer-rights exposure; processor obligations remain |

If a jurisdiction file does not yet exist: draft from model knowledge, tag all claims `[M]`,
add to hypothesis queue for live verification.

---

## ③ Operating Modes

| Mode | Trigger | Output |
|---|---|---|
| **DRAFT** | New policy from scratch | Full three-part output |
| **REFRESH** | Existing policy provided | Diff: legal changes + redlined clauses |
| **AUDIT** | "Review our policy" / "are we compliant" | Gap analysis + prioritised fix list |
| **CLAUSE** | "Write the cookie section" / "draft our retention policy" | Single section with alternatives |
| **LEARN** | "Our lawyer flagged X" / "legal said we need Y" | Legal feedback → knowledge base |

Default: **DRAFT**.

---

## ④ Drafting Protocol

Follow this sequence — it prevents confident-sounding errors.

1. Confirm all inputs are verified, not inferred
2. Load jurisdiction rules — apply 🟢 rules silently
3. Load clause patterns — apply 🟢 patterns silently
4. Identify special categories and industry overlays
5. List every named third-party processor before drafting Section 4
6. Load `references/policy-sections.md` — draft all twelve sections in order
7. Run self-audit (Section ⑦) — all four layers must pass before output
8. Deliver three-part output (Section ⑤)
9. Run self-improvement loop (Section ⑧)

**The specificity rule** — apply to every clause:

❌ `"We use your data to improve our services."`
✅ `"We analyse session recordings and feature usage logs to identify friction in onboarding
     flows and prioritise product improvements. This is based on our legitimate interest in
     improving the product experience. [⚠️ LEGAL REVIEW REQUIRED]"`

If a clause could appear in any product's privacy policy unchanged, rewrite it.

---

## ⑤ Output Format

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
KNOWLEDGE APPLIED:   [rules and clause patterns loaded this session]
```

**Part 2 — Full Policy Document**

Complete, ready-to-send-to-legal policy using the section architecture in
`references/policy-sections.md`. Write in plain English. No legalese. Define
technical terms on first use. Every `[⚠️ LEGAL REVIEW REQUIRED]` marker visible inline.

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

## ⑥ Hard Rules

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

**Never present memory-generated compliance requirements as confirmed law.**
Tag any claim not drawn from a loaded knowledge file as `[M]`. Add to hypothesis queue.
Do not omit — flag it.

---

## ⑦ Self-Audit

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

## ⑧ Self-Improvement Loop

Run at end of every session, after output delivered and audit passed.

**Why this matters**

A clause that reads well can still get flagged by a data protection authority.
The skill cannot infer legal quality from silence — learning only fires when the
user explicitly reports legal outcomes. This is what separates a compounding system
from a static template.

**Prompt the user before closing:**
> "Before I close — did your lawyer flag anything in a previous policy review,
> or do you have feedback from a legal or compliance review?
> Even a quick note helps the skill improve for next time."

**LEARN mode triggers:**

| User input | Action |
|---|---|
| "Our lawyer flagged [clause]" | Store as clause risk → 🟡 hypothesis |
| "Legal said [X] needed to be added / removed / reworded" | Store as jurisdiction rule → 🟡 hypothesis |
| "This draft got approved unchanged" | Promote clause pattern → 🟢 rule (after 2nd confirmation) |
| "We were fined / audited about [X]" | Immediate 🔴 rule — highest priority |

**Promotion / demotion logic:**

| Status | Promoted when | Demoted when |
|---|---|---|
| 🟡 Hypothesis | Added after first legal feedback signal | — |
| 🟢 Rule | Confirmed across 2+ sessions or jurisdictions | Contradicted by new legal data |
| 🔴 Rule | Triggered by fine, audit, or formal complaint | — |
| Stale hypothesis | — | Untested for 180 days → flag for pruning |

**Decision log** — record any structural decisions about output format, clause defaults,
or jurisdiction handling:

```
decisions/YYYY-MM-DD-{topic}.md

## Decision:     {what was decided}
## Context:      {why this came up}
## Alternatives: {what else was considered}
## Reasoning:    {why this option won}
## Trade-offs:   {what was given up}
## Supersedes:   {prior decision if replacing one}
```

**Session log** — append to `sessions/log.md` every session:

```
DATE:                [YYYY-MM-DD]
PRODUCT:             [name or "undisclosed"]
JURISDICTIONS:       [list]
MODE:                [DRAFT / REFRESH / AUDIT / CLAUSE / LEARN]
SPECIAL CATEGORIES:  [list or none]
THIRD PARTIES:       [count]
LEGAL FEEDBACK:      [Yes — summary / No]
KNOWLEDGE UPDATES:   [files written or updated]
RULES PROMOTED:      [list or none]
RULES DEMOTED:       [list or none]
```

**Deployment note:**
Claude Code → knowledge files update automatically each session.
Claude.ai → output a copyable block at session end:
`📋 SAVE THIS — Knowledge updates, new rules, and session log for manual save`

---

## ⑨ Knowledge Structure

```
knowledge/
  INDEX.md                        ← router — update every session
  jurisdiction/
    gdpr.md                       ← GDPR clause rules + hypothesis queue
    uk-gdpr.md                    ← UK GDPR post-Brexit divergence
    ccpa.md                       ← CCPA / CPRA specifics
    us-states.md                  ← state patchwork (VA, CO, TX, CT…)
    canada.md
    australia.md
  clauses/
    retention.md                  ← retention patterns by industry + jurisdiction
    consent.md                    ← consent language — flagged vs approved
    legitimate-interests.md       ← LI balancing test patterns (legally confirmed)
    cookies.md                    ← cookie clause patterns + CMP recommendations
    international-transfers.md    ← SCC / UK IDTA / adequacy patterns
    special-categories.md         ← health, biometric, children, financial patterns
    security.md                   ← security clause language confirmed by legal

decisions/                        ← structural decisions about this skill's behaviour
sessions/log.md                   ← session history + legal feedback received
craft/examples.md                 ← anonymised examples of approved clause language

references/
  policy-sections.md              ← twelve-section drafting architecture
                                     (load during DRAFT and REFRESH modes)
```

---

## ⑩ Ecosystem Integration

| Upstream | This skill | Downstream |
|---|---|---|
| `hs-product-marketing-context` → product, market, ICP | `hs-privacy-policy` | Legal review → published policy |
| User confirms data types and jurisdiction | | `hs-gaccs-brief` if policy change triggers comms |
| Legal feedback → LEARN mode | | `knowledge/` compounds across sessions |

If product context changes — new market, new data type, new feature:
→ Re-run in **REFRESH** mode. Log the trigger in `sessions/log.md`.
