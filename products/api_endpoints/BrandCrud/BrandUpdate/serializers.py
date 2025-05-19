from rest_framework import serializers
from products.models import Brand

class BrandPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'logo'] 
