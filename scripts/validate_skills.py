#!/usr/bin/env python3
"""Validate the required offsec-agent Skill catalog."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"

REQUIRED_SKILLS = {
    "recon-osint",
    "web-api",
    "active-directory",
    "linux-security",
    "windows-security",
    "cloud-security",
    "kubernetes-security",
    "docker-security",
    "mobile",
    "llm-security",
    "prompt-injection",
    "agent-security",
    "jailbreak-evals",
    "reporting",
    "poc-automation",
    "mcp-security",
    "bug-bounty",
    "ctf-labs",
    "threat-modeling",
    "secure-code-review",
    "cicd-security",
    "devsecops",
    "ai-assisted-pentesting",
}

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_SAFETY = {"authorized-only", "contained-only", "defensive"}


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) == 3 else ""


def top_level_value(metadata: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", metadata, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def nested_value(metadata: str, key: str) -> str | None:
    match = re.search(rf"^\s+{re.escape(key)}:\s*(.+?)\s*$", metadata, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def main() -> int:
    errors: list[str] = []

    if not SKILLS_ROOT.is_dir():
        print(f"ERROR: missing directory {SKILLS_ROOT}", file=sys.stderr)
        return 1

    present = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
    for missing in sorted(REQUIRED_SKILLS - present):
        errors.append(f"missing required Skill directory: {missing}")

    for skill_name in sorted(REQUIRED_SKILLS & present):
        skill_file = SKILLS_ROOT / skill_name / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {skill_name}")
            continue

        text = skill_file.read_text(encoding="utf-8")
        metadata = frontmatter(text)
        if not metadata:
            errors.append(f"{skill_name}: missing or malformed YAML frontmatter")
            continue

        declared_name = top_level_value(metadata, "name")
        description = top_level_value(metadata, "description")
        safety = nested_value(metadata, "safety")

        if declared_name != skill_name:
            errors.append(
                f"{skill_name}: frontmatter name must match directory "
                f"(found {declared_name!r})"
            )
        if declared_name and not NAME_RE.fullmatch(declared_name):
            errors.append(f"{skill_name}: invalid Skill name format")
        if not description or len(description) < 20:
            errors.append(f"{skill_name}: description is missing or too short")
        if safety is not None and safety not in ALLOWED_SAFETY:
            errors.append(f"{skill_name}: unsupported metadata safety value {safety!r}")
        if "## Approval boundaries" not in text:
            errors.append(f"{skill_name}: missing section ## Approval boundaries")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} problem(s).", file=sys.stderr)
        return 1

    print(f"Skill validation passed: {len(REQUIRED_SKILLS)} required Skills present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
