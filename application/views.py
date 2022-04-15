from django.shortcuts import render
from . import views

def application_list(request):
    return render(request, 'application/application_list.html')

def application_terminal_info(request):
    return render(request, 'application/terminal_info.html')

def application_webssh_info(request):
    return render(request, 'application/webssh_info.html')

def application_chat_info(request):
    return render(request, 'application/chat_info.html')

def application_ide_info(request):
    return render(request, 'application/ide_info.html')

def application_terminal(request):
    return render(request, 'terminal/linux_terminal.html')

def application_webos_info(request):
    return render(request, 'application/webos_info.html')

def application_webos(request):
    return render(request, 'webos/webos.html')
