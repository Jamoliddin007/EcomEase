from rest_framework.generics import ListAPIView
from products.models import Brand
from .serializers import BrandListSerializer

class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
