#!/usr/bin/env python3
"""Generate every connector list in this repo from connectors.json.

You edit ONE file: connectors.json (in the repo root).
This script copies what is in it into:
  - each plugin's .mcp.json, and the root .mcp.json (every server, for people who install the whole repo)
  - the "Wired today" column in each plugin's CONNECTORS.md and README.md and in the root CONNECTORS.md
  - the "Servers in this plugin's .mcp.json" line in each plugin's CONNECTORS.md
  - the Google table in the root CONNECTORS.md
  - the plugin table in the root README.md
  - the Tools table and the "Connect your own" table in docs/connect-your-tools.md

Usage:
  python3 scripts/generate_connectors.py --check   # report anything out of date (changes nothing)
  python3 scripts/generate_connectors.py --write   # rewrite the generated files

You normally never run this by hand: the "Connectors sync" GitHub Action
runs --write for you whenever connectors.json changes on main.

Text between "<!-- generated:NAME begin -->" and "<!-- generated:NAME end -->"
markers is overwritten. Do not edit inside those markers.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "connectors.json"

SERVER_FIELDS = {"name", "tool", "label", "docs", "category", "type", "url",
                 "plugins", "signin", "unlocks", "if_fails"}
OWN_FIELDS = {"tool", "category", "documents", "todo"}
GOOGLE = [("Gmail", "gmail"), ("Calendar", "google-calendar"), ("Drive", "google-drive"),
          ("Docs", "google-docs"), ("Sheets", "google-sheets"), ("Slides", "google-slides")]


def load():
    try:
        return json.loads(CATALOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"connectors.json is not valid JSON (line {e.lineno}, column {e.colno}): {e.msg}\n"
                 "Usual cause: a missing or extra comma, or a missing quote mark. "
                 "Compare with the block above or below yours.")


def cats_of(s):
    """A server can serve more than one category: "market data, SEO"."""
    return [c.strip() for c in str(s.get("category", "")).split(",") if c.strip()]


def validate(cat):
    problems = []
    plugins = cat["plugins"]
    foundation = cat["foundation"]
    if foundation not in plugins:
        problems.append(f"foundation '{foundation}' must be listed in plugins")
    root_conn = (ROOT / "CONNECTORS.md").read_text(encoding="utf-8")
    root_cats = set(re.findall(r"`~~([^`]+)`", root_conn))
    names = set()
    for s in cat["servers"]:
        n = s.get("name", "?")
        extra = set(s) - SERVER_FIELDS
        if extra:
            problems.append(f"server '{n}': unknown field(s) {sorted(extra)}. Never add keys, tokens or headers here")
        for f in ("name", "tool", "category", "type", "url", "signin", "unlocks", "if_fails"):
            if not s.get(f):
                problems.append(f"server '{n}': '{f}' is missing or empty")
        if n in names:
            problems.append(f"server '{n}' appears twice")
        names.add(n)
        if s.get("type") not in ("http", "sse"):
            problems.append(f"server '{n}': type must be \"http\"")
        if not str(s.get("url", "")).startswith("https://"):
            problems.append(f"server '{n}': url must start with https://")
        if "<" in str(s.get("url", "")) or "{" in str(s.get("url", "")):
            problems.append(f"server '{n}': url has a placeholder in it. Per-customer addresses go in connect_your_own, not servers")
        for c in cats_of(s):
            if c not in root_cats:
                problems.append(f"server '{n}': category '{c}' is not in the root CONNECTORS.md table. Add the category row there first")
        for p in s.get("plugins", []):
            if p not in plugins or p == foundation:
                problems.append(f"server '{n}': '{p}' is not a valid plugin here (the brain plugin always gets every server, so do not list it)")
    for o in cat["connect_your_own"]:
        extra = set(o) - OWN_FIELDS
        if extra or not all(o.get(f) for f in OWN_FIELDS):
            problems.append(f"connect_your_own '{o.get('tool', '?')}': needs exactly tool, category, documents, todo")
        elif o["category"].split(",")[0].strip() not in root_cats:
            problems.append(f"connect_your_own '{o['tool']}': category '{o['category']}' is not in the root CONNECTORS.md")
    return problems


def wired(cat, plugin):
    return [s for s in cat["servers"] if plugin == cat["foundation"] or plugin in s.get("plugins", [])]


def labels(servers):
    out = []
    for s in servers:
        lab = s.get("label", s["tool"])
        if lab and lab not in out:
            out.append(lab)
    return out


def mcp_json(cat, plugin):
    data = {"mcpServers": {s["name"]: {"type": s["type"], "url": s["url"]} for s in wired(cat, plugin)}}
    return json.dumps(data, indent=2) + "\n"


def region(name, body):
    return f"<!-- generated:{name} begin -->\n{body}\n<!-- generated:{name} end -->"


def servers_line(cat, plugin):
    names = ", ".join(s["name"] for s in wired(cat, plugin))
    return f"Servers in this plugin's `.mcp.json`: {names}."


def google_table(cat):
    head = "| Plugin | " + " | ".join(g[0] for g in GOOGLE) + " |\n|---|" + "---|" * len(GOOGLE)
    rows = []
    for p in cat["plugins"] + cat["no_connector_plugins"]:
        have = {s["name"] for s in wired(cat, p)} if p in cat["plugins"] else set()
        rows.append(f"| {p} | " + " | ".join("yes" if g[1] in have else "" for g in GOOGLE) + " |")
    return head + "\n" + "\n".join(rows)


def readme_table(cat):
    rows = ["| Plugin | Connectors wired |", "|---|---|"]
    for p in cat["plugins"]:
        rows.append(f"| {p} | {', '.join(labels(wired(cat, p)))} |")
    for p in cat["no_connector_plugins"]:
        rows.append(f"| {p} | None |")
    return "\n".join(rows)


def tools_table(cat):
    rows = ["| Tool | Category | Sign-in | Unlocks | If it fails |", "|---|---|---|---|---|"]
    for s in cat["servers"]:
        if s.get("docs", True):
            rows.append(f"| {s['tool']} | {s['category']} | {s['signin']} | {s['unlocks']} | {s['if_fails']} |")
    return "\n".join(rows)


def own_table(cat):
    rows = ["| Tool | Category | What the vendor documents | What to do |", "|---|---|---|---|"]
    for o in cat["connect_your_own"]:
        rows.append(f"| {o['tool']} | {o['category']} | {o['documents']} | {o['todo']} |")
    return "\n".join(rows)


def replace_region(text, name, body, where):
    pat = re.compile(rf"<!-- generated:{name} begin -->.*?<!-- generated:{name} end -->", re.S)
    if not pat.search(text):
        sys.exit(f"{where}: the marker lines for '{name}' are missing. "
                 f"Put back <!-- generated:{name} begin --> and <!-- generated:{name} end -->")
    return pat.sub(lambda m: region(name, body), text, count=1)


NONE_TEXT = "none wired: paste, or connect your own server"


def wired_cell(servers, category):
    labs = labels([s for s in servers if category in cats_of(s)])
    return ", ".join(labs)


def fix_wired_column(text, servers, cells, root):
    """Rewrite the 'Wired today' cell of every `~~category` row.
    Plugin tables have 3 columns (wired is last); the root table has 4 (wired is third)."""
    out = []
    for line in text.split("\n"):
        if line.startswith("| `~~"):
            parts = line.strip().strip("|").split(" | ")
            parts = [x.strip() for x in parts]
            idx = 2
            if len(parts) == cells and parts[0].startswith("`~~"):
                cat = parts[0].strip("`").lstrip("~")
                w = wired_cell(servers, cat)
                if w:
                    parts[idx] = w
                elif not root:
                    parts[idx] = NONE_TEXT
                line = "| " + " | ".join(parts) + " |"
        out.append(line)
    return "\n".join(out)


def desired(cat):
    """Return {relative path: full new file text} for every generated file."""
    out = {}
    for p in cat["plugins"]:
        out[f"{p}/.mcp.json"] = mcp_json(cat, p)
        rel = f"{p}/CONNECTORS.md"
        txt = replace_region((ROOT / rel).read_text(encoding="utf-8"), "servers", servers_line(cat, p), rel)
        out[rel] = fix_wired_column(txt, wired(cat, p), 3, False)
        rrel = f"{p}/README.md"
        out[rrel] = fix_wired_column((ROOT / rrel).read_text(encoding="utf-8"), wired(cat, p), 3, False)
    out[".mcp.json"] = json.dumps({"mcpServers": {s["name"]: {"type": s["type"], "url": s["url"]} for s in cat["servers"]}}, indent=2) + "\n"
    rel = "CONNECTORS.md"
    txt = replace_region((ROOT / rel).read_text(encoding="utf-8"), "google-table", google_table(cat), rel)
    out[rel] = fix_wired_column(txt, cat["servers"], 4, True)
    rel = "README.md"
    out[rel] = replace_region((ROOT / rel).read_text(encoding="utf-8"), "plugin-table", readme_table(cat), rel)
    rel = "docs/connect-your-tools.md"
    t = (ROOT / rel).read_text(encoding="utf-8")
    t = replace_region(t, "tools-table", tools_table(cat), rel)
    t = replace_region(t, "own-table", own_table(cat), rel)
    out[rel] = t
    return out


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--check", "--write"):
        sys.exit(__doc__)
    cat = load()
    problems = validate(cat)
    if problems:
        print("connectors.json has problems:")
        for p in problems:
            print("  -", p)
        return 1
    stale = []
    for rel, text in desired(cat).items():
        path = ROOT / rel
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            stale.append(rel)
            if mode == "--write":
                path.write_text(text, encoding="utf-8")
    if mode == "--check":
        if stale:
            print("These files are out of date with connectors.json:")
            for r in stale:
                print("  -", r)
            print("Fix: run  python3 scripts/generate_connectors.py --write  (the 'Connectors sync' Action does this for you on main).")
            return 1
        print("Generated connector files are up to date.")
        return 0
    print(f"Rewrote {len(stale)} file(s)." if stale else "Nothing to change.")
    for r in stale:
        print("  -", r)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
