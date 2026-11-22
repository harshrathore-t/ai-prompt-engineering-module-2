def factorial(n):
    """Return n! for a non-negative integer."""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


if __name__ == "__main__":
    print("factorial(5) =", factorial(5))
