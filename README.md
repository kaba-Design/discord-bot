# Discord Bot (discord.py)

このリポジトリは、Python と discord.py を使った **Discord ボットのサンプル** です。  
初心者でも簡単に自分の Discord サーバーで動かせます。

## 機能

- ✨ 新しいメンバーが参加したときに **自動で DM** を送信
- 🚫 **NGワード** を含むメッセージを自動削除
- 📝 NGワードは `banned_words.txt` で簡単にカスタマイズ可能
- 🔐 `.env` ファイルでトークンを安全に管理

---

## 📋 必要なもの

- **Python 3.8 以上**
- **Discord サーバー**（テスト用）
- **Discord Bot アカウント**（Discord Developer Portal で作成）

---

## 🚀 セットアップ手順

### Step 1：Discord Developer Portal でボットを作成

1. ブラウザで `https://discord.com/developers/applications` を開く
2. **`New Application`** をクリック
3. アプリ名を入力して **`Create`** をクリック
4. 左側メニューから **`Bot`** を選択
5. **`Add Bot`** をクリック
6. `TOKEN` の右側にある **`Copy`** をクリック（コピーしたトークンは安全に保管）

### Step 2：Intent を有効にする（重要！）

1. Bot ページで下方へスクロール
2. **`GATEWAY INTENTS`** セクションで以下の 2 つを **ON** にしてください：
   - ✅ `Server Members Intent`
   - ✅ `Message Content Intent`
3. **Save Changes** をクリック

### Step 3：ローカルにコードをセットアップ

```bash
# このリポジトリをクローン
git clone https://github.com/kaba-Design/discord-bot.git
cd discord-bot

# Python 仮想環境を作成
python3 -m venv .venv

# 仮想環境を有効化
source .venv/bin/activate

# 依存ライブラリをインストール
pip install -r requirements.txt
```

### Step 4：`.env` ファイルを作成してトークンを設定

```bash
# .env.example をコピー
cp .env.example .env
```

`discord-bot/.env` をテキストエディタで開き、Step 1 でコピーしたトークンを貼り付けます：

```text
DISCORD_TOKEN=ここにボットトークンを貼り付け
```

### Step 5：ボットを起動

```bash
python bot.py
```

ターミナルに以下が表示されれば成功です：
```
[2026-05-21 12:34:56] INFO: Logged in as <ボット名>#0000 (123456789)
[2026-05-21 12:34:56] INFO: Bot is ready.
```

---

## 🎯 ボットをサーバーに招待

### 招待用 URL を生成

1. Discord Developer Portal を開く
2. 左側メニューから **`OAuth2`** → **`URL Generator`** を選択
3. **`SCOPES`** で `bot` をチェック
4. **`PERMISSIONS`** で以下をチェック：
   - ✅ View Channels
   - ✅ Send Messages
   - ✅ Manage Messages
   - ✅ Read Message History
5. 下部の URL をコピーしてブラウザで開く
6. ボットを招待したいサーバーを選択して **`認可`** をクリック

これでボットがサーバーに参加しました！

---

## 💬 ボットの使い方

### 新規メンバーへの自動 DM

新しいメンバーが参加すると、自動で以下の DM が送信されます：

```
ようこそ。ここは何も説明しなくていい場所です
ご参加ありがとうございます！
```

> ⚠️ ユーザーが DM を拒否設定している場合は、DM が届きません

### NGワードの自動削除

`banned_words.txt` に含まれた言葉をメッセージに入れると：
1. そのメッセージが自動削除される
2. チャンネルに警告メッセージが 8 秒表示される

---

## ✏️ NGワード を追加・変更する

`banned_words.txt` をテキストエディタで開き、1 行ごとに追加します：

```text
# NGワードリスト
# コメント行は # で始めてください

ばか
くそ
死ね
新しい言葉
もう1つ追加
```

追加後、ボットを再起動すれば反映されます。

---

## ❓ よくある質問（FAQ）

### Q：`Improper token has been passed` というエラーが出ます

**A：** トークンが間違っているか、無効です。以下を確認してください：
1. Bot タブから正しい TOKEN をコピーしましたか？
2. `.env` ファイルに正しく貼り付けましたか？
3. トークンに余分なスペースがないか確認してください
4. 必要に応じてトークンを再生成してください

### Q：新規メンバーに DM が届きません

**A：** 以下の理由が考えられます：
1. ユーザーがボットからの DM を拒否設定にしている
2. `Server Members Intent` が有効になっていない
3. ボットがサーバーに正しく追加されていない

### Q：NGワードが効きません

**A：** 以下を確認してください：
1. `banned_words.txt` にワードが正しく追加されていますか？
2. ボットを再起動しましたか？
3. 大文字・小文字の区別はしないので、そこは大丈夫です

### Q：Bot をずっと起動させておきたいです

**A：** Mac が起動している限り、以下で起動できます：

```bash
python bot.py
```

**常時起動させたい場合：**
- VPS（AWS、Google Cloud 等）を使用
- Replit や Heroku などのクラウドプラットフォームを使用

---

## 📂 フォルダ構成

```
discord-bot/
├── bot.py              # メインのボットコード
├── banned_words.txt    # NGワードリスト
├── requirements.txt    # 依存ライブラリ
├── .env                # トークン設定（Git に含まれない）
├── .env.example        # .env のテンプレート
├── README.md           # このファイル
└── LICENSE             # ライセンス
```

---

## 🛠️ トラブルシューティング

### Python が見つかりませんと言われます

```bash
# Python のバージョンを確認
python3 --version

# Python 3.8 以上が必要です
```

### 仮想環境が有効になりません

```bash
# Mac / Linux の場合
source .venv/bin/activate

# Windows の場合
.venv\Scripts\activate
```

### ライブラリのインストールでエラーが出ます

```bash
# pip を最新版にアップグレード
pip install --upgrade pip

# もう一度インストール
pip install -r requirements.txt
```

---

## 📝 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。  
詳細は [LICENSE](LICENSE) を参照してください。

---

## 💡 さらに学ぶ

- [discord.py 公式ドキュメント](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/docs)
- [GitHub Copilot](https://github.com/copilot) で質問できます

---

## 🤝 貢献

バグ報告や機能リクエストは、GitHub Issues で受け付けています。
改善提案があれば、Pull Request をしてください！

---

**Happy Coding! 🚀**
