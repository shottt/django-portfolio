バージョン：Python:3.11


## 仮想環境を構築
仮想環境の作成
```
python3 -m venv myvenv
```
仮想環境の実行
```
source myvenv/vin/activate
```
パッケージのインストール
```
pip 3 install -r requirements.txt
```
データベース作成
```
python3 manage.py migrate
```
webサーバー立ち上げ
```
python3 manage.py runserver
```


以下は初期構築時の手順
### プロジェクト作成
setting.pyに画像ファイルを配置するパス設定を記述

```
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

migrateコマンドを実行し、データベースを作る
```
python3 manage.py migrate
```

webサーバーを立ち上げる
```
python3 manage.py runserver
```

urlをクリックして、インストール成功画面が表示されることを確認する

### アプリケーション作成
```
python3 manage.py startapp app
```
setting.pyのINSTALLED_APPSに'widget_tweaks'(フォームカスタマイズ用)と'app'を追加

### モデル作成
models.pyにProfileモデルを作成する

### 管理画面にモデル登録
admin.pyにProfileモデルを登録する

### データベース再構築
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

### 管理ユーザー作成
```
python3 manage.py createsuperuser
```
ユーザー名：sh_sho
メールアドレス：aa@aa.com
パスワード：qwert123
パスワード(admin)：qwert123

### 管理画面にアクセスしてデータを登録
webサーバーを立ち上げる
```
python3 manage.py runserver
```
http://127.0.0.1:8000/admin
にアクセスしてデータを登録

### プロジェクトURLを設定
mysite/urls.pyに画像用のurlを設定

### アプリケーションURLを設定
app配下にurls.pyを作成

### viewsを編集

### templatesを作成
app配下にtemplate/appを作成。
その下にbase.htmlを作成。
bootstrapとfontawesomeをcdnで読み込むよう設定
index.htmlを作成

### staticを作成
app配下にstaticフォルダを作成


