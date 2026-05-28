def calculate_factorial(n: int) -> int:
    """
    Calculate factorial of n.
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")

    if n > 10:
        raise ValueError("n must not be greater than 10")

    if n == 0:
        return 1

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result