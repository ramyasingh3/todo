# Palindrome Number

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome number reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

## Examples
1. Positive palindrome:
   ```
   Input: x = 121
   Output: true
   Explanation: 121 reads the same from left to right and right to left.
   ```

2. Negative number:
   ```
   Input: x = -121
   Output: false
   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
   ```

3. Non-palindrome:
   ```
   Input: x = 10
   Output: false
   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
   ```

## Solution Approaches

### 1. String Conversion (O(n))
- Converts number to string and compares with reverse
- Time Complexity: O(n)
- Space Complexity: O(n)
- Simple but uses extra space
- Good for understanding the problem

### 2. Number Reversal (O(log n))
- Reverses the entire number and compares
- Time Complexity: O(log n)
- Space Complexity: O(1)
- More efficient in terms of space
- Good for learning number manipulation

### 3. Half Number Comparison (O(log n))
- Reverses only half of the number
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Most efficient solution
- Optimized for large numbers

## Time Complexity
- String Conversion: O(n)
- Number Reversal: O(log n)
- Half Comparison: O(log n)

## Space Complexity
- String Conversion: O(n)
- Number Reversal: O(1)
- Half Comparison: O(1)

## Usage
```python
from palindrome_number import Solution

solution = Solution()
x = 121

# Using string conversion
result = solution.is_palindrome_string(x)
print(f"Is palindrome: {result}")

# Using number reversal
result = solution.is_palindrome_reverse(x)
print(f"Is palindrome: {result}")

# Using half comparison
result = solution.is_palindrome_half(x)
print(f"Is palindrome: {result}")
```

## Common Applications
- Number validation
- Data integrity checks
- Cryptography
- Error detection
- Numerical analysis 