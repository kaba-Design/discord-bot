# Discord Bot (discord.py)

このリポジトリは、Python と discord.py を使った Discord ボットのサンプルです。

## 機能

- 新しいメンバーが参加したときに DM で挨拶メッセージを送信
- NGワードを含むメッセージを検出して自動削除
- NGワードは `banned_words.txt` で管理
- `.env` でトークン管理

## セットアップ

1. `discord_bot` フォルダに移動

```bash
cd /Users/hiratakaoru/discord_bot
```

2. 仮想環境を作成して有効化

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

4. `.env.example` をコピーし、トークンを設定

```bash
cp .env.example .env
```

`.env` の内容:

```text
DISCORD_TOKEN=あなたのボットトークン
```

## NGワード追加方法

`banned_words.txt` に 1 行ごとに単語を追加します。
`#` で始まる行はコメントとして無視されます。

## 実行方法

```bash
python bot.py
```

## 公開準備

1. Git リポジトリを初期化する

```bash
git init
```

2. すべてのファイルを追加してコミット

```bash
git add .
git commit -m "Initial Discord bot setup"
```

3. GitHub に新しいリポジトリを作成し、リモートを追加してプッシュ

```bash
git remote add origin https://github.com/<ユーザー名>/<リポジトリ名>.git
git branch -M main
git push -u origin main
```

4. GitHub Actions で自動チェックが有効になります

- `.github/workflows/python-lint.yml` は `bot.py` の構文チェックを実行します

## Discord 側の設定

Discord Developer Portal でボットを作成し、以下を有効にしてください:

- `Server Members Intent`
- `Message Content Intent`

ボットを招待する際の必要権限:

- Send Messages
- Manage Messages
- Read Messages/View Channels

## 注意

- ユーザーが DM を受信拒否している場合、ウェルカム DM は送れません。
- `banned_words.txt` にワードを追加すると、自動的に検出対象になります。
