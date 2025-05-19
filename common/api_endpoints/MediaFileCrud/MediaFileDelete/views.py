from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import MediaFile


class MediaFileDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            media = MediaFile.objects.get(pk=pk)
        except MediaFile.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
