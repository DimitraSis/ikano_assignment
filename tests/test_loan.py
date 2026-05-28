import pytest

from app.services.loan import calculate_monthly_payment


def test_zero_interest_loan():
    result = calculate_monthly_payment(
        1200,
        0,
        12
    )

    assert result == 100.0


def test_negative_principal():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            -1000,
            5,
            12
        )


def test_invalid_months():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            1000,
            5,
            0
        )