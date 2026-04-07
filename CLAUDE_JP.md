# Android Claude Code Skills

## プロジェクト概要

これは OpenAI Codex と Claude Code に対応した、再利用可能な Android 開発スキルのリポジトリです。Claude プラグインのレイアウトを保持しつつ、スキルファイルを Codex 互換の形式で管理します。

## リポジトリ情報

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **ライセンス**: MIT

## スキルの説明

すべてのスキルは `skills/` ディレクトリに格納されています。各スキルは `SKILL.md` ファイルを含むサブディレクトリです。Codex 互換性のため、`SKILL.md` は YAML frontmatter（`name`、`description`）で始まる必要があり、UI メタデータ用に `agents/openai.yaml` の追加を推奨します。

## よく使うコマンド

```bash
# プラグインをインストール
/plugin marketplace add aihip/android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills

# プラグインを更新（必須の方法）
/plugin marketplace update aihip/android-claude-code-skills
/plugin update android-claude-code-skills

# プラグインを再インストール
/plugin uninstall android-claude-code-skills
/plugin install android-claude-code-skills@android-claude-code-skills
```

**注意:** 最新バージョンを取得するには、必ず先に `marketplace update` を実行してから `plugin update` を行ってください。

## 新しいスキルの追加

`skills/` ディレクトリに新しいサブディレクトリを作成し、`SKILL.md` ファイルを追加します（Codex UI 向けにオプションで `agents/openai.yaml` も追加）：

```
skills/your-skill-name/SKILL.md
```

### SKILL.md テンプレート

```markdown
---
name: your-skill-name
description: "スキルの内容と Codex がいつ使用すべきかを説明します。"
---

# スキル名

> スキルの説明

## 使用場面

**トリガーフレーズ：**
- "キーワード1"
- "キーワード2"

## 内容

スキルの内容をここに記述...
```

## プロジェクト構成

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # プラグインマニフェスト
│   └── marketplace.json    # マーケットプレイス設定
├── skills/                 # スキルディレクトリ
│   ├── figma-to-android/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # Codex 互換スキルテンプレート
│       └── agents/openai.yaml
├── AGENTS.md               # エージェント指示（OpenAI Codex）
├── CLAUDE.md               # プロジェクト概要（英語）
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # このファイル（日本語）
├── README.md               # ドキュメント（英語）
├── README_CN.md            # 说明文档（中文）
└── README_JP.md            # ドキュメント（日本語）
```
