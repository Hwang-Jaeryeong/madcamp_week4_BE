# models.py
from django.db import models

class SelectedTeam(models.Model):
    team_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
