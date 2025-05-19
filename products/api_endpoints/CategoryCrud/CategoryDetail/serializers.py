from rest_framework import serializers
from products.models import Category, Product

class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'default_images']

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products']
        read_only_fields = ['id', 'slug']
