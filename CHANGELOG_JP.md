# 変更履歴

このプロジェクトの注目すべき変更はすべてこのファイルに記録されます。

## [1.9.0] - 2026-04-07

### 追加
- **発見性の向上** — SEO とプロジェクトの可視性を強化
  - すべての README ファイル（EN/CN/JP）に Star/Fork/ダウンロードバッジを追加
  - 「課題とソリューション」の比較テーブルを含む「なぜこのツールを使うのか？」セクションを追加
  - すべてのプラットフォームのインストール例を含む「クイックスタート」セクションを追加
  - Claude Code、Codex、Gemini CLI、Cursor、コミュニティプロジェクトへのリンクを含む「関連プロジェクト」セクションを追加
  - 検索可視性を向上させるための「Star 履歴」チャートと「キーワード」セクションを追加
  - `package.json` のキーワードを 24 から 40+ 以上に拡張（java、mvvm、mvi、clean-architecture、cursor-ide、google-gemini、code-generation など）
- **多言語コントリビューションガイド** — 3 つの言語（EN/CN/JP）すべてで `CONTRIBUTING.md` を追加
  - バグ報告ガイドライン
  - 新スキル提案プロセス
  - コードコントリビューションワークフロー
  - スキル構造テンプレート（SKILL.md + agents/openai.yaml）
  - プラットフォームファイル要件（Cursor/Gemini/Codex）
- **ソーシャルプレビュー画像** — より良い GitHub シェアリングのための `.github/social-preview.svg` を追加

### 変更
- **ドキュメント（EN/CN/JP）** — 発見性の完全な見直し
  - 一貫した構造とバッジですべての 3 つの README ファイルを更新
  - SEO と明確性のために説明を改善
  - より目立つコールトゥアクションボタンとリンクを追加
  - すべての言語バージョン間でコンテンツを同期
- **`package.json`** — npm の発見性を向上させるために説明を改善しキーワードを拡張
- **`llms.txt`** — 強化された説明とクイックインストールガイドで AI クローラー発見ファイルを更新
- **`.claude-plugin/plugin.json` & `marketplace.json`** — キーワードを拡張し説明を改善

### 改善されたキーワードカバレッジ
- **Android**: kotlin、java、jetpack、compose、mvvm、mvi、clean-architecture、android-studio、gradle
- **AI プラットフォーム**: claude-code、claude、anthropic、openai-codex、codex、gemini、gemini-cli、google-gemini、cursor、cursor-ide
- **機能**: code-review、apk-analyzer、android-security、translation、i18n、figma-to-android、design-to-code、code-generation
- **ツール**: skill、plugin、extension、android-automation、developer-tools、productivity

### バリデーション
- `scripts/validate_skills.py` がすべての 6 つのスキルで通過
- 一貫した構造ですべての README ファイル（EN/CN/JP）を更新

## [1.8.0] - 2026-04-07

### 追加
- **Figma to Android** スキル（`skills/figma-to-android/`）
  - `SKILL.md` と `agents/openai.yaml` を追加
  - Figma デザインデータ（ノード JSON、レイヤー説明、アノテーション、スクリーンショット）を本番対応の Android ネイティブ XML + Kotlin コードに変換
  - ConstraintLayout ファーストアプローチによる 1:1 の視覚的再現
  - 厳密な出力順序：ページ構造分析 → ディレクトリ構造 → XML レイアウト → RecyclerView アイテム → ドロアブル → リソース値 → Kotlin コード → リスクノート
  - すべての色、寸法、シェイプをリソースファイルに抽出（インラインハードコーディングなし）
  - ViewBinding ベースの Kotlin コード（Activity/Fragment、Adapter/ViewHolder、データクラス）
  - `<include>` サブレイアウトによる再利用可能なモジュール抽出
  - 命名規則の強制：`tv_title`、`color_primary`、`dp_4`、`bg_card_white_radius_12`
  - リストページの補足ルール（NestedScrollView、フォーム入力、再利用可能なバー）
  - Jetpack Compose は厳密に禁止 — ネイティブ View/XML 出力のみ

### 変更
- **Cursor サポート** — `cursor-rules/figma-to-android.mdc` を追加
- **Gemini CLI サポート** — `gemini-rules/figma-to-android.md` と `gemini-rules/commands/figma-to-android.toml` を追加
- **`AGENTS.md`** — `$figma-to-android` スキルエントリをトリガーフレーズと機能説明で追加。スキルディレクトリリストとインストールコマンドを更新
- **`plugin.json`** — `figma`、`figma-to-android`、`design-to-code`、`xml-layout` キーワードを追加
- **`llms.txt`** — Figma to Android スキルエントリを追加
- **ドキュメント（EN/CN/JP）**
  - 3 つの README すべてに `Figma to Android` を目次と利用可能なスキルセクションに追加
  - Codex CLI インストールコマンド、明示的/暗黙的使用例、`/skills` 検証リストを更新
  - Cursor ルールテーブルと curl インストールコマンドを更新
  - Gemini CLI `@import` 例とスラッシュコマンドリストを更新
  - 新しいファイルを含めるようにプロジェクト構成一覧を拡張
- **`CLAUDE.md` / `CLAUDE_CN.md` / `CLAUDE_JP.md`** — プロジェクト構造に `figma-to-android/` を追加

### バリデーション
- `scripts/validate_skills.py` がすべての 6 つのスキルで通過

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
