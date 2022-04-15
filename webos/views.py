from django.shortcuts import render
from django.http import HttpResponse

def webos(request):
    return render(request, 'webos/webos.html')
