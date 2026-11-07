"""Skill metadata that lives in a plugin-level skills.meta.json sidecar instead of SKILL.md frontmatter.

The Claude directory refuses frontmatter keys outside its allowed list from unverified
organizations, so pmm-positioning keeps version, context, quality_gate and last_updated
in pmm-positioning/skills.meta.json. Other plugins still use frontmatter.
"""
import json
from pathlib import Path


def sidecar_get(skill_md: Path, key: str):
    """Return the sidecar value for this skill's key, or None when there is no sidecar entry."""
    meta_file = skill_md.parent.parent.parent / "skills.meta.json"
    if not meta_file.is_file():
        return None
    data = json.loads(meta_file.read_text(encoding="utf-8"))
    return data.get(skill_md.parent.name, {}).get(key)
