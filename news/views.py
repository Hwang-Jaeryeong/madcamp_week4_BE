# news/views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import CustomUser
from llo.models import SelectedTeam

@api_view(['GET'])
def user_team_info(request):
    user = request.user  # 현재 로그인한 사용자
    if user.is_authenticated:
        selected_team = user.selected_team

        if selected_team:
            logo_url = request.build_absolute_uri(selected_team.logo.url)
            response_data = {
                'logo_url': logo_url,
                'team_name': selected_team.team_name,
                'news_text': f"{selected_team.team_name} News"
            }
            return Response(response_data)
        else:
            return Response({'error': 'No team selected for the user.'}, status=400)
    else:
        return Response({'error': 'User not authenticated.'}, status=401)

