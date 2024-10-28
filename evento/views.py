from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento

# Create your views here.
# def home(request):
#     return render(request, "evento/Home/home.html")

def home(request):
    eventos = Evento.objects.all()
    print(eventos)
    return render(request, "evento/Home/home.html", {"eventos": eventos})
