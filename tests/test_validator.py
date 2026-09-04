import pytest

from validator import is_valid_username, is_valid_age

@pytest.mark.parametrize("username, expected", [
    ("abc", False),
    ("abcd", True),
    ("tester", True),
    ("", False),
])

def test_valid_username(username, expected):
    assert is_valid_username(username) is expected

@pytest.mark.parametrize("age, expected", [
    (-1, False),
    (0, True),
    (1, True),
    (119, True),
    (120, True),
    (121, False),
])

def test_valid_age(age, expected):
    assert is_valid_age(age) is expected