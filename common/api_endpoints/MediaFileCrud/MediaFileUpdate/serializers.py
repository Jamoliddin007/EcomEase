from rest_framework import serializers
from common.models import MediaFile


class MediaFileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['file'] 
