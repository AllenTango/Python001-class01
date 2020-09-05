from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse

def register(request: HttpRequest):
    if request.method == 'POST':
        # username = request.POST['username'] 出错 raise MultiValueDictKeyError(key) 改用 get
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=username, password=password)
        user.save()
        context = {
            "status": 200,
            "msg": "用户注册成功",
        }
        return JsonResponse(context)

def login(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            context = {
                "status": 200,
                "msg": "用户登录成功",
            }
        else:
            context = {
                "status": 403,
                "msg": "用户或密码错误",
            }
        return JsonResponse(context)

def logout(request: HttpRequest):
    if request.method == 'POST':
        auth.logout(request)
        context = {
            "status": 200,
            "msg": "退出成功",
        }
        return JsonResponse(context)

def password(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = auth.authenticate(request, username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            context = {
                "status": 200,
                "msg": "修改成功",
            }
        else:
            context = {
                "status": 403,
                "msg": "用户名或密码错误",
            }
        return JsonResponse(context)