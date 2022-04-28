# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的QuestionPostForm表单类
from .forms import QuestionPostForm
# 引入User模型
from django.contrib.auth.models import User

# 导入数据模型QuestionPost
from .models import QuestionPost
# 引入markdown模块
import markdown

# 提问列表
def question_list(request):
    # 取出所有提问文章
    questions = QuestionPost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'questions': questions }
    # render函数：载入模板，并返回context对象
    return render(request, 'question/list.html', context)


# 提问详情
def question_detail(request, id):
    question = QuestionPost.objects.get(id=id)

    # 将markdown语法渲染成html样式
    question.body = markdown.markdown(question.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

    context = { 'question': question }
    return render(request, 'question/detail.html', context)


# 写提问的视图
def question_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        question_post_form = QuestionPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if question_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_question = question_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_question.author = User.objects.get(id=5)
            # 将新提问保存到数据库中
            new_question.save()
            # 完成后返回到提问列表
            return redirect("question:question_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        question_post_form = QuestionPostForm()
        # 赋值上下文
        context = { 'question_post_form': question_post_form }
        # 返回模板
        return render(request, 'question/create.html', context)


# 删提问
def question_delete(request, id):
    # 根据 id 获取需要删除的提问
    question = QuestionPost.objects.get(id=id)
    # 调用.delete()方法删除提问
    question.delete()
    # 完成删除后返回提问列表
    return redirect("question:question_list")


# 安全删除提问
def question_safe_delete(request, id):
    if request.method == 'POST':
        question = QuestionPost.objects.get(id=id)
        question.delete()
        return redirect("question:question_list")
    else:
        return HttpResponse("仅允许post请求")


# 更新提问
def question_update(request, id):
    """
    更新提问的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体提问对象
    question = QuestionPost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        question_post_form = QuestionPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if question_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            question.title = request.POST['title']
            question.body = request.POST['body']
            question.save()
            # 完成后返回到修改后的提问中。需传入提问的 id 值
            return redirect("question:question_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        question_post_form = QuestionPostForm()
        # 赋值上下文，将 question 提问对象也传递进去，以便提取旧的内容
        context = { 'question': question, 'question_post_form': question_post_form }
        # 将响应返回到模板中
        return render(request, 'question/update.html', context)
