from django.contrib import admin
from escritores.models import Escritor

@admin.register(Escritor)
class EscritorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'nacionalidade', 'data_criado', 'ultima_atualizacao')
    search_fields = ('nome',)

