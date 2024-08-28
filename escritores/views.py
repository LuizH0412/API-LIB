from rest_framework import viewsets
from dj_rql.drf import RQLFilterBackend
from escritores.models import Escritor
from escritores.serializers import EscritorSerializer
from rest_framework.permissions import IsAuthenticated
from escritores.filters import EscritorFilterClass

class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [RQLFilterBackend]
    rql_filter_class = EscritorFilterClass


