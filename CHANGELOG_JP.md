# 変更履歴

このプロジェクトの注目すべき変更はすべてこのファイルに記録されます。

## [1.5.0] - 2026-02-27

### 追加
- **マルチプラットフォームスキルサポート**
  - **OpenAI Codex CLI** — `.agents/skills/` インストールによるネイティブサポート。`$skill-name` または暗黙的な自動検出でスキルを起動。プロジェクトレベルのエージェント指示用に `AGENTS.md` を追加
  - **Cursor** — `cursor-rules/` に `android-translation-sync` と `android-change-review` の `.mdc` ルールファイルを追加。ルールは Agent-requested タイプで、一致するリクエスト時に自動起動
  - **Gemini CLI** — `gemini-rules/` に GEMINI.md 互換の `.md` ファイルとカスタム Slash コマンド `.toml` ファイル（`/translation-sync`、`/change-review`）を追加
- **`AGENTS.md`** — OpenAI Codex CLI 向けのリポジトリレベルのエージェント指示ファイル。利用可能なスキル、トリガーフレーズ、インストール手順を記載

### 変更
- **ドキュメント（英語/中国語/日本語）**
  - 3 つの README すべてに「Codex CLI でのスキルの使用」「Cursor でのスキルの使用」「Gemini CLI でのスキルの使用」セクションを追加
  - 4 プラットフォーム能力比較表を全 README に追加
  - 全 README の目次を更新
- **`CLAUDE.md` / `CLAUDE_CN.md` / `CLAUDE_JP.md`**
  - プロジェクト構成一覧に `AGENTS.md` を追加
- **`agents/openai.yaml`**（両スキル）
  - 暗黙的な呼び出しマッチング向けにトリガー例コメントを追加

## [1.4.0] - 2026-02-26

### 追加
- **Android Change Review** スキル
  - `skills/android-change-review/SKILL.md` と `agents/openai.yaml` を追加
  - `git add .` 後の `git diff --cached` を使用したステージされた変更のレビューに対応
  - `git show <commit-id>` を使用した特定 `commit-id` のレビューに対応
  - Android のクラッシュリスク、境界条件、リグレッション検出に重点
  - Android 特有のチェックポイントを含む：Fragment/Activity ライフサイクル、Compose 再コンポーズ、コルーチン/Flow、パーミッション、WorkManager、Room、ナビゲーション、RecyclerView/Paging、Manifest/リソース設定
  - ファイル/行番号と深刻度順の問題優先出力を推奨

### 変更
- **ドキュメント（英語/中国語）**
  - `README.md` / `README_CN.md` に `Android Change Review` スキルの使用例とトリガーフレーズを追加

### 修正
- **デスクトップアップロード向け YAML 互換性**
  - YAML パース互換性を向上させるため、必要な `SKILL.md` frontmatter の `description` 値をクォートで囲むよう修正

### バリデーション
- `quick_validate.py` が全スキルで通過
- `scripts/validate_skills.py` が全スキルで通過

## [1.3.0] - 2026-02-26

### 追加
- **OpenAI Codex スキル互換性**
  - `skills/android-translation-sync/SKILL.md` に YAML frontmatter（`name`、`description`）を追加
  - frontmatter と再利用可能なワークフローガイダンスを含む Codex 互換の `skills/template/SKILL.md` を追加
  - 両スキル（`android-translation-sync`、`template`）に `agents/openai.yaml` メタデータを追加
- **リポジトリスキルバリデーションツール**
  - 以下を検証する `scripts/validate_skills.py` を追加：
    - `SKILL.md` frontmatter の形式と許可キー
    - スキルディレクトリ名 ↔ frontmatter `name` の整合性
    - `agents/openai.yaml` の必須フィールドと基本制約
    - `interface.default_prompt` が正しい `$skill-name` を参照しているか
- **CI 自動化**
  - GitHub Actions ワークフロー `.github/workflows/validate-skills.yml` を追加
  - スキル関連の変更に対する `push` と `pull_request` 時に自動バリデーションを実行
- **Pre-commit フック**
  - コミット前に `python scripts/validate_skills.py` を実行するローカルフック `.pre-commit-config.yaml` を追加

### 変更
- **ドキュメント（英語/中国語）**
  - `README.md` / `README_CN.md` を更新し、Codex 互換スキル形式を説明
  - バリデーション手順（ローカル + CI + pre-commit）を追加
  - `agents/openai.yaml` を含むプロジェクト構成例を更新
- **プロジェクト概要ドキュメント（英語/中国語）**
  - `CLAUDE.md` / `CLAUDE_CN.md` を更新し、デュアル互換性（Claude Code + OpenAI Codex）を説明

### バリデーション
- ローカルで `PyYAML` をインストールし、現在の全スキルに対して公式 `quick_validate.py` を実行
- リポジトリバリデーター `scripts/validate_skills.py` が全スキルで正常に通過

## [1.2.1] - 2025-02-26

### 修正
- **スキル読み込み問題** - plugin.json のスキルパスを修正
  - `./skills/android-translation-sync/` から `./skills/` に変更
  - 全 SKILL.md ファイルが正しく読み込まれるよう修正
  - 誤ったスキルがトリガーされる問題を修正

## [1.2.0] - 2025-02-26

### 変更
- **Android Translation Sync** - 精度向上のため更新ルールを改善
  - 強調：`<string>` タグ間の値コンテンツのみを置換すること
  - 新しい行を追加しないこと
  - 既存の行を削除しないこと
  - 空行とコメントをすべてそのまま保持すること

### 修正
- 不要なフォーマット変更を避けるため、正確な値置換を明確化

## [1.1.0] - 2025-02-26

### 追加
- **Android Translation Sync** スキル
  - Excel から strings.xml へ多言語リソースを同期
  - 一意のキーを自動生成（10〜20 文字）
  - Excel の先頭列にキーを書き込む
  - 全言語ファイルを更新（values、values-zh、values-es など）
  - コード変更最小化の原則（空行とコメントを保持）

### 変更
- スキルリストを含むプラグインマニフェストを更新
- バージョン追跡を追加

## [1.0.0] - 2025-02-26

### 追加
- 初期リリース
- `.claude-plugin/` 設定を含むプラグイン構成
- スキルテンプレート
- 二言語ドキュメント（英語/中国語）
