from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_recomendations():
    response = client.get(url="/api/v1/get_recomendations")
    assert response.status_code == status.HTTP_200_OK
