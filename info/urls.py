from django.urls import path
from .views import get_fixtures, get_predictions, GetLineupPredictions,GetFixtureEvents, GetStandings, get_top_scorers, get_match

urlpatterns = [
    path('get_fixtures/', get_fixtures, name='get_fixtures'),
    path('get_predictions/<int:fixture_id>/', get_predictions, name='get_predictions'),
    path('get_lineup_predictions/<int:fixture_id>/', GetLineupPredictions.as_view(), name='get_lineup_predictions'),
    path('get_events/<int:fixture_id>/', GetFixtureEvents.as_view(), name='get_fixture_events'),
    path('get_standings/', GetStandings.as_view(), name='get_standings'),
    path('get_top_scorers/', get_top_scorers, name='get_top_scorers'),
    path('get_match/', get_match, name='get_match'),
]