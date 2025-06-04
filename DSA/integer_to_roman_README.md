# Integer to Roman

## Problem Description
Given an integer, convert it to a roman numeral. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

## Examples
1. Basic conversion:
   ```
   Input: 3
   Output: "III"
   ```

2. Subtraction case:
   ```
   Input: 4
   Output: "IV"
   ```

3. Complex number:
   ```
   Input: 1994
   Output: "MCMXCIV"
   ```

4. Large number:
   ```
   Input: 3999
   Output: "MMMCMXCIX"
   ```

5. Single digit:
   ```
   Input: 9
   Output: "IX"
   ```

## Solution Approaches

### 1. Naive Solution (O(1))
- Create a mapping of values to Roman symbols
- Process the number from largest to smallest
- Append symbols while subtracting values
- Return the final string

### 2. Optimized Solution (O(1))
- Use separate lists for values and symbols
- Process the number from largest to smallest
- Use list operations for better performance
- Return the joined string

## Time Complexity
- Both solutions: O(1) (constant time as the number of operations is fixed)

## Space Complexity
- Both solutions: O(1) (constant space as the output size is bounded)

## Usage
```python
from integer_to_roman import Solution

solution = Solution()
num = 1994

# Using naive solution
result = solution.int_to_roman_naive(num)
print(result)  # Output: "MCMXCIV"

# Using optimized solution (recommended)
result = solution.int_to_roman_optimized(num)
print(result)  # Output: "MCMXCIV"
```

## Common Applications
- Historical data representation
- Clock face design
- Book chapter numbering
- Movie release years
- Monument inscriptions 