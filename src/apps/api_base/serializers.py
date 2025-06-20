from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Agressor, Assistida, Guarnicao, GuarnicaoIntegrante, Policial


class PolicialSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="user",
        write_only=True,
        required=False,  # Torna opcional para permitir que a view associe automaticamente
    )

    class Meta:
        model = Policial
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}  # O campo user será tratado apenas internamente
        }

    def validate_cpf(self, value):
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError(
                "CPF deve conter apenas números e ter 11 dígitos."
            )
        return value


class GuarnicaoIntegranteSerializer(serializers.ModelSerializer):
    policial = PolicialSerializer(read_only=True)
    policial_id = serializers.PrimaryKeyRelatedField(
        queryset=Policial.objects.all(), source="policial", write_only=True
    )

    class Meta:
        model = GuarnicaoIntegrante
        fields = ["id", "guarnicao", "policial", "policial_id", "funcao"]


class GuarnicaoSerializer(serializers.ModelSerializer):
    integrantes = GuarnicaoIntegranteSerializer(many=True, read_only=True)

    class Meta:
        model = Guarnicao
        fields = "__all__"


class AgressorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agressor
        fields = "__all__"


class AssistidaSerializer(serializers.ModelSerializer):
    agressor = AgressorSerializer()
    guarnicao = GuarnicaoSerializer()

    class Meta:
        model = Assistida
        fields = "__all__"
