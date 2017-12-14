from django.contrib import admin

from .models import AggPlay, Drive, Game, Meta, Play,PlayPlayer, Player, Team

# Register your models here.
admin.site.register(AggPlay)
admin.site.register(Drive)
admin.site.register(Game)
admin.site.register(Meta)
admin.site.register(Play)
admin.site.register(PlayPlayer)
admin.site.register(Player)
admin.site.register(Team)
