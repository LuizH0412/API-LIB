from rest_framework import viewsets
from escritores.models import Escritor
from escritores.serializers import EscritorSerializer
from rest_framework.permissions import IsAuthenticated

class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer
    permission_classes = (IsAuthenticated,)


