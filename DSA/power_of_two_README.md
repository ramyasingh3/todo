# Power of Two

## Problem Description
Given an integer `n`, determine if it is a power of two. An integer `n` is a power of two if there exists an integer `x` such that `n == 2^x`.

## Examples
1. Basic case:
   ```
   Input: n = 16
   Output: true
   Explanation: 16 = 2^4
   ```

2. Not power of two:
   ```
   Input: n = 6
   Output: false
   ```

3. Edge case:
   ```
   Input: n = 1
   Output: true
   Explanation: 1 = 2^0
   ```

## Solution Approaches

### 1. Iterative Division (O(log n))
- Repeatedly divide by 2 and check remainder
- If any remainder is not 0, return false
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Best for understanding

### 2. Bit Manipulation (O(1))
- Uses property that powers of 2 have exactly one '1' bit
- n & (n-1) removes rightmost '1' bit
- Time Complexity: O(1)
- Space Complexity: O(1)
- Best for performance

### 3. Mathematical (O(1))
- Uses logarithm to check if log2(n) is integer
- Time Complexity: O(1)
- Space Complexity: O(1)
- Best for mathematical approach

## Time Complexity
- Iterative: O(log n)
- Bit/Math: O(1)

## Space Complexity
- All methods: O(1)

## Usage
```python
from power_of_two import Solution

solution = Solution()

# Using iterative method
print(solution.is_power_of_two_loop(16))  # Output: True

# Using bit manipulation method
print(solution.is_power_of_two_bit(6))    # Output: False

# Using mathematical method
print(solution.is_power_of_two_math(32))  # Output: True
```

## Common Applications
- Memory allocation (buffer sizes)
- Data structure sizing
- Image processing (dimensions)
- Network packet sizes
- Hardware optimization 