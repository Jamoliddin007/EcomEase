from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
]