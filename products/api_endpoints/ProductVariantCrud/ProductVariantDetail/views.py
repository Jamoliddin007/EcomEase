from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductVariant
from products.api_endpoints.ProductVariantCrud.ProductVariantDetail.serializers import ProductVariantDetailSerializer

class ProductVariantDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            variant = ProductVariant.objects.get(pk=pk)
        except ProductVariant.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductVariantDetailSerializer(variant)
        return Response(serializer.data)
