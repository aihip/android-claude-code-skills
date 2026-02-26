# Android Claude Code Skills

> Android development skills for Claude Code - A customizable collection of Android development skills.

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT

## Installation

```bash
# Add this repository as a marketplace
/plugin marketplace add aihip/android-claude-code-skills

# Install the plugin
/plugin install android-claude-code-skills@android-claude-code-skills
```

## Updating Plugin

When new skills are added to this repository, update your installed plugin:

```bash
# Method 1: Update the plugin (recommended)
/plugin update android-claude-code-skills

# Method 2: Reinstall the plugin
/plugin uninstall android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# Method 3: Update marketplace first, then plugin
/plugin marketplace update aihip/android-claude-code-skills
/plugin update android-claude-code-skills
```

### What Gets Updated

When you update the plugin, you'll receive:
- New skills added to the repository
- Improvements to existing skills
- Bug fixes and enhancements

## Adding Skills

Create your skills in the `skills/` directory:

```
skills/
└── your-skill-name/
    └── SKILL.md
```

Each skill requires a `SKILL.md` file with:

- **Trigger phrases** - Keywords that activate the skill
- **When to use** - Guidance on when the skill applies
- **Content** - The actual knowledge/patterns

## Example Skill Structure

```markdown
# Your Skill Name

> Brief description of what this skill does.

## When to Use

**Trigger phrases:**
- "keyword 1"
- "keyword 2"

## Content

Your skill content here...
```

## Project Structure

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # Plugin manifest
│   └── marketplace.json    # Marketplace configuration
├── skills/                 # Add your skills here
│   └── template/
│       └── SKILL.md        # Skill template
├── CLAUDE.md               # Project overview (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── README.md               # This file (English)
└── README_CN.md            # 说明文档（中文）
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
