# stadium/models.py


from django.db import models
from accounts.models import CustomUser

class Stadium(models.Model):
    team_name = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)
    stadium_image = models.ImageField(upload_to='stadium_images/', null=True, blank=True)
    teamId = models.IntegerField(max_length=255)

    def __str__(self):
        return self.team_name