import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from apps.api_base.models import Policial


# Fixtures
@pytest.fixture
def user(db):
    return User.objects.create_superuser(
        username="testadmin", password="testpass123", email="admin@test.com"
    )


@pytest.fixture
def user(db):
    return User.objects.create_user(username="teste", password="123456")


@pytest.fixture
def token(user):
    return Token.objects.create(user=user)


@pytest.fixture
def api_client(token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.fixture
def policial_data(user):
    return {
        "user": user,  # Instância de User
        "nome_completo": "João Teste",
        "nome_guerra": "JT",
        "nome_mae": "Maria Teste",
        "nome_pai": "José Teste",
        "data_nascimento": "1990-01-01",
        "matricula": "MAT1234",
        "identidade_militar": "IDM1234",
        "cpf": "12345678900",
        "posto_graduacao": "SD",
        "sexo": "M",
        "tipagem_sanguinea": "O",
        "fator_rh": "+",
        "data_ingresso": "2010-01-01",
        "funcao": "PATRULHEIRO",
        "endereco": "Rua Teste",
        "telefone": "(99)99999-9999",
    }


@pytest.fixture
def policial(policial_data):
    return Policial.objects.create(**policial_data)


# Testes
@pytest.mark.django_db
def test_list_policiais(api_client, policial):
    response = api_client.get("/api/policiais/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["nome_completo"] == policial.nome_completo


@pytest.mark.django_db
def test_create_policial(api_client, user):
    data = {
        # Não envie user_id, será automaticamente associado
        "nome_completo": "Maria Souza",
        "nome_guerra": "Souza",
        "nome_mae": "Josefa Souza",
        "nome_pai": "Carlos Souza",
        "data_nascimento": "1991-05-05",
        "matricula": "MAT5678",
        "identidade_militar": "IDM5678",
        "cpf": "98765432100",
        "posto_graduacao": "CB",
        "sexo": "F",
        "tipagem_sanguinea": "A",
        "fator_rh": "-",
        "data_ingresso": "2012-03-15",
        "funcao": "ADMINISTRATIVO",
        "endereco": "Av. Central",
        "telefone": "(98)99999-8888",
    }
    response = api_client.post("/api/policiais/", data, format="json")
    assert response.status_code == 201
    assert Policial.objects.count() == 1
    assert Policial.objects.first().user == user


@pytest.mark.django_db
def test_update_policial(api_client, policial):
    url = f"/api/policiais/{policial.id}/"
    new_data = {"nome_guerra": "JT-Atualizado"}
    response = api_client.patch(url, new_data, format="json")
    assert response.status_code == 200
    policial.refresh_from_db()
    assert policial.nome_guerra == "JT-Atualizado"


@pytest.mark.django_db
def test_delete_policial(api_client, policial):
    initial_count = Policial.objects.count()
    url = f"/api/policiais/{policial.id}/"
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Policial.objects.count() == initial_count - 1


@pytest.mark.django_db
def test_unauthenticated_access():
    client = APIClient()  # Client sem autenticação
    response = client.get("/api/policiais/")
    assert response.status_code == 401  # Não autorizado
