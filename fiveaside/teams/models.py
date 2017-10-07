from django.db import models

POSITIONS = [
    ('GK', 'Goalkeeper'),
    ('DEF', 'Defender'),
    ('MID', 'Midfielder'),
    ('FW', 'Forward'),
]


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(choices=POSITIONS, max_length=255)
    team = models.ForeignKey(Team, related_name="players")

    def __str__(self):
        return "{name} plays for {team}".format(name=self.name, team=self.team)
