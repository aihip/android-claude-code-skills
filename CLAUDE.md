# Android Claude Code Skills

## Project Overview

This is an Android development skills plugin repository for Claude Code. Contains a customizable collection of Android development skills.

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT

## Skills Description

All skills are located in the `skills/` directory. Each skill is a subdirectory containing a `SKILL.md` file.

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

Create a new subdirectory in `skills/` and add a `SKILL.md` file:

```
skills/your-skill-name/SKILL.md
```

### SKILL.md Template

```markdown
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
│       └── SKILL.md        # Skill template
├── CLAUDE.md               # This file (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── README.md               # Documentation (English)
└── README_CN.md            # 说明文档（中文）
```
