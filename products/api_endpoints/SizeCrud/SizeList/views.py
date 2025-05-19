from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Size
from .serializers import SizeListSerializer

class SizeListAPIView(APIView):
    def get(self, request):
        sizes = Size.objects.all()
        serializer = SizeListSerializer(sizes, many=True)
        return Response(serializer.data)
