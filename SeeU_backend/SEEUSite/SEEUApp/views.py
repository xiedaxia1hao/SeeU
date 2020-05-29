from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.shortcuts import render
from django.contrib.sessions import serializers
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from SEEUApp.forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
import json
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from .SEEUserializers import *
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
# Create your views here.


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
# @login_required(login_url="/pages/index/logIn")
def show_specific_user(request,u_id):
    obj = SEEU_User.objects.get(u_id=u_id)

    context= {
        "object":obj
    }
    return render(request,"test.html",context)


class MomentPublishView(APIView):
    #method for show all the moments so far, interface 2
    def get(self,request,format=None):
        moments = SEEU_Moment.objects.order_by('-m_id')
        moments_serializer = MomentPublishSerializer(moments,many=True)
        return Response(moments_serializer.data,status=status.HTTP_200_OK)

class ShowUserView(APIView):
    def get(self,request,format=None):
        users = SEEU_User.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)

class UserViewSet(CreateModelMixin,viewsets.GenericViewSet):

    serializer_class = UserRegister
    queryset = SEEU_User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["email"] = user.email
        #frontend can get the token
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

class MomentCreateView(CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = MomentCreate

class UserLogViewSet(CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserLogin
    queryset = SEEU_User.objects.all()
    def create(self, request, *args, **kwargs):
        data = request.data
        res = UserLogin(data=data)
        if res.is_valid():
            return Response(res.validated_data)
        return Response(res.errors)

