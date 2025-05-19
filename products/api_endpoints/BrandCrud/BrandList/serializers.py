from rest_framework import serializers
from products.models import Brand, Product

class ProductNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'is_active']
        ref_name = "BrandListProductNestedSerializer_ProductNested"

class BrandListSerializer(serializers.ModelSerializer):
    products = ProductNestedSerializer(many=True, read_only=True, source='product_set')

    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'products']
        ref_name = "BrandListSerializer"