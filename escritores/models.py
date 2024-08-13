from django.db import models

class Escritor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    data_falecimento = models.DateField(null=True, blank=True)
    idade = models.IntegerField()
    nacionalidade = models.CharField(max_length=20)
    data_criado = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'escritores'

    def __str__(self):
        return self.nome
    