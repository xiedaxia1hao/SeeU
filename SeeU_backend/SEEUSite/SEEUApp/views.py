from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from .models import User_Account
from SEEUApp.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
import json
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

# class UserAPIView(View):
#     def post(request):
#         json_bytes=request.body
#         json_str=json_bytes.decode()
#         user_dict=json.loads(json_str)
#         user = MyUser.objects.create(
#             email = user_dict.get('email'),
#             password = user_dict.get('password')
#         )
#         return JsonResponse(
#             {
#
#                 'email':user.email,
#                 'password':user.password
#
#             },status=201 #user create successful
#         )


# def user_register(request):
#     response = {}
#     registered = False
#     try:
#         if request.method =='POST':
#             user_form = UserForm(data=request.POST)
#             if user_form.is_valid():
#                 user=user_form.save()
#                 user.set_password(user.password)
#                 user.save()
#                 registered=True
#                 response['msg'] = 'success'
#                 response['error_num'] = 0
#
#             else:
#                 print(user_form.errors)
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
