from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    slug = models.SlugField(blank=False, null=False, unique=True)
    idCriador = models.CharField(null=True, max_length=100)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return self.titulo