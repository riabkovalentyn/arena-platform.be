from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'games_played', 'kills', 'deaths', 'kd_ratio')
