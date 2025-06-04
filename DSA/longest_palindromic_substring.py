"""
Find the longest palindromic substring in a given string.

Example 1:
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.

Example 2:
Input: s = "cbbd"
Output: "bb"

Time Complexity:
- Dynamic Programming: O(n²)
- Expand Around Center: O(n²)
Space Complexity:
- Dynamic Programming: O(n²)
- Expand Around Center: O(1)
"""

from typing import List, Tuple

def longest_palindrome_dp(s: str) -> str:
    """
    Solution using dynamic programming.
    dp[i][j] represents whether s[i:j+1] is a palindrome.
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

def expand_around_center(s: str, left: int, right: int) -> Tuple[int, int]:
    """
    Helper function for expand around center solution.
    Returns the start and end indices of the longest palindrome centered at left and right.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longest_palindrome_expand(s: str) -> str:
    """
    Solution using expand around center approach.
    For each position, we expand around it to find the longest palindrome.
    """
    if not s:
        return ""
    
    start = 0
    max_length = 1
    
    for i in range(len(s)):
        # Check for odd length palindromes
        left, right = expand_around_center(s, i, i)
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        
        # Check for even length palindromes
        left, right = expand_around_center(s, i, i + 1)
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
    
    return s[start:start + max_length]

# Test cases
def test_longest_palindrome():
    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("", [""]),
        ("racecar", ["racecar"]),
        ("aaa", ["aaa"]),
        ("abc", ["a", "b", "c"]),
    ]
    
    for s, expected in test_cases:
        # Test dynamic programming solution
        result_dp = longest_palindrome_dp(s)
        assert result_dp in expected, f"DP solution failed for '{s}'. Expected one of {expected}, got '{result_dp}'"
        
        # Test expand around center solution
        result_expand = longest_palindrome_expand(s)
        assert result_expand in expected, f"Expand solution failed for '{s}'. Expected one of {expected}, got '{result_expand}'"
        
        print(f"Test passed for s='{s}'")

if __name__ == "__main__":
    test_longest_palindrome() 