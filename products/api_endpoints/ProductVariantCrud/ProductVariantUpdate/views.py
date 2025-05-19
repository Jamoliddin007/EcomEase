from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductVariant
from products.api_endpoints.ProductVariantCrud.ProductVariantUpdate.serializers import ProductVariantUpdateSerializer

class ProductVariantUpdateAPIView(APIView):
    def patch(self, request, id):
        try:
            variant = ProductVariant.objects.get(id=id)
        except ProductVariant.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductVariantUpdateSerializer(variant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
