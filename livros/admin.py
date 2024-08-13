from django.contrib import admin
from livros.models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'escritor', 'genero', 'data_criado', 'ultima_atualizacao')
    search_fields = ('nome', 'escritor', 'genero',)
