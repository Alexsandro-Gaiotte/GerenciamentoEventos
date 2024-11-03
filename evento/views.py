from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento
from django.views.generic import ListView
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     return render(request, "evento/Home/home.html")

def home(request):
    eventos = Evento.objects.all()
    print(eventos)
    return render(request, "evento/Home/home.html", {"eventos": eventos})

class EventoListView(ListView):
    model = Evento

class EventoCreateView(CreateView):
    model = Evento
    fields = ["titulo", "data", "local", "descricao", "idCriador"]

class TodoCreateView(CreateView):
    model = Evento
    fields = ["titulo", "data", "local", "descricao", "idCriador"]
    success_url = reverse_lazy("evento_list")