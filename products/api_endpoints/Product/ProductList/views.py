from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from .serializers import ProductListSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
