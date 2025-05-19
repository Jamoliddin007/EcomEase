from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.models import MediaFile
from common.api_endpoints.MediaFileCrud.MediaFileUpdate.serializers import MediaFileUpdateSerializer


class MediaFileUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            media = MediaFile.objects.get(id=id)
        except MediaFile.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MediaFileUpdateSerializer(media, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
