# pmm-go-to-market

Brain-powered GTM strategy generator for B2B SaaS Product Marketing Managers.

## What It Does

- **Assigns launch tier** (T1/T2/T3/T4) using proven framework
- **Generates strategic brief** (messaging, channels, metrics, timeline)
- **Reads your PMM brain** for context and past launch learnings
- **Routes to execution skills** (product-launch-playbook, positioning, battlecards)
- **Self-learns** from every launch via Section 7 memory

## How It Works

```
User: "We're launching SSO integration"
    ↓
go-to-market-strategy:
  1. Reads /foundation/brain.md (all 7 sections)
  2. Assigns tier (T2 - major feature)
  3. Generates 2-3 page strategy doc
  4. Routes to product-launch-playbook for full execution
    ↓
Launch happens → Retro → Brain Section 7 updated
    ↓
Next launch: Plugin reads Section 7 → adjusts recommendations
```

## Installation

1. Download this folder
2. Place in your skills directory: `/skills/go-to-market-strategy/`
3. Trigger phrases: "create GTM strategy", "plan this launch", "tier this feature"

## Dependencies

**Required:**
- Brain system (`/foundation/brain.md`)

**Integrates with:**
- `product-launch-playbook` (full execution plans)
- `hs-positioning-messaging` (if positioning stale)
- `hs-competitive-battlecard` (if competitive intel missing)
- `hs-retro` (post-launch retrospectives)

**Optional:**
- Notion MCP (searches past launch briefs)
- Google Drive MCP (searches competitive docs)

## File Structure

```
go-to-market-strategy/
├── SKILL.md (main plugin logic)
├── config/
│   ├── tier-framework.md (T1/T2/T3/T4 classification)
│   ├── tactics-by-tier.md (channel playbooks)
│   ├── success-metrics-defaults.md (targets by tier)
│   └── messaging-structure.md (positioning framework)
├── templates/
│   ├── t1-strategy-template.md (major launch)
│   ├── t2-strategy-template.md (integrated campaign)
│   └── t3-strategy-template.md (lightweight campaign)
├── evals/
│   └── gtm-strategy-EVAL.md (10 test cases)
└── INTEGRATION.md (integration guide)
```

## Output Examples

**Tier 1 (Major Launch):**
- 1500-2000 words
- 12-week timeline
- Full messaging, channel plan, metrics, risks
- Routes to product-launch-playbook for execution

**Tier 2 (Integrated Campaign):**
- 800-1200 words
- 8-week timeline
- Targeted strategy for major features
- Routes to product-launch-playbook if needed

**Tier 3 (Lightweight Campaign):**
- 300-500 words
- 3-week timeline
- Quick strategy for enhancements
- No additional skills needed

## Self-Learning

After each launch, capture results in brain Section 7:
- What worked (channels, tactics, messaging)
- What didn't work (with root cause)
- Tier calibration (was tier correct?)

Next launch → plugin adjusts recommendations based on YOUR past performance.

## Configuration

All config files are separate from skill logic:
- **Tier criteria:** Edit `config/tier-framework.md`
- **Success metrics:** Edit `config/success-metrics-defaults.md`
- **Channel tactics:** Edit `config/tactics-by-tier.md`

## Version

v1.0 — May 2026

## Author

Built for B2B SaaS PMM teams running product launches at scale.

---

*Part of the Brain-Powered PMM System*
