# django imports
from django.views.generic import (ListView, DetailView, UpdateView,
                                  CreateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
# model imports
from teams import models


class TeamList(ListView):
    context_object_name = 'teams'
    model = models.Team


class TeamDetail(DetailView):
    model = models.Team


class TeamCreate(CreateView):
    fields = ['name', 'coach']
    model = models.Team


class TeamUpdate(UpdateView):
    fields = ['name', 'coach']
    model = models.Team


class TeamDelete(DeleteView):
    model = models.Team
    success_url = reverse_lazy('teams:list')
