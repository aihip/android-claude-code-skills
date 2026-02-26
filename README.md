# Android Claude Code Skills

> Android development skills for Claude Code - A customizable collection of Android development skills.

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT
- **Current Version**: 1.2.1
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

## Installation

```bash
# Add this repository as a marketplace
/plugin marketplace add aihip/android-claude-code-skills

# Install the plugin
/plugin install android-claude-code-skills@android-claude-code-skills
```

## Updating Plugin

**IMPORTANT: Only this method works for updating:**

```bash
# Step 1: Update marketplace
/plugin marketplace update aihip/android-claude-code-skills

# Step 2: Update plugin
/plugin update android-claude-code-skills
```

**Note:** Other update methods may not fetch the latest version. Always use `marketplace update` first.

### What Gets Updated

When you update the plugin, you'll receive:
- New skills added to the repository
- Improvements to existing skills
- Bug fixes and enhancements

### Verify Update Success

After updating, check the version:

```bash
# View installed plugins and versions
/plugin list

# You should see:
# android-claude-code-skills  v1.1.0
```

Compare with the latest version on GitHub: https://github.com/aihip/android-claude-code-skills/blob/main/.claude-plugin/plugin.json

## Available Skills

### Android Translation Sync

Synchronize Android project multilingual resources from Excel spreadsheet.

**Usage:**

```
Please sync translations from excel: /path/to/translations.xlsx
```

**Features:**
- Read Excel file with translations (English + other languages)
- Generate unique keys (10-20 chars) based on English text
- Avoid conflicts with existing keys in strings.xml
- Update all language files (values, values-zh, values-es, etc.)
- New entries appended at bottom, existing keys updated

**Example:**

```
你：请帮我同步多语言翻译，Excel 文件是 ./translations/strings.xlsx

Claude：好的，我来处理...
- Reading Excel file...
- Checking existing strings.xml...
- Generating new keys...
- Updating all language files...
```

**Trigger phrases:**
- `sync translations from excel`
- `update android strings from excel`
- `多语言翻译同步`
- `更新strings.xml`

---

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

## Project Structure

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # Plugin manifest
│   └── marketplace.json    # Marketplace configuration
├── skills/                 # Available skills
│   ├── android-translation-sync/
│   │   └── SKILL.md
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
