from test_data.users import CREATE_USER_PAYLOAD, UPDATE_USER_PAYLOAD
import requests
import pytest

from tests.helpers import (
    assert_status,
    assert_json_response,
    assert_required_fields,
    assert_response_data,
    assert_success_json_response
)

@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(api_client, user_id):
    response = api_client.get_user(user_id)

    assert_status(response, 200)
    assert_json_response(response)

    data = response.json()

    assert data["id"] == user_id

def test_get_user_detail(api_client):
    response = api_client.get_user(1)

    assert_status(response, 200)
    assert_json_response(response)

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["username"] == "Bret"
    assert "email" in data
    assert "address" in data
    assert "company" in data

@pytest.mark.api
def test_create_user(api_client):
    response = api_client.create_user(CREATE_USER_PAYLOAD)

    assert_status(response, 201)
    assert_json_response(response)

    data = response.json()

    assert_required_fields(data, ["id", "name", "username"])

    print("RESPONSE:", data)
    

@pytest.mark.parametrize("user_id, expected_status", [
    (9999, 404),
    (99999, 404),
])
def test_get_user_not_found(api_client, user_id, expected_status):
    response = api_client.get_user(user_id)

    assert_status(response, expected_status)

def test_create_user_with_empty_payload(api_client):
    response = api_client.create_user({})

    print(response.status_code)
    print(response.json())

    assert_status(response, 201)
    assert_json_response(response)

@pytest.mark.api
def test_update_user(api_client):
    response = api_client.update_user(1, UPDATE_USER_PAYLOAD)

    assert_status(response, 200)
    assert_json_response(response)

    data = response.json()

    assert_required_fields(data, ["id", "name", "username"])

    assert_response_data(
        data,
        {
            "name": UPDATE_USER_PAYLOAD["name"],
            "username": UPDATE_USER_PAYLOAD["username"]
        }
    )

@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_delete_user(api_client, user_id):
    response = api_client.delete_user(user_id)

    assert_status  (response, 200)

def test_api_client_auth_header(api_client):
    assert api_client.session.headers["Authorization"] == "Bearer test-token-123"

@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_data_type(api_client, user_id):
    response = api_client.get_user(user_id)

    assert_status(response, 200)

    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

@pytest.mark.api
def test_get_user_required_fields(api_client):
    response = api_client.get_user(1)

    assert_status(response, 200)

    data = response.json()

    assert_required_fields(
        data,
        [
            "id",
            "name",
            "username",
            "email",
            "address",
            "phone",
            "website",
            "company"
        ]
    )

@pytest.mark.api
@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])
def test_get_user_name(api_client, user_id, expected_name):
    response = api_client.get_user(user_id)

    assert_status(response, 200)

    data = response.json()

    assert data["name"] == expected_name

@pytest.mark.api
def test_get_user_response_schema(api_client):
    response = api_client.get_user(1)

    assert_status(response, 200)

    data = response.json()

    expected_schema = {
        "id": int,
        "name": str,
        "username": str,
        "email": str,
        "address": dict,
        "phone": str,
        "website": str,
        "company": dict,
    }

    for field, expected_type in expected_schema.items():
        assert field in data
        assert isinstance(data[field], expected_type)

@pytest.mark.api
def test_get_user_nested_fields(api_client):
    response = api_client.get_user(1)

    assert_status(response, 200)

    data = response.json()

    # address 검증
    assert "address" in data
    assert isinstance(data["address"], dict)

    assert "street" in data["address"]
    assert "suite" in data["address"]
    assert "city" in data["address"]
    assert "zipcode" in data["address"]
    assert "geo" in data["address"]

    # geo 검증
    assert isinstance(data["address"]["geo"], dict)
    assert "lat" in data["address"]["geo"]
    assert "lng" in data["address"]["geo"]

    # company 검증
    assert "company" in data
    assert isinstance(data["company"], dict)

    assert "name" in data["company"]
    assert "catchPhrase" in data["company"]
    assert "bs" in data["company"]

@pytest.mark.api
@pytest.mark.parametrize("user_id", [
    0,
    -1,
    9999,
])
def test_get_user_invalid_id(api_client, user_id):
    response = api_client.get_user(user_id)

    assert_status(response, 404)

@pytest.mark.api
@pytest.mark.parametrize("payload", [
    {
        "name": "tester",
        "username": "qa_tester"
    },
    {
        "name": "automation",
        "username": "qa_automation"
    },
    {
        "name": "api_test",
        "username": "api_tester"
    }
])
def test_create_user_with_valid_payload(api_client, payload):
    response = api_client.create_user(payload)

    assert_status(response, 201)
    assert_json_response(response)

    data = response.json()

    assert_required_fields(
        data,
        ["id", "name", "username"]
    )

    assert_response_data(
        data,
        {
            "name": payload["name"],
            "username": payload["username"]
        }
    )

@pytest.mark.api
@pytest.mark.parametrize("payload", [
    {},
    {"name": ""},
    {"username": ""},
    {"name": "", "username": ""},
])
def test_create_user_with_invalid_payload(api_client, payload):
    response = api_client.create_user(payload)

    print(f"\nPayload: {payload}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    assert response.status_code == 201

@pytest.mark.api
@pytest.mark.parametrize(
    "payload",
    [
        {
            "name": "updated_user",
            "username": "updated_qa"
        },
        {
            "name": "automation_user",
            "username": "automation_qa"
        },
        {
            "name": "api_user",
            "username": "api_qa"
        }
    ]
)
def test_update_user_with_valid_payload(api_client, payload):
    response = api_client.update_user(1, payload)

    assert_success_json_response(response, 200)

    data = response.json()

    assert_required_fields(
        data,
        ["id", "name", "username"]
    )

    assert_response_data(
        data,
        {
            "name": payload["name"],
            "username": payload["username"]
        }
    )

@pytest.mark.api
def test_api_base_url(api_base_url):
    assert api_base_url == "https://jsonplaceholder.typicode.com"