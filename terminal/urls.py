from django.urls import path
from . import views

app_name = 'terminal'

urlpatterns = [
    path('', views.linux_terminal, name='linux_terminal'),
]
