from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Brand
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class BrandDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        brand = get_object_or_404(Brand, id=id)
        brand.delete()
        return Response({"detail": "Brand deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
