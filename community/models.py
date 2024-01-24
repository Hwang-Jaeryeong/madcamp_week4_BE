# community/models.py

from django.db import models
from accounts.models import CustomUser

class Team(models.Model):
    team_name = models.CharField(max_length=50)

class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    is_like = models.BooleanField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


