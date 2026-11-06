# EMEA Mode

Read at the Region check and again at Steps 2, 3, 6, 8, 9 and 10. EMEA mode is a set of conservative defaults for research that touches people in Europe. It is not a legal determination and not legal advice.

## 1. Why it exists

Company facts are mostly outside data protection law. A named person is not, even when they act in a business capacity: the UK regulator states that UK GDPR applies "even if they are acting in their business capacity", and that sole traders and some partnerships are treated as individuals. So the mode governs person-level reads, contact fields from enrichment, saved records and the outreach channel. It does not change how a company is researched or scored.

## 2. When it is on

`emea_mode: auto` in `_config.md` (default). On for a run when any of these is true:

- your team sells from the EEA, the UK or Switzerland (`home_region` in `_config.md`, or Section 2 `geography`);
- the account's headquarters, or the named contact, is in the EEA, the UK or Switzerland;
- the user set `emea_mode: on`.

`off` switches it off for every run; the brief then says "EMEA mode off by your setting" for an account in scope. Say in the Region check which condition fired.

## 3. What it changes

| Area | EMEA mode on |
|---|---|
| Company research | Unchanged, plus local registries and filings and local-language news (for example UK Companies House, the German Handelsregister, the Dutch KvK) |
| Legal form | Read in Step 3. A sole trader or small partnership is handled as a person: person rules below apply to the whole brief |
| Named-person research | Only on explicit request; business role, tenure and public professional statements from the company's own pages, press or filings |
| Sensitive traits | Never researched or inferred (all modes) |
| Enrichment | Company fields only. Do not request or show email, phone or personal profile fields |
| Sources | Every person-fact carries source and date, so the seller can say where it came from. Under Article 14 of GDPR, a person whose data came from a third party is generally to be told, as secondary sources summarise it, within a reasonable period and at the latest one month, or at first contact. Confirm with counsel |
| CRM | Read opt-out, unsubscribe and legal-basis fields by their live label. An opt-out stops the run. Suppress rather than delete |
| Slack | Role titles only; no person names or contact details |
| Records | `retain_until` in the header (default 180 days); say how to delete the record; no person names in `_patterns.md` (all modes) |
| Channel note | One line in the brief: rules for cold outreach differ by country and by who the recipient is; check before sequencing |

## 4. Channel note, for reference only

The skill never sends and never advises. The note exists so a seller does not start a sequence on a false assumption. As summarised by the UK regulator and a secondary source:

- **UK:** the PECR rule on marketing email does not apply to corporate subscribers; it does apply to sole traders and some partnerships. UK GDPR still applies to a named person's data, with legitimate interests the usual basis, a transparency duty and an absolute right to object.
- **Germany:** commonly read as consent-first for marketing email under UWG section 7(2).
- **France:** legitimate interest can work if the message relates to the person's profession, they were told, and objecting is simple.
- **Elsewhere:** no single EU answer. Confirm each market.

## 4a. Usage rows

`_usage.md` records a seller handle per run so the PMM can see adoption. Whether that is allowed is the employer's call (privacy review, works council). Set `usage_identity: team` to log a team label instead. The handle stays in `_usage.md`; it never appears in a brief, `_patterns.md` or a proposal.

## 5. What it does not change

Fit and timing scoring, signal windows, hit and miss counts, the learning loop and every hand-off. Those carry no personal data by design.

## 6. Limits to state when asked

- It reduces risk; it does not make a team compliant. The sender, the legal basis and the channel are the user's decisions.
- The UK regulator's business-to-business marketing guidance is under review because of the Data (Use and Access) Act. Re-check before relying on section 4.
- Sections 3 and 4 beyond the UK rest on secondary summaries. Have someone qualified review this file before it is described to a customer as compliant.
- Do not call the skill "GDPR compliant". Say "EMEA-aware defaults".

## Sources

- ICO, Business-to-business marketing: ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
- Rework, Cold outreach laws explained (secondary; cites EUR-Lex, UWG section 7, CNIL, ICO)
