from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

def index(request: HttpRequest):
    return render(request, 'index.html', context={})

def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html', context={})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = User(username=username, password=password) # 明文保存密码，无法验证
        user = User.objects.create_user(username=username, password=password)
        user.save()
        context = {
            "status": 200,
            "msg": "用户注册成功",
        }
        return JsonResponse(context)

def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html', context={})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # context = {
            #     "status": 200,
            #     "msg": "用户登录成功",
            # }
            # return redirect(to=request.GET.get('next')) # 'next' 参数为空时，无法返回
            return redirect('index')
        else:
            context = {
                "status": 403,
                "msg": "用户或密码错误",
            }
            return JsonResponse(context)
        # return JsonResponse(context)

@login_required
def logout(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'logout.html', context={})
    if request.method == 'POST':
        auth.logout(request)
        # context = {
        #     "status": 200,
        #     "msg": "退出成功",
        # }
        # return JsonResponse(context)
        return redirect('index')

@login_required
def password(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'password.html', context={})
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