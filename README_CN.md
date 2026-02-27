# Android Claude Code Skills

> 面向 Android 开发场景的可复用 Skills 仓库，兼容 **Claude Code**、**OpenAI Codex**、**Gemini CLI** 与 **Cursor**。

## 目录

- [仓库信息](#仓库信息)
- [OpenAI Codex 兼容性](#openai-codex-兼容性)
- [安装](#安装)
- [更新插件](#更新插件)
- [可用技能](#可用技能)
  - [Android 多语言翻译同步](#android-多语言翻译同步)
  - [Android 代码变更审查](#android-代码变更审查android-change-review)
  - [APK 分析器](#apk-分析器)
- [第三方技能](#第三方技能)
  - [review-loop — 自动化代码审查循环](#review-loop--自动化代码审查循环)
  - [claude-codex — 多 AI 编排流水线](#claude-codex--多-ai-编排流水线)
- [在 Codex CLI 中使用技能](#在-codex-cli-中使用技能)
- [在 Cursor 中使用技能](#在-cursor-中使用技能)
- [在 Gemini CLI 中使用技能](#在-gemini-cli-中使用技能)
- [添加技能](#添加技能)
- [校验](#校验)
- [项目结构](#项目结构)
- [贡献](#贡献)
- [许可证](#许可证)

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT
- **当前版本**: 1.6.0
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

### APK 分析器

解析 Android APK 文件：提取元数据、按风险等级分类权限、验证签名、检查导出组件、检测原生库和第三方 SDK，并生成安全审计报告。

**使用方法：**

```
请帮我分析这个 APK：/path/to/your.apk
```

**功能特性：**
- 通过 `aapt` 提取包名、版本号/名称、Min/Target SDK
- 将所有权限分为危险权限 / 高风险权限 / 普通权限三档并标注
- 验证 V1/V2/V3 签名方案，输出证书主体、SHA-256 指纹和有效期；自动检测调试密钥库
- 通过 `apktool` 解码 `AndroidManifest.xml`，识别缺少 `android:permission` 保护的导出组件
- 检查安全标志：`debuggable`、`allowBackup`、明文流量
- 列出原生库 ABI 并检测第三方 SDK（Firebase、Flutter、React Native 等）
- 扫描字符串资源中的硬编码密钥
- 提供完整的 `apk-analyze.sh` 脚本和 Python (androguard) 分析路径
- 生成包含 CRITICAL / HIGH / MEDIUM / INFO 级别的结构化安全报告

**触发词：**
- `analyze apk`
- `check apk permissions`
- `verify apk signature`
- `audit apk security`
- `apk信息提取`
- `apk权限分析`
- `apk签名检查`
- `apk安全审计`

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

### claude-codex — 多 AI 编排流水线

> **来源**: [Z-M-Huang/claude-codex](https://github.com/Z-M-Huang/claude-codex)
> **注意**: 本项目已迁移至 [Z-M-Huang/vcp](https://github.com/Z-M-Huang/vcp/plugins/dev-buddy)，后续开发在新仓库继续。

一个 Claude Code 插件，提供**多 AI 编排流水线**，让代码在被接受前经过三个独立审查者——Claude Sonnet、Claude Opus 和 Codex——的逐层把关。基于"没有代码应该只经过一个人审查就上线"的专业开发原则。

**为什么需要多 AI 审查？**

| 审查者 | 擅长发现 |
|---|---|
| Claude Sonnet | 明显 Bug、基础安全问题、代码风格 |
| Claude Opus | 架构问题、隐性 Bug、边界用例 |
| Codex | 来自不同 AI 模型的全新视角 |

每位审查者都会检查 OWASP Top 10 漏洞、错误处理规范和代码质量。循环审查机制确保代码在三个审查者全部通过前不会进入下一阶段。

**可用技能：**

| 技能 | 用途 |
|---|---|
| `multi-ai` | 完整功能开发流水线（需求 → 规划 → 实现 → 审查） |
| `bug-fix` | Bug 修复流水线（双路根因分析 + Codex 验证 + 精准修复） |

**内置自定义 Agent：**

| Agent | 模型 | 职责 |
|---|---|---|
| `requirements-gatherer` | Opus | 业务分析师 + PM 混合角色 |
| `planner` | Opus | 架构师 + 全栈混合角色 |
| `plan-reviewer` | Sonnet + Opus | 架构、安全与 QA 验证 |
| `implementer` | Sonnet | 全栈 + TDD + 质量实现 |
| `code-reviewer` | Sonnet + Opus | 安全、性能与 QA 验证 |
| `root-cause-analyst` | Sonnet + Opus | 并行 Bug 根因分析（bug-fix 流水线） |

**环境要求：**

- Claude Code CLI
- Codex CLI — `npm install -g @openai/codex`
- Bun（用于跨平台 JSON 处理，替代 `jq`）

**安装方法：**

```bash
# 第一步：添加市场
/plugin marketplace add Z-M-Huang/claude-codex

# 第二步：安装插件（user 范围——所有项目均可用，推荐）
/plugin install claude-codex@claude-codex --scope user

# 第三步：将 .task 加入 .gitignore
echo ".task" >> .gitignore
```

**使用方法：**

```text
# 功能开发流水线
/claude-codex:multi-ai 添加带 JWT 令牌的用户认证功能

# Bug 修复流水线
/claude-codex:bug-fix 登录时 session token 过期后静默失败
```

> 从外部项目调用时，必须使用完整命名空间 `claude-codex:<skill>`。也可以自然语言描述任务，Claude 会自动调用对应技能。

**`/multi-ai` 流水线流程：**

1. **需求收集** — 多个专家 Agent 并行探索，`requirements-gatherer` 汇总整合
2. **规划** — `planner` Agent 制定实现方案
3. **方案审查** — `plan-reviewer`（Sonnet + Opus）+ Codex 闸门
4. **实现** — `implementer` 循环迭代直到测试通过
5. **代码审查** — `code-reviewer`（Sonnet + Opus）+ Codex 最终闸门
6. **完成** — 输出报告

**`/bug-fix` 流水线流程：**

1. **双路根因分析** — 两个 `root-cause-analyst`（Sonnet + Opus）并行分析
2. **整合** — Orchestrator 综合两份分析，制定修复方案
3. **Codex 验证** — Codex 审查整合后的根因分析与修复方案
4. **实现** — 针对根因的最小化精准修复
5. **代码审查** — `code-reviewer`（Sonnet + Opus）+ Codex 闸门

**流水线任务依赖强制执行：**

```
1. 实现  →  2. 审查（Sonnet）  →  3. 审查（Opus）  →  4. 审查（Codex）
                  ↓ needs_changes?
             创建修复任务 → 同一审查者重新验证 → 继续
```

**默认限制：**

| 配置项 | 默认值 |
|---|---|
| 方案审查循环上限 | 10 次 |
| 代码审查循环上限 | 15 次 |
| 自动重试次数 | 3 次 |

**许可证：** GPL-3.0，需注明来源（作者：Z-M-Huang）。

---

## 在 Codex CLI 中使用技能

本仓库的技能与 **OpenAI Codex CLI 原生兼容** —— `SKILL.md` 文件已包含必要的 YAML frontmatter（`name`、`description`），每个技能也有对应的 `agents/openai.yaml` UI 元数据。

### 安装

Codex 从 `.agents/skills/` 目录发现技能，将技能复制到用户级或项目级：

```bash
# 用户级安装 —— 所有项目均可用（推荐）
mkdir -p ~/.agents/skills
cp -r skills/android-translation-sync ~/.agents/skills/
cp -r skills/android-change-review ~/.agents/skills/
cp -r skills/apk-analyzer ~/.agents/skills/
```

```bash
# 项目级安装 —— 仅当前项目可用
mkdir -p .agents/skills
cp -r skills/android-translation-sync .agents/skills/
cp -r skills/android-change-review .agents/skills/
cp -r skills/apk-analyzer .agents/skills/
```

或使用符号链接，自动跟随仓库更新：

```bash
ln -s "$(pwd)/skills/android-translation-sync" ~/.agents/skills/
ln -s "$(pwd)/skills/android-change-review" ~/.agents/skills/
ln -s "$(pwd)/skills/apk-analyzer" ~/.agents/skills/
```

### 使用方法

**显式调用**（输入 `$` 打开技能选择器）：

```text
$android-translation-sync  ./translations/strings.xlsx

$android-change-review  review my staged changes

$apk-analyzer  ./build/outputs/apk/release/app-release.apk
```

**隐式调用** —— Codex 根据描述自动匹配技能（`allow_implicit_invocation: true`）：

```text
请帮我同步多语言翻译，Excel 文件是 ./translations/strings.xlsx

帮我检查当前已暂存的代码，重点看 Android 崩溃风险和边界条件。

帮我分析这个 APK 的权限和安全问题：./app-release.apk
```

### 验证安装

```bash
# 在 Codex CLI 会话中执行
/skills
# 应看到：android-translation-sync、android-change-review、apk-analyzer
```

---

## 在 Cursor 中使用技能

预转换好的 `.mdc` 规则文件位于 [`cursor-rules/`](cursor-rules/) 目录。

### 安装

```bash
mkdir -p .cursor/rules
cp android-claude-code-skills/cursor-rules/*.mdc .cursor/rules/
```

或通过 curl 下载：

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/android-translation-sync.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-translation-sync.mdc
curl -o .cursor/rules/android-change-review.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-change-review.mdc
curl -o .cursor/rules/apk-analyzer.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/apk-analyzer.mdc
```

### 使用方法

所有规则均为 **Agent-requested** 类型，Cursor AI 会根据请求自动激活：

```text
请帮我同步多语言翻译，Excel 文件是 ./translations/strings.xlsx

帮我检查已暂存的代码，重点看 Android 崩溃风险和边界条件。

帮我分析这个 APK 的权限和安全问题：./build/outputs/apk/release/app-release.apk
```

---

## 在 Gemini CLI 中使用技能

预转换好的文件位于 [`gemini-rules/`](gemini-rules/) 目录，提供两种接入方式。

### 方式一：GEMINI.md 注入（推荐）

```bash
mkdir -p .gemini/skills
cp android-claude-code-skills/gemini-rules/*.md .gemini/skills/

# 在 GEMINI.md 中添加引用
cat >> GEMINI.md << 'EOF'
@.gemini/skills/android-translation-sync.md
@.gemini/skills/android-change-review.md
@.gemini/skills/apk-analyzer.md
EOF
```

添加后，自然语言描述任务即可：

```text
请帮我同步多语言翻译，Excel 文件是 ./translations/strings.xlsx

帮我检查已暂存代码的崩溃风险。

帮我分析这个 APK：./build/outputs/apk/release/app-release.apk
```

### 方式二：自定义 Slash 命令

```bash
# 全局安装（所有项目可用）
mkdir -p ~/.gemini/commands
cp android-claude-code-skills/gemini-rules/commands/*.toml ~/.gemini/commands/
```

```text
/translation-sync ./translations/strings.xlsx
/change-review staged
/apk-analyzer ./build/outputs/apk/release/app-release.apk
```

### 四端能力对比

| 功能 | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---|---|---|---|---|
| 工作流知识 | ✅ 完整 | ✅ 完整 | ✅ 完整 | ✅ 完整 |
| 技能格式 | SKILL.md | SKILL.md（原生）| GEMINI.md / `.md` | `.mdc` rules |
| 技能触发 | `/plugin` + slash | `$skill-name` 或自动 | 自然语言 | 自然语言 |
| 自动识别描述 | ✅ | ✅（`allow_implicit_invocation`）| ✅ | ✅ |
| 上下文文件 | CLAUDE.md | AGENTS.md | GEMINI.md | `.cursor/rules/` |
| Stop Hook / 生命周期钩子 | ✅ | ❌ | ❌ | ❌ |
| 多 Agent 编排 | ✅ | ❌ | ❌ | ❌ |

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
│   ├── android-change-review/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── apk-analyzer/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # 兼容 Codex 的技能模板
│       └── agents/openai.yaml
├── CLAUDE.md               # Project overview (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # プロジェクト概要（日本語）
├── README.md               # Documentation (English)
├── README_CN.md            # 说明文档（中文）
├── README_JP.md            # ドキュメント（日本語）
├── CHANGELOG.md            # Changelog (English)
└── CHANGELOG_JP.md         # 変更履歴（日本語）
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT License
