# Contributing to Android Claude Code Skills

Thank you for your interest in contributing! This project welcomes all types of contributions.

## How to Contribute

### Report Bugs

Found a bug? Please open an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, AI platform, etc.)

### Suggest New Skills

Have an idea for a new Android development skill? Open an issue or PR with:
- Skill name and description
- Use cases and trigger phrases
- Expected workflow/behavior

### Submit Code Changes

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-skill`)
3. Follow the skill template structure
4. Run validation: `python scripts/validate_skills.py`
5. Commit your changes (`git commit -m 'feat: add amazing skill'`)
6. Push to the branch (`git push origin feature/amazing-skill`)
7. Open a Pull Request

## Skill Structure

```
skills/your-skill-name/
├── SKILL.md              # Main skill documentation (with YAML frontmatter)
└── agents/
    └── openai.yaml       # Codex UI metadata (optional but recommended)
```

### SKILL.md Template

```markdown
---
name: your-skill-name
description: "Clear description of when Codex should use this skill. Include trigger phrases."
---

# Your Skill Name

> Brief one-line description.

## When to Use

**Trigger phrases:**
- "keyword1"
- "keyword2"
- "中文触发词"

## Workflow

Step-by-step instructions...

## Examples

Example usage...
```

### agents/openai.yaml Template

```yaml
interface:
  display_name: "Your Skill Display Name"
  short_description: "25-64 char description for Codex UI."
  default_prompt: "Use $your-skill-name to..."

policy:
  allow_implicit_invocation: true
```

## Validation

All skills must pass:

```bash
pip install PyYAML
python scripts/validate_skills.py
```

Checks include:
- YAML frontmatter format
- Skill directory name matches frontmatter `name`
- `agents/openai.yaml` has required fields
- `default_prompt` references correct `$skill-name`

## Platform Files

When adding a new skill, also create:

1. **Cursor rules**: `cursor-rules/your-skill-name.mdc`
2. **Gemini rules**: `gemini-rules/your-skill-name.md`
3. **Gemini command**: `gemini-rules/commands/your-skill-name.toml`
4. **Update**: `README.md`, `AGENTS.md`, `CHANGELOG.md`

## Code Style

- Follow existing patterns
- Use clear, concise language
- Include examples for all workflows
- Support English, Chinese, and Japanese where possible

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
