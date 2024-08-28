from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from livros.models import Livro


class LivroFilterClass(AutoRQLFilterClass):
    MODEL = Livro
    FILTERS = [
        {
            'filter': 'escritor',
            'source': 'escritor__nome',
        },
        {
            'filter': 'genero',
            'source': 'genero__nome',
        }
    ]