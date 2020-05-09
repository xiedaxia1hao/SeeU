from django import forms
from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=16,min_length=8)
    password_again = forms.CharField(max_length=16,min_length=8)

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).count()>0:
            raise forms.ValidationError('Email already exists')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('Two passwords are not the same!')
        return password_again