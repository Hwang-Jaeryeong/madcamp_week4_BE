# serializers.py
from rest_framework import serializers
from .models import SelectedTeam

class SelectedTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedTeam
        fields = '__all__'
