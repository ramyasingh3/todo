"""
Find the length of the longest common subsequence between two strings.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Time Complexity:
- Recursive: O(2^(m+n))
- Dynamic Programming: O(m*n)
Space Complexity:
- Recursive: O(m+n) for call stack
- Dynamic Programming: O(m*n)
"""

from typing import List
from functools import lru_cache

def longest_common_subsequence_recursive(text1: str, text2: str) -> int:
    """
    Recursive solution with memoization using lru_cache.
    """
    @lru_cache(maxsize=None)
    def lcs(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            return 1 + lcs(i + 1, j + 1)
        
        return max(lcs(i + 1, j), lcs(i, j + 1))
    
    return lcs(0, 0)

def longest_common_subsequence_dp(text1: str, text2: str) -> int:
    """
    Dynamic programming solution.
    dp[i][j] represents the length of LCS of text1[0:i] and text2[0:j].
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def get_lcs_string(text1: str, text2: str) -> str:
    """
    Helper function to get the actual LCS string using the DP table.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Test cases
def test_longest_common_subsequence():
    test_cases = [
        ("abcde", "ace", 3, "ace"),
        ("abc", "abc", 3, "abc"),
        ("abc", "def", 0, ""),
        ("", "", 0, ""),
        ("abcde", "ace", 3, "ace"),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd", 4, "hbcb"),
        ("oxcpqrsvwf", "shmtulqrypy", 2, "qr"),
    ]
    
    for text1, text2, expected_length, expected_string in test_cases:
        # Test recursive solution
        result_recursive = longest_common_subsequence_recursive(text1, text2)
        assert result_recursive == expected_length, \
            f"Recursive solution failed for '{text1}' and '{text2}'. Expected {expected_length}, got {result_recursive}"
        
        # Test DP solution
        result_dp = longest_common_subsequence_dp(text1, text2)
        assert result_dp == expected_length, \
            f"DP solution failed for '{text1}' and '{text2}'. Expected {expected_length}, got {result_dp}"
        
        # Test LCS string reconstruction
        result_string = get_lcs_string(text1, text2)
        assert result_string == expected_string, \
            f"String reconstruction failed for '{text1}' and '{text2}'. Expected '{expected_string}', got '{result_string}'"
        
        print(f"Test passed for text1='{text1}', text2='{text2}'")

if __name__ == "__main__":
    test_longest_common_subsequence() 