# Android Claude Code Skills

> A repository of reusable Android development skills, compatible with OpenAI Codex and Claude Code.

## Table of Contents

- [Repository Information](#repository-information)
- [OpenAI Codex Compatibility](#openai-codex-compatibility)
- [Installation](#installation)
- [Updating Plugin](#updating-plugin)
- [Available Skills](#available-skills)
  - [Android Translation Sync](#android-translation-sync)
  - [Android Change Review](#android-change-review)
- [Third-Party Skills](#third-party-skills)
  - [review-loop — Automated Code Review Loop](#review-loop--automated-code-review-loop)
- [Adding Skills](#adding-skills)
- [Validation](#validation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT
- **Current Version**: 1.4.0
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

## OpenAI Codex Compatibility

This project primarily provides Android development skills, and the skill files are maintained in a format compatible with both OpenAI Codex and Claude Code:

- `skills/<skill-name>/SKILL.md` includes YAML frontmatter with `name` and `description`
- Optional `skills/<skill-name>/agents/openai.yaml` provides Codex UI metadata
- Existing Claude plugin structure (`.claude-plugin/`) is preserved for dual compatibility

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
# android-claude-code-skills  v1.4.0
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

### Android Change Review

Review Android code changes after coding to catch crash risks, boundary-condition bugs, and regressions.

**Usage (staged changes):**

```bash
git add .
```

Then ask:

```text
Review my staged changes for crash risks and boundary conditions.
```

**Usage (specific commit):**

```text
Please review commit abc1234 for crash risks and regressions.
```

**Features:**
- Review staged changes (`git diff --cached`) after `git add .`
- Review a specific commit (`git show <commit-id>`)
- Focus on crash paths, boundary conditions, and regressions
- Android-focused checks (lifecycle, nullability, threading, permission gating)
- Findings-first output with file/line references

**Trigger phrases:**
- `review staged changes`
- `review commit-id`
- `code review after coding`
- `检查当前修改代码`
- `边界条件检查`
- `崩溃风险检查`

---

## Third-Party Skills

Community-maintained plugins that extend Claude Code with additional workflows.

---

### review-loop — Automated Code Review Loop

> **Source**: [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop)

A Claude Code plugin that adds an automated, two-phase code review loop to every task. After Claude finishes implementing a task, a stop hook automatically triggers an independent Codex review, then asks Claude to address the findings — giving every change a second opinion before you accept it.

**How it works:**

1. **Task phase** — You describe a task, Claude implements it.
2. **Review phase** — When Claude finishes, the stop hook runs Codex (`codex exec`) for an independent review, writes findings to `reviews/review-<id>.md`, then asks Claude to address the feedback.
3. Claude resolves the items it agrees with and exits cleanly.

State is tracked in `.claude/review-loop.local.md` (add to `.gitignore`).

**Review coverage:**

| Area | What gets checked |
|---|---|
| Code quality | Organization, modularity, DRY, naming |
| Test coverage | New tests, edge cases, test quality |
| Security | Input validation, injection, secrets, OWASP Top 10 |
| Docs & agent harness | AGENTS.md, CLAUDE.md symlinks, telemetry, type system |
| UX & design | E2E tests, visual quality, accessibility (UI projects) |

**Requirements:**

- Claude Code CLI
- `jq` — `brew install jq` (macOS) / `apt install jq` (Linux)
- Codex CLI (recommended, falls back to Claude self-review if absent) — `npm install -g @openai/codex`

**Installation:**

```bash
# From within a Claude Code session
/plugin marketplace add hamelsmu/claude-review-loop
/plugin install review-loop@hamel-review
```

Or from the CLI directly:

```bash
claude plugin marketplace add hamelsmu/claude-review-loop
claude plugin install review-loop@hamel-review
```

**Usage:**

```text
# Start a review loop for a task
/review-loop Add user authentication with JWT tokens and test coverage

# Cancel an in-progress review loop
/cancel-review
```

**Configuration:**

| Environment Variable | Default | Description |
|---|---|---|
| `REVIEW_LOOP_CODEX_FLAGS` | `--dangerously-bypass-approvals-and-sandbox` | Flags passed to `codex`. Use `--sandbox workspace-write` for safer sandboxed reviews. |

The stop hook timeout is 900 seconds (15 min) by default — adjust in `hooks/hooks.json` if your reviews take longer.

**Logs:** Execution logs with timestamps, codex exit codes, and elapsed times are written to `.claude/review-loop.log` (gitignored).

---

## Adding Skills

Create your skills in the `skills/` directory:

```
skills/
└── your-skill-name/
    ├── SKILL.md
    └── agents/
        └── openai.yaml   # Optional (recommended for Codex UI)
```

Each skill requires a `SKILL.md` file with:

- **YAML frontmatter** - `name` and `description` (required for Codex skill triggering)
- **Description body** - Workflow, rules, and reusable knowledge for the skill
- **Optional agent metadata** - `agents/openai.yaml` for Codex UI display name/description/prompt

Minimal `SKILL.md` example:

```markdown
---
name: your-skill-name
description: Describe what the skill does and when to use it so Codex can trigger it.
---

# Your Skill Name

Skill instructions...
```

## Validation

Local validation (Codex-compatible `SKILL.md` + `agents/openai.yaml`):

```bash
python3 -m pip install --user PyYAML
python3 scripts/validate_skills.py
```

Pre-commit hook (run validation automatically before commit):

```bash
python3 -m pip install --user pre-commit
pre-commit install
pre-commit run --all-files
```

This repository also includes GitHub Actions CI at `.github/workflows/validate-skills.yml` to run the same checks on push/pull request.

## Project Structure

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # Plugin manifest
│   └── marketplace.json    # Marketplace configuration
├── skills/                 # Available skills
│   ├── android-translation-sync/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # Codex-compatible skill template
│       └── agents/openai.yaml
├── CLAUDE.md               # Project overview (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # プロジェクト概要（日本語）
├── README.md               # This file (English)
├── README_CN.md            # 说明文档（中文）
├── README_JP.md            # ドキュメント（日本語）
├── CHANGELOG.md            # Changelog (English)
└── CHANGELOG_JP.md         # 変更履歴（日本語）
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
