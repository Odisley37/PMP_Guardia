from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Policial
from .serializers import PolicialSerializer


class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response(
            {
                "token": token.key,
                "user_id": token.user.id,
                "username": token.user.username,
            }
        )


class PolicialViewSet(viewsets.ModelViewSet):
    queryset = Policial.objects.all()
    serializer_class = PolicialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra para mostrar apenas policiais do usuário logado
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associa automaticamente o usuário logado ao policial
        serializer.save(user=self.request.user)
