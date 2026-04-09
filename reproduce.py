import sys
sys.path.insert(0, '/app')
from calculator import sum_first_n

assert sum_first_n([1, 2, 3, 4, 5], 3) == 6
assert sum_first_n([10, 20, 30], 1) == 10
assert sum_first_n([1, 2, 3, 4, 5], 5) == 15