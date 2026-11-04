# Competitive Programming Helper Algorithms

Small, reusable algorithms and data structures for competitive programming. Implementations live in standalone Python files and use the standard library where possible.

## Algorithms

| File | Description | Operations |
| --- | --- | --- |
| [`MedianFinder.py`](MedianFinder.py) | Dynamic lower-median structure using two heaps and lazy deletion. Also tracks sums on each side of the median. | `add` and `remove`: O(log n) amortized; queries: O(1) |

## Usage

```python
from MedianFinder import MedianFinder

median = MedianFinder()
median.add(3)
median.add(1)
median.add(2)

print(median.get_median())  # 2 (lower median when count is even)
median.remove(2)
print(median.get_median())  # 1
```

`get_median()` returns `None` when structure is empty. `get_size()` returns `(left_size, right_size)`; `get_sum()` returns `(left_sum, right_sum)`. `remove(value)` expects a value currently present.

## Adding an algorithm

- Add one focused `.py` file per algorithm or closely related data structure.
- Document expected inputs, important behavior, and time/space complexity.
- Keep implementations self-contained and suitable for adapting to online judge solutions.
- Add the file and a short entry to the table above.
