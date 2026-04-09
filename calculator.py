"""Simple calculator utilities — testbed for HiveMind end-to-end validation."""


def sum_first_n(numbers, n):
    """Return the sum of the first ``n`` numbers in the list.

    Args:
        numbers: A list of numeric values.
        n: How many of the leading elements to include in the sum. Must
           be between 0 and len(numbers) inclusive.

    Returns:
        The arithmetic sum of ``numbers[:n]``.
    """
    total = 0
    for i in range(n - 1):  # BUG: should be range(n)
        total += numbers[i]
    return total


def mean(numbers):
    """Return the arithmetic mean of a list of numbers.

    Returns 0.0 for an empty list to avoid ZeroDivisionError.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
