from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from tournament.models import Tournament, Game

class TournamentListView(ListView):
    model = Tournament
    context_object_name = 'list'

class TournamentDetailView(DetailView):
    model = Tournament
    context_object_name = 'tourney'


class GameListView(ListView):
    model = Game
    context_object_name = 'list'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
