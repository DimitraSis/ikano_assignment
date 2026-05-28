from decimal import Decimal, ROUND_HALF_UP


def calculate_monthly_payment(
    principal: float,
    annual_rate: float,
    months: int
) -> float:
    """
    Calculate monthly loan repayment.
    """

    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal must be greater than 0")

    if annual_rate < -2:
        raise ValueError("Annual rate is unrealistically low")    

    # From 0 to 40 years
    if months <= 0 or months > 480:
        raise ValueError("Months must be between 1 and 480")

    # Convert to Decimal for financial accuracy
    principal = Decimal(str(principal))
    annual_rate = Decimal(str(annual_rate))

    # Handle zero-interest loans
    if annual_rate == Decimal("0"):
        payment = principal / Decimal(months)

    else:
        monthly_rate = annual_rate / Decimal("12") / Decimal("100")

        numerator = monthly_rate * ((1 + monthly_rate) ** months)
        denominator = ((1 + monthly_rate) ** months) - 1

        payment = principal * (numerator / denominator)

    
    return float(
    payment.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
)