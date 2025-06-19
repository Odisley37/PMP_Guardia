import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_login_api():
    # Criar usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")

    # Enviar requisição de login
    response = client.post(
        "/api/login/", {"username": "testuser", "password": "testpass"}, format="json"
    )

    assert response.status_code == 200
    assert "token" in response.data
    assert response.data["username"] == "testuser"


@pytest.mark.django_db
def test_protected_hello_api():
    user = User.objects.create_user(username="user2", password="12345")
    token = Token.objects.create(user=user)

    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = client.get("/api/hello/")

    assert response.status_code == 200
    assert "message" in response.data
