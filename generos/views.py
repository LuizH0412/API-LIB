from rest_framework import viewsets
from generos.models import Genero
from generos.serializers import GeneroSerializer
from rest_framework.permissions import IsAuthenticated

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = (IsAuthenticated,)
