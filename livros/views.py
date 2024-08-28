from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from livros.models import Livro
from livros.serializers import LivroSerializer
from rest_framework.permissions import IsAuthenticated
from livros.filters import LivroFilterClass

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [RQLFilterBackend]
    rql_filter_class = LivroFilterClass
    
