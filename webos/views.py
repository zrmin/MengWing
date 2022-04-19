from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


def webos(request):
    return render(request, 'webos/webos.html')

@xframe_options_exempt
def chat(request):
    return render(request, 'webos/chat.html')

@xframe_options_exempt
def extend1(request):
    return render(request, 'webos/extend1.html')

@xframe_options_exempt
def sabey(request):
    HttpResponseRedirect("https://sabeythenoob-chat.herokuapp.com/")
