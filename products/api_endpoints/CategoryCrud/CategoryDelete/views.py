from rest_framework.generics import DestroyAPIView
from products.models import Category
from .serializers import CategoryDeleteSerializer

class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field = 'id'  
