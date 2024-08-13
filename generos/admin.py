from django.contrib import admin
from generos.models import Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criado', 'ultima_atualizacao')
    search_fields = ('nome',)
