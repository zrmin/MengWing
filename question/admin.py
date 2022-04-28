from django.contrib import admin

# 别忘了导入QuestionPost
from .models import QuestionPost

# 注册QuestionPost到admin中
admin.site.register(QuestionPost)
