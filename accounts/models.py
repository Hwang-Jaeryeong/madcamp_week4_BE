# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from llo.models import SelectedTeam

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=255, blank=True)
    selected_team = models.ForeignKey(SelectedTeam, null=True, blank=True, on_delete=models.SET_NULL)
