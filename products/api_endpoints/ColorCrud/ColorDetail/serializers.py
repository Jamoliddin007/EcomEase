from rest_framework import serializers
from products.models import Color

class ColorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'slug']
