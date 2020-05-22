from rest_framework import serializers
from .models import *
class MomentPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEEU_Moment
        fields ="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEEU_User
        fields ="__all__"