"""mengwing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import notifications.urls
from linux.views import linux_article_list

urlpatterns = [
    path('', linux_article_list, name='home'),
    path('linux/', include('linux.urls', namespace='linux')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('admin/', admin.site.urls),
    path('password-reset/', include('password_reset.urls')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    # django-notifications
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),
    # django-allauth
    path('accounts/', include('allauth.urls')),
    # terminal
    path('terminal/', include('terminal.urls', namespace='terminal')),
    # 应用中心
    path('application/', include('application.urls', namespace='application')),
    # webos
    path('webos/', include('webos.urls', namespace='webos')),
    # chat
    path('chat/', include('chat.urls', namespace='chat')),
]

# 为以后上传的图片配置URL路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
