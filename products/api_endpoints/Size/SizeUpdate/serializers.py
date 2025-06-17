from rest_framework import serializers
from products.models import Size

class SizeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name', 'slug']
