import pytest

from app.services.factorial import calculate_factorial


def test_factorial_zero():
    assert calculate_factorial(0) == 1


def test_factorial_five():
    assert calculate_factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-1)


def test_factorial_above_limit():
    with pytest.raises(ValueError):
        calculate_factorial(11)