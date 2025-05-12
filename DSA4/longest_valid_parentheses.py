"""
Longest Valid Parentheses

Problem:
Given a string containing just the characters '(' and ')', find the length of the longest valid
(well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
Explanation: There are no valid parentheses.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""

def longestValidParentheses(s: str) -> int:
    """
    Find the length of the longest valid (well-formed) parentheses substring.
    
    Args:
        s: Input string containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    if not s:
        return 0
        
    n = len(s)
    # dp[i] represents the length of longest valid parentheses ending at index i
    dp = [0] * n
    max_len = 0
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                # Case: "()"
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                # Case: "(())"
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
            max_len = max(max_len, dp[i])
            
    return max_len

def longestValidParenthesesStack(s: str) -> int:
    """
    Find the length of the longest valid parentheses substring using stack.
    
    Args:
        s: Input string containing only '(' and ')'
        
    Returns:
        Length of the longest valid parentheses substring
    """
    if not s:
        return 0
        
    stack = [-1]  # Initialize stack with -1
    max_len = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
                
    return max_len

def getValidParentheses(s: str) -> list[str]:
    """
    Get all valid parentheses substrings.
    
    Args:
        s: Input string containing only '(' and ')'
        
    Returns:
        List of all valid parentheses substrings
    """
    def isValid(sub: str) -> bool:
        count = 0
        for char in sub:
            if char == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0
        
    n = len(s)
    valid_substrings = []
    
    for i in range(n):
        for j in range(i + 2, n + 1, 2):  # Only check even lengths
            substring = s[i:j]
            if isValid(substring):
                valid_substrings.append(substring)
                
    return valid_substrings

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "(()"
    print(f"Input: '{s1}'")
    print(f"Length (DP): {longestValidParentheses(s1)}")  # Expected: 2
    print(f"Length (Stack): {longestValidParenthesesStack(s1)}")  # Expected: 2
    print("Valid substrings:")
    for substr in getValidParentheses(s1):
        print(f"- '{substr}'")
    
    # Test case 2
    s2 = ")()())"
    print(f"\nInput: '{s2}'")
    print(f"Length (DP): {longestValidParentheses(s2)}")  # Expected: 4
    print(f"Length (Stack): {longestValidParenthesesStack(s2)}")  # Expected: 4
    print("Valid substrings:")
    for substr in getValidParentheses(s2):
        print(f"- '{substr}'")
    
    # Test case 3
    s3 = ""
    print(f"\nInput: '{s3}'")
    print(f"Length (DP): {longestValidParentheses(s3)}")  # Expected: 0
    print(f"Length (Stack): {longestValidParenthesesStack(s3)}")  # Expected: 0
    print("Valid substrings:")
    for substr in getValidParentheses(s3):
        print(f"- '{substr}'")
    
    # Test case 4
    s4 = "((()))"
    print(f"\nInput: '{s4}'")
    print(f"Length (DP): {longestValidParentheses(s4)}")  # Expected: 6
    print(f"Length (Stack): {longestValidParenthesesStack(s4)}")  # Expected: 6
    print("Valid substrings:")
    for substr in getValidParentheses(s4):
        print(f"- '{substr}'") 