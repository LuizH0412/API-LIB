from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from generos.models import Genero

class GeneroFilterClass(AutoRQLFilterClass):
    MODEL = Genero