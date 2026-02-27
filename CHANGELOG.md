# Changelog

All notable changes to this project will be documented in this file.

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
