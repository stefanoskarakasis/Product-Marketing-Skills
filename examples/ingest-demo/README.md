# Ingest demo: build a brain from your material

> **FICTIONAL.** Ledgerlane, Harbor & Pine Freight, Northgate Supply, every name, number, quote, email address and phone number in this folder is invented. Do not cite any of it.

This folder shows what the `product-marketing-context` skill does when you point it at your own material (Step 8, "Add material"). It has five fictional source documents, the evidence the skill should extract from them, and the Brain Diff it should propose.

## Try it

1. Start a new chat or session with the `product-marketing-context` skill installed, in an empty working folder.
2. Say: "Build my brain from my website and these docs."
3. When it asks for your website and pricing page, paste the text of `sources/01-website-home.md` and `sources/02-pricing-page.md` instead of URLs (Ledgerlane has no real website).
4. When it asks what else you have, paste `sources/03-call-controller-2026-09-12.md`, `sources/04-call-cfo-2026-09-18.md` and `sources/05-planning-note-2026-09-30.md`.
5. Compare what it does with `expected-evidence.md` and `expected-brain-diff.md`.

## What a good run looks like

- **Website claims are not proof.** "Up to 90% fewer invoice errors" lands in Section 6 as a draft marked `[NEEDS PROOF]`, never as an approved metric.
- **Disagreements are shown, not settled.** The two calls disagree about when a CFO signs off ($60,000 versus $25,000). The website, a customer call and an internal note give three different go-live times. The skill shows every version with its source and asks.
- **One source is flagged.** The "never say seamless" rule appears only in the planning note, so it is proposed as `inferred`, resting on one source.
- **Personal details stay out.** The first call contains an email address and a phone number. Neither appears in the evidence.
- **Nothing reaches the brain until you approve it,** section by section.
- **Gaps become questions.** What the material could not answer (champion profile, geography, voice, market maturity) is queued in `gaps.md` and asked one question at a time.

## Files

| File | What it is |
|---|---|
| `sources/` | The five fictional source documents |
| `expected-evidence.md` | The facts the skill should extract, in `references/evidence-format.md` format |
| `expected-brain-diff.md` | The proposed brain changes, by section, with the questions it should ask |
