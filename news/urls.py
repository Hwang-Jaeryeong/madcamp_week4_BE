# news/urls.py
from django.urls import path
from .views import user_team_info

urlpatterns = [
    path('user_team_info/', user_team_info, name='user_team_info'),
]
