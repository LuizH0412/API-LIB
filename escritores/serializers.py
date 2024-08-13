from rest_framework import serializers
from escritores.models import Escritor


class EscritorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escritor
        fields = '__all__'