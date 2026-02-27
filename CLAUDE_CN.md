# Android Claude Code Skills

## 项目概述

这是一个面向 Android 开发场景的可复用技能仓库，兼容 OpenAI Codex 与 Claude Code。它保留 Claude 插件结构，同时提供兼容 Codex 的技能文件格式。

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT

## 技能说明

所有技能位于 `skills/` 目录下，每个技能是一个包含 `SKILL.md` 的子目录。为兼容 Codex，`SKILL.md` 需要以 YAML frontmatter（`name`、`description`）开头，并建议添加 `agents/openai.yaml` 作为 UI 元数据。

## 常用命令

```bash
# 安装插件
/plugin marketplace add aihip/android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# 更新插件（必需的方法）
/plugin marketplace update aihip/android-claude-code-skills
/plugin update android-claude-code-skills

# 重新安装插件
/plugin uninstall android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills
```

**注意：** 务必先使用 `marketplace update`，然后再 `plugin update` 才能获取最新版本。

## 添加新技能

在 `skills/` 目录创建新子目录并添加 `SKILL.md` 文件（Codex UI 可再加 `agents/openai.yaml`）：

```
skills/your-skill-name/SKILL.md
```

### SKILL.md 模板

```markdown
---
name: your-skill-name
description: 描述技能的作用以及 Codex 应在何种场景触发它。
---

# 技能名称

> 技能描述

## 何时使用

**触发短语：**
- "关键词1"
- "关键词2"

## 内容

你的技能内容...
```

## 项目结构

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # 插件清单
│   └── marketplace.json    # 市场配置
├── skills/                 # 技能目录
│   └── template/
│       ├── SKILL.md        # 兼容 Codex 的技能模板
│       └── agents/openai.yaml
├── CLAUDE.md               # 本文件（英文版）
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # プロジェクト概要（日本語）
├── README.md               # Documentation (English)
├── README_CN.md            # 说明文档（中文）
├── README_JP.md            # ドキュメント（日本語）
├── CHANGELOG.md            # Changelog (English)
└── CHANGELOG_JP.md         # 変更履歴（日本語）
```
