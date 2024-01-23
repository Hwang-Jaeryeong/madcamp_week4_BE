from rest_framework import serializers
from .models import Stadium

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ('team_name', 'stadium', 'stadium_image')
