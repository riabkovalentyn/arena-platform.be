from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player_profile')
    rating = models.FloatField(default=1500.0)
    games_played = models.PositiveIntegerField(default=0)
    kills = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    headshots = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} (Rating: {self.rating})"
    
    @property
    def kd_ratio(self):
        return round(self.kills / self.deaths, 2) if self.deaths > 0 else self.kills

