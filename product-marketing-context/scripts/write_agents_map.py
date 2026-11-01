#!/usr/bin/env python3
"""Write the product marketing map into the user's project AGENTS.md.

What it does (all safe to repeat):
  1. Writes or refreshes ONE block in AGENTS.md between the pmm-skills:map markers.
     Nothing outside the markers is ever touched.
  2. Makes Claude Code read AGENTS.md: adds a marked '@AGENTS.md' block to CLAUDE.md
     (created if missing, appended if the file has no '@AGENTS.md' line yet).
  3. Copies brain_section.py and lint_draft.py to foundation/tools/ so the map can name them.

Usage:
    python3 write_agents_map.py                  # run from the project root
    python3 write_agents_map.py --project DIR
    python3 write_agents_map.py --dry-run        # show what would change, write nothing
    python3 write_agents_map.py --no-tools       # skip step 3

Exit code: 0 done or unchanged, 2 no brain found. Plain Python 3, no installs.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

START = "<!-- pmm-skills:map start"
END = "<!-- pmm-skills:map end -->"
CL_START = "<!-- pmm-skills:import start -->"
CL_END = "<!-- pmm-skills:import end -->"
HERE = Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "agents-map-template.md"
TOOLS = ["brain_section.py", "lint_draft.py"]

SECTION_HINT = {
    1: "what we sell, claims we may make",
    2: "who we sell to, pains, triggers",
    3: "competitors, alternatives, objections",
    4: "voice, tone, forbidden phrases",
    5: "why now, market context",
    6: "approved numbers and quotes, forbidden claims",
    7: "priorities, launches, quarter goals",
    8: "stakeholders, approvals, prohibited topics",
}
RECORDS = [
    ("foundation/me.md", "how the user likes to work (format and detail only)"),
    ("foundation/gaps.md", "open questions about the brain"),
    ("foundation/evidence.md", "raw facts behind the brain, with sources"),
    ("context/competitor-profiles", "dated profile per competitor"),
    ("context/battlecards", "saved battlecards and deal outcomes"),
    ("context/monitoring", "weekly competitor sweep records"),
    ("context/signals", "ranked market signals"),
    ("context/industry-newsletter", "newsletter issues and call ledger"),
    ("context/meta-patterns.md", "guardrails every skill follows"),
]


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else None


def brain_sections(brain_text):
    return [(int(m.group(1)), m.group(2).strip())
            for m in re.finditer(r"^##\s+Section\s+(\d+)\s*:\s*(.*)$", brain_text, re.M)]


def render(project, brain_text):
    tpl = read(TEMPLATE)
    if tpl is None:
        raise SystemExit(f"Template missing: {TEMPLATE}")
    secs = brain_sections(brain_text)
    sec_lines = "\n".join(
        f"- Section {n} {name}: {SECTION_HINT.get(n, '')}".rstrip(": ") for n, name in secs
    ) or "- (no sections found yet)"
    rec = [f"- `{path}`: {why}" for path, why in RECORDS if (project / path).exists()]
    rec_lines = "\n".join(rec) or "- None yet. They appear as you use the skills."
    return tpl.replace("{{SECTIONS}}", sec_lines).replace("{{RECORDS}}", rec_lines).strip() + "\n"


def upsert_block(text, block, start_marker, end_marker):
    """Replace the marked block, or append it. Returns the new text."""
    if text is None or not text.strip():
        return block
    s = text.find(start_marker)
    e = text.find(end_marker)
    if s != -1 and e != -1 and e > s:
        return text[:s] + block.rstrip("\n") + "\n" + text[e + len(end_marker):].lstrip("\n")
    return text.rstrip("\n") + "\n\n" + block


def main(argv=None):
    ap = argparse.ArgumentParser(description="Write the product marketing map.")
    ap.add_argument("--project", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-tools", action="store_true")
    a = ap.parse_args(argv)

    project = Path(a.project).resolve()
    brain = project / "foundation" / "brain.md"
    if not brain.is_file():
        print("No foundation/brain.md here. Build the brain first (product-marketing-context).", file=sys.stderr)
        return 2

    changes = []
    block = render(project, brain.read_text(encoding="utf-8"))

    agents = project / "AGENTS.md"
    old = read(agents)
    new = upsert_block(old, block, START, END)
    if old is None:
        new = "# AGENTS.md\n\n" + new
    if new != old:
        changes.append(("AGENTS.md", "created" if old is None else "map block updated"))
        if not a.dry_run:
            agents.write_text(new, encoding="utf-8")

    claude = project / "CLAUDE.md"
    cold = read(claude)
    imp = f"{CL_START}\n@AGENTS.md\n{CL_END}\n"
    if cold is None:
        changes.append(("CLAUDE.md", "created with @AGENTS.md import"))
        if not a.dry_run:
            claude.write_text(imp, encoding="utf-8")
    elif not re.search(r"^\s*@AGENTS\.md\s*$", cold, re.M):
        changes.append(("CLAUDE.md", "import line appended"))
        if not a.dry_run:
            claude.write_text(cold.rstrip("\n") + "\n\n" + imp, encoding="utf-8")

    if not a.no_tools:
        tools_dir = project / "foundation" / "tools"
        for name in TOOLS:
            src, dst = HERE / name, tools_dir / name
            if not src.is_file():
                continue
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                changes.append((f"foundation/tools/{name}", "installed" if not dst.exists() else "updated"))
                if not a.dry_run:
                    tools_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src, dst)

    prefix = "Would change" if a.dry_run else "Changed"
    if not changes:
        print("Unchanged: the map, the CLAUDE.md import and the tools are already current.")
    else:
        for f, what in changes:
            print(f"{prefix}: {f} ({what})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
