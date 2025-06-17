from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Size
from .serializers import SizeCreateSerializer

class SizeCreateAPIView(APIView):
    def post(self, request):
        serializer = SizeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
