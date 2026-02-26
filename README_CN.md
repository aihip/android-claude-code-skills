# Android Claude Code Skills

> Android 开发技能集合 - 用于 Claude Code，可根据需要自定义添加技能。

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT

## 安装

```bash
# 添加此仓库作为市场
/plugin marketplace add aihip/android-claude-code-skills

# 安装插件
/plugin install android-claude-code-skills@android-claude-code-skills
```

## 更新插件

当仓库中有新技能添加时，更新已安装的插件：

```bash
# 方法 1：更新插件（推荐）
/plugin update android-claude-code-skills

# 方法 2：重新安装插件
/plugin uninstall android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# 方法 3：先更新市场，再更新插件
/plugin marketplace update aihip/android-claude-code-skills
/plugin update android-claude-code-skills
```

### 更新内容包括

更新插件后，您将获得：
- 仓库中新增的技能
- 现有技能的改进
- Bug 修复和功能增强

## 添加技能

在 `skills/` 目录下创建你的技能：

```
skills/
└── your-skill-name/
    └── SKILL.md
```

每个技能需要一个 `SKILL.md` 文件，包含以下内容：

- **触发短语** - 激活该技能的关键词
- **何时使用** - 指导何时应用该技能
- **内容** - 实际的知识/模式

## 技能结构示例

```markdown
# 你的技能名称

> 简要描述这个技能的作用。

## 何时使用

**触发短语：**
- "关键词 1"
- "关键词 2"

## 内容

你的技能内容在这里...
```

## 项目结构

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # 插件清单
│   └── marketplace.json    # 市场配置
├── skills/                 # 在这里添加你的技能
│   └── template/
│       └── SKILL.md        # 技能模板
├── CLAUDE.md               # Project overview (English)
├── CLAUDE_CN.md            # 项目概述（中文）
├── README.md               # This file (English)
└── README_CN.md            # 说明文档（中文）
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT License
