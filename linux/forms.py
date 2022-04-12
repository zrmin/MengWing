# 引入表单类
from django import forms
# 引入LinuxDoc模型
from .models import LinuxDoc

# 写文章的表单类
class LinuxDocForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = LinuxDoc
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags', 'avatar')
