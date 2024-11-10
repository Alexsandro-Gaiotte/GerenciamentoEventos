from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    slug = models.SlugField(blank=False, null=False, unique=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos', null= False, blank=False, default=4)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return self.titulo