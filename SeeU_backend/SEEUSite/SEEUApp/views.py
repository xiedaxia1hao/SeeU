from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from .models import *
from SEEUApp.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
import json
# Create your views here.

#The method for create one user
@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = SEEU_User(userName=request.GET.get('userName'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#Used to display all users
@require_http_methods(["GET"])
def show_users(request):
    response = {}
    try:
        users =SEEU_User.objects.filter()
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



def user_login(request):
    response = {}
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        try:
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user=login_form.cleaned_data['user']
                if user is not None:
                    auth.login(request,user)
                    response['msg'] = 'success'
                    response['error_num'] = 0
        except Exception as e:
                # login_form=LoginForm()
                response['msg'] = str(e)
                response['error_num'] = 1

    return JsonResponse(request,safe=False)

#method for show all the moments so far
@require_http_methods(["GET"])
def show_moments(request):
    response ={}
    try:
        moments = SEEU_Moment.objects.order_by('-m_id')#desc order
        response['list']=json.loads(serializers.serialize("json", moments))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#once user login successfully show his info
# @require_http_methods(["GET"])
# def show_user_info(request):
