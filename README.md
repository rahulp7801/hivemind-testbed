# hivemind-testbed

A minimal Python project used to validate HiveMind end-to-end. It contains
a deliberately buggy function (`sum_first_n` in `calculator.py`) and a
pytest suite that exposes the bug.

## Setup

```bash
pip install -r requirements.txt
```

## Running tests

```bash
python -m pytest -x -q
```

Expected on the `main` branch: `test_sum_first_three`, `test_sum_first_one`,
and `test_sum_first_all` all fail with `AssertionError`. The `mean` tests pass.

## The bug

`calculator.sum_first_n(numbers, n)` loops `range(n - 1)` instead of
`range(n)`, so it sums the first `n - 1` elements instead of the first `n`.
Fix: change `range(n - 1)` to `range(n)` on line 15 of `calculator.py`.
