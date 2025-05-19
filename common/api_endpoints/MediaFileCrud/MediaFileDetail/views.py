from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import MediaFile
from common.api_endpoints.MediaFileCrud.MediaFileDetail.serializers import MediaFileSerializer


class MediaFileDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            media_file = MediaFile.objects.get(pk=pk)
        except MediaFile.DoesNotExist:
            return Response({"detail": "MediaFile not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MediaFileSerializer(media_file)
        return Response(serializer.data)
