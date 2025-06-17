from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Size

class SizeDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
