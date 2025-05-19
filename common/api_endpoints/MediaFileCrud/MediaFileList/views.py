from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import MediaFile
from common.api_endpoints.MediaFileCrud.MediaFileList.serializers import MediaFileListSerializer

class MediaFileListAPIView(APIView):
    def get(self, request):
        mediafiles = MediaFile.objects.all()
        serializer = MediaFileListSerializer(mediafiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
