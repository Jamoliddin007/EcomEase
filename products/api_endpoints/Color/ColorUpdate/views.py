from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Color
from products.api_endpoints.Color.ColorUpdate.serializers import ColorUpdateSerializer


class ColorUpdateAPIView(APIView):
    def patch(self, request, pk):
        try:
            color = Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            return Response({'detail': 'Color not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ColorUpdateSerializer(color, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
