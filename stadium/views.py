from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stadium
from .serializers import StadiumSerializer

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

    def post(self, request):
        user = request.user

        if user.selected_team:
            team_name = request.data.get('team_name')
            stadium_name = request.data.get('stadium')
            stadium_image = request.data.get('stadium_image')

            # 이미지 파일 저장
            stadium = Stadium.objects.create(team_name=team_name, stadium=stadium_name, stadium_image=stadium_image)

            return Response({'detail': f'Stadium information for {team_name} added successfully.'}, status=status.HTTP_201_CREATED)

        return Response({'detail': 'No selected team.'}, status=status.HTTP_403_FORBIDDEN)

class StadiumUploadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        team_name = request.data.get('team_name')
        stadium_name = request.data.get('stadium')
        stadium_image = request.data.get('stadium_image')

        try:
            # 이미지 파일 저장
            stadium = Stadium.objects.get(team_name=team_name)
            stadium.stadium_image = stadium_image
            stadium.save()
        except Stadium.DoesNotExist:
            raise Http404(f"Stadium matching query does not exist for team '{team_name}'.")

        return Response({'detail': f'Stadium information for {team_name} updated successfully.'}, status=status.HTTP_200_OK)


