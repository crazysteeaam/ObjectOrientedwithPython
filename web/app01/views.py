from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # 默认情况下会去当前app目录下地templates文件夹找(app顺序逐一查找)
    name = "韩超"
    rules = ['管理员', 'CEO', '你好']
    user_info = {"name": "弱智", "salary": 100000, "rules": "CEO"}
    return render(request, "user_list.html", {"n1": name, 'n2': rules, "n3": user_info})


def user_add(request):
    return HttpResponse('添加用户')
