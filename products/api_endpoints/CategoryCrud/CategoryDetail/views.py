from rest_framework.generics import RetrieveAPIView
from products.models import Category
from products.api_endpoints.CategoryCrud.CategoryDetail.serializers import CategoryDetailSerializer

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'  