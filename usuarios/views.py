from rest_framework import viewsets
from django.contrib.auth.models import User
from usuarios.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
