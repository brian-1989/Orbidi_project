from app.main import app
from faker import Faker
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)
fake = Faker()


def generate_random_place():
    place_name = fake.city()
    return place_name


random_place = generate_random_place()


def test_create_category():
    print(random_place)
    response = client.post(
        url="/api/v1/create_category",
        json={"place_name": random_place}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["place_name"] == random_place


def test_create_category_invalid_values():
    invalid_location_data = {"place_name": 272829}
    response = client.post(
        "/api/v1/create_category",
        json=invalid_location_data
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_category_repeated_value():
    invalid_location_data = {"place_name": random_place}
    response = client.post(
        "/api/v1/create_category",
        json=invalid_location_data
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
