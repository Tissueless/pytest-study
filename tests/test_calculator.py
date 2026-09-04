import pytest

from calculator import add, subtract, multiply, divide

@pytest.mark.calculator
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 20, 30),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a,b) == expected

@pytest.mark.calculator
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (20, 10, 10),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    assert subtract(a,b) == expected

@pytest.mark.calculator
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)