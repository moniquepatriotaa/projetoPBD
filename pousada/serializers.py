from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = "__all__"


class ComodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comodo
        fields = "__all__"




class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reserva
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user