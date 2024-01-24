# community/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Team, Vote, Player
from rest_framework import status
from .serializers import TeamSerializer, VoteSerializer, PlayerSerializer, DetailedPlayerSerializer, DetailedTeamSerializer

class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerCreateView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer  # 변경된 부분

class TeamDetailView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = DetailedTeamSerializer


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        selected_team_id = self.request.user.selected_team_id
        player_id = self.request.data.get('player')
        player = Player.objects.get(id=player_id, team_id=selected_team_id)
        serializer.save(user=self.request.user, player=player)

class PlayerVoteStatsView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get(self, request, *args, **kwargs):
        player_id = self.kwargs['pk']
        player = self.get_object()

        total_votes = Vote.objects.filter(player=player).count()
        likes = Vote.objects.filter(player=player, is_like=True).count()
        dislikes = total_votes - likes

        vote_percentage = {
            'likes': (likes / total_votes) * 100 if total_votes > 0 else 0,
            'dislikes': (dislikes / total_votes) * 100 if total_votes > 0 else 0,
        }

        comments = Vote.objects.filter(player=player).order_by('-created_at')
        serializer = VoteSerializer(comments, many=True)

        response_data = {
            'vote_percentage': vote_percentage,
            'comments': serializer.data
        }

        return Response(response_data)


class PlayerListView(generics.ListAPIView):
    serializer_class = DetailedPlayerSerializer

    def get_queryset(self):
        selected_team_id = self.request.user.selected_team_id
        return Player.objects.filter(team_id=selected_team_id).order_by('id')
