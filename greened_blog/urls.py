# 这里创建这个 learning_logs 中会用到的 URLs
#定义learning_logs 的 URL 模式
from django.urls import path, re_path
#导入 views, views 中是我们要返回给请求的页面
from . import views

# 这里的 path 会调用 view.py 中的函数, name 名 必须和函数名一致
urlpatterns = [
    # 主页
    path('', views.index, name = 'index'),   # name 就是在 view.py 中调用的函数名
    path('catlogs/', views.catlogs, name = 'catlogs'),
    # path(r'^catlogs/(?P<catlog_id>\d+)/$', views.articles, name = 'articles'),
    path('catlogs/<catlog_id>/', views.articles, name = 'articles'),
    path('new_catlog/', views.new_catlog, name='new_catlog'),
    # path(r'^new_article/(?P<catlog_id>\d+)/$', views.new_article, name='new_article'),
    path('new_article/<catlog_id>/', views.new_article, name='new_article'),
    path('edit_article/<article_id>/', views.edit_article, name='edit_article'),
]


