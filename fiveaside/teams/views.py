# django imports
from django.views.generic import ListView, DetailView

# model imports
from teams import models


class TeamList(ListView):
    context_object_name = 'teams'
    model = models.Team


class TeamDetail(DetailView):
    model = models.Team
