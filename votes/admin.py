from django.contrib import admin

from votes.models import Game, Vote

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)
