from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HelloSerializer


class HelloAPI(APIView):
    def get(self, request):
        return Response(
            {"message": "API funcionando com sucesso!"}, status=status.HTTP_200_OK
        )


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
