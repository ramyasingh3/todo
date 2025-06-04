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

## Approach
The solution uses a stack-based approach:
1. Initialize an empty stack
2. Create a mapping of closing brackets to their corresponding opening brackets
3. Iterate through each character in the string:
   - If it's an opening bracket, push it onto the stack
   - If it's a closing bracket:
     - If the stack is empty or the top of the stack doesn't match the corresponding opening bracket, return false
     - Otherwise, pop the top element from the stack
4. After processing all characters, the stack should be empty for a valid string

## Time Complexity
- O(n), where n is the length of the input string
- We process each character exactly once

## Space Complexity
- O(n), where n is the length of the input string
- In the worst case, we might need to store all opening brackets in the stack

## Solution
The solution is implemented in `valid_parentheses.py` with detailed comments and test cases.

## Common Applications
- Syntax checking in programming languages
- XML/HTML tag validation
- Mathematical expression validation
- Code editor bracket matching
- Configuration file validation 