# stadium/models.py


from django.db import models
from accounts.models import CustomUser

class Stadium(models.Model):
    team_name = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)
    stadium_image = models.ImageField(upload_to='team_logos/', null=True, blank=True)

    def __str__(self):
        return self.team_name