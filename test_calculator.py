"""Tests for calculator.py — the sum_first_n tests are currently failing."""

from calculator import mean, sum_first_n


def test_sum_first_three():
    """First 3 elements of [1, 2, 3, 4, 5] should sum to 6."""
    assert sum_first_n([1, 2, 3, 4, 5], 3) == 6


def test_sum_first_one():
    """First 1 element of [10, 20] should sum to 10."""
    assert sum_first_n([10, 20], 1) == 10


def test_sum_first_all():
    """First 5 elements of [1, 2, 3, 4, 5] should sum to 15."""
    assert sum_first_n([1, 2, 3, 4, 5], 5) == 15


def test_mean_simple():
    """Mean of [2, 4, 6] is 4.0."""
    assert mean([2, 4, 6]) == 4.0


def test_mean_empty():
    """Mean of [] is 0.0 (no ZeroDivisionError)."""
    assert mean([]) == 0.0
