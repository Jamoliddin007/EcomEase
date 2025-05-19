from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Brand
from products.api_endpoints.BrandCrud.BrandUpdate.serializers import BrandPatchSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser

class BrandPatchView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, id):
        brand = get_object_or_404(Brand, id=id)
        serializer = BrandPatchSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
