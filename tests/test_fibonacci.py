import pytest

from app.services.fibonacci import calculate_fibonacci


def test_fibonacci_zero():
    assert calculate_fibonacci(0) == 0


def test_fibonacci_one():
    assert calculate_fibonacci(1) == 1


def test_fibonacci_ten():
    assert calculate_fibonacci(10) == 55


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)