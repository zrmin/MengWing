from django.contrib import admin

# 别忘了导入LinuxDoc
from .models import LinuxDoc

# 注册LinuxDoc到admin中
admin.site.register(LinuxDoc)
