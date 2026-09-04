import pytest

from user import get_user, is_admin
from test_data.users import USERS

def test_get_user():
    user = get_user()

    assert user["id"] == 1
    assert user["name"] == "tester"
    assert user["age"] == 30

def test_user_fixture(user):
    assert user["name"] == "tester"
    assert user["role"] == "tester"

def test_admin_user(admin_user):
    assert admin_user["name"] =="admin"
    assert admin_user["role"] =="admin"

def test_is_admin(admin_user):
    assert is_admin(admin_user) is True


def test_normal_user(normal_user):
    assert normal_user["name"] == "normal"
    assert normal_user["role"] == "user"
    assert normal_user["age"] == 30


def test_admin_user(admin_user):
    assert admin_user["name"] == "admin"
    assert admin_user["role"] == "admin"
    assert admin_user["age"] == 40


def test_users_have_id(normal_user, admin_user):
    assert normal_user["id"] > 0
    assert admin_user["id"] > 0

def test_users_are_independent(normal_user, admin_user):
    normal_user["name"] = "changed"

    assert normal_user["name"] == "changed"
    assert admin_user["name"] == "admin"

def test_base_url(base_url):
    assert base_url == "https://example.com"

def test_test_config(test_config):
    assert test_config["base_url"] == "https://example.com"
    assert test_config["timeout"] == 10
    assert test_config["environment"] == "test"

def test_module_config_1(module_config):
    assert module_config["environment"] == "test"


def test_module_config_2(module_config):
    assert module_config["environment"] == "test"

def test_autouse_1():
    print(">>> TEST 1")
    assert True


def test_autouse_2():
    print(">>> TEST 2")
    assert True

def test_environment_1(test_environment):
    print(">>> TEST 1")
    assert True


def test_environment_2(test_environment):
    print(">>> TEST 2")
    assert True

def test_user_profile(user_profile):
    assert user_profile["name"] == "tester"
    assert user_profile["role"] == "user"

def test_api_client(api_client):
    assert api_client.base_url == "https://example.com"