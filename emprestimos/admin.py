from django.contrib import admin
from emprestimos.models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'status')
    search_fields = ('usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'status')
