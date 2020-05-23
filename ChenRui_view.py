  
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core import serializers
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

#Used to display a special user
@require_http_methods(["GET"])
def show_certain_user(request):
    response = {}
    
if 'uid' in request.GET:
    try:
        user =SEEU_User.objects.filter(u_id = request.GET[uid])
	response['list'] = json.loads(serializers.serialize("json", user))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#Used to display all moments of a special user
@require_http_methods(["GET"])
def show_certain_user(request):
    response = {}

if 'uid' in request.GET:
    try:
        moment = SEEU_Moment.objects.filter(u_id = request.GET[uid])
	response['list'] = json.loads(serializers.serialize("json", moment))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
