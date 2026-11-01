# Modes detail

Moved verbatim from `SKILL.md`.

## AI PMM Mode, Level Calibration, Story Archetypes, Resume Build Mode (moved verbatim)

## AI PMM Mode

Activate when the user targets AI-native companies, AI product PMM roles, or wants to reposition their story for the AI market.

**What AI company hiring execs look for:**

| Signal | What it looks like on a resume |
|--------|-------------------------------|
| AI product GTM | Launched AI features/products, not just "software with AI inside" |
| Technical fluency | Worked with LLMs, RAG, model evaluation — can brief engineers and customers both |
| Trust and adoption framing | Positioned around ROI proof, explainability, responsible use — not just features |
| Category creation | Helped define how the market thinks about an AI capability |
| Cross-functional with AI teams | Led alongside data science, ML engineering, or AI research |
| Responsible AI narrative | Ethics, safety, transparency as PMM positioning elements |

**Example rewrites:**
- ❌ "Marketed AI features to enterprise customers"
- ✅ "Positioned LLM-powered workflow automation for enterprise buyers — built the ROI narrative that reduced sales cycle by 3 weeks and improved win rate vs. incumbent by 22%"

**Title landscape:** "AI PMM," "PMM for AI Platform," "Senior PMM — Machine Learning," "Product Marketing Lead, GenAI" are all valid. Flag if the user is underselling AI exposure with a generic title.

---

## Level Calibration

- **Manager PMM:** Execution excellence, clean launch ownership, measurable outputs, cross-functional coordination
- **Director PMM:** GTM system ownership, commercial influence (pipeline, win rate, ACV), cross-functional leadership, team or program leadership
- **VP PMM:** Market shaping, category creation, org design, board-level narrative, revenue accountability

Calibrate every rewrite to the stated target level. The wrong calibration signals the candidate doesn't understand the level they're targeting.

---

## Story Archetype Detection

Identify which archetype the resume reads as, and what's needed to advance it:

| Archetype | Signals | What's Missing | Next Stage |
|-----------|---------|---------------|------------|
| **Operator** | Task-level bullets, execution metrics, "ran campaigns" | System-level framing, cross-functional ownership | Orchestrator |
| **Orchestrator** | Cross-functional leadership, GTM motion ownership, launch outcomes | Commercial ownership, market narrative, named GTM motion | Market Shaper |
| **Market Shaper** | Category creation, analyst narrative, revenue accountability, org-building | VP-ready signal confirmed | — |

Tell the user which archetype their resume reads as, and exactly what language shifts would advance it.

---

## Resume Build Mode

Activate after a Full Audit or TAILOR session is complete and the user has confirmed the rewritten content — never generate a final file before that.

**Trigger phrases:** "Build my resume," "Generate the final version," "Give me the formatted resume."

**Confirm before building:**
> "Ready to build the final version? I'll use everything we've rewritten today and format it into a clean resume."

**Output:** a clean, well-formatted document (markdown or plain text) containing:
- The approved rewritten summary (3-part formula)
- Each role entry: scope paragraph → Key Achievements (metric-first, impact-ordered) → Responsibilities
- Skills section: AI PMM tier first if targeting AI roles, then PMM Specialties → GTM & Commercial → Tools
- Education, with sub-fields only where they add a signal
- PMM-relevant certifications only

If the user wants a polished HTML or PDF version, use the `docx` or `pdf` skill to produce it from this content rather than hand-rolling a template here.

---
