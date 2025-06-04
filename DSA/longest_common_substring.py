"""
Find the length of the longest common substring between two strings.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: text1 = "ABCDGH", text2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" with length 4.

Example 2:
Input: text1 = "ABC", text2 = "DEF"
Output: 0
Explanation: There is no common substring.

Time Complexity:
- Dynamic Programming: O(m*n)
- Suffix Tree: O(m+n)
Space Complexity:
- Dynamic Programming: O(m*n)
- Suffix Tree: O(m+n)
"""

from typing import List, Tuple

def longest_common_substring_dp(text1: str, text2: str) -> int:
    """
    Dynamic programming solution.
    dp[i][j] represents the length of the longest common substring ending at text1[i] and text2[j].
    """
    if not text1 or not text2:
        return 0
    
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length

def get_longest_common_substring(text1: str, text2: str) -> str:
    """
    Helper function to get the actual longest common substring.
    Uses the DP table to reconstruct the substring.
    """
    if not text1 or not text2:
        return ""
    
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_pos = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
    
    return text1[end_pos - max_length:end_pos]

def longest_common_substring_suffix_tree(text1: str, text2: str) -> int:
    """
    Solution using suffix tree approach.
    This is a more efficient solution for very long strings.
    """
    if not text1 or not text2:
        return 0
    
    # Combine strings with special characters
    combined = text1 + '#' + text2 + '$'
    n = len(combined)
    
    # Generate all suffixes
    suffixes = []
    for i in range(n):
        suffixes.append((combined[i:], i))
    suffixes.sort()
    
    # Find longest common prefix between adjacent suffixes
    max_length = 0
    for i in range(len(suffixes) - 1):
        s1, pos1 = suffixes[i]
        s2, pos2 = suffixes[i + 1]
        
        # Check if suffixes are from different strings
        if (pos1 < len(text1) and pos2 > len(text1)) or \
           (pos2 < len(text1) and pos1 > len(text1)):
            # Find common prefix length
            common_length = 0
            while common_length < len(s1) and common_length < len(s2) and \
                  s1[common_length] == s2[common_length]:
                common_length += 1
            max_length = max(max_length, common_length)
    
    return max_length

# Test cases
def test_longest_common_substring():
    test_cases = [
        ("ABCDGH", "ACDGHR", 4, "CDGH"),
        ("ABC", "DEF", 0, ""),
        ("", "", 0, ""),
        ("A", "A", 1, "A"),
        ("A", "B", 0, ""),
        ("ABCDE", "ABCDE", 5, "ABCDE"),
        ("ABCDE", "FGHIJ", 0, ""),
        ("ABCDE", "CDE", 3, "CDE"),
        ("ABCDE", "XYZCDE", 3, "CDE"),
        ("ABCDE", "ABCDEF", 5, "ABCDE"),
    ]
    
    for text1, text2, expected_length, expected_substring in test_cases:
        # Test DP solution
        result_dp = longest_common_substring_dp(text1, text2)
        assert result_dp == expected_length, \
            f"DP solution failed for '{text1}' and '{text2}'. Expected length {expected_length}, got {result_dp}"
        
        # Test suffix tree solution
        result_suffix = longest_common_substring_suffix_tree(text1, text2)
        assert result_suffix == expected_length, \
            f"Suffix tree solution failed for '{text1}' and '{text2}'. Expected length {expected_length}, got {result_suffix}"
        
        # Test substring reconstruction
        result_substring = get_longest_common_substring(text1, text2)
        assert len(result_substring) == expected_length, \
            f"Substring reconstruction failed for '{text1}' and '{text2}'. Expected length {expected_length}, got {len(result_substring)}"
        if expected_length > 0:
            assert result_substring in text1 and result_substring in text2, \
                f"Substring reconstruction failed for '{text1}' and '{text2}'. Result '{result_substring}' is not common"
        
        print(f"Test passed for text1='{text1}' and text2='{text2}'")

if __name__ == "__main__":
    test_longest_common_substring() 