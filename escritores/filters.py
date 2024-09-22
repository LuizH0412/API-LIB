from dj_rql.filter_cls import AutoRQLFilterClass
from escritores.models import Escritor


class EscritorFilterClass(AutoRQLFilterClass):
    MODEL = Escritor
    