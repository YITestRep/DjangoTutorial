## adminサイトの有効化
1. INSTALLED_APPS設定に"django.contrib.admin"を追加する
2. `python manage.py syncdb`を実行する（新たなアプリケーションをINSTALLED_APPSに追加した場合にはDBの更新が必要）
3. prj-name/urls.pyファイルにある`Uncomment this for admim:`をコメントアウトして解除する 

```
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
```

## 開発サーバの機動と管理者サイトの利用
1. 開発用サーバを次のコマンドで起動する 
`python manage.py runserver`
2. http://127.0.0.1:8000/admin/にアクセスする
3. スーパユーザとしてログイン（スーパユーザの登録方法はググる）


## 開発したアプリケーションの登録
* prj-name/polls/models.pyを編集し、末尾に次の一文を加える
```
from django.contrib import admin

admin.site.register(Poll)
```
