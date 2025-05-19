from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductVariant

class ProductVariantDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            variant = ProductVariant.objects.get(pk=pk)
        except ProductVariant.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
