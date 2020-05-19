from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class SEEU_User(models.Model):
    u_id = models.AutoField(db_column='uid', primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8)])
    clips = models.IntegerField()
    followings = models.IntegerField()
    followers = models.IntegerField()
    sex = models.CharField(max_length=10)

    def __unicode__(self):
        return self.email

class SEEU_Moment(models.Model):
    m_id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    video_url =models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    u_id = models.ForeignKey(SEEU_User,on_delete=models.CASCADE)

class SEEU_User_Following(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=255)
    following_id = models.ManyToManyField(SEEU_User)

class SEEU_User_Followed(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=255)
    followed_id = models.ManyToManyField(SEEU_User)
