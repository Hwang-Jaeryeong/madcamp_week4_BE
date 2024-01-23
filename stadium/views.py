# stadium/views.py
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

from .models import Stadium
from .serializers import StadiumSerializer

class StadiumAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.selected_team:
            selected_team_id = user.selected_team.id
            stadium_data = Stadium.objects.filter(id=selected_team_id).values('team_name', 'stadium', 'stadium_image').first()

            if stadium_data:
                return Response(stadium_data, status=status.HTTP_200_OK)

        return Response({'detail': 'No selected team.'}, status=status.HTTP_403_FORBIDDEN)
class StadiumUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


