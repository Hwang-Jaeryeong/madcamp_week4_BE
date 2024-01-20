from django.urls import path
from .views import get_fixtures, get_predictions, GetLineupPredictions

urlpatterns = [
    path('get_fixtures/', get_fixtures, name='get_fixtures'),
    path('get_predictions/<int:fixture_id>/', get_predictions, name='get_predictions'),
    path('get_lineup_predictions/<int:fixture_id>/', GetLineupPredictions.as_view(), name='get_lineup_predictions'),
]