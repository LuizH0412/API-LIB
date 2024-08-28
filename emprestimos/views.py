from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from emprestimos.models import Emprestimo
from emprestimos.serializers import EmprestimoSerializer
from rest_framework.permissions import IsAuthenticated
from emprestimos.filters import EmprestimoFilterClass


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [RQLFilterBackend]
    rql_filter_class = EmprestimoFilterClass
    
