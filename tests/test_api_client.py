from unittest.mock import Mock, call
from api.client import APIClient
import pytest
import requests

def test_api_client_called_once():
    api_client = APIClient("https://example.com")

    api_client.session.request = Mock()

    api_client.request("GET", "/users/1")
    api_client.request("GET", "/users/2")

    assert api_client.session.request.call_count == 2

    assert api_client.session.request.call_args_list[0] == call(
        "GET",
        "https://example.com/users/1"
    )

    assert api_client.session.request.call_args_list[1] == call(
        "GET",
        "https://example.com/users/2"
    )

def test_api_client_mock_response():
    api_client = APIClient("https://example.com")

    mock_response = Mock()
    mock_response.status_code = 200

    api_client.session.request = Mock(return_value=mock_response)

    response = api_client.request("GET", "/users/1")

    assert response.status_code == 200

    assert response is mock_response
    api_client.session.request.assert_called_once_with(
    "GET",
    "https://example.com/users/1"
)

def test_api_client_mock_fail_response():
    api_client = APIClient("https://example.com")

    mock_response = Mock()
    mock_response.status_code = 404

    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
    api_client.session.request = Mock(return_value=mock_response)

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.request("GET", "/users/9999")

def test_api_client_get_user():
    api_client = APIClient("https://example.com")

    mock_response = Mock()
    mock_response.status_code = 200

    api_client.session.request = Mock(return_value=mock_response)

    response = api_client.get_user(123)

    assert response is mock_response

    api_client.session.request.assert_called_once_with(
        "GET",
        "https://example.com/users/123"
    )

def test_api_client_mock_500():
    api_client = APIClient("https://example.com")

    mock_response = Mock()
    mock_response.status_code = 500

    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

    api_client.session.request = Mock(return_value=mock_response)

    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_user(123)


payload = {
    "name": "test",
    "username": "tester"
}

def test_creat_user():
    api_client = APIClient("https://example.com")

    mock_response = Mock()

    api_client.session.request = Mock(return_value=mock_response)

    payload = {
        "name": "test",
        "username": "tester"
    }

    response = api_client.create_user(payload)

    assert response is mock_response

    api_client.session.request.assert_called_once_with(
        "POST",
        "https://example.com/users",
        json=payload
    )

@pytest.fixture
def api_client():
    return APIClient("https://example.com")

@pytest.mark.parametrize(
    "payload",
    [
        {
            "name": "test1",
            "username": "tester1"
        },
        {
            "name": "test2",
            "username": "tester2"
        }
    ]
)
def test_create_user(api_client, payload):
    mock_response = Mock()

    api_client.session.request = Mock(
        return_value=mock_response
    )
    response = api_client.create_user(payload)
    assert response is mock_response
    
    api_client.session.request.assert_called_once_with(
        "POST", 
        "https://example.com/users",
        json=payload
        )


@pytest.mark.parametrize(
    "status_code, should_raise",
    [
        (200, False),
        (404, True),
    ]
)
def test_api_client_response(api_client, status_code, should_raise):
    mock_response = Mock()
    mock_response.status_code = status_code

    if should_raise:
        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError()
        )

    api_client.session.request = Mock(
        return_value=mock_response
    )

    if should_raise:
        with pytest.raises(requests.exceptions.HTTPError):
            api_client.get_user(123)
    else:
        response = api_client.get_user(123)
        assert response is mock_response

