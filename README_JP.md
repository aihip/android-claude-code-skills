# Android Claude Code Skills

> **Claude Code**、**OpenAI Codex**、**Gemini CLI**、**Cursor** に対応した、再利用可能な Android 開発スキルのリポジトリ。

## 目次

- [リポジトリ情報](#リポジトリ情報)
- [OpenAI Codex 互換性](#openai-codex-互換性)
- [インストール](#インストール)
- [プラグインの更新](#プラグインの更新)
- [利用可能なスキル](#利用可能なスキル)
  - [Android 多言語翻訳同期](#android-多言語翻訳同期)
  - [Android コード変更レビュー](#android-コード変更レビュー)
  - [APK アナライザー](#apk-アナライザー)
- [サードパーティスキル](#サードパーティスキル)
  - [review-loop — 自動コードレビューループ](#review-loop--自動コードレビューループ)
  - [claude-codex — マルチ AI オーケストレーションパイプライン](#claude-codex--マルチ-ai-オーケストレーションパイプライン)
- [Codex CLI でのスキルの使用](#codex-cli-でのスキルの使用)
- [Cursor でのスキルの使用](#cursor-でのスキルの使用)
- [Gemini CLI でのスキルの使用](#gemini-cli-でのスキルの使用)
- [スキルの追加](#スキルの追加)
- [バリデーション](#バリデーション)
- [プロジェクト構成](#プロジェクト構成)
- [コントリビューション](#コントリビューション)
- [ライセンス](#ライセンス)

## リポジトリ情報

- **GitHub**: https://github.com/aihip/android-claude-code-skills
- **作者**: aihip
- **ライセンス**: MIT
- **現在のバージョン**: 1.6.0
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

### APK アナライザー

Android APK ファイルを解析します：メタデータ抽出、リスクレベル別の権限分類、署名検証、エクスポートされたコンポーネントの検査、ネイティブライブラリ・サードパーティ SDK の検出、セキュリティ監査レポートの生成。

**使い方：**

```
このAPKを解析してください: /path/to/your.apk
```

**機能：**
- `aapt` でパッケージ名・バージョンコード/名・Min/Target SDK を抽出
- 全権限を危険・高リスク・通常の 3 段階に分類して注釈付きで一覧化
- V1/V2/V3 署名スキームを検証し、証明書のサブジェクト・SHA-256 フィンガープリント・有効期限を表示；デバッグキーストアを自動検出
- `apktool` で `AndroidManifest.xml` をデコードし、`android:permission` 保護のないエクスポートコンポーネントを特定
- セキュリティフラグを確認：`debuggable`・`allowBackup`・平文トラフィック
- ネイティブライブラリ ABI を列挙し、サードパーティ SDK（Firebase・Flutter・React Native 等）を検出
- 文字列リソース内のハードコードされたシークレットをスキャン
- 完全な `apk-analyze.sh` スクリプトと Python (androguard) 分析パスを同梱
- CRITICAL / HIGH / MEDIUM / INFO 重大度の構造化セキュリティレポートを生成

**トリガーフレーズ：**
- `analyze apk`
- `check apk permissions`
- `verify apk signature`
- `audit apk security`
- `apk情報抽出`
- `apk権限分析`
- `apk署名確認`
- `apkセキュリティ監査`

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

### claude-codex — マルチ AI オーケストレーションパイプライン

> **ソース**: [Z-M-Huang/claude-codex](https://github.com/Z-M-Huang/claude-codex)
> **注意**: このプロジェクトは [Z-M-Huang/vcp](https://github.com/Z-M-Huang/vcp/plugins/dev-buddy) に移行しました。今後の開発は新リポジトリで継続されます。

Claude Sonnet、Claude Opus、Codex の**3 つの独立したレビュアー**がコードを順番にチェックする、**マルチ AI オーケストレーションパイプライン**を提供する Claude Code プラグイン。「1 人しかレビューしていないコードをデプロイすべきではない」というプロフェッショナルな開発原則に基づいています。

**なぜマルチ AI レビューなのか？**

| レビュアー | 発見できる問題 |
|---|---|
| Claude Sonnet | 明らかなバグ、基本的なセキュリティ問題、コードスタイル |
| Claude Opus | アーキテクチャの問題、潜在的なバグ、エッジケース |
| Codex | 異なる AI モデルによる新鮮な視点 |

各レビュアーは OWASP Top 10 の脆弱性、適切なエラー処理、コード品質をチェックします。承認されるまでループするモデルにより、3 つすべてのレビュアーが承認するまでコードは次のフェーズに進みません。

**利用可能なスキル：**

| スキル | 用途 |
|---|---|
| `multi-ai` | 完全な機能開発パイプライン（要件 → 計画 → 実装 → レビュー） |
| `bug-fix` | バグ修正パイプライン（デュアル根本原因分析 + Codex 検証 + 的を絞った修正） |

**内蔵カスタムエージェント：**

| エージェント | モデル | 役割 |
|---|---|---|
| `requirements-gatherer` | Opus | ビジネスアナリスト + PM ハイブリッド |
| `planner` | Opus | アーキテクト + フルスタックハイブリッド |
| `plan-reviewer` | Sonnet + Opus | アーキテクチャ・セキュリティ・QA 検証 |
| `implementer` | Sonnet | フルスタック + TDD + 品質実装 |
| `code-reviewer` | Sonnet + Opus | セキュリティ・パフォーマンス・QA 検証 |
| `root-cause-analyst` | Sonnet + Opus | 並列バグ診断（bug-fix パイプライン） |

**必要条件：**

- Claude Code CLI
- Codex CLI — `npm install -g @openai/codex`
- Bun（クロスプラットフォームの JSON 処理に使用、`jq` の代替）

**インストール：**

```bash
# ステップ 1: マーケットプレイスを追加
/plugin marketplace add Z-M-Huang/claude-codex

# ステップ 2: プラグインをインストール（user スコープ — 全プロジェクトで利用可、推奨）
/plugin install claude-codex@claude-codex --scope user

# ステップ 3: .task を .gitignore に追加
echo ".task" >> .gitignore
```

**使い方：**

```text
# 機能開発パイプライン
/claude-codex:multi-ai JWT トークンを使ったユーザー認証を追加する

# バグ修正パイプライン
/claude-codex:bug-fix セッショントークン失効時にログインが無音で失敗する
```

> 外部プロジェクトから呼び出す場合は、必ずフルネームスペース `claude-codex:<skill>` を使用してください。自然言語でタスクを説明するだけで、Claude が適切なスキルを呼び出すことも可能です。

**`/multi-ai` パイプラインの流れ：**

1. **要件収集** — 専門エージェントが並列で調査し、`requirements-gatherer` が統合
2. **計画** — `planner` エージェントが実装計画を作成
3. **計画レビュー** — `plan-reviewer`（Sonnet + Opus）+ Codex ゲート
4. **実装** — `implementer` がテストに通るまで反復
5. **コードレビュー** — `code-reviewer`（Sonnet + Opus）+ Codex 最終ゲート
6. **完了** — 結果を報告

**`/bug-fix` パイプラインの流れ：**

1. **デュアル根本原因分析** — 2 つの `root-cause-analyst`（Sonnet + Opus）が並列分析
2. **統合** — オーケストレーターが両分析を統合し修正計画を作成
3. **Codex 検証** — Codex が統合された根本原因分析と修正計画をレビュー
4. **実装** — 根本原因を狙った最小限の修正
5. **コードレビュー** — `code-reviewer`（Sonnet + Opus）+ Codex ゲート

**パイプラインのタスク依存関係による強制実行：**

```
1. 実装  →  2. レビュー（Sonnet）  →  3. レビュー（Opus）  →  4. レビュー（Codex）
                  ↓ needs_changes?
             修正タスク作成 → 同じレビュアーが再検証 → 継続
```

**デフォルト設定：**

| 設定項目 | デフォルト値 |
|---|---|
| 計画レビューループ上限 | 10 回 |
| コードレビューループ上限 | 15 回 |
| 自動リトライ回数 | 3 回 |

**ライセンス:** GPL-3.0（帰属表示必須、著者：Z-M-Huang）。

---

## Codex CLI でのスキルの使用

このリポジトリのスキルは **OpenAI Codex CLI とネイティブ互換** です —— `SKILL.md` ファイルには必須の YAML frontmatter（`name`、`description`）が含まれており、各スキルには `agents/openai.yaml` UI メタデータも用意されています。

### インストール

Codex は `.agents/skills/` ディレクトリからスキルを検出します。ユーザーレベルまたはプロジェクトレベルにコピーします：

```bash
# ユーザーレベル —— すべてのプロジェクトで利用可能（推奨）
mkdir -p ~/.agents/skills
cp -r skills/android-translation-sync ~/.agents/skills/
cp -r skills/android-change-review ~/.agents/skills/
cp -r skills/apk-analyzer ~/.agents/skills/
```

```bash
# プロジェクトレベル —— このプロジェクトのみ
mkdir -p .agents/skills
cp -r skills/android-translation-sync .agents/skills/
cp -r skills/android-change-review .agents/skills/
cp -r skills/apk-analyzer .agents/skills/
```

リポジトリの更新に自動的に追従するシンボリックリンクを使用することもできます：

```bash
ln -s "$(pwd)/skills/android-translation-sync" ~/.agents/skills/
ln -s "$(pwd)/skills/android-change-review" ~/.agents/skills/
ln -s "$(pwd)/skills/apk-analyzer" ~/.agents/skills/
```

### 使い方

**明示的な呼び出し**（`$` を入力してスキルセレクターを開く）：

```text
$android-translation-sync  ./translations/strings.xlsx

$android-change-review  review my staged changes

$apk-analyzer  ./build/outputs/apk/release/app-release.apk
```

**暗黙的な呼び出し** —— Codex が説明に基づいてスキルを自動選択（`allow_implicit_invocation: true`）：

```text
翻訳を Excel から同期してください: ./translations/strings.xlsx

ステージされた変更を Android のクラッシュリスクと境界条件の観点でレビューしてください。

このAPKの権限とセキュリティ問題を分析してください: ./app-release.apk
```

### インストールの確認

```bash
# Codex CLI セッション内で実行
/skills
# 以下が表示されるはずです: android-translation-sync, android-change-review, apk-analyzer
```

---

## Cursor でのスキルの使用

変換済みの `.mdc` ルールファイルが [`cursor-rules/`](cursor-rules/) ディレクトリに用意されています。

### インストール

```bash
mkdir -p .cursor/rules
cp android-claude-code-skills/cursor-rules/*.mdc .cursor/rules/
```

または curl でダウンロード：

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/android-translation-sync.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-translation-sync.mdc
curl -o .cursor/rules/android-change-review.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/android-change-review.mdc
curl -o .cursor/rules/apk-analyzer.mdc \
  https://raw.githubusercontent.com/aihip/android-claude-code-skills/main/cursor-rules/apk-analyzer.mdc
```

### 使い方

すべてのルールは **Agent-requested** タイプ —— Cursor AI がリクエストに基づいて自動的に適用します：

```text
翻訳を Excel から同期してください: ./translations/strings.xlsx

ステージされた変更を Android のクラッシュリスクと境界条件の観点でレビューしてください。

このAPKの権限とセキュリティ問題を分析してください: ./build/outputs/apk/release/app-release.apk
```

---

## Gemini CLI でのスキルの使用

変換済みのファイルが [`gemini-rules/`](gemini-rules/) ディレクトリにあります。2 つの統合方法を提供します。

### 方法 1 — GEMINI.md（推奨）

```bash
mkdir -p .gemini/skills
cp android-claude-code-skills/gemini-rules/*.md .gemini/skills/

# GEMINI.md に参照を追加
cat >> GEMINI.md << 'EOF'
@.gemini/skills/android-translation-sync.md
@.gemini/skills/android-change-review.md
@.gemini/skills/apk-analyzer.md
EOF
```

追加後は自然言語でタスクを説明するだけです：

```text
翻訳を Excel から同期してください: ./translations/strings.xlsx

ステージされた変更のクラッシュリスクをレビューしてください。

このAPKを分析してください: ./build/outputs/apk/release/app-release.apk
```

### 方法 2 — カスタム Slash コマンド

```bash
# グローバルインストール（全プロジェクトで利用可能）
mkdir -p ~/.gemini/commands
cp android-claude-code-skills/gemini-rules/commands/*.toml ~/.gemini/commands/
```

```text
/translation-sync ./translations/strings.xlsx
/change-review staged
/apk-analyzer ./build/outputs/apk/release/app-release.apk
```

### 4 プラットフォーム比較

| 機能 | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---|---|---|---|---|
| ワークフロー知識 | ✅ 完全 | ✅ 完全 | ✅ 完全 | ✅ 完全 |
| スキル形式 | SKILL.md | SKILL.md（ネイティブ）| GEMINI.md / `.md` | `.mdc` rules |
| スキルトリガー | `/plugin` + slash | `$skill-name` または自動 | 自然言語 | 自然言語 |
| 説明からの自動検出 | ✅ | ✅（`allow_implicit_invocation`）| ✅ | ✅ |
| コンテキストファイル | CLAUDE.md | AGENTS.md | GEMINI.md | `.cursor/rules/` |
| Stop Hook / ライフサイクルフック | ✅ | ❌ | ❌ | ❌ |
| マルチエージェント orchestration | ✅ | ❌ | ❌ | ❌ |

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
│   ├── android-change-review/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── apk-analyzer/
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
