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


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
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
        if not text.startswith("---\n"):
            errors.append(f"{skill_name}: YAML frontmatter must start on line 1")

        declared_name = frontmatter_value(text, "name")
        description = frontmatter_value(text, "description")
        safety = frontmatter_value(text, "safety")

        if declared_name != skill_name:
            errors.append(
                f"{skill_name}: frontmatter name must match directory "
                f"(found {declared_name!r})"
            )
        if declared_name and not NAME_RE.fullmatch(declared_name):
            errors.append(f"{skill_name}: invalid Skill name format")
        if not description or len(description) < 20:
            errors.append(f"{skill_name}: description is missing or too short")
        if safety not in {"authorized-only", "contained-only", "defensive"}:
            errors.append(
                f"{skill_name}: metadata safety must be authorized-only, "
                "contained-only, or defensive"
            )

        required_sections = ("## Purpose", "## Approval boundaries", "## Deliverables")
        for section in required_sections:
            if section not in text:
                errors.append(f"{skill_name}: missing section {section}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed: {len(errors)} problem(s).", file=sys.stderr)
        return 1

    print(f"Skill validation passed: {len(REQUIRED_SKILLS)} required Skills present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
