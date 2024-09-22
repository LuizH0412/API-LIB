from dj_rql.filter_cls import AutoRQLFilterClass
from emprestimos.models import Emprestimo

class EmprestimoFilterClass(AutoRQLFilterClass):
    MODEL = Emprestimo
    FILTERS = [
        {
            'filter': 'usuario',
            'source': 'usuario__username',
        },
        {
            'filter': 'livro',
            'source': 'livro__nome',
        }
    ]