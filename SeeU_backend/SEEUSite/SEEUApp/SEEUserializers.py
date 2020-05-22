from rest_framework import serializers

class MomentPublishSerializer(serializers.Serializer):
    video_url = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)