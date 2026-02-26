# Changelog

All notable changes to this project will be documented in this file.

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
