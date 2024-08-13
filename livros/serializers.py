from rest_framework import serializers
from livros.models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

    
    def validate_paginas(self, value):
        if value < 10:
            raise serializers.ValidationError("O livro deve conter no minimo 10 páginas.")
        else:
            return value