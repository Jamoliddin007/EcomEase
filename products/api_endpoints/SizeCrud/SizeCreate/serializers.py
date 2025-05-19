from rest_framework import serializers
from products.models import Size

class SizeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name', 'slug']
