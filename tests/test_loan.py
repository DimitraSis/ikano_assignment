import pytest

from app.services.loan import calculate_monthly_payment


def test_zero_interest_loan():
    result = calculate_monthly_payment(
        1200,
        0,
        12
    )

    assert result == 100.0

def test_zero_principal():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            0,
            5,
            12
        )


def test_negative_principal():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            -1000,
            5,
            12
        )

def test_maximum_loan_duration():
    result = calculate_monthly_payment(
        100000,
        5,
        480
    )

    assert result > 0

def test_one_month_loan():
    result = calculate_monthly_payment(
        1200,
        0,
        1
    )

    assert result == 1200.0

def test_invalid_months():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            1000,
            5,
            0
        )

def test_months_above_maximum():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            100000,
            5,
            481
        )

def test_negative_interest_rate():
    result = calculate_monthly_payment(
            1000,
            -2,
            12
        )
    assert result == 82.43

def test_invalid_negative_interest_rate():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            1000,
            -5,
            12
        )

