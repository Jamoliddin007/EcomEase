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
    path('product_variants/', ProductVariantListAPIView.as_view(), name='product-variant-list-create'),
    path('product_variants/<int:id>/', ProductVariantDetailAPIView.as_view(), name='product-variant-detail'),
    path('product_variants/<int:id>/delete/', ProductVariantDeleteAPIView.as_view(), name='product-variant-delete'),
    path('product_variants/<int:id>/update/', ProductVariantUpdateAPIView.as_view(), name='product-variant-update'),
    path('product_variants/', ProductVariantCreateAPIView.as_view(), name='product-variant-list-create'),
    path('colors/', ColorListAPIView.as_view(), name='color-list-create'),  
    path('colors/<int:id>/', ColorDetailAPIView.as_view(), name='color-detail'),
    path('colors/<int:id>/delete/', ColorDeleteAPIView.as_view(), name='color-delete'),
    path('colors/<int:id>/update/', ColorUpdateAPIView.as_view(), name='color-update'),
    path('colors/', ColorCreateAPIView.as_view(), name='color-list-create'),
    path('sizes/', SizeListAPIView.as_view(), name='size-list-create'),
    path('sizes/<int:id>/', SizeDetailAPIView.as_view(), name='size-detail'),
    path('sizes/<int:id>/delete/', SizeDeleteAPIView.as_view(), name='size-delete'),
    path('sizes/<int:id>/update/', SizeUpdateAPIView.as_view(), name='size-update'),
    path('sizes/', SizeCreateAPIView.as_view(), name='size-list-create'),

]