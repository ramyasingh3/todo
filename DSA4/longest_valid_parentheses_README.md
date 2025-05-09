# Longest Valid Parentheses

## Problem Description
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. A valid parentheses substring must have matching opening and closing brackets.

## Examples

### Example 1:
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

### Example 2:
```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

### Example 3:
```
Input: s = ""
Output: 0
Explanation: There are no valid parentheses.
```

## Solution Approach

The solution uses a stack-based approach with the following steps:

1. Initialize a stack with -1 to handle edge cases
2. For each character in the string:
   - If it's an opening bracket '(':
     - Push its index onto the stack
   - If it's a closing bracket ')':
     - Pop the top element from the stack
     - If stack becomes empty:
       - Push current index onto stack
     - Otherwise:
       - Calculate length of valid parentheses
       - Update maximum length if needed

The key insights are:
- Use stack to keep track of indices of opening brackets
- Initialize stack with -1 to handle edge cases
- Calculate length using current index and stack top
- Keep track of maximum length found

## Time and Space Complexity

- **Time Complexity**: O(n)
  - n is the length of the string
  - We process each character exactly once
  - Stack operations are O(1)

- **Space Complexity**: O(n)
  - n is the length of the string
  - In worst case, we store all indices in the stack
  - This happens when string has all opening brackets

## Edge Cases

1. Empty string
2. String with no valid parentheses
3. String with all valid parentheses
4. String with nested valid parentheses
5. String with alternating valid and invalid parts
6. String starting with closing bracket
7. String ending with opening bracket

## Implementation Notes

- The solution uses a stack to track indices
- The solution handles all edge cases correctly
- The solution is efficient with O(n) time and space
- The solution can be modified to return the actual substring
- The solution works with any string containing '(' and ')'

## Alternative Approaches

1. **Dynamic Programming**:
   - Use dp array to store lengths
   - dp[i] represents length of valid parentheses ending at i
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - More complex to implement

2. **Two Pointers**:
   - Use left and right counters
   - Scan string twice (left to right and right to left)
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Less intuitive but more space efficient

3. **Brute Force**:
   - Check all possible substrings
   - Time Complexity: O(n³)
   - Space Complexity: O(n)
   - Not efficient for large inputs

## Common Applications
- Syntax validation
- Code parsing
- Expression evaluation
- XML/HTML parsing
- Regular expression matching
- Compiler design
- Text processing 