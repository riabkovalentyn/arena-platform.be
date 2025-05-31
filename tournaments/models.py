from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    nickname = models.CharField(max_length=100, unique=True)  
    steam_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Optional Steam ID
    rating = models.FloatField(default=1500.0) 
    games_played = models.PositiveIntegerField(default=0)  # Number of games played

    def __str__(self):
        return f"{self.nickname} - Rating: {self.rating}"

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    players = models.ManyToManyField(Player, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    teams = models.ManyToManyField(Team, related_name='tournaments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"
    

class Map(models.Model):
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
    
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2_matches')
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='matches')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    is_fineished = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_matches')

    def __str__(self):
        return f"{self.tournament.name}: {self.team1.name} vs {self.team2.name} on {self.map.name}"   

class MapResult(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='map_results')
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='map_results')
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='map_won_matches')

    def __str__(self):
        return f"{self.match.tournament.name}: {self.map.name} - {self.team1_score}:{self.team2_score}"     