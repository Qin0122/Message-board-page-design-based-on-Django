from django.contrib import admin

# Register your models here.
from message_form.models import Message

@admin.register(Message)
class Message_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'message', 'send_time']

    # 搜索框
    search_fields = ['name']

    # 设置最大浏览条数
    list_per_page = 5

    # 调整选项框位置
    actions_on_bottom = True
    actions_on_top = False