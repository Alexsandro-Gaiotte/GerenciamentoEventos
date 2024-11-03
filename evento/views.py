from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento
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
    fields = ["titulo", "data", "local", "descricao","imagem", "idCriador"]
    success_url = reverse_lazy("evento_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adiciona a classe 'form-control' a todos os inputs, textareas e selects
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})  # ou outra classe desejada
        return form

