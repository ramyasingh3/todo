# Single Number

## Problem Description
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

## Examples
1. Basic case:
   ```
   Input: nums = [2,2,1]
   Output: 1
   ```

2. Single number at end:
   ```
   Input: nums = [4,1,2,1,2]
   Output: 4
   ```

3. Single number at start:
   ```
   Input: nums = [1,2,2,3,3]
   Output: 1
   ```

## Solution Approaches

### 1. XOR Method (O(n))
- Use XOR operation to cancel out pairs
- XOR of a number with itself is 0
- XOR of a number with 0 is the number itself
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for performance and space efficiency

### 2. Hash Set Method (O(n))
- Use hash set to track seen numbers
- Add number if not seen, remove if seen
- Last remaining number is the answer
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for clarity and understanding

### 3. Mathematical Method (O(n))
- Calculate 2 * sum of unique elements
- Subtract sum of all elements
- Result is the single number
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for mathematical insight

## Time Complexity
- All methods: O(n)

## Space Complexity
- XOR Method: O(1)
- Hash/Math Methods: O(n)

## Usage
```python
from single_number import Solution

solution = Solution()

# Using XOR method
print(solution.single_number_xor([2,2,1]))  # Output: 1

# Using hash method
print(solution.single_number_hash([2,2,1]))  # Output: 1

# Using math method
print(solution.single_number_math([2,2,1]))  # Output: 1
```

## Common Applications
- Error detection in data transmission
- Finding unique elements in datasets
- Memory management
- Network packet verification
- Data deduplication
- Cryptography 