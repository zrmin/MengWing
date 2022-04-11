from django.shortcuts import render

# 导入数据模型LinuxDoc
from .models import LinuxDoc

# 引入markdown模块——>将markdown语法书写的文章渲染为html文本
import markdown

def linux_terminal(request):
    return HttpResponse("Linux Terminal")

# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的LinuxDocForm表单类
from .forms import LinuxDocForm
# 引入User模型
from django.contrib.auth.models import User

def linux_article_list(request):
    # 取出所有LinuxDoc
    articles = LinuxDoc.objects.all()
    # 需要传递给模板templates的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'linux/linux_article_list.html', context)


# LinuxDoc详情
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
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'linux/linux_article_detail.html', context)

# 写文章的视图
def linux_article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = LinuxDocForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id = 1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("linux:linux_article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = LinuxDocForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回数据
        return render(request, 'linux/linux_article_create.html', context)

# 安全删文章
def linux_article_safe_delete(request, id):
    if request.method == 'POST':
        article = LinuxDoc.objects.get(id=id)
        article.delete()
        return redirect("linux:linux_article_list")
    else:
        return HttpResponse("仅允许POST请求")


