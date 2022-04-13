from django.shortcuts import render
from . import views

def application_list(request):
    return render(request, 'application/application_list.html')

def application_terminal_info(request):
    return render(request, 'application/terminal_info.html')

def application_chat_info(request):
    return render(request, 'application/chat_info.html')

def application_ide_info(request):
    return render(request, 'application/ide_info.html')
