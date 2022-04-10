from django.shortcuts import render
from .models import LinuxDoc
import markdown

def linux_terminal(request):
    return render(request, 'linux/linux_terminal.html')

def linux_article_list(request):
    # 取出所有linux文章
    articles = LinuxDoc.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'linux/linux_article_list.html', context)

# 文章详情
def linux_article_detail(request, id):
    # 取出相应的文章
    article = LinuxDoc.objects.get(id=id)

   # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

    # 需要传递给模板的对象
    context = { 'article': article }
    # 载入模板，并返回context对象
    return render(request, 'linux/linux_article_detail.html', context)
