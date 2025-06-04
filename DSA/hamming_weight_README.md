# Number of 1 Bits (Hamming Weight)

## Problem Description
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## Examples
1. Basic case:
   ```
   Input: n = 11 (00000000000000000000000000001011)
   Output: 3
   Explanation: The input binary string has three '1' bits.
   ```

2. Single bit:
   ```
   Input: n = 16 (00000000000000000000000000010000)
   Output: 1
   ```

3. All ones:
   ```
   Input: n = 15 (00000000000000000000000000001111)
   Output: 4
   ```

## Solution Approaches

### 1. Loop and Check (O(32))
- Check each bit using right shift and AND
- Simple and straightforward approach
- Time Complexity: O(32) = O(1)
- Space Complexity: O(1)
- Best for understanding

### 2. Brian Kernighan's Algorithm (O(k))
- Uses n & (n-1) to clear rightmost 1 bit
- Counts number of operations needed
- Time Complexity: O(number of 1 bits)
- Space Complexity: O(1)
- Best for performance

### 3. Built-in Method (O(1))
- Uses Python's bin() and count()
- Most concise solution
- Time Complexity: O(1)
- Space Complexity: O(1)
- Best for readability

## Time Complexity
- Loop: O(32) = O(1)
- Kernighan: O(number of 1 bits)
- Built-in: O(1)

## Space Complexity
- All methods: O(1)

## Usage
```python
from hamming_weight import Solution

solution = Solution()

# Using loop method
print(solution.hamming_weight_loop(11))  # Output: 3

# Using Brian Kernighan's algorithm
print(solution.hamming_weight_trick(11))  # Output: 3

# Using built-in method
print(solution.hamming_weight_builtin(11))  # Output: 3
```

## Common Applications
- Error detection in data transmission
- Digital communication systems
- Population count in databases
- Cryptography
- Network packet analysis
- Hardware performance optimization 