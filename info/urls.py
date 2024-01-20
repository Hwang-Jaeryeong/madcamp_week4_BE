from django.urls import path
from .views import get_fixtures, get_predictions

urlpatterns = [
    path('get_fixtures/', get_fixtures, name='get_fixtures'),
    path('get_predictions/<int:fixture_id>/', get_predictions, name='get_predictions'),
]