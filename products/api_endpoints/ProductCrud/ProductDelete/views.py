from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product

class ProductDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
