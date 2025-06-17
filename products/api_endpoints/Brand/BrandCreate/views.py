
from rest_framework.generics import RetrieveAPIView
from products.models import Brand
from products.api_endpoints.BrandCrud.BrandDetail.serializers import BrandDetailSerializer

class BrandDetailView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    lookup_field = 'id'
