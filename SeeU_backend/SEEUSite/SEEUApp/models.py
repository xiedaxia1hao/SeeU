from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class User_Account(models.Model):
    userName=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __unicode__(self):
        return self.userName

class User(models.Model):
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=16,validators=[MinLengthValidator(8)])

    def __unicode__(self):
        return self.email

