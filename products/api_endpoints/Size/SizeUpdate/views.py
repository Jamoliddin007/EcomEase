from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Size
from products.api_endpoints.Size.SizeUpdate.serializers import SizeUpdateSerializer

class SizeRetrieveUpdateDestroyView(APIView):
    def patch(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SizeUpdateSerializer(size, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
