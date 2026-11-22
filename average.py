def average(numbers):
    """Return arithmetic mean; reject an empty sequence."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("average([1, 2]) =", average([1, 2]))
