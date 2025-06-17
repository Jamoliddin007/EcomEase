from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Color
from products.api_endpoints.Color.ColorDetail.serializers import ColorDetailSerializer


class ColorDetailAPIView(APIView):
    def get(self, request, id):
        try:
            color = Color.objects.get(id=id)
        except Color.DoesNotExist:
            return Response({'detail': 'Color not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ColorDetailSerializer(color)
        return Response(serializer.data)
