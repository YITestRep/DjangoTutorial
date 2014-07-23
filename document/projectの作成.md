##参考リンク
[初めてのDjangoアプリ作成その1](http://www.djangoproject.jp/doc/ja/1.0/intro/tutorial01.html)

##プロジェクトの作成方法
* Djangoでは、1つのアプリケーションを作るときに~~プロジェクト~~と~~アプリケーション~~の2つを作成する
* プロジェクトの作成は次のコマンドで行える
`django-admin.py startproject mysite`

* 上記コマンドを実行すると、下記のようなファイルを含んだフォルダ（prj-name）が作成される
  1. __init__.py: Pythonパッケージであることを知らせるためのフォルダ
  2. manage.py: （重要）Djangoで作成したプロジェクトに対して様々な操作を行うためのコマンドラインツール。
  3. setting.py: （重要）Djangoプロジェクトの設定ファイル。
  4. urls.py: DjangoプロジェクトのURL。多分どのリンクにどのサイトを割り当てるかといった感じ。

## プロジェクトの動作確認
* 開発したサーバを動かしてみる
* prj-nameディレクトリに移り、`python manage.py runserver`を実行する
* ブラウザでhttp://127.0.0.1:8000にアクセスする

