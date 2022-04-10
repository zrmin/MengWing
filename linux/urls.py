from django.urls import path
from . import views

app_name = 'linux'

urlpatterns = [
    path('linux-terminal/', views.linux_terminal, name='linux_terminal'),
    path('linux-doc/', views.linux_doc, name='linux_doc'),
]
