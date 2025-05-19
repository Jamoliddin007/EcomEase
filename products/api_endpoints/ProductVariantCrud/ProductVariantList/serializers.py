from rest_framework import serializers
from products.models import ProductVariant
from common.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file']


class ProductVariantListSerializer(serializers.ModelSerializer):
    images = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = ProductVariant
        fields = [
            'id', 'name', 'price', 'stock', 'is_active',
            'color', 'size', 'product', 'images'
        ]
