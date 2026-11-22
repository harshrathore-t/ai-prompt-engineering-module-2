def fibonacci(n):
    """Return the first n Fibonacci terms, starting at 0."""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    terms = []
    a, b = 0, 1
    for _ in range(n):
        terms.append(a)
        a, b = b, a + b
    return terms


if __name__ == "__main__":
    print("fibonacci(7) =", fibonacci(7))
