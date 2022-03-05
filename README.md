# ファイル構成は以下のようになっています

## ファイルの構成について

* bitcoin
  * cms
    * migrations(デフォ)
    * static(cssとか写真とかをいれる)
      * css(cssファイルを入れる)
      * images(写真を入れる)
    * templates(htmlを入れる)
      * base.html(それぞれの共通部分を抽出したもの)
      * top.html(トップ)
    * __init__.py(デフォ)
    * admin.py(デフォ)
    * apps.py(デフォ)
    * models.py(ユーザーモデル)
    * test.py(空)
    * urls.py(URLをいじるときはここをいじる)
    * views.py(Djangoでは汎用ビュー（generic view）と言ってよく使うようなビューは全て用意されていて、それを継承するためにクラスを使います。)
  * config(あまりいじらない)
    * __init__.py
    * settings.py(時間とか国とかをセッティングする)
    * urls.py(ここはいじらない)
    * wsgi.py
  * docker-compose.yml
  * Dockerfile
  * main.py
  * manage.py
  * README.md(これ)
