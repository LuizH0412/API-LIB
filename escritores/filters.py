from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from escritores.models import Escritor


class EscritorFilterClass(AutoRQLFilterClass):
    MODEL = Escritor
    