from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .serializers import ProductDetailSerializer

class ProductDetailAPIView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
