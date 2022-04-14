from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('application-list/', views.application_list, name='application_list'),
    path('terminal-info', views.application_terminal_info, name='terminal_info'),
    path('webssh-info/', views.application_webssh_info, name='webssh_info'),
    path('chat-info', views.application_chat_info, name='chat_info'),
    path('ide-info', views.application_ide_info, name='ide_info'),
    path('terminal', views.application_terminal, name='terminal'),
]
