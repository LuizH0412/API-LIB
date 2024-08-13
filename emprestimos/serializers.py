from rest_framework import serializers
from emprestimos.models import Emprestimo
from datetime import timedelta

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
    
