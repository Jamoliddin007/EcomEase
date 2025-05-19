from django.urls import path

from products.api_endpoints import *



urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:id>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('brands/<int:id>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/', BrandListView.as_view(), name='brand-list-create'),
    path('brands/<int:id>/delete/', BrandDeleteView.as_view(), name='brand-delete'),
    path('brands/<int:id>/update/', BrandPatchView.as_view(), name='brand-update'),
    path('product/', ProductListAPIView.as_view(), name='product-list-create'),
    path('product/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product/<int:id>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('product/<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
]