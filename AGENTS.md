# Android Claude Code Skills — Agent Instructions

This repository provides reusable Android development skills compatible with OpenAI Codex, Claude Code, Cursor, and Gemini CLI.

## Available Skills

### $android-translation-sync

Synchronize Android multilingual `strings.xml` resources from an Excel spreadsheet.

**Use when:**
- User asks to sync Android translations from Excel
- User provides an `.xlsx` / `.xls` file path and asks to update strings
- Trigger phrases: "sync translations from excel", "update android strings from excel", "多语言翻译同步", "更新strings.xml"

**What it does:**
1. Reads the Excel file (col 1 = key, col 2 = English, rest = target languages)
2. Generates unique keys (10-20 chars, `lowercase_with_underscores`) for empty key cells
3. Writes generated keys back to Excel first column
4. Updates all `app/src/main/res/values-*/strings.xml` with precise value-only replacement (no added/removed lines, no formatting changes)
5. Reports a sync summary

### $android-change-review

Review Android code changes after implementation to catch crash risks, boundary-condition bugs, and regressions.

**Use when:**
- User asks to review staged changes (after `git add .`)
- User asks to review a specific commit-id or branch diff
- Trigger phrases: "review staged changes", "code review after coding", "检查当前修改代码", "边界条件检查", "崩溃风险检查"

**What it does:**
1. Runs `git diff --cached`, `git show <commit-id>`, or `git diff <base>...HEAD`
2. Triages large diffs by risk tier (lifecycle/ViewModel first, utilities last)
3. Checks crash paths, boundary conditions, regressions, and Android component hotspots
4. Reports findings ordered by severity (High / Medium / Low) with file/line references

## Skill Files

Skills are located in `skills/` and follow the standard SKILL.md format:

```
skills/
├── android-translation-sync/
│   ├── SKILL.md            ← Full workflow instructions + YAML frontmatter
│   └── agents/openai.yaml  ← Codex UI metadata
└── android-change-review/
    ├── SKILL.md
    └── agents/openai.yaml
```

## Installing in Codex CLI

```bash
# User-level — available in all your projects (recommended)
mkdir -p ~/.agents/skills
cp -r skills/android-translation-sync ~/.agents/skills/
cp -r skills/android-change-review ~/.agents/skills/

# Project-level — this project only
mkdir -p .agents/skills
cp -r skills/android-translation-sync .agents/skills/
cp -r skills/android-change-review .agents/skills/
```

After installing, invoke explicitly with `$android-translation-sync` or `$android-change-review`, or let Codex auto-select based on your task description.
