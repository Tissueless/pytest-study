import requests
import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(api_client, user_id):
    response = api_client.get_user(user_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id

def test_get_user_detail(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["username"] == "Bret"
    assert "email" in data
    assert "address" in data
    assert "company" in data

def test_create_user(api_client):
    payload = {
        "name": "tester",
        "username": "qa_tester"
    }

    response = api_client.create_user(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "tester"
    assert data["username"] == "qa_tester"
    assert "id" in data

@pytest.mark.parametrize("user_id, expected_status", [
    (9999, 404),
    (99999, 404),
])
def test_get_user_not_found(api_client, user_id, expected_status):
    response = api_client.get_user(user_id)

    assert response.status_code == expected_status

    data = response.json()

    assert data["id"] == user_id