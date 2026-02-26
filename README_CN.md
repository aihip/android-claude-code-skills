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
    └── SKILL.md
```

每个技能需要一个 `SKILL.md` 文件，包含以下内容：

- **触发短语** - 激活该技能的关键词
- **何时使用** - 指导何时应用该技能
- **内容** - 实际的知识/模式

## 项目结构

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # 插件清单
│   └── marketplace.json    # 市场配置
├── skills/                 # 可用技能
│   ├── android-translation-sync/
│   │   └── SKILL.md
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
