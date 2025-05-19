from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductVariant
from products.api_endpoints.ProductVariantCrud.ProductVariantList.serializers import ProductVariantListSerializer


class ProductVariantListAPIView(APIView):
    def get(self, request):
        variants = ProductVariant.objects.all()
        serializer = ProductVariantListSerializer(variants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
