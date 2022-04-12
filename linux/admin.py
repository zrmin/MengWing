from django.contrib import admin

# 别忘了导入LinuxDoc
from .models import LinuxDoc, ArticleColumn

# 注册LinuxDoc到admin中
admin.site.register(LinuxDoc)

# 注册文章栏目
admin.site.register(ArticleColumn)
