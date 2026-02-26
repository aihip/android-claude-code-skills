# Android Claude Code Skills

> 面向 Android 开发场景的可复用 Skills 仓库，兼容 OpenAI Codex 与 Claude Code。

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT
- **当前版本**: 1.3.0
- **更新日志**: [CHANGELOG.md](CHANGELOG.md)

## OpenAI Codex 兼容性

本项目主要提供 Android 开发相关 skills，并将技能文件维护为同时兼容 OpenAI Codex 与 Claude Code 的格式：

- `skills/<skill-name>/SKILL.md` 包含 YAML frontmatter（`name` 和 `description`）
- 可选 `skills/<skill-name>/agents/openai.yaml`，用于 Codex UI 元数据
- 同时保留现有 Claude 插件结构（`.claude-plugin/`），实现双兼容

## 安装

```bash
# 添加此仓库作为市场
/plugin marketplace add aihip/android-claude-code-skills

# 安装插件
/plugin install android-claude-code-skills@android-claude-code-skills
```

## 更新插件

**重要：只有以下方法才能成功更新：**

```bash
# 步骤 1：更新市场
/plugin marketplace update aihip/android-claude-code-skills

# 步骤 2：更新插件
/plugin update android-claude-code-skills
```

**注意：** 其他更新方法可能无法获取最新版本。请务必先使用 `marketplace update`。

### 更新内容包括

更新插件后，您将获得：
- 仓库中新增的技能
- 现有技能的改进
- Bug 修复和功能增强

### 验证更新成功

更新后，检查版本号：

```bash
# 查看已安装的插件和版本
/plugin list

# 您应该看到：
# android-claude-code-skills  v1.3.0
```

与 GitHub 上的最新版本对比：https://github.com/aihip/android-claude-code-skills/blob/main/.claude-plugin/plugin.json

## 可用技能

### Android 多语言翻译同步

从 Excel 表格同步 Android 项目多语言资源到 strings.xml。

**使用方法：**

```
请帮我同步多语言翻译，Excel 文件是：/path/to/translations.xlsx
```

**功能特性：**
- 读取 Excel 表格（英文 + 其他语言）
- 根据英文生成唯一 key（10-20 字符）
- 避免与 strings.xml 中现有 key 冲突
- 更新所有语言文件（values、values-zh、values-es 等）
- 新增内容添加到底部，已存在的 key 则更新

**使用示例：**

```
你：请帮我同步多语言翻译，Excel 文件是 ./translations/strings.xlsx

Claude：好的，我来处理...
- 正在读取 Excel 文件...
- 正在检查现有 strings.xml...
- 正在生成新的 key...
- 正在更新所有语言文件...
```

**触发词：**
- `sync translations from excel`
- `update android strings from excel`
- `多语言翻译同步`
- `更新strings.xml`

---

## 添加技能

在 `skills/` 目录下创建你的技能：

```
skills/
└── your-skill-name/
    ├── SKILL.md
    └── agents/
        └── openai.yaml   # 可选（推荐，用于 Codex UI）
```

每个技能需要一个 `SKILL.md` 文件，包含以下内容：

- **YAML frontmatter** - `name` 和 `description`（Codex 触发所必需）
- **技能正文** - 工作流程、规则与可复用知识
- **可选元数据** - `agents/openai.yaml`（Codex UI 展示名称/描述/默认提示词）

最小 `SKILL.md` 示例：

```markdown
---
name: your-skill-name
description: 描述技能做什么，以及在什么场景下使用，方便 Codex 正确触发。
---

# 技能名称

技能说明内容...
```

## 校验

本地校验（检查 Codex 兼容的 `SKILL.md` + `agents/openai.yaml`）：

```bash
python3 -m pip install --user PyYAML
python3 scripts/validate_skills.py
```

Pre-commit 钩子（提交前自动执行校验）：

```bash
python3 -m pip install --user pre-commit
pre-commit install
pre-commit run --all-files
```

仓库还提供 GitHub Actions CI：`.github/workflows/validate-skills.yml`，会在 push / pull request 时自动执行同样的校验。

## 项目结构

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # 插件清单
│   └── marketplace.json    # 市场配置
├── skills/                 # 可用技能
│   ├── android-translation-sync/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # 兼容 Codex 的技能模板
│       └── agents/openai.yaml
├── CLAUDE.md               # Project overview (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── README.md               # This file (English)
└── README_CN.md            # 说明文档（中文）
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT License
