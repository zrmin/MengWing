from django.shortcuts import render
from .models import LinuxDoc

def linux_terminal(request):
    return render(request, 'linux/linux_terminal.html')

def linux_article_list(request):
    # 取出所有linux文章
    articles = LinuxDoc.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'linux/linux_article_list.html', context)
