from django.shortcuts import render

# Create your views here.
from message_form.models import Message

# 默认接受一个参数request，是Django传递进来的，每一个请求都会包装成一个request对象
def message_form(request):
    # 从html中提取数据保存到数据库中
    # 如果是POST，进行取数据
    if request.method == "POST":
        # 进行值的提取
        # POST属性调用get方法，可理解为dict字典所有用get方法,""代表值不存在的话设置默认值
        name = request.POST.get("name","")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message", "")

        message = Message()

        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()

    # 如果是get，直接render页面
    return render(request,"message_form.html")
