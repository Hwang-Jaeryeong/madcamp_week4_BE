# community/serializers.py

from rest_framework import serializers
from .models import Team, Vote, Player

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']

    def create(self, validated_data):
        # validated_data에서 'team' 필드를 올바르게 가져오는지 확인
        team_instance = validated_data.get('team')
        # 모델 인스턴스 생성 시 'team' 필드에 올바른 값이 들어가는지 확인
        player_instance = Player.objects.create(team=team_instance, **validated_data)
        return player_instance

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.nickname', read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'is_like', 'comment', 'user', 'created_at']

class DetailedPlayerSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'votes']

class DetailedTeamSerializer(serializers.ModelSerializer):
    players = DetailedPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'team_name', 'players']
