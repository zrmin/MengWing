from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
        # 提问列表
        path('question-list/', views.question_list, name='question_list'),
        # 提问详情
        path('question-detail/<int:id>/', views.question_detail, name='question_detail'),
        # 写提问
        path('question-create/', views.question_create, name='question_create'),
         # 删除提问
        path('question-delete/<int:id>/', views.question_delete, name='question_delete'),
        # 安全删除提问
        path(
            'question-safe-delete/<int:id>/',
            views.question_safe_delete,
            name='question_safe_delete'
        ),
        # 更新提问
        path('question-update/<int:id>/', views.question_update, name='question_update'),

]
