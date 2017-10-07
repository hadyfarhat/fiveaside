from django.contrib import admin

from .models import Team, Player


class PlayerInline(admin.TabularInline):
    model = Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "team"]


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, ]


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
