"""Docs and manifest consistency checks for the Product-Marketing-Skills repo.

Run manually with:
    python3 -m unittest tests/test_consistency.py -v

Wired into CI at .github/workflows/structure-check.yml alongside the
existing check_structure.py structural check. That script checks whether
references RESOLVE (a skill name mentioned somewhere really exists on
disk); this file checks whether COUNTS AGREE (a stated "N skills" or
"## Skills (N)" number actually matches what's on disk). The two are
complementary, not redundant — check_structure.py would not have caught
the writing-assistant.eval.m filename-truncation or the "(3)" vs "(4)"
README drift this workstream hit; this file exists specifically to catch
those classes of problem going forward.

What this locks in:
- marketplace.json's plugin list matches the plugin directories on disk;
- one version everywhere: newest CHANGELOG.md heading == marketplace.json's
  metadata.version == every plugin.json's version (per CLAUDE.md's
  "Versioning & Releases" rule — this repo already states the rule and
  already says CI enforcement doesn't exist yet; this file is that
  enforcement);
- CHANGELOG.md headings are well-formed, dated, unique, and newest-first;
- every plugin README's "## Skills (N)" / "## Commands (N)" header matches
  the actual skill folder count / command file count on disk;
- the root README's "## Available Skills (N Total)" table has exactly N
  rows and N matches the total skill count across all plugins;
- every `pmm-x:y`-style command reference in a plugin README resolves to
  a real commands/y.md file in that same plugin.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CHANGELOG = ROOT / "CHANGELOG.md"
ROOT_README = ROOT / "README.md"


def plugin_dirs():
    """Every directory with a .claude-plugin/plugin.json — the same
    definition check_structure.py uses, kept identical on purpose so the
    two scripts never disagree about what counts as a plugin."""
    return sorted(
        p
        for p in ROOT.iterdir()
        if p.is_dir() and (p / ".claude-plugin" / "plugin.json").is_file()
    )


def skill_dirs(plugin: Path):
    """Skill folders under a plugin's declared skills path — resolves the
    plugin.json 'skills' field rather than assuming skills/ by name, since
    at least one plugin in this repo (pmm-foundation) points 'skills' at
    the plugin root itself, not a skills/ subfolder."""
    pj = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    skills_field = pj.get("skills")
    if not skills_field:
        return []
    candidates = [skills_field] if isinstance(skills_field, str) else skills_field
    dirs = []
    for c in candidates:
        target = (plugin / c).resolve()
        if target.is_dir():
            dirs.append(target)
    out = []
    for d in dirs:
        if (d / "SKILL.md").is_file():
            out.append(d)  # flat: skills path IS a single skill folder
        else:
            out.extend(s for s in d.iterdir() if s.is_dir() and (s / "SKILL.md").is_file())
    return out


def skill_count(plugin: Path) -> int:
    return len(skill_dirs(plugin))


def command_count(plugin: Path) -> int:
    cmds = plugin / "commands"
    if not cmds.is_dir():
        return 0
    return len(list(cmds.glob("*.md")))


def marketplace() -> dict:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))


def latest_changelog_version() -> str:
    for line in CHANGELOG.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## v(\d+\.\d+\.\d+)\b", line)
        if m:
            return m.group(1)
    raise AssertionError("no '## vX.Y.Z' heading found in CHANGELOG.md")


class TestMarketplaceList(unittest.TestCase):
    def test_marketplace_lists_exactly_the_plugins_on_disk(self):
        listed = {p["name"] for p in marketplace()["plugins"]}
        on_disk = {p.name for p in plugin_dirs()}
        self.assertEqual(
            listed,
            on_disk,
            f"marketplace.json vs disk — only listed: {sorted(listed - on_disk)}, "
            f"only on disk: {sorted(on_disk - listed)}",
        )

    def test_sources_resolve_to_real_directories(self):
        for p in marketplace()["plugins"]:
            src = p["source"].lstrip("./")
            target = ROOT / src
            self.assertTrue(
                target.is_dir(),
                f"plugin '{p['name']}' source '{p['source']}' does not resolve to a real directory",
            )


class TestVersionSync(unittest.TestCase):
    """CLAUDE.md states one version everywhere; this is that rule enforced."""

    def test_all_versions_identical_and_match_changelog(self):
        want = latest_changelog_version()
        mismatches = []
        mp_version = marketplace()["metadata"]["version"]
        if mp_version != want:
            mismatches.append(f"marketplace.json metadata.version={mp_version}")
        for p in plugin_dirs():
            manifest = p / ".claude-plugin" / "plugin.json"
            v = json.loads(manifest.read_text(encoding="utf-8"))["version"]
            if v != want:
                mismatches.append(f"{p.name}/.claude-plugin/plugin.json={v}")
        self.assertEqual(
            mismatches,
            [],
            f"CHANGELOG.md says v{want}; out of sync: {mismatches}",
        )


class TestChangelogFormat(unittest.TestCase):
    def test_headings_well_formed_dated_unique_descending(self):
        text = CHANGELOG.read_text(encoding="utf-8")
        text = text.split("\n# Legacy releases", 1)[0]  # old-numbering releases are listed after this line
        headings = [l for l in text.splitlines() if l.startswith("## ")]
        self.assertTrue(headings, "CHANGELOG.md has no '## ' headings")

        versions = []
        for h in headings:
            if h.strip() == "## Unreleased":
                continue
            m = re.match(r"^## v(\d+\.\d+\.\d+) — (\d{4})-(\d{2})-(\d{2})$", h)
            self.assertIsNotNone(
                m,
                f"malformed CHANGELOG heading {h!r} — expected "
                f"'## vX.Y.Z — YYYY-MM-DD'",
            )
            year, month, day = int(m.group(2)), int(m.group(3)), int(m.group(4))
            self.assertTrue(
                1 <= month <= 12 and 1 <= day <= 31,
                f"CHANGELOG heading {h!r} has an impossible date "
                f"(month={month}, day={day}) — likely DD-MM swapped for MM-DD",
            )
            versions.append(tuple(int(x) for x in m.group(1).split(".")))

        self.assertEqual(
            len(versions), len(set(versions)), "duplicate version headings in CHANGELOG.md"
        )
        self.assertEqual(
            versions,
            sorted(versions, reverse=True),
            "CHANGELOG.md version headings are not newest-first",
        )


class TestReadmeCounts(unittest.TestCase):
    def _totals(self):
        plugins = plugin_dirs()
        return sum(skill_count(p) for p in plugins), sum(command_count(p) for p in plugins), len(plugins)

    def test_root_readme_available_skills_total(self):
        """'## Available Skills (N Total)' header must match both the
        total on disk AND the number of rows actually in the table below
        it — catches the header drifting from the table as much as from
        disk."""
        total_skills, _, _ = self._totals()
        text = ROOT_README.read_text(encoding="utf-8")

        m = re.search(r"^## Available Skills \((\d+) Total\)", text, re.M)
        self.assertIsNotNone(
            m, "README.md has no '## Available Skills (N Total)' header"
        )
        header_count = int(m.group(1))

        # count table rows: lines starting with "| [" between this header
        # and the next "## " header
        start = m.end()
        next_header = text.find("\n## ", start)
        table_block = text[start:next_header if next_header != -1 else None]
        row_count = len(re.findall(r"^\| \[", table_block, re.M))

        self.assertEqual(
            header_count,
            row_count,
            f"README.md header says ({header_count} Total) but the skills "
            f"table has {row_count} rows",
        )
        self.assertEqual(
            header_count,
            total_skills,
            f"README.md header says ({header_count} Total) but {total_skills} "
            f"skill folders exist on disk across all plugins",
        )

    def test_plugin_readme_section_counts(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            m = re.search(r"^## Skills \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(
                    int(m.group(1)),
                    skill_count(p),
                    f"{p.name}/README.md '## Skills (N)' header doesn't match disk",
                )
            m = re.search(r"^## Commands \((\d+)\)", text, re.M)
            if m:
                self.assertEqual(
                    int(m.group(1)),
                    command_count(p),
                    f"{p.name}/README.md '## Commands (N)' header doesn't match disk",
                )


class TestCommandReferences(unittest.TestCase):
    """Every /plugin:command mentioned in a plugin README must resolve to
    a real commands/*.md file in that same plugin."""

    def test_plugin_readme_command_refs_exist(self):
        for p in plugin_dirs():
            readme = p / "README.md"
            if not readme.is_file():
                continue
            text = readme.read_text(encoding="utf-8")
            for m in re.finditer(rf"/{re.escape(p.name)}:([\w-]+)", text):
                cmd = p / "commands" / f"{m.group(1)}.md"
                self.assertTrue(
                    cmd.is_file(),
                    f"{p.name}/README.md references /{p.name}:{m.group(1)} "
                    f"but commands/{m.group(1)}.md is missing",
                )


class TestContextClassification(unittest.TestCase):
    """SKILL-SPEC.md lists which skills are brain-dependent or context-agnostic.
    Each skill's `context:` frontmatter must agree with those lists."""

    def _spec_list(self, label):
        spec = (ROOT / "SKILL-SPEC.md").read_text(encoding="utf-8")
        m = re.search(r"\*\*" + re.escape(label) + r":\*\*([^\n]*)", spec)
        self.assertIsNotNone(m, f"SKILL-SPEC.md has no '{label}' list")
        return set(re.findall(r"`([^`]+)`", m.group(1)))

    def test_frontmatter_matches_spec_lists(self):
        dep = self._spec_list("Brain-dependent skills")
        agn = self._spec_list("Context-agnostic skills")
        bad = []
        for skill in ROOT.rglob("SKILL.md"):
            if ".git" in skill.parts:
                continue
            m = re.search(r"^  context: (\S+)", skill.read_text(encoding="utf-8"), re.M)
            if not m:
                continue
            name = skill.parent.name
            want = dep if m.group(1) == "brain-dependent" else agn
            if name not in want:
                bad.append(f"{name}: frontmatter says {m.group(1)}, not in the matching SKILL-SPEC list")
        self.assertEqual(bad, [])


class TestPhantomSections(unittest.TestCase):
    """Brain sections that never existed must not come back in skills or evals."""

    PHANTOMS = ("Revenue " + "Levers", "Personas (\u00a74)")
    ALLOWED = {"pmm-okrs.eval.md", "CHANGELOG.md", "test_consistency.py"}

    def test_no_phantom_sections(self):
        bad = []
        for f in ROOT.rglob("*.md"):
            if ".git" in f.parts or f.name in self.ALLOWED:
                continue
            text = f.read_text(encoding="utf-8")
            for ph in self.PHANTOMS:
                if ph in text:
                    bad.append(f"{f.relative_to(ROOT)}: {ph}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()


class TestBrainSchema(unittest.TestCase):
    SCHEMA = ROOT / "product-marketing-context" / "references" / "brain-schema.md"

    def schema_sections(self):
        text = self.SCHEMA.read_text(encoding="utf-8")
        return {int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", text, re.M)}

    def test_template_sections_match_schema(self):
        template = ROOT / "product-marketing-context" / "templates" / "brain-template.md"
        found = {int(m.group(1)) for m in re.finditer(r"^## Section (\d+):", template.read_text(encoding="utf-8"), re.M)}
        self.assertEqual(found, self.schema_sections(),
                         "brain-template.md sections differ from brain-schema.md")

    def test_skills_cite_only_real_sections(self):
        """Only paragraphs that talk about the brain are checked, so a skill's
        own 'Section 12' of SKILL-SPEC or a '0-100' score is not a brain citation."""
        valid = self.schema_sections()
        cite = re.compile(r"\bSections?\s+(\d+)(?:\s*(?:,|and|&|to|-|\u2013)\s*(\d+))*\b(?!\s*-\s*\d)")
        bad = []
        for skill in ROOT.rglob("SKILL.md"):
            if ".git" in skill.parts:
                continue
            text = skill.read_text(encoding="utf-8")
            for para in re.split(r"\n\s*\n", text):
                if not re.search(r"brain", para, re.I):
                    continue
                for m in cite.finditer(para):
                    for n in re.findall(r"\d+", m.group(0)):
                        if int(n) not in valid:
                            bad.append(f"{skill.relative_to(ROOT)}: {m.group(0)}")
        self.assertEqual(bad, [], "Skill cites a brain section missing from brain-schema.md")


class TestNextSkillMap(unittest.TestCase):
    MAP = ROOT / "product-marketing-context" / ".claude-plugin" / "next-skill-map.md"

    def real_skill_names(self):
        return {p.parent.name for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts}

    def test_every_hyphenated_skill_in_the_map_exists(self):
        names = self.real_skill_names()
        text = self.MAP.read_text(encoding="utf-8")
        found = set()
        for line in text.splitlines():
            m = re.match(r"^## After ([a-z0-9]+(?:-[a-z0-9]+)+)\b", line)
            if m:
                found.add(m.group(1))
            m = re.match(r"^\*\*Next:\*\*\s+([a-z0-9]+(?:-[a-z0-9]+)+)", line)
            if m:
                found.add(m.group(1))
            m = re.match(r"^- ([a-z0-9]+(?:-[a-z0-9]+)+) \u2014", line)
            if m:
                found.add(m.group(1))
        missing = sorted(n for n in found if n not in names)
        self.assertEqual(missing, [], "next-skill-map.md names a skill that does not exist")


class TestBanList(unittest.TestCase):
    NVT = "n.v" + ".t."
    HS = "hs" + "-"
    TEXT = {".md", ".json", ".py", ".yml", ".yaml"}

    def files(self):
        for p in ROOT.rglob("*"):
            if p.is_file() and ".git" not in p.parts and p.suffix in self.TEXT:
                yield p

    # Two files must name the legacy marker so old logs and forks still read correctly.
    NVT_ALLOWED = {
        "product-marketing-context/.claude-plugin/skill-sessions-format.md",
        "pmm-meta/skills/meta-review/SKILL.md",
    }

    def test_no_dutch_marker(self):
        hits = [str(p.relative_to(ROOT)) for p in self.files()
                if self.NVT in p.read_text(encoding="utf-8", errors="ignore")
                and str(p.relative_to(ROOT)) not in self.NVT_ALLOWED]
        self.assertEqual(hits, [])

    def test_no_retired_prefix(self):
        hits = [str(p.relative_to(ROOT)) for p in self.files()
                if re.search(r"\b" + re.escape(self.HS), p.read_text(encoding="utf-8", errors="ignore"))]
        self.assertEqual(hits, [])
