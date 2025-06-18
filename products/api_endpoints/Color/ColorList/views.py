from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Color
from products.api_endpoints.Color.ColorList.serializers import ColorListSerializer


class ColorListCreateView(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorListSerializer(colors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

