# コントリビューションガイド

本プロジェクトへの貢献に関心をお寄せいただきありがとうございます！あらゆる種類のコントリビューションを歓迎します。

## コントリビューション方法

### バグ報告

バグを見つけましたか？Issue を開いてください：
- 明確なタイトルと説明
- 再現手順
- 期待される動作 vs 実際の動作
- 環境詳細（OS、AI プラットフォームなど）

### 新スキルの提案

新スキルのアイデアがありますか？Issue または PR を開いてください：
- スキル名と説明
- ユースケースとトリガーフレーズ
- 期待されるワークフロー/動作

### コード変更の提交

1. 本リポジトリを Fork
2. 機能ブランチを作成 (`git checkout -b feature/amazing-skill`)
3. スキルテンプレート構造に従う
4. 検証を実行：`python scripts/validate_skills.py`
5. 変更をコミット (`git commit -m 'feat: add amazing skill'`)
6. ブランチにプッシュ (`git push origin feature/amazing-skill`)
7. Pull Request を開く

## スキル構造

```
skills/your-skill-name/
├── SKILL.md              # メインスキルドキュメント（YAML frontmatter 含む）
└── agents/
    └── openai.yaml       # Codex UI メタデータ（推奨）
```

### SKILL.md テンプレート

```markdown
---
name: your-skill-name
description: "Codex がこのスキルを使用するタイミングを明確に説明。トリガーフレーズを含める。"
---

# スキル名

> 簡潔な一行説明。

## 使用タイミング

**トリガーフレーズ：**
- "キーワード1"
- "キーワード2"
- "日本語トリガー"

## ワークフロー

ステップバイステップの手順...

## 例

使用例...
```

### agents/openai.yaml テンプレート

```yaml
interface:
  display_name: "スキル表示名"
  short_description: "25-64文字の Codex UI 説明。"
  default_prompt: "Use $your-skill-name to..."

policy:
  allow_implicit_invocation: true
```

## 検証

すべてのスキルは以下を通過する必要があります：

```bash
pip install PyYAML
python scripts/validate_skills.py
```

チェック内容：
- YAML frontmatter 形式
- スキルディレクトリ名が frontmatter `name` と一致
- `agents/openai.yaml` に必須フィールドが含まれている
- `default_prompt` が正しい `$skill-name` を参照

## プラットフォームファイル

新スキル追加時、以下も作成：

1. **Cursor ルール**: `cursor-rules/your-skill-name.mdc`
2. **Gemini ルール**: `gemini-rules/your-skill-name.md`
3. **Gemini コマンド**: `gemini-rules/commands/your-skill-name.toml`
4. **更新**: `README.md`、`AGENTS.md`、`CHANGELOG.md`

## コードスタイル

- 既存のパターンに従う
- 明確で簡潔な言語を使用
- すべてのワークフローの例を含める
- 可能な限り英語、中国語、日本語をサポート

## ライセンス

コントリビューションにより、あなたの貢献が MIT ライセンスの下でライセンスされることに同意したものとみなされます。
