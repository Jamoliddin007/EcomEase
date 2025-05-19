from rest_framework import serializers
from products.models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'slug', 'default_images', 'is_active', 'category']
