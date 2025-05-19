from django.urls import path
from common.api_endpoints import *

urlpatterns = [
    path('mediafiles/', MediaFileListAPIView.as_view(), name='mediafile-list'),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name='mediafile-create'),
    path('mediafiles/<int:id>/', MediaFileDetailAPIView.as_view(), name='mediafile-detail'),
    path('mediafiles/<int:id>/update/', MediaFileUpdateAPIView.as_view(), name='mediafile-update'),
    path('mediafiles/<int:id>/delete/', MediaFileDeleteAPIView.as_view(), name='mediafile-delete'),
]
