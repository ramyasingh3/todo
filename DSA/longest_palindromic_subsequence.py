"""
Find the length of the longest palindromic subsequence in a string.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Time Complexity:
- Recursive with memoization: O(n²)
- Dynamic Programming: O(n²)
Space Complexity:
- Recursive with memoization: O(n²)
- Dynamic Programming: O(n²)
"""

from typing import Dict, Tuple
from functools import lru_cache

def longest_palindromic_subsequence_recursive(s: str) -> int:
    """
    Recursive solution with memoization using lru_cache.
    """
    @lru_cache(maxsize=None)
    def lps(i: int, j: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        
        if s[i] == s[j]:
            return 2 + lps(i + 1, j - 1)
        return max(lps(i + 1, j), lps(i, j - 1))
    
    return lps(0, len(s) - 1)

def longest_palindromic_subsequence_dp(s: str) -> int:
    """
    Dynamic programming solution.
    dp[i][j] represents the length of the longest palindromic subsequence
    in the substring s[i:j+1].
    """
    if not s:
        return 0
    
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

def get_palindromic_subsequence(s: str) -> str:
    """
    Helper function to get the actual longest palindromic subsequence.
    Uses the DP table to reconstruct the sequence.
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Fill the dp table
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # Reconstruct the sequence
    result = []
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            result.append(s[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    
    # Add the second half of the palindrome
    if len(result) * 2 > dp[0][n - 1]:
        return ''.join(result + result[:-1][::-1])
    return ''.join(result + result[::-1])

# Test cases
def test_longest_palindromic_subsequence():
    test_cases = [
        ("bbbab", 4, "bbbb"),
        ("cbbd", 2, "bb"),
        ("a", 1, "a"),
        ("", 0, ""),
        ("abc", 1, "a"),
        ("aaa", 3, "aaa"),
        ("racecar", 7, "racecar"),
        ("leetcode", 3, "eee"),
        ("abcdba", 5, "abcba"),
        ("bbbab", 4, "bbbb"),
    ]
    
    for s, expected_length, expected_subsequence in test_cases:
        # Test recursive solution
        result_recursive = longest_palindromic_subsequence_recursive(s)
        assert result_recursive == expected_length, \
            f"Recursive solution failed for '{s}'. Expected length {expected_length}, got {result_recursive}"
        
        # Test DP solution
        result_dp = longest_palindromic_subsequence_dp(s)
        assert result_dp == expected_length, \
            f"DP solution failed for '{s}'. Expected length {expected_length}, got {result_dp}"
        
        # Test subsequence reconstruction
        result_subsequence = get_palindromic_subsequence(s)
        assert len(result_subsequence) == expected_length, \
            f"Subsequence reconstruction failed for '{s}'. Expected length {expected_length}, got {len(result_subsequence)}"
        assert result_subsequence == result_subsequence[::-1], \
            f"Subsequence reconstruction failed for '{s}'. Result is not a palindrome: {result_subsequence}"
        
        print(f"Test passed for s='{s}'")

if __name__ == "__main__":
    test_longest_palindromic_subsequence() 