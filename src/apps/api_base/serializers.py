from rest_framework import serializers

from .models import Policial


class PolicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policial
        fields = "__all__"

    def validate_cpf(self, value):
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError(
                "CPF deve conter apenas números e ter 11 dígitos."
            )
        return value
