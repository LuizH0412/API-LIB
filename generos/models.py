from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_criado = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
