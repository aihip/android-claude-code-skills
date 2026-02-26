# Android Claude Code Skills

## 项目概述

这是一个 Android 开发技能插件仓库，用于 Claude Code。包含可自定义的 Android 开发技能集合。

## 仓库信息

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **许可证**: MIT

## 技能说明

所有技能位于 `skills/` 目录下，每个技能是一个包含 `SKILL.md` 的子目录。

## 添加新技能

在 `skills/` 目录创建新子目录并添加 `SKILL.md` 文件：

```
skills/your-skill-name/SKILL.md
```

### SKILL.md 模板

```markdown
# 技能名称

> 技能描述

## 何时使用

**触发短语：**
- "关键词1"
- "关键词2"

## 内容

你的技能内容...
```

## 常用命令

```bash
# 安装插件
/plugin marketplace add aihip/android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# 更新插件
/plugin update android-claude-code-skills
```

## 项目结构

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # 插件清单
│   └── marketplace.json    # 市场配置
├── skills/                 # 技能目录
│   └── template/
│       └── SKILL.md        # 技能模板
├── CLAUDE.md               # 本文件（英文版）
├── CLAUDE_CN.md            # 项目概述（中文版）
├── README.md               # Documentation (English)
└── README_CN.md            # 说明文档（中文）
```
