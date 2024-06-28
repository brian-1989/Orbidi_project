from app.main import app
from fastapi import status
from fastapi.testclient import TestClient
import random
from decimal import Decimal

def generate_random_coordinates():
    latitude = Decimal(random.uniform(-90.0, 90.0))
    longitude = Decimal(random.uniform(-180.0, 180.0))
    return format(latitude, ".4f"), format(longitude, ".4f")

client = TestClient(app)

def test_create_location():
    lat_long = generate_random_coordinates()
    location_data = {
        "latitude": float(lat_long[0]),
        "longitude": float(lat_long[1])
    }
    response = client.post(
        url="/api/v1/create_location",
        json=location_data
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["latitude"] == location_data["latitude"]
    assert response.json()["longitude"] == location_data["longitude"]

def test_create_location_invalid_values():
    invalid_location_data = {"latitude": "invalid", "longitude": "invalid"}
    response = client.post(
        "/api/v1/create_location",
        json=invalid_location_data
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
