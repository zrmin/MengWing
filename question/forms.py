# 引入表单类
from django import forms
# 引入文章模型
from .models import QuestionPost

# 写提问的表单类
class QuestionPostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = QuestionPost
        # 定义表单包含的字段
        fields = ('title', 'body')
