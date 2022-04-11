from django.urls import path
from . import views

app_name = 'linux'

urlpatterns = [
    path('linux-terminal/', views.linux_terminal, name='linux_terminal'),
    path('linux-article-list/', views.linux_article_list, name='linux_article_list'),
    # 文章详情
    path('linux-article-detail/<int:id>/', views.linux_article_detail, name='linux_article_detail'),
    # 写文章
    path('linux-article-create/', views.linux_article_create, name='linux_article_create'),
    # 安全删除文章
    path('linux-article-safe-delete/<int:id>/', views.linux_article_safe_delete, name='linux_article_safe_delete'),
    # 更新文章
    path('linux-article-update/<int:id>/', views.linux_article_update, name='linux_article_update'),
]
