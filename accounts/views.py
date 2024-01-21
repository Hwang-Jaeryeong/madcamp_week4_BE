# accounts/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer
from llo.models import SelectedTeam

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    serializer = CustomUserSerializer(data=data)
    selected_team_id = request.data.get('selected_team')  # 'selected_team'로부터 팀 ID를 받아옴
    if serializer.is_valid():
        user = serializer.save()

        # 선택한 팀 정보를 사용자와 연결
        if selected_team_id:
            selected_team = SelectedTeam.objects.get(id=selected_team_id)
            user.selected_team = selected_team
            user.save()

        return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # 이메일로 유저 찾기
    user = CustomUser.objects.filter(email=email).first()

    # 유저가 존재하고 비밀번호가 일치하면
    if user and user.password == password:
        refresh = RefreshToken.for_user(user)
        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'email': user.email,
            'username': user.username,
            'phone_number': user.phone_number,
            'nickname': user.nickname,
        }
        return Response(data, status=status.HTTP_200_OK)

    # 인증 실패
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    # You can add additional logout logic here if needed
    return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)
