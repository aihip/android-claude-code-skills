# Android Claude Code Skills

> 面向 Android 开发场景的可复用 Skills 仓库，兼容 OpenAI Codex 与 Claude Code。

## 目录

- [仓库信息](#仓库信息)
- [OpenAI Codex 兼容性](#openai-codex-兼容性)
- [安装](#安装)
- [更新插件](#更新插件)
- [可用技能](#可用技能)
  - [Android 多语言翻译同步](#android-多语言翻译同步)
  - [Android 代码变更审查](#android-代码变更审查android-change-review)
- [第三方技能](#第三方技能)
  - [review-loop — 自动化代码审查循环](#review-loop--自动化代码审查循环)
- [添加技能](#添加技能)
- [校验](#校验)
- [项目结构](#项目结构)
- [贡献](#贡献)
- [许可证](#许可证)

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT
- **当前版本**: 1.4.0
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
# android-claude-code-skills  v1.4.0
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

### Android 代码变更审查（Android Change Review）

在代码写完后，对 Android 代码变更做风险审查，重点检查崩溃风险、边界条件问题和回归风险。

**用法（检查当前已暂存修改）**

```bash
git add .
```

然后提问：

```text
请检查我当前修改代码（已 git add .），重点看边界条件和会不会 crash。
```

**用法（检查指定 commit-id）**

```text
请检查 commit abc1234，看看会不会导致新的 crash 或回归。
```

**功能特性：**
- 审查 `git add .` 后的暂存代码（`git diff --cached`）
- 审查指定 `commit-id`（`git show <commit-id>`）
- 聚焦崩溃路径、边界条件和行为回归
- Android 重点检查（生命周期、空指针、线程、权限闸门）
- 按严重度输出问题，并附文件/行号定位

**触发词：**
- `review staged changes`
- `review commit-id`
- `code review after coding`
- `检查当前修改代码`
- `边界条件检查`
- `崩溃风险检查`

---

## 第三方技能

社区维护的插件，为 Claude Code 扩展额外的工作流能力。

---

### review-loop — 自动化代码审查循环

> **来源**: [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop)

一个 Claude Code 插件，为每次任务引入自动化的两阶段代码审查循环。Claude 完成任务实现后，Stop Hook 会自动触发独立的 Codex 审查，并要求 Claude 处理反馈意见——让每次改动在接受前都获得第二视角的把关。

**工作原理：**

1. **任务阶段** — 你描述任务，Claude 实现代码。
2. **审查阶段** — Claude 完成后，Stop Hook 自动运行 Codex（`codex exec`）进行独立审查，将发现的问题写入 `reviews/review-<id>.md`，再要求 Claude 逐条处理。
3. Claude 处理认可的问题后正常退出。

状态记录在 `.claude/review-loop.local.md`（建议加入 `.gitignore`）。

**审查覆盖范围：**

| 维度 | 检查内容 |
|---|---|
| 代码质量 | 结构组织、模块化、DRY 原则、命名规范 |
| 测试覆盖 | 新增测试、边界用例、测试质量 |
| 安全性 | 输入校验、注入漏洞、密钥泄露、OWASP Top 10 |
| 文档与 Agent 规范 | AGENTS.md、CLAUDE.md 符号链接、遥测、类型系统 |
| UX 与设计 | E2E 测试、视觉质量、无障碍访问（UI 项目适用） |

**环境要求：**

- Claude Code CLI
- `jq` — `brew install jq`（macOS）/ `apt install jq`（Linux）
- Codex CLI（推荐，未安装时自动回退到 Claude 自审）— `npm install -g @openai/codex`

**安装方法：**

```bash
# 在 Claude Code 会话中执行
/plugin marketplace add hamelsmu/claude-review-loop
/plugin install review-loop@hamel-review
```

或直接通过 CLI 执行：

```bash
claude plugin marketplace add hamelsmu/claude-review-loop
claude plugin install review-loop@hamel-review
```

**使用方法：**

```text
# 启动一个带审查循环的任务
/review-loop 添加带测试覆盖的 JWT 用户认证功能

# 取消正在进行的审查循环
/cancel-review
```

**配置项：**

| 环境变量 | 默认值 | 说明 |
|---|---|---|
| `REVIEW_LOOP_CODEX_FLAGS` | `--dangerously-bypass-approvals-and-sandbox` | 传给 `codex` 的参数。可改为 `--sandbox workspace-write` 以启用更安全的沙箱审查。 |

Stop Hook 超时默认为 900 秒（15 分钟），可在 `hooks/hooks.json` 中调整。

**日志：** 执行日志（含时间戳、Codex 退出码、耗时）写入 `.claude/review-loop.log`（已 gitignore）。

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
