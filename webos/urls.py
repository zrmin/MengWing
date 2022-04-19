from django.urls import path
from . import views

app_name = 'webos'

urlpatterns = [
        path('', views.webos, name='webos'),
        path('chat.html/', views.chat, name='chat'),
        path('extend1.html/', views.extend1, name='extend1'),
        path('sabey/', views.sabey, name='sabey'),
]
