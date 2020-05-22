from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from SEEUApp.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .SEEUserializers import MomentPublishSerializer,UserSerializer
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
                #create user
                user = User.objects.create_user(email,password)
                user.save()
                response['msg']= 'success'
                response['error_num'] = 0
                #login after sign up
                user = auth.authenticate(email=email,password=password)
                auth.login(request,user)
                #redirect
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


#once user login successfully show his info
@login_required(login_url="/pages/index/logIn")
@require_http_methods(["GET"])
def show_userInfo(request,id):
    response = {}
    try:
        specific_user = SEEU_User.objects.filter(id=id).values("username","clips","followers","followings")
        response['list'] = json.loads(serializers.serialize("json", specific_user))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


class MomentPublishView(APIView):
    #method for show all the moments so far, interface 3
    def get(self,request,format=None):
        moments = SEEU_Moment.objects.order_by('-m_id')
        moments_serializer = MomentPublishSerializer(moments,many=True)
        return Response(moments_serializer.data,status=status.HTTP_200_OK)
    # interface 2
    def post(self,request,format=None):
        moment_serializer = MomentPublishSerializer(data=request.data)
        if moment_serializer.is_valid():
            moment_serializer.save()
            return Response(moment_serializer.data,status= status.HTTP_201_CREATED)
        return Response(moment_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ShowUserView(APIView):
    def get(self,request,format=None):
        users = SEEU_User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)

# class UserViewSet()