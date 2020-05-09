from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import auth
from .models import User_Account
from SEEUApp.forms import RegisterForm
from django.contrib.auth.models import User
from .models import User as MyUser
# Create your views here.

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User_Account(userName=request.GET.get('userName'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_users(request):
    response = {}
    try:
        users = User_Account.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# @require_http_methods(["POST"])
def user_register(request):
    response = {}
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        print(reg_form)
        try:
            if reg_form.is_valid():
                email = reg_form.cleaned_data['email']
                password = reg_form.cleaned_data['password']
                #创建用户
                user = User.objects.create_user(email,password)
                user.save()
                response['msg']= 'success'
                response['error_num'] = 0
                #注册完后登录
                user = auth.authenticate(email=email,password=password)
                auth.login(request,user)
                #redirect 将在合在一起后调用
                #return redirect('http://localhost:8080/#/pages/Main/main')
        except Exception as e:
            response['msg'] =str(e)
            response['error_num'] = 1

    return JsonResponse(response)


    # try:
    #     email = MyUser(email=request.POST.get('email'))
    #     password = MyUser(password=request.POST.get('password'))
    #     user = User.objects.create_user(email, password)
    #     user.save()
    #     response['msg'] = 'success'
    #     response['error_num'] = 0
    # except Exception as e:
    #     response['msg'] = str(e)
    #     response['error_num'] = 1