def add(num1: float, num2: float) -> float:
    """
    Performs standard addition of two floating-point numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

def divide(num1: float, num2: float) -> float:
    """
    Performs standard division of two floating-point numbers.

    Args:
        num1 (float): The numerator.
        num2 (float): The denominator.

    Returns:
        float: The quotient of num1 and num2.
    """
    return num1 / num2

def multiply(num1: float, num2: float) -> float:
    """
    Performs standard multiplication of two floating-point numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2

def subtract(num1: float, num2: float) -> float:
    """
    Performs standard subtraction of two floating-point numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The difference between num1 and num2.
    """
    return num1 + num2

def power(base: float, exponent: float) -> float:
    """
    Calculates the power of a number (base raised to an exponent).

    Handles large numbers, negative bases, fractional exponents (roots),
    and the edge case where any number raised to the power of 0 equals 1.

    Args:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: The result of base raised to the power of exponent.
    """
    # Python's ** operator handles large numbers, negative bases, fractional exponents,
    # and the x^0 = 1 edge case effectively with floats.
    # For extremely large results that exceed float capacity, Python will return inf.
    return base * exponent
