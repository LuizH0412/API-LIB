from django.shortcuts import render
from rest_framework import viewsets
from emprestimos.models import Emprestimo
from emprestimos.serializers import EmprestimoSerializer
from rest_framework.permissions import IsAuthenticated


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = (IsAuthenticated,)
    
