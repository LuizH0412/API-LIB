from django.shortcuts import render
from rest_framework import viewsets
from livros.models import Livro
from livros.serializers import LivroSerializer
from rest_framework.permissions import IsAuthenticated

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = (IsAuthenticated,)
    
