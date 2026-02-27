# Android Claude Code Skills

## Project Overview

This is a repository of reusable Android development skills, compatible with OpenAI Codex and Claude Code. It preserves the Claude plugin layout while keeping skill files Codex-compatible.

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT

## Skills Description

All skills are located in the `skills/` directory. Each skill is a subdirectory containing a `SKILL.md` file. For Codex compatibility, `SKILL.md` should start with YAML frontmatter (`name`, `description`), and `agents/openai.yaml` is recommended for UI metadata.

## Common Commands

```bash
# Install plugin
/plugin marketplace add aihip/android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# Update plugin (REQUIRED METHOD)
/plugin marketplace update aihip/android-claude-code-skills
/plugin update android-claude-code-skills

# Reinstall plugin
/plugin uninstall android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills
```

**Note:** Always use `marketplace update` first, then `plugin update` to get the latest version.

## Adding New Skills

Create a new subdirectory in `skills/` and add a `SKILL.md` file (plus optional `agents/openai.yaml` for Codex UI):

```
skills/your-skill-name/SKILL.md
```

### SKILL.md Template

```markdown
---
name: your-skill-name
description: "Describe what the skill does and when Codex should use it."
---

# Skill Name

> Skill description

## When to Use

**Trigger phrases:**
- "keyword1"
- "keyword2"

## Content

Your skill content here...
```

## Project Structure

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # Plugin manifest
│   └── marketplace.json    # Marketplace config
├── skills/                 # Skills directory
│   └── template/
│       ├── SKILL.md        # Codex-compatible skill template
│       └── agents/openai.yaml
├── AGENTS.md               # Agent instructions (OpenAI Codex)
├── CLAUDE.md               # This file (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # プロジェクト概要（日本語）
├── README.md               # Documentation (English)
├── README_CN.md            # 说明文档（中文）
├── README_JP.md            # ドキュメント（日本語）
├── CHANGELOG.md            # Changelog (English)
└── CHANGELOG_JP.md         # 変更履歴（日本語）
```
