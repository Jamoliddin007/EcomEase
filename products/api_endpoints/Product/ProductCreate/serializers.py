from rest_framework import serializers
from products.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'slug', 'default_images', 'is_active', 'category']
