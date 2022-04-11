from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
# 引入分页模块
from django.core.paginator import Paginator

def linux_article_list(request):
    # 取出所有LinuxDoc
    article_list = LinuxDoc.objects.all()

    # 每页显示3篇文章
    paginator = Paginator(article_list, 3)
    # 获取url中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给articles
    articles = paginator.get_page(page)

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
# 检查记录
@login_required(login_url='/userprofile/login/')
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
            new_article.author = User.objects.get(id=request.user.id)
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


# 更新文章
def linux_article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体文章对象
    article = LinuxDoc.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = LinuxDocForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("linux:linux_article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = LinuxDocForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'linux/linux_article_update.html', context)
