from django.urls import path
from . import views

app_name = 'linux'

urlpatterns = [
    path('linux-terminal/', views.linux_terminal, name='linux_terminal'),
    path('linux-article-list/', views.linux_article_list, name='linux_article_list'),
    # 文章详情
    path('linux-article-detail/<int:id>/', views.linux_article_detail, name='linux_article_detail'),
]
