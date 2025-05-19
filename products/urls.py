from django.urls import path

from products.api_endpoints import *



urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:id>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('brands/<int:id>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/', BrandListView.as_view(), name='brand-list-create'),
    
]