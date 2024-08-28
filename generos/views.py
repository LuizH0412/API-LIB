from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from generos.filters import GeneroFilterClass
from generos.models import Genero
from generos.serializers import GeneroSerializer
from rest_framework.permissions import IsAuthenticated

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [RQLFilterBackend]
    rql_filter_class = GeneroFilterClass
