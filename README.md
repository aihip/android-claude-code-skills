# Android Claude Code Skills

**Languages:** English | [中文](README_CN.md) | [日本語](README_JP.md)

[![npm](https://img.shields.io/npm/v/android-claude-code-skills)](https://www.npmjs.com/package/android-claude-code-skills)
[![Validate Skills](https://github.com/aihip/android-claude-code-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/aihip/android-claude-code-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-blue)](https://github.com/aihip/android-claude-code-skills)
[![OpenAI Codex](https://img.shields.io/badge/OpenAI_Codex-compatible-green)](https://github.com/aihip/android-claude-code-skills)
[![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-compatible-orange)](https://github.com/aihip/android-claude-code-skills)
[![Cursor](https://img.shields.io/badge/Cursor-rules-purple)](https://github.com/aihip/android-claude-code-skills)

> A repository of reusable Android development skills, compatible with **Claude Code**, **OpenAI Codex**, **Gemini CLI**, and **Cursor**.

## Table of Contents

- [Repository Information](#repository-information)
- [OpenAI Codex Compatibility](#openai-codex-compatibility)
- [Installation](#installation)
- [Updating Plugin](#updating-plugin)
- [Available Skills](#available-skills)
  - [Android Project Analyzer](#android-project-analyzer)
  - [Android Translation Sync](#android-translation-sync)
  - [Android Change Review](#android-change-review)
  - [APK Analyzer](#apk-analyzer)
  - [Figma to Android](#figma-to-android)
- [Third-Party Skills](#third-party-skills)
  - [review-loop — Automated Code Review Loop](#review-loop--automated-code-review-loop)
  - [claude-codex — Multi-AI Orchestration Pipeline](#claude-codex--multi-ai-orchestration-pipeline)
  - [Android AI Skills — Production-Grade Android Best Practices](#android-ai-skills--production-grade-android-best-practices)
- [Using Skills in Codex CLI](#using-skills-in-codex-cli)
- [Using Skills in Cursor](#using-skills-in-cursor)
- [Using Skills in Gemini CLI](#using-skills-in-gemini-cli)
- [Adding Skills](#adding-skills)
- [Validation](#validation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Repository Information

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **Author**: aihip
- **License**: MIT
- **Current Version**: 1.8.0
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
# android-claude-code-skills  v1.8.0
```

Compare with the latest version on GitHub: https://github.com/aihip/android-claude-code-skills/blob/main/.claude-plugin/plugin.json

## Available Skills

### Android Project Analyzer

Analyze an Android project codebase and produce a comprehensive technical report covering structure, features, architecture, dependencies, code quality, and potential issues.

**Usage:**

```
Analyze the Android project in the current directory.
```

**Features:**
- Project overview: applicationId, SDK versions, module structure, file counts
- Architecture detection: MVVM / MVI / Clean Architecture, DI framework, navigation, Compose vs View
- Feature inventory: entry points, packages, deep links
- Full dependency list with versions grouped by category (UI / Network / DI / Database / Testing)
- Code quality metrics: test coverage surface, TODO/FIXME count, force-unwrap (`!!`) count, large files
- Potential issues: hardcoded secrets, cleartext HTTP, memory leaks, crash risks, outdated libraries
- Prioritized recommendations

**Trigger phrases:**
- `analyze android project`
- `analyze this project`
- `project architecture review`
- `dependency audit`
- `code quality review`
- `project health check`
- `分析安卓项目`
- `项目架构分析`
- `依赖审计`
- `代码质量分析`

---

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

### APK Analyzer

Parse and audit Android APK files: extract metadata, classify permissions by risk, verify signatures, inspect exported components, detect native libraries and third-party SDKs, and produce a security report.

**Usage:**

```
Analyze this APK: /path/to/your.apk
```

**Features:**
- Extract package name, version code/name, min/target SDK from APK
- Classify all permissions as Dangerous / High-Risk / Normal
- Verify V1/V2/V3 signature schemes and print certificate details
- Detect debug keystore by SHA-1 fingerprint
- Identify exported Activities, Services, Receivers, and Providers
- Check security flags: `debuggable`, `allowBackup`, cleartext traffic
- Detect native library ABIs and third-party SDKs (Flutter, React Native, Firebase, etc.)
- Includes a full shell script (`apk-analyze.sh`) and Python (androguard) analysis path
- Produces a structured security audit report with CRITICAL / HIGH / MEDIUM / INFO findings

**Trigger phrases:**
- `analyze apk`
- `check apk permissions`
- `verify apk signature`
- `audit apk security`
- `apk信息提取`
- `apk权限分析`
- `apk签名检查`
- `apk安全审计`

---

### Figma to Android

Convert Figma design data (node JSON, layer descriptions, annotations, or screenshot descriptions) into production-ready Android native XML + Kotlin code with 1:1 visual fidelity.

**Usage:**

```
Convert this Figma design to Android native code:
[paste Figma node JSON / layer description / annotation data]
```

**Features:**
- Page structure analysis and component hierarchy identification
- ConstraintLayout-first XML layouts with proper constraint-based positioning
- RecyclerView for all list/repeating content with separate item layouts
- All colors, dimensions, shapes extracted to resource files (no inline hardcoding)
- ViewBinding-based Kotlin code (Activity/Fragment, Adapter/ViewHolder, data classes)
- Reusable module extraction via `<include>` sub-layouts
- Risk notes for visual effects that cannot be fully inferred
- Strictly forbids Jetpack Compose — only native View/XML output

**Trigger phrases:**
- `figma to android`
- `convert figma design`
- `design to android code`
- `figma node json`
- `figma 转 android`
- `figma 生成代码`
- `设计稿转代码`
- `还原设计稿`

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

### claude-codex — Multi-AI Orchestration Pipeline

> **Source**: [Z-M-Huang/claude-codex](https://github.com/Z-M-Huang/claude-codex)
> **Note**: This project has moved to [Z-M-Huang/vcp](https://github.com/Z-M-Huang/vcp/plugins/dev-buddy). Future development continues there.

A Claude Code plugin providing a **multi-AI orchestration pipeline** that runs your code through three independent reviewers — Claude Sonnet, Claude Opus, and Codex — before accepting any change. Based on the professional principle that no code should be deployed after only one reviewer.

**Why multi-AI review?**

| Reviewer | What It Catches |
|---|---|
| Claude Sonnet | Obvious bugs, security basics, code style |
| Claude Opus | Architectural issues, subtle bugs, edge cases |
| Codex | Fresh perspective from a different AI model |

Each reviewer checks for OWASP Top 10 vulnerabilities, proper error handling, and code quality. The loop-until-approved model means code doesn't proceed until all three reviewers give the green light.

**Available skills:**

| Skill | Purpose |
|---|---|
| `multi-ai` | Full feature development pipeline (requirements → plan → implement → review) |
| `bug-fix` | Bug-fix pipeline with dual root-cause analysis + Codex validation |

**Custom agents used internally:**

| Agent | Model | Role |
|---|---|---|
| `requirements-gatherer` | Opus | Business Analyst + PM hybrid |
| `planner` | Opus | Architect + Fullstack hybrid |
| `plan-reviewer` | Sonnet + Opus | Architecture, Security & QA validation |
| `implementer` | Sonnet | Fullstack + TDD + quality implementation |
| `code-reviewer` | Sonnet + Opus | Security, Performance & QA validation |
| `root-cause-analyst` | Sonnet + Opus | Parallel bug diagnosis (bug-fix pipeline) |

**Requirements:**

- Claude Code CLI
- Codex CLI — `npm install -g @openai/codex`
- Bun (used for cross-platform JSON processing, replaces `jq`)

**Installation:**

```bash
# Step 1: Add marketplace
/plugin marketplace add Z-M-Huang/claude-codex

# Step 2: Install plugin (user scope — available in all projects, recommended)
/plugin install claude-codex@claude-codex --scope user

# Step 3: Add .task to .gitignore
echo ".task" >> .gitignore
```

**Usage:**

```text
# Feature development pipeline
/claude-codex:multi-ai Add user authentication with JWT tokens

# Bug-fix pipeline
/claude-codex:bug-fix Login fails silently when session token expires
```

> Always use the full namespace `claude-codex:<skill>` when invoking from external projects. Or describe the task naturally and Claude will invoke the right skill.

**Pipeline flow (`/multi-ai`):**

1. **Requirements** — Specialist agents explore in parallel; `requirements-gatherer` synthesizes
2. **Planning** — `planner` agent creates implementation plan
3. **Plan Reviews** — `plan-reviewer` (Sonnet + Opus) + Codex gate
4. **Implementation** — `implementer` iterates until tests pass
5. **Code Reviews** — `code-reviewer` (Sonnet + Opus) + Codex final gate
6. **Complete** — Reports results

**Pipeline flow (`/bug-fix`):**

1. **Dual RCA** — Two `root-cause-analyst` agents (Sonnet + Opus) analyze in parallel
2. **Consolidation** — Orchestrator synthesizes both analyses into a fix plan
3. **Codex Validation** — Codex reviews the consolidated RCA and fix plan
4. **Implementation** — Minimal fix targeting the root cause
5. **Code Reviews** — `code-reviewer` (Sonnet + Opus) + Codex gate

**Pipeline enforcement (task dependencies):**

```
1. Implement  →  2. Review (Sonnet)  →  3. Review (Opus)  →  4. Review (Codex)
                      ↓ needs_changes?
                 Create fix task → same reviewer re-validates → continue
```

**Default limits:**

| Setting | Default |
|---|---|
| Plan review loop limit | 10 iterations |
| Code review loop limit | 15 iterations |
| Auto-resolve attempts | 3 retries |

**License:** GPL-3.0 with attribution requirement (author: Z-M-Huang).

---

### Android AI Skills — Production-Grade Android Best Practices

> **Source**: [noloman/Android-AI-skills](https://github.com/noloman/Android-AI-skills)

A comprehensive collection of **23 opinionated, production-grade AI skills** for Android, Kotlin Multiplatform (KMP), and Compose Multiplatform projects. Compatible with 10 AI tools: Claude Code, Codex, GitHub Copilot, Cursor, Windsurf, Cline, JetBrains AI, Amazon Q, Aider, and OpenCode.

**Skill categories:**

| Category | Skills |
|---|---|
| Project type | `compose-best-practices`, `kmp-architecture-best-practices`, `compose-multiplatform-best-practices` |
| Code quality | `kotlin-coroutines-best-practices`, `android-testing-best-practices`, `android-accessibility-best-practices` |
| Security & privacy | `android-security-best-practices`, `android-auth-identity` |
| Performance & infra | `android-performance-best-practices`, `android-build-infra`, `android-ci-cd` |
| Architecture | `android-dependency-injection`, `android-navigation-best-practices`, `android-background-work` |
| Data & network | `android-networking`, `android-local-storage` |
| Platform features | `android-media`, `android-maps-location`, `android-ml-ondevice` |
| Monetization | `play-store-readiness`, `play-billing-best-practices`, `revenuecat-best-practices` |
| Third-party | `firebase-best-practices` |

**Enterprise Mode** auto-activates when `detekt.yml`, `lint.xml`, or `ktlint` / `spotless` config is detected — enforcing zero new violations.

**Installation:**

```bash
# Global install (Codex + Claude Code + OpenCode)
npx android-ai-skills@latest

# Project-level install (all 10 tools)
npx android-ai-skills@latest init

# Target specific tools
npx android-ai-skills@latest init --tools claude,codex
npx android-ai-skills@latest init --tools cursor,copilot

# Install only specific skill sets
npx android-ai-skills@latest --android-only
npx android-ai-skills@latest --kmp-only
```

**License:** MIT

---

## Using Skills in Codex CLI

The skills in this repository are **natively compatible with OpenAI Codex CLI** — the `SKILL.md` files already include the required YAML frontmatter (`name`, `description`) and each skill has an `agents/openai.yaml` for UI metadata.

### Installation

Codex discovers skills from `.agents/skills/` directories. Copy the skills to either user-level or project-level:

```bash
# User-level — available in ALL your projects (recommended)
mkdir -p ~/.agents/skills
cp -r skills/android-project-analyzer ~/.agents/skills/
cp -r skills/android-translation-sync ~/.agents/skills/
cp -r skills/android-change-review ~/.agents/skills/
cp -r skills/apk-analyzer ~/.agents/skills/
cp -r skills/figma-to-android ~/.agents/skills/
```

```bash
# Project-level — this project only
mkdir -p .agents/skills
cp -r skills/android-project-analyzer .agents/skills/
cp -r skills/android-translation-sync .agents/skills/
cp -r skills/android-change-review .agents/skills/
cp -r skills/apk-analyzer .agents/skills/
cp -r skills/figma-to-android .agents/skills/
```

Or use symlinks to always stay in sync with repo updates:

```bash
ln -s "$(pwd)/skills/android-project-analyzer" ~/.agents/skills/
ln -s "$(pwd)/skills/android-translation-sync" ~/.agents/skills/
ln -s "$(pwd)/skills/android-change-review" ~/.agents/skills/
ln -s "$(pwd)/skills/apk-analyzer" ~/.agents/skills/
ln -s "$(pwd)/skills/figma-to-android" ~/.agents/skills/
```

### Usage

**Explicit invocation** (type `$` to open the skill selector):

```text
$android-project-analyzer  analyze the current project

$android-translation-sync  ./translations/strings.xlsx

$android-change-review  review my staged changes

$apk-analyzer  ./build/outputs/apk/release/app-release.apk

$figma-to-android  convert the following Figma node JSON to Android native code
```

**Implicit invocation** — Codex auto-selects the skill based on your description (`allow_implicit_invocation: true`):

```text
Analyze the Android project architecture and dependencies.

Sync translations from Excel: ./translations/strings.xlsx

Review my staged changes for Android crash risks and boundary conditions.

Analyze this APK for permissions and security issues: ./app-release.apk

Convert this Figma design to Android native code: [paste design data]
```

### Verify Installation

```bash
# In a Codex CLI session
/skills
# Should list: android-project-analyzer, android-translation-sync, android-change-review, apk-analyzer, figma-to-android
```

---

## Using Skills in Cursor

The skills in this repository are natively designed for **Claude Code CLI**. For **Cursor** users, pre-converted `.mdc` rule files are provided in the [`cursor-rules/`](cursor-rules/) directory.

### Available Cursor Rules

| File | Skill |
|---|---|
| `cursor-rules/android-project-analyzer.mdc` | Android Project Analyzer |
| `cursor-rules/android-translation-sync.mdc` | Android Translation Sync |
| `cursor-rules/android-change-review.mdc` | Android Change Review |
| `cursor-rules/apk-analyzer.mdc` | APK Analyzer |
| `cursor-rules/figma-to-android.mdc` | Figma to Android |

### Installation

Copy the `.mdc` files into your Android project's `.cursor/rules/` directory:

```bash
# In your Android project root
mkdir -p .cursor/rules

curl -o .cursor/rules/android-project-analyzer.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-project-analyzer.mdc

curl -o .cursor/rules/android-translation-sync.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-translation-sync.mdc

curl -o .cursor/rules/android-change-review.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-change-review.mdc

curl -o .cursor/rules/apk-analyzer.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/apk-analyzer.mdc

curl -o .cursor/rules/figma-to-android.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/figma-to-android.mdc
```

Or clone this repo and copy manually:

```bash
cp android-claude-code-skills/cursor-rules/*.mdc your-android-project/.cursor/rules/
```

### Usage in Cursor

All rules are **Agent-requested** type — Cursor's AI automatically activates them when it detects a matching request. You can also trigger them explicitly:

```text
# Project analysis
Analyze the Android project architecture and dependencies.

# Translation sync
Sync translations from Excel: ./translations/strings.xlsx

# Code review
Review my staged changes for Android crash risks and boundary conditions.

# APK analysis
Analyze this APK for permissions and security issues: ./build/outputs/apk/release/app-release.apk

Convert this Figma design to Android native code: [paste design data]
```

> **Note:** Cursor rules are static prompt injection and do not support hooks, slash commands, or multi-agent orchestration. The workflow knowledge is fully preserved, but automated triggers (e.g. Stop Hook in `review-loop`) are not available.

---

## Using Skills in Gemini CLI

Pre-converted files for [Gemini CLI](https://github.com/google-gemini/gemini-cli) are in the [`gemini-rules/`](gemini-rules/) directory. Two integration methods are available.

### Method 1 — GEMINI.md (Recommended)

Inject the skill content into your project's `GEMINI.md` using the `@import` syntax:

```bash
# In your Android project root
mkdir -p .gemini

# Append import references to your project GEMINI.md
cat >> GEMINI.md << 'EOF'

# Android Skills
@/path/to/android-claude-code-skills/gemini-rules/android-project-analyzer.md
@/path/to/android-claude-code-skills/gemini-rules/android-translation-sync.md
@/path/to/android-claude-code-skills/gemini-rules/android-change-review.md
@/path/to/android-claude-code-skills/gemini-rules/apk-analyzer.md
@/path/to/android-claude-code-skills/gemini-rules/figma-to-android.md
EOF
```

Or copy the files directly and reference them locally:

```bash
mkdir -p .gemini/skills
cp android-claude-code-skills/gemini-rules/*.md .gemini/skills/

# Then in GEMINI.md
cat >> GEMINI.md << 'EOF'
@.gemini/skills/android-project-analyzer.md
@.gemini/skills/android-translation-sync.md
@.gemini/skills/android-change-review.md
@.gemini/skills/apk-analyzer.md
@.gemini/skills/figma-to-android.md
EOF
```

Once added, simply describe your task naturally:

```text
Sync translations from Excel: ./translations/strings.xlsx

Review my staged changes for Android crash risks.

Analyze this APK: ./build/outputs/apk/release/app-release.apk

Convert this Figma design to Android native code: [paste design data]
```

### Method 2 — Custom Slash Commands

Install the `.toml` command files to get `/project-analyzer`, `/translation-sync`, `/change-review`, and `/apk-analyzer` slash commands:

```bash
# Global install (available in all projects)
mkdir -p ~/.gemini/commands
cp android-claude-code-skills/gemini-rules/commands/*.toml ~/.gemini/commands/

# OR project-level install
mkdir -p .gemini/commands
cp android-claude-code-skills/gemini-rules/commands/*.toml .gemini/commands/
```

Then use directly in Gemini CLI:

```text
# Analyze project
/project-analyzer

# Sync translations
/translation-sync ./translations/strings.xlsx

# Review staged changes
/change-review staged

# Review a specific commit
/change-review abc1234

# Analyze an APK
/apk-analyzer ./build/outputs/apk/release/app-release.apk

# Convert Figma design
/figma-to-android [paste Figma node JSON or design description]
```

### Capability Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---|---|---|---|---|
| Workflow knowledge | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| Skill format | SKILL.md | SKILL.md (native) | GEMINI.md / `.md` | `.mdc` rules |
| Skill trigger | `/plugin` + slash | `$skill-name` or auto | natural language | natural language |
| Auto-detect from description | ✅ | ✅ (`allow_implicit_invocation`) | ✅ | ✅ |
| Context file | CLAUDE.md | AGENTS.md | GEMINI.md | `.cursor/rules/` |
| Stop Hook / lifecycle hooks | ✅ | ❌ | ❌ | ❌ |
| Multi-agent orchestration | ✅ | ❌ | ❌ | ❌ |

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
├── .github/
│   └── workflows/
│       ├── validate-skills.yml   # CI: validate all skills on push
│       └── publish-npm.yml       # CI: publish to npm on version tag
├── skills/                 # Available skills
│   ├── android-project-analyzer/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── android-translation-sync/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── android-change-review/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── apk-analyzer/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── figma-to-android/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # Codex-compatible skill template
│       └── agents/openai.yaml
├── cursor-rules/           # Cursor IDE rules (.mdc)
│   ├── android-project-analyzer.mdc
│   ├── android-translation-sync.mdc
│   ├── android-change-review.mdc
│   ├── apk-analyzer.mdc
│   └── figma-to-android.mdc
├── gemini-rules/           # Gemini CLI rules
│   ├── android-project-analyzer.md
│   ├── android-translation-sync.md
│   ├── android-change-review.md
│   ├── apk-analyzer.md
│   ├── figma-to-android.md
│   └── commands/           # Gemini slash commands (.toml)
│       ├── project-analyzer.toml
│       ├── translation-sync.toml
│       ├── change-review.toml
│       ├── apk-analyzer.toml
│       └── figma-to-android.toml
├── llms.txt                # AI crawler discoverability
├── package.json            # npm registry metadata
├── AGENTS.md               # Agent instructions (OpenAI Codex)
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
