from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('application-list/', views.application_list, name='application_list'),
    path('terminal-info', views.application_terminal_info, name='terminal_info'),
    path('chat-info', views.application_chat_info, name='chat_info'),
    path('ide-info', views.application_ide_info, name='ide_info'),
]
