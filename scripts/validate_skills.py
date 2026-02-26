#!/usr/bin/env python3
"""Validate Codex-compatible skill files in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

MAX_SKILL_NAME_LENGTH = 64
SHORT_DESCRIPTION_MIN = 25
SHORT_DESCRIPTION_MAX = 64
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in `{path}`: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"`{path}` must contain a YAML mapping at the top level")
    return data


def parse_frontmatter(skill_md: Path) -> dict[str, Any]:
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        raise ValueError(f"`{skill_md}` missing YAML frontmatter")

    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        raise ValueError(f"`{skill_md}` has invalid YAML frontmatter format")

    frontmatter_text = match.group(1)
    try:
        data = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid frontmatter YAML in `{skill_md}`: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Frontmatter in `{skill_md}` must be a YAML mapping")
    return data


def validate_skill_name(name: Any, skill_dir: Path) -> str:
    if not isinstance(name, str):
        raise ValueError(f"`{skill_dir}/SKILL.md` frontmatter `name` must be a string")
    name = name.strip()
    if not name:
        raise ValueError(f"`{skill_dir}/SKILL.md` frontmatter `name` cannot be empty")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        raise ValueError(f"`{skill_dir}/SKILL.md` frontmatter `name` must be hyphen-case")
    if name.startswith("-") or name.endswith("-") or "--" in name:
        raise ValueError(
            f"`{skill_dir}/SKILL.md` frontmatter `name` cannot start/end with '-' or contain '--'"
        )
    if len(name) > MAX_SKILL_NAME_LENGTH:
        raise ValueError(
            f"`{skill_dir}/SKILL.md` frontmatter `name` exceeds {MAX_SKILL_NAME_LENGTH} characters"
        )
    if skill_dir.name != name:
        raise ValueError(
            f"Skill directory `{skill_dir.name}` must match frontmatter `name: {name}`"
        )
    return name


def validate_skill_md(skill_dir: Path) -> str:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise ValueError(f"Missing `{skill_md}`")

    frontmatter = parse_frontmatter(skill_md)
    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        raise ValueError(
            f"`{skill_md}` has unexpected frontmatter keys: {', '.join(sorted(unexpected))}"
        )

    if "name" not in frontmatter:
        raise ValueError(f"`{skill_md}` frontmatter missing `name`")
    if "description" not in frontmatter:
        raise ValueError(f"`{skill_md}` frontmatter missing `description`")

    skill_name = validate_skill_name(frontmatter["name"], skill_dir)

    description = frontmatter["description"]
    if not isinstance(description, str) or not description.strip():
        raise ValueError(f"`{skill_md}` frontmatter `description` must be a non-empty string")
    if "<" in description or ">" in description:
        raise ValueError(f"`{skill_md}` frontmatter `description` cannot contain '<' or '>'")
    if len(description.strip()) > 1024:
        raise ValueError(f"`{skill_md}` frontmatter `description` exceeds 1024 characters")

    return skill_name


def require_non_empty_string(parent: dict[str, Any], key: str, path: Path) -> str:
    value = parent.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"`{path}` requires non-empty string `{key}`")
    return value.strip()


def validate_openai_yaml(skill_dir: Path, skill_name: str) -> None:
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        raise ValueError(f"Missing `{openai_yaml}`")

    data = load_yaml(openai_yaml)

    interface = data.get("interface")
    if not isinstance(interface, dict):
        raise ValueError(f"`{openai_yaml}` requires top-level `interface` mapping")

    display_name = require_non_empty_string(interface, "display_name", openai_yaml)
    short_description = require_non_empty_string(interface, "short_description", openai_yaml)
    default_prompt = require_non_empty_string(interface, "default_prompt", openai_yaml)

    if len(short_description) < SHORT_DESCRIPTION_MIN or len(short_description) > SHORT_DESCRIPTION_MAX:
        raise ValueError(
            f"`{openai_yaml}` `interface.short_description` must be {SHORT_DESCRIPTION_MIN}-{SHORT_DESCRIPTION_MAX} chars"
        )

    if f"${skill_name}" not in default_prompt:
        raise ValueError(
            f"`{openai_yaml}` `interface.default_prompt` must explicitly mention `${skill_name}`"
        )

    if display_name.startswith("$"):
        raise ValueError(f"`{openai_yaml}` `interface.display_name` should be a user-facing title")

    policy = data.get("policy")
    if not isinstance(policy, dict):
        raise ValueError(f"`{openai_yaml}` requires top-level `policy` mapping")

    allow_implicit = policy.get("allow_implicit_invocation")
    if not isinstance(allow_implicit, bool):
        raise ValueError(
            f"`{openai_yaml}` `policy.allow_implicit_invocation` must be a boolean"
        )


def find_skill_dirs(repo_root: Path) -> list[Path]:
    skills_root = repo_root / "skills"
    if not skills_root.exists():
        raise ValueError(f"Missing skills directory: `{skills_root}`")

    return sorted(path for path in skills_root.iterdir() if path.is_dir())


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        skill_dirs = find_skill_dirs(repo_root)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if not skill_dirs:
        print("ERROR: No skill directories found under `skills/`")
        return 1

    failures: list[str] = []

    for skill_dir in skill_dirs:
        try:
            skill_name = validate_skill_md(skill_dir)
            validate_openai_yaml(skill_dir, skill_name)
            print(f"OK   {skill_dir.relative_to(repo_root)}")
        except ValueError as exc:
            failures.append(str(exc))
            print(f"FAIL {skill_dir.relative_to(repo_root)}")

    if failures:
        print("\nValidation errors:")
        for err in failures:
            print(f"- {err}")
        return 1

    print(f"\nValidated {len(skill_dirs)} skill(s): all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
