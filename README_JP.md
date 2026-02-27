# Android Claude Code Skills

> OpenAI Codex と Claude Code に対応した、再利用可能な Android 開発スキルのリポジトリ。

## 目次

- [リポジトリ情報](#リポジトリ情報)
- [OpenAI Codex 互換性](#openai-codex-互換性)
- [インストール](#インストール)
- [プラグインの更新](#プラグインの更新)
- [利用可能なスキル](#利用可能なスキル)
  - [Android 多言語翻訳同期](#android-多言語翻訳同期)
  - [Android コード変更レビュー](#android-コード変更レビュー)
- [サードパーティスキル](#サードパーティスキル)
  - [review-loop — 自動コードレビューループ](#review-loop--自動コードレビューループ)
- [スキルの追加](#スキルの追加)
- [バリデーション](#バリデーション)
- [プロジェクト構成](#プロジェクト構成)
- [コントリビューション](#コントリビューション)
- [ライセンス](#ライセンス)

## リポジトリ情報

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **ライセンス**: MIT
- **現在のバージョン**: 1.4.0
- **変更履歴**: [CHANGELOG.md](CHANGELOG.md)

## OpenAI Codex 互換性

本プロジェクトは主に Android 開発スキルを提供しており、スキルファイルは OpenAI Codex と Claude Code の両方に対応した形式で管理されています：

- `skills/<skill-name>/SKILL.md` に `name` と `description` の YAML frontmatter を含む
- オプションで `skills/<skill-name>/agents/openai.yaml` により Codex UI メタデータを提供
- 既存の Claude プラグイン構成 (`.claude-plugin/`) を保持し、二重互換性を実現

## インストール

```bash
# マーケットプレイスにリポジトリを追加
/plugin marketplace add aihip/android-claude-code-skills

# プラグインをインストール
/plugin install android-claude-code-skills@android-claude-code-skills
```

## プラグインの更新

**重要: 更新はこの方法のみ有効です：**

```bash
# ステップ 1: マーケットプレイスを更新
/plugin marketplace update aihip/android-claude-code-skills

# ステップ 2: プラグインを更新
/plugin update android-claude-code-skills
```

**注意:** 他の更新方法では最新バージョンが取得できない場合があります。必ず先に `marketplace update` を実行してください。

### 更新される内容

プラグインを更新すると以下が反映されます：
- リポジトリに追加された新しいスキル
- 既存スキルの改善
- バグ修正と機能強化

### 更新の確認

更新後、バージョンを確認します：

```bash
# インストール済みプラグインとバージョンを確認
/plugin list

# 以下のように表示されるはずです：
# android-claude-code-skills  v1.4.0
```

GitHub 上の最新バージョンと比較: https://github.com/aihip/android-claude-code-skills/blob/main/.claude-plugin/plugin.json

## 利用可能なスキル

### Android 多言語翻訳同期

Excel スプレッドシートから Android プロジェクトの多言語リソースを同期します。

**使い方：**

```
Please sync translations from excel: /path/to/translations.xlsx
```

**機能：**
- 翻訳を含む Excel ファイルを読み込む（英語 + その他の言語）
- 英語テキストをもとに一意のキーを生成（10〜20 文字）
- strings.xml の既存キーとの競合を回避
- 全言語ファイルを更新（values、values-zh、values-es など）
- 新規エントリは末尾に追加、既存キーは更新

**使用例：**

```
あなた：多言語翻訳を同期してください。Excel ファイルは ./translations/strings.xlsx です。

Claude：承知しました。処理を開始します...
- Excel ファイルを読み込み中...
- 既存の strings.xml を確認中...
- 新しいキーを生成中...
- 全言語ファイルを更新中...
```

**トリガーフレーズ：**
- `sync translations from excel`
- `update android strings from excel`
- `多言語翻訳同期`
- `更新strings.xml`

---

### Android コード変更レビュー

コーディング後に Android のコード変更をレビューし、クラッシュリスク、境界条件のバグ、リグレッションを検出します。

**使い方（ステージされた変更）：**

```bash
git add .
```

その後、以下のように依頼します：

```text
Review my staged changes for crash risks and boundary conditions.
```

**使い方（特定のコミット）：**

```text
Please review commit abc1234 for crash risks and regressions.
```

**機能：**
- `git add .` 後のステージされた変更をレビュー（`git diff --cached`）
- 特定のコミットをレビュー（`git show <commit-id>`）
- クラッシュパス、境界条件、リグレッションに重点を置く
- Android 特有のチェック（ライフサイクル、null 安全性、スレッド、パーミッションゲート）
- ファイル/行番号を含む、問題優先の出力形式

**トリガーフレーズ：**
- `review staged changes`
- `review commit-id`
- `code review after coding`
- `検査当前修改代码`
- `边界条件检查`
- `崩溃风险检查`

---

## サードパーティスキル

Claude Code にさらなるワークフローを追加するコミュニティ管理のプラグイン。

---

### review-loop — 自動コードレビューループ

> **ソース**: [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop)

すべてのタスクに自動化された 2 フェーズのコードレビューループを追加する Claude Code プラグイン。Claude がタスクの実装を完了すると、Stop Hook が自動的に独立した Codex レビューをトリガーし、その後 Claude にフィードバックへの対応を依頼します。変更を受け入れる前に、必ずセカンドオピニオンが得られます。

**仕組み：**

1. **タスクフェーズ** — タスクを説明すると、Claude が実装します。
2. **レビューフェーズ** — Claude が完了すると、Stop Hook が Codex（`codex exec`）を実行して独立したレビューを行い、結果を `reviews/review-<id>.md` に書き込み、Claude にフィードバックへの対応を依頼します。
3. Claude は同意した項目を修正し、正常に終了します。

状態は `.claude/review-loop.local.md` で追跡されます（`.gitignore` への追加を推奨）。

**レビュー対象：**

| 領域 | チェック内容 |
|---|---|
| コード品質 | 構成、モジュール性、DRY 原則、命名規則 |
| テストカバレッジ | 新規テスト、エッジケース、テスト品質 |
| セキュリティ | 入力バリデーション、インジェクション、シークレット、OWASP Top 10 |
| ドキュメント & エージェント | AGENTS.md、CLAUDE.md シンボリックリンク、テレメトリ、型システム |
| UX & デザイン | E2E テスト、視覚的品質、アクセシビリティ（UI プロジェクト） |

**必要条件：**

- Claude Code CLI
- `jq` — `brew install jq`（macOS）/ `apt install jq`（Linux）
- Codex CLI（推奨。未インストール時は Claude による自己レビューにフォールバック）— `npm install -g @openai/codex`

**インストール：**

```bash
# Claude Code セッション内から
/plugin marketplace add hamelsmu/claude-review-loop
/plugin install review-loop@hamel-review
```

または CLI から直接：

```bash
claude plugin marketplace add hamelsmu/claude-review-loop
claude plugin install review-loop@hamel-review
```

**使い方：**

```text
# レビューループ付きでタスクを開始
/review-loop JWT トークンとテストカバレッジを含むユーザー認証を追加する

# 進行中のレビューループをキャンセル
/cancel-review
```

**設定：**

| 環境変数 | デフォルト値 | 説明 |
|---|---|---|
| `REVIEW_LOOP_CODEX_FLAGS` | `--dangerously-bypass-approvals-and-sandbox` | `codex` に渡すフラグ。より安全なサンドボックスレビューには `--sandbox workspace-write` を使用。 |

Stop Hook のタイムアウトはデフォルト 900 秒（15 分）です。レビューに時間がかかる場合は `hooks/hooks.json` で調整してください。

**ログ:** タイムスタンプ、Codex 終了コード、経過時間を含む実行ログは `.claude/review-loop.log` に書き込まれます（gitignore 済み）。

---

## スキルの追加

`skills/` ディレクトリにスキルを作成します：

```
skills/
└── your-skill-name/
    ├── SKILL.md
    └── agents/
        └── openai.yaml   # オプション（Codex UI 向けに推奨）
```

各スキルには以下を含む `SKILL.md` ファイルが必要です：

- **YAML frontmatter** - `name` と `description`（Codex スキルトリガーに必須）
- **説明本文** - スキルのワークフロー、ルール、再利用可能な知識
- **オプションのエージェントメタデータ** - Codex UI の表示名/説明/プロンプト用 `agents/openai.yaml`

最小限の `SKILL.md` の例：

```markdown
---
name: your-skill-name
description: スキルの内容と使用場面を説明し、Codex が正しくトリガーできるようにします。
---

# スキル名

スキルの説明...
```

## バリデーション

ローカルバリデーション（Codex 互換の `SKILL.md` + `agents/openai.yaml`）：

```bash
python3 -m pip install --user PyYAML
python3 scripts/validate_skills.py
```

Pre-commit フック（コミット前に自動でバリデーションを実行）：

```bash
python3 -m pip install --user pre-commit
pre-commit install
pre-commit run --all-files
```

このリポジトリには `.github/workflows/validate-skills.yml` に GitHub Actions CI も含まれており、push / pull request 時に同じチェックが自動実行されます。

## プロジェクト構成

```
android-claude-code-skills/
├── .claude-plugin/
│   ├── plugin.json         # プラグインマニフェスト
│   └── marketplace.json    # マーケットプレイス設定
├── skills/                 # 利用可能なスキル
│   ├── android-translation-sync/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── template/
│       ├── SKILL.md        # Codex 互換スキルテンプレート
│       └── agents/openai.yaml
├── CLAUDE.md               # プロジェクト概要（英語）
├── CLAUDE_CN.md            # 项目概述（中文）
├── CLAUDE_JP.md            # プロジェクト概要（日本語）
├── README.md               # ドキュメント（英語）
├── README_CN.md            # 说明文档（中文）
└── README_JP.md            # このファイル（日本語）
```

## コントリビューション

コントリビューションを歓迎します！お気軽に Pull Request をお送りください。

## ライセンス

MIT License
