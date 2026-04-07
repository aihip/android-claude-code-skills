# 贡献指南

感谢您对本项目的兴趣！我们欢迎各种类型的贡献。

## 如何贡献

### 报告 Bug

发现了 Bug？请提交 Issue，包含：
- 清晰的标题和描述
- 复现步骤
- 预期行为 vs 实际行为
- 环境详情（操作系统、AI 平台等）

### 建议新技能

有新技能的想法？请提交 Issue 或 PR，包含：
- 技能名称和描述
- 用例和触发短语
- 预期的工作流程/行为

### 提交代码更改

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-skill`)
3. 按照技能模板结构
4. 运行验证：`python scripts/validate_skills.py`
5. 提交更改 (`git commit -m 'feat: add amazing skill'`)
6. 推送到分支 (`git push origin feature/amazing-skill`)
7. 创建 Pull Request

## 技能结构

```
skills/your-skill-name/
├── SKILL.md              # 主要技能文档（包含 YAML frontmatter）
└── agents/
    └── openai.yaml       # Codex UI 元数据（可选但推荐）
```

### SKILL.md 模板

```markdown
---
name: your-skill-name
description: "清晰描述 Codex 何时应使用此技能。包含触发短语。"
---

# 技能名称

> 简洁的一句话描述。

## 使用时机

**触发短语：**
- "关键词1"
- "关键词2"
- "中文触发词"

## 工作流程

分步说明...

## 示例

使用示例...
```

### agents/openai.yaml 模板

```yaml
interface:
  display_name: "技能显示名称"
  short_description: "25-64 字符的 Codex UI 描述。"
  default_prompt: "Use $your-skill-name to..."

policy:
  allow_implicit_invocation: true
```

## 验证

所有技能必须通过：

```bash
pip install PyYAML
python scripts/validate_skills.py
```

检查内容包括：
- YAML frontmatter 格式
- 技能目录名称与 frontmatter `name` 匹配
- `agents/openai.yaml` 包含必需字段
- `default_prompt` 引用正确的 `$skill-name`

## 平台文件

添加新技能时，还需创建：

1. **Cursor 规则**: `cursor-rules/your-skill-name.mdc`
2. **Gemini 规则**: `gemini-rules/your-skill-name.md`
3. **Gemini 命令**: `gemini-rules/commands/your-skill-name.toml`
4. **更新**: `README.md`、`AGENTS.md`、`CHANGELOG.md`

## 代码风格

- 遵循现有模式
- 使用清晰简洁的语言
- 为所有工作流程包含示例
- 尽可能支持英文、中文和日文

## 许可证

通过贡献，您同意您的贡献将在 MIT 许可证下授权。
