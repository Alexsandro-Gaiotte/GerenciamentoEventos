from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(auto_now_add=True, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.DateField(null=False, blank=False)
    idCriador = models.TextField(null=True)
