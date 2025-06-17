from rest_framework import serializers
from products.models import Color

class ColorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'slug']
