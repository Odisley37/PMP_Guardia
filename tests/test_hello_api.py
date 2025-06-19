import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_hello_api():
    client = APIClient()
    response = client.get("/api/hello/")
    assert response.status_code == 200
    assert "message" in response.data
