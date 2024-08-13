from django.db import models
from django.contrib.auth.models import User
from livros.models import Livro

STATUS_EMPRESTIMO = (
    ('Pen', 'Pendente'),
    ('Dev', 'Devolvido'),
)

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    status = models.CharField(
        max_length=10, 
        choices=STATUS_EMPRESTIMO,
        default='Pendente'
        )
    
    def __str__(self):
        return f'Livro {self.livro} emprestado a {self.usuario}'

