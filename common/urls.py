from django.urls import path
from common.api_endpoints import *
from common.views import *
app_name = 'common'

urlpatterns = [
    path('mediafiles/', MediaFileListAPIView.as_view(), name='mediafile-list'),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name='mediafile-create'),
    path('mediafiles/<int:id>/', MediaFileDetailAPIView.as_view(), name='mediafile-detail'),
    path('mediafiles/<int:id>/update/', MediaFileUpdateAPIView.as_view(), name='mediafile-update'),
    path('mediafiles/<int:id>/delete/', MediaFileDeleteAPIView.as_view(), name='mediafile-delete'),
    path('index/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-details/', BlogDetailView.as_view(), name='blog-details'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('main/', MainView.as_view(), name='main'),
    path('shop-details/', ShopDetailView.as_view(), name='shop-details'),
    path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
    path('shoping-cart/', ShopingCartView.as_view(), name='shoping-cart'),

]
