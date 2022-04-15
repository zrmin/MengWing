from django.urls import path
from . import views

app_name = 'webos'

urlpatterns = [
        path('', views.webos, name='webos'),
]
