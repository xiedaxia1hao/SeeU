from django.forms import ValidationError
from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password,check_password
class MomentPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEEU_Moment
        fields ="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEEU_User
        fields ="__all__"

class UserLogin(serializers.ModelSerializer):

    email = serializers.EmailField(allow_blank=False,required=True)
    password = serializers.CharField(allow_blank=False, required=True,
                                     style={'input_type': 'password'})
    class Meta:
        model = SEEU_User
        fields = ['email', 'password']

    def validate(self, attrs):
        user_obj = SEEU_User.objects.filter(email = attrs['email'])
        print(user_obj)
        if user_obj:
            if check_password(attrs['password'],user_obj.password):
                return attrs
        raise ValidationError('Email or password is wrong!')

class UserRegister(serializers.ModelSerializer):

    #check whether the user has already exists
    email = serializers.EmailField(allow_blank=False,required=True,
                                   validators=[UniqueValidator(queryset=SEEU_User.objects.all(),message="user already exists")]
                                   )
    password = serializers.CharField(allow_blank=False,required=True,
                                     style={'input_type':'password'})

    class Meta:
        model = SEEU_User
        fields = ['email', 'password']

class MomentCreate(serializers.ModelSerializer):
    class Meta:
        model = SEEU_Moment
        fields = ['video_url','location','u_id']