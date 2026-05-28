def calculate_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using an iterative approach.
    Each number = previous number + number before that
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to 0")

    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize variables for iterative calculation
    previous = 0
    current = 1

    # Iterate from 2 to n, calculating each fibonacci number
    for _ in range(2, n + 1):
        previous, current = current, previous + current


    return current

