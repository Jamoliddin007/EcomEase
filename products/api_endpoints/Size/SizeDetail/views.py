from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Size
from products.api_endpoints.Size.SizeDetail.serializers import SizeDetailSerializer

class SizeDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SizeDetailSerializer(size)
        return Response(serializer.data)
