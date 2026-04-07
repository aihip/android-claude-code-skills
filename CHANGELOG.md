# Changelog

All notable changes to this project will be documented in this file.

## [1.8.0] - 2026-04-07

### Added
- **Figma to Android** skill (`skills/figma-to-android/`)
  - Add `SKILL.md` and `agents/openai.yaml`
  - Convert Figma design data (node JSON, layer descriptions, annotations, screenshots) to production-ready Android native XML + Kotlin code
  - 1:1 visual fidelity reproduction with ConstraintLayout-first approach
  - Strict output order: page structure analysis → directory structure → XML layouts → RecyclerView items → drawables → resource values → Kotlin code → risk notes
  - All colors, dimensions, shapes extracted to resource files (no inline hardcoding)
  - ViewBinding-based Kotlin code (Activity/Fragment, Adapter/ViewHolder, data classes)
  - Reusable module extraction via `<include>` sub-layouts
  - Naming conventions enforced: `tv_title`, `color_primary`, `dp_4`, `bg_card_white_radius_12`
  - Supplementary rules for list pages (NestedScrollView, form inputs, reusable bars)
  - Jetpack Compose strictly forbidden — only native View/XML output

### Changed
- **Cursor support** — Add `cursor-rules/figma-to-android.mdc`
- **Gemini CLI support** — Add `gemini-rules/figma-to-android.md` and `gemini-rules/commands/figma-to-android.toml`
- **`AGENTS.md`** — Add `$figma-to-android` skill entry with trigger phrases and capability description; update skill directory listing and install commands
- **`plugin.json`** — Add `figma`, `figma-to-android`, `design-to-code`, `xml-layout` keywords
- **`llms.txt`** — Add Figma to Android skill entry
- **Documentation (EN/CN/JP)**
  - Add `Figma to Android` to TOC and Available Skills section in all three README files
  - Update Codex CLI install commands, explicit/implicit usage examples, and `/skills` verify list
  - Update Cursor rules table and curl install commands
  - Update Gemini CLI `@import` examples and slash commands list
  - Expand Project Structure listing to include new files
- **`CLAUDE.md` / `CLAUDE_CN.md` / `CLAUDE_JP.md`** — Add `figma-to-android/` to project structure

### Validation
- `scripts/validate_skills.py` passes for all 6 skills

## [1.7.0] - 2026-02-27

### Added
- **Android Project Analyzer** skill (`skills/android-project-analyzer/`)
  - Add `SKILL.md` and `agents/openai.yaml`
  - Analyze project structure and Gradle modules from `settings.gradle[.kts]`
  - Extract app metadata from `AndroidManifest.xml`: applicationId, SDK versions, permissions (Dangerous / Normal / Signature), exported components, security flags
  - Parse all dependencies with versions from `gradle/libs.versions.toml` and `build.gradle[.kts]`, grouped by category (UI / Network / DI / Database / Testing / Other)
  - Detect architecture pattern (MVVM / MVI / Clean Architecture / MVP), DI framework (Hilt / Koin / Dagger), navigation setup, Compose vs View system, async approach
  - Build feature inventory from modules, feature packages, Activity/Screen entry points, and deep link declarations
  - Measure code quality: unit/instrumented test file counts, TODO/FIXME markers, `!!` force-unwrap count, files exceeding 500 lines, top-5 largest files
  - Scan for potential issues: hardcoded secrets, cleartext HTTP, sensitive log output, WebView misconfigurations, main-thread blocking, static Context leaks, outdated/legacy libraries
  - Produce structured report: 📱 Overview / 🏗️ Architecture / ✨ Features / 📦 Dependencies / 📊 Code Quality / ⚠️ Issues / 💡 Recommendations
- **npm package** (`package.json`) — publish to npm registry for broader discoverability
- **`llms.txt`** — AI crawler discoverability file (robots.txt equivalent for LLMs)
- **GitHub Actions** — `.github/workflows/publish-npm.yml` auto-publishes to npm on version tag push

### Changed
- **Cursor support** — Add `cursor-rules/android-project-analyzer.mdc`
- **Gemini CLI support** — Add `gemini-rules/android-project-analyzer.md` and `gemini-rules/commands/project-analyzer.toml`
- **`plugin.json`** — Bump version to `1.7.0`; expand keywords with `claude-code`, `gemini`, `cursor`, `codex`, `ai`, `llm`, `apk-analyzer`, `security`, etc.
- **`marketplace.json`** — Sync expanded keywords and tags; update description to mention all 4 platforms
- **Documentation (EN)**
  - Add `Android Project Analyzer` to TOC and Available Skills section
  - Add platform badges (npm, CI, Claude Code, Codex, Gemini CLI, Cursor) to README header
  - Update Codex CLI install commands, explicit/implicit usage examples, and `/skills` verify list
  - Update Cursor rules table and curl install commands
  - Update Gemini CLI `@import` examples and slash commands list
  - Expand Project Structure listing to include new files

### Validation
- `scripts/validate_skills.py` passes for all 5 skills

## [1.6.0] - 2026-02-27

### Added
- **APK Analyzer** skill (`skills/apk-analyzer/`)
  - Add `SKILL.md` and `agents/openai.yaml`
  - Extract APK metadata: package name, version code/name, min SDK, target SDK, app label
  - Classify all declared permissions into Dangerous / High-Risk / Normal tiers with annotated reference lists
  - Verify APK signature schemes (V1/V2/V3) via `apksigner`; print certificate subject, issuer, SHA-256 fingerprint, and expiry; detect debug keystore by known SHA-1
  - Decode `AndroidManifest.xml` via `apktool` and audit exported Activities, Services, Receivers, and Providers for missing permission protection
  - Check security flags: `debuggable`, `allowBackup`, cleartext traffic (`usesCleartextTraffic`), and `network_security_config.xml`
  - Detect native library ABIs (`armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64`) and common third-party SDKs (Firebase, React Native, Flutter, AppsFlyer, Sentry, etc.)
  - Scan for hardcoded secrets in `res/values/strings.xml` and decompiled Java sources
  - Include a complete `apk-analyze.sh` shell script covering all 7 analysis phases
  - Include a Python analysis path using `androguard` for programmatic/batch use
  - Produce a structured report with CRITICAL / HIGH / MEDIUM / INFO severity findings

### Changed
- **Cursor support** — Add `cursor-rules/apk-analyzer.mdc`
  - Agent-requested rule; auto-activates on "analyze apk", "apk权限分析", "apk签名检查", etc.
  - Covers: metadata extraction, permission tier table, signature check, manifest component audit, native library detection, security flag checklist, structured report format
- **Gemini CLI support** — Add `gemini-rules/apk-analyzer.md` and `gemini-rules/commands/apk-analyzer.toml`
  - `apk-analyzer.md`: GEMINI.md-compatible `@import` skill with condensed workflow
  - `apk-analyzer.toml`: `/apk-analyzer <path>` slash command with step-by-step prompt template
- **Codex CLI support** — `agents/openai.yaml` already included with `SKILL.md`
- **`AGENTS.md`** — Add `$apk-analyzer` skill entry with trigger phrases, use-when guide, and 8-step capability description; update skill directory listing and install commands
- **Documentation (EN)**
  - Add `APK Analyzer` entry to TOC and Available Skills section in `README.md`
  - Update Cursor rules table to include `apk-analyzer.mdc`
  - Update Gemini Method 1 `@import` examples and Method 2 slash command list to include `/apk-analyzer`
  - Update Codex CLI installation, explicit/implicit usage examples, and `/skills` verify list
  - Update Project Structure listing to include `apk-analyzer/`
- **Version**: bump to `1.6.0`

## [1.5.0] - 2026-02-27

### Added
- **Multi-platform skill support**
  - **OpenAI Codex CLI** — Native support via `.agents/skills/` installation; skills trigger with `$skill-name` or implicit auto-detection; add `AGENTS.md` for project-level agent instructions
  - **Cursor** — Add `cursor-rules/` with `.mdc` rule files for `android-translation-sync` and `android-change-review`; rules are Agent-requested type and auto-activate on matching requests
  - **Gemini CLI** — Add `gemini-rules/` with GEMINI.md-compatible `.md` files and custom slash command `.toml` files (`/translation-sync`, `/change-review`)
- **`AGENTS.md`** — Repository-level agent instructions file for OpenAI Codex CLI describing available skills, trigger phrases, and installation steps

### Changed
- **Documentation (EN/CN/JP)**
  - Add "Using Skills in Codex CLI", "Using Skills in Cursor", "Using Skills in Gemini CLI" sections to all three README files
  - Add 4-platform capability comparison table to all README files
  - Update TOC in all README files
- **`CLAUDE.md` / `CLAUDE_CN.md` / `CLAUDE_JP.md`**
  - Add `AGENTS.md` to project structure listing
- **`agents/openai.yaml`** (both skills)
  - Add trigger example comments for improved implicit invocation matching

## [1.4.0] - 2026-02-26

### Added
- **Android Change Review** skill
  - Add `skills/android-change-review/SKILL.md` and `agents/openai.yaml`
  - Support reviewing staged changes after `git add .` using `git diff --cached`
  - Support reviewing a specific `commit-id` using `git show <commit-id>`
  - Focus on Android crash risks, boundary conditions, and regression detection
  - Include Android-specific hotspots: Fragment/Activity lifecycle, Compose recomposition, coroutines/Flow, permissions, WorkManager, Room, navigation, RecyclerView/Paging, Manifest/resource config
  - Recommend findings-first output with file/line references and severity ordering

### Changed
- **Documentation (EN/CN)**
  - Add `Android Change Review` skill usage examples and trigger phrases to `README.md` / `README_CN.md`

### Fixed
- **YAML compatibility for desktop upload**
  - Quote `description` values in `SKILL.md` frontmatter where needed to improve YAML parsing compatibility

### Validation
- `quick_validate.py` passes for all skills
- `scripts/validate_skills.py` passes for all skills

## [1.3.0] - 2026-02-26

### Added
- **OpenAI Codex skill compatibility**
  - Add YAML frontmatter (`name`, `description`) to `skills/android-translation-sync/SKILL.md`
  - Add Codex-compatible `skills/template/SKILL.md` with frontmatter and reusable workflow guidance
  - Add `agents/openai.yaml` metadata for both skills (`android-translation-sync`, `template`)
- **Repository skill validation tooling**
  - Add `scripts/validate_skills.py` to validate:
    - `SKILL.md` frontmatter format and allowed keys
    - skill directory name ↔ frontmatter `name` consistency
    - `agents/openai.yaml` required fields and basic constraints
    - `interface.default_prompt` references the correct `$skill-name`
- **CI automation**
  - Add GitHub Actions workflow `.github/workflows/validate-skills.yml`
  - Run automatic validation on `push` and `pull_request` for skill-related changes
- **Pre-commit hook**
  - Add `.pre-commit-config.yaml` local hook to run `python scripts/validate_skills.py` before commit

### Changed
- **Documentation (EN/CN)**
  - Update `README.md` / `README_CN.md` to document Codex-compatible skill format
  - Add validation instructions (local + CI + pre-commit)
  - Update project structure examples to include `agents/openai.yaml`
- **Project overview docs (EN/CN)**
  - Update `CLAUDE.md` / `CLAUDE_CN.md` to describe dual compatibility (Claude Code + OpenAI Codex)

### Validation
- Install `PyYAML` locally and run official `quick_validate.py` against all current skills
- Run repository validator `scripts/validate_skills.py` successfully for all skills

## [1.2.1] - 2025-02-26

### Fixed
- **Skill loading issue** - Correct skills path in plugin.json
  - Change from `./skills/android-translation-sync/` to `./skills/`
  - This ensures all SKILL.md files are properly loaded
  - Fixes wrong skill being triggered

## [1.2.0] - 2025-02-26

### Changed
- **Android Translation Sync** - Refine update rules for precision
  - Emphasize: Replace ONLY the value content between `<string>` tags
  - DO NOT add any new lines
  - DO NOT remove any existing lines
  - Preserve all empty lines and comments exactly

### Fixed
- Clarify precise value replacement to avoid unwanted formatting changes

## [1.1.0] - 2025-02-26

### Added
- **Android Translation Sync** skill
  - Sync multilingual resources from Excel to strings.xml
  - Generate unique keys (10-20 chars) automatically
  - Write keys to Excel first column
  - Update all language files (values, values-zh, values-es, etc.)
  - Minimize code changes principle (preserve empty lines and comments)

### Changed
- Update plugin manifest with skills list
- Add version tracking

## [1.0.0] - 2025-02-26

### Added
- Initial release
- Plugin structure with `.claude-plugin/` configuration
- Skills template
- Bilingual documentation (EN/CN)
