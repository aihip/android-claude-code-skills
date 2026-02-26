# Changelog

All notable changes to this project will be documented in this file.

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
