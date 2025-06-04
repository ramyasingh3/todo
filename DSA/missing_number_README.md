# Missing Number

## Problem Description
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Examples
1. Basic case:
   ```
   Input: nums = [0,1,3]
   Output: 2
   Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number.
   ```

2. Missing last number:
   ```
   Input: nums = [0,1,2]
   Output: 3
   ```

3. Missing first number:
   ```
   Input: nums = [1,2,3]
   Output: 0
   ```

## Solution Approaches

### 1. Sum Method (O(n))
- Calculate expected sum using arithmetic series formula
- Subtract actual sum to find missing number
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for simplicity and performance

### 2. XOR Method (O(n))
- Use XOR properties to find missing number
- XOR all numbers and indices
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for avoiding overflow

### 3. Sort Method (O(n log n))
- Sort array and find first mismatch
- Time Complexity: O(n log n)
- Space Complexity: O(1)
- Best for understanding

### 4. Hash Set Method (O(n))
- Use hash set to track seen numbers
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for clarity

## Time Complexity
- Sum/XOR/Hash: O(n)
- Sort: O(n log n)

## Space Complexity
- Sum/XOR/Sort: O(1)
- Hash: O(n)

## Usage
```python
from missing_number import Solution

solution = Solution()

# Using sum method
print(solution.missing_number_sum([0,1,3]))  # Output: 2

# Using XOR method
print(solution.missing_number_xor([0,1,3]))  # Output: 2

# Using sort method
print(solution.missing_number_sort([0,1,3]))  # Output: 2

# Using hash method
print(solution.missing_number_hash([0,1,3]))  # Output: 2
```

## Common Applications
- Data validation
- Error detection
- Database integrity checks
- Memory management
- Network packet verification
- Array indexing validation 