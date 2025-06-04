# Longest Valid Parentheses

## Problem Statement
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

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
```

## Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a DP array where dp[i] represents the length of the longest valid parentheses substring ending at index i.

2. For each character at index i:
   - If s[i] is ')':
     - If s[i-1] is '(', then dp[i] = dp[i-2] + 2
     - If s[i-1] is ')', check if there's a matching '(' before the current valid substring

3. Return the maximum value in the dp array

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input string
- Space Complexity: O(n) for the DP array

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation. 