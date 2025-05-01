# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

## Solution Approach
The solution uses a stack data structure to keep track of opening brackets. Here's how it works:

1. Create a dictionary to map closing brackets to their corresponding opening brackets.
2. Initialize an empty stack.
3. Iterate through each character in the string:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket:
     - Check if the stack is empty (no matching opening bracket)
     - Check if the top of the stack matches the corresponding opening bracket
     - If either condition fails, return false
4. After processing all characters, check if the stack is empty (all brackets are properly matched)

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input string
- Space Complexity: O(n), where n is the length of the input string (in worst case, all characters are opening brackets)

## Implementation
The solution is implemented in `valid_parentheses.py` with detailed comments and test cases. 