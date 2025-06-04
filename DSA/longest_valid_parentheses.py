"""
Find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Time Complexity:
- Stack Solution: O(n)
- Dynamic Programming Solution: O(n)
Space Complexity:
- Stack Solution: O(n)
- Dynamic Programming Solution: O(n)
"""

from typing import List

def longest_valid_parentheses_stack(s: str) -> int:
    """
    Solution using stack.
    We keep track of the indices of unmatched parentheses.
    """
    if not s:
        return 0
    
    stack = [-1]  # Initialize with -1 to handle edge cases
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

def longest_valid_parentheses_dp(s: str) -> int:
    """
    Solution using dynamic programming.
    dp[i] represents the length of the longest valid parentheses ending at index i.
    """
    if not s:
        return 0
    
    n = len(s)
    dp = [0] * n
    max_length = 0
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
            max_length = max(max_length, dp[i])
    
    return max_length

def get_longest_valid_parentheses(s: str) -> str:
    """
    Helper function to get the actual longest valid parentheses substring.
    Uses the stack approach to find the substring.
    """
    if not s:
        return ""
    
    stack = [-1]
    max_length = 0
    start_idx = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                current_length = i - stack[-1]
                if current_length > max_length:
                    max_length = current_length
                    start_idx = stack[-1] + 1
    
    return s[start_idx:start_idx + max_length]

# Test cases
def test_longest_valid_parentheses():
    test_cases = [
        ("(()", 2, "()"),
        (")()())", 4, "()()"),
        ("", 0, ""),
        ("(", 0, ""),
        (")", 0, ""),
        ("()", 2, "()"),
        ("()()", 4, "()()"),
        ("(())", 4, "(())"),
        ("(()())", 6, "(()())"),
        ("((()))", 6, "((()))"),
    ]
    
    for s, expected_length, expected_substring in test_cases:
        # Test stack solution
        result_stack = longest_valid_parentheses_stack(s)
        assert result_stack == expected_length, \
            f"Stack solution failed for '{s}'. Expected length {expected_length}, got {result_stack}"
        
        # Test DP solution
        result_dp = longest_valid_parentheses_dp(s)
        assert result_dp == expected_length, \
            f"DP solution failed for '{s}'. Expected length {expected_length}, got {result_dp}"
        
        # Test substring reconstruction
        result_substring = get_longest_valid_parentheses(s)
        assert len(result_substring) == expected_length, \
            f"Substring reconstruction failed for '{s}'. Expected length {expected_length}, got {len(result_substring)}"
        assert result_substring == expected_substring, \
            f"Substring reconstruction failed for '{s}'. Expected '{expected_substring}', got '{result_substring}'"
        
        print(f"Test passed for s='{s}'")

if __name__ == "__main__":
    test_longest_valid_parentheses() 