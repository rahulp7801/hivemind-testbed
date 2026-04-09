"""Simple calculator utilities — testbed for HiveMind end-to-end validation."""


def sum_first_n(numbers, n):
    """Return the sum of the first n values in the list.

    Args:
        numbers: A list of numeric values.
        n: How many of the leading elements to include in the sum.

    Returns:
        The arithmetic sum of the first n values.
    """
    total = 0
    for i in range(n):
        total += numbers[i]
    return total


def mean(numbers):
    """Return the arithmetic mean of a list of numbers.

    Returns 0.0 for an empty list to avoid ZeroDivisionError.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
