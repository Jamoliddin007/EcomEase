from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Color

class ColorDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            color = Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            return Response({'detail': 'Color not found.'}, status=status.HTTP_404_NOT_FOUND)

        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
