from django.db import models
from generos.models import Genero
from escritores.models import Escritor

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    data_criado = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
