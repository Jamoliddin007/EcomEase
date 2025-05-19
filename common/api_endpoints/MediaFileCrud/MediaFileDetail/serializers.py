from rest_framework import serializers
from common.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file', 'created_at', 'updated_at']
