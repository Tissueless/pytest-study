import os
import pytest
from config import get_base_url

from api.client import APIClient

from test_data.users import USERS

@pytest.fixture
def user():
    return {
        "id": 1,
        "name": "tester",
        "age": 30,
        "role": "tester"
    }

@pytest.fixture
def normal_user():
    return USERS["normal"].copy()

@pytest.fixture
def admin_user():
    return USERS["admin"].copy()

@pytest.fixture
def base_url():
    return "https://example.com"

@pytest.fixture(scope="function")
def scope_test():
    print(">>>FIXTURE 실행")
    return "test"

@pytest.fixture
def test_config():
    return {
        "base_url": "https://example.com",
        "timeout": 10,
        "environment": "test"
    }

@pytest.fixture(scope="module")
def module_config():
    print("\n[SETUP] module_config")
    return {
        "environment": "test"
    }

@pytest.fixture(autouse=True)
def test_start():
    print("\n>>> TEST START")

@pytest.fixture
def test_environment():
    print("\n>>> SETUP")

    yield

    print("\n>>> TEARDOWN")

@pytest.fixture
def user_name():
    return "tester"


@pytest.fixture
def user_profile(user_name):
    return {
        "name": user_name,
        "role": "user"
    }



import requests

@pytest.fixture
def api_client(base_url):
    session = requests.Session()
    session.base_url = base_url

    return session

# @pytest.fixture
# def api_base_url():
#     return os.getenv(
#         "API_BASE_URL",
#         "https://jsonplaceholder.typicode.com"
#     )
# from api.client import APIClient


@pytest.fixture
def api_client(api_base_url, auth_token):
    return APIClient(api_base_url, auth_token)

@pytest.fixture
def auth_token():
    return "test-token-123"

@pytest.fixture
def api_base_url():
    return get_base_url()