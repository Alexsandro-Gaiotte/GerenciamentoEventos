from django.shortcuts import render
from .models import Evento
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def evento_home(request):
    return render(request, "home.html")

class EventoListView(ListView):
    model = Evento

def evento_page(request, slug):
    evento = Evento.objects.get(slug=slug)
    return render(request, "evento/evento.html", {"evento": evento})

 # Verifica se o usuário está logado. Caso não esteja, será redirecionado para o login
class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    fields = ["titulo", "data", "local", "descricao", "imagem", "slug"]
    success_url = reverse_lazy("evento:evento_list")
    login_url = "/users/login/"  # URL para redirecionamento caso não esteja logado
    redirect_field_name = "next"  # Campo de redirecionamento após login

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adiciona a classe 'form-control' a todos os inputs, textareas e selects
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control m-3'})
        return form
    

    def form_valid(self, form):
        # Define o usuário logado como criador do evento
        form.instance.criador = self.request.user
        return super().form_valid(form)

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'evento/evento_confirm_delete.html'
    context_object_name = 'evento'
    success_url = reverse_lazy('evento:evento_list')

    # Redefinindo o método para garantir que apenas o criador possa excluir
    def get_queryset(self):
        return Evento.objects.filter(criador=self.request.user.id)


class EventoUpdateView(UpdateView):
    model = Evento
    fields = ['titulo', 'data', 'local', 'descricao', 'imagem', 'slug']
    template_name = 'evento/evento_edit.html'
    success_url = reverse_lazy('evento:evento_list')  # Redireciona após a edição
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adiciona a classe 'form-control' a todos os inputs, textareas e selects
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control m-3'})
        return form

    def get_queryset(self):
        return Evento.objects.filter(id=self.kwargs['pk'])
