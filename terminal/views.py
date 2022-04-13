from django.shortcuts import render
from django.http import HttpResponse

def linux_terminal(request):
    return render(request, 'terminal/linux_terminal.html')
