from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)

def test_location_category_reviewed():
    response = client.post(
        url="/api/v1/create_location_category_reviewed",
        json={
            "location_id": 4,
            "category_id": 4
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["location_id"] == 4
    assert response.json()["category_id"] == 4

def test_create_location_category_reviewed_invalid_values():
    response = client.post(
        "/api/v1/create_category",
        json={
            "location_id": "4",
            "category_id": "4"
        }
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
