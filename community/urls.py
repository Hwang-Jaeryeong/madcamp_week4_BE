# community/urls.py

from django.urls import path
from .views import TeamCreateView, PlayerVoteStatsView, TeamDetailView, VoteCreateView, PlayerListView

urlpatterns = [
    path('team/create/', TeamCreateView.as_view(), name='team-create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('vote/create/', VoteCreateView.as_view(), name='vote-create'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('vote/stats/<int:pk>/', PlayerVoteStatsView.as_view(), name='player-vote-stats'),
]

