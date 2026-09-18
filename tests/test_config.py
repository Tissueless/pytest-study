import pytest

from config import BASE_URLS, get_base_url


@pytest.mark.parametrize(
    "environment",
    ["dev", "qa", "stg"]
)
def test_get_base_url(environment, monkeypatch):
    monkeypatch.setenv("TEST_ENV", environment)

    assert get_base_url() == BASE_URLS[environment]


def test_invalid_environment(monkeypatch):
    monkeypatch.setenv("TEST_ENV", "production")

    with pytest.raises(ValueError):
        get_base_url()

def test_api_client_uses_environment_url(api_client, api_base_url):
    assert api_client.base_url == api_base_url

def test_auth_token(auth_token):
    assert auth_token == "my-test-token"

def test_api_client_uses_auth_token(api_client, auth_token):
    assert api_client.session.headers["Authorization"] == f"Bearer {auth_token}"
