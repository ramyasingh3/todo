def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # Create a dp table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    # Test case 1
    text1_1, text2_1 = "abcde", "ace"
    print(f"Input: text1 = '{text1_1}', text2 = '{text2_1}'")
    print(f"Output: {longestCommonSubsequence(text1_1, text2_1)}")  # Expected: 3
    
    # Test case 2
    text1_2, text2_2 = "abc", "abc"
    print(f"\nInput: text1 = '{text1_2}', text2 = '{text2_2}'")
    print(f"Output: {longestCommonSubsequence(text1_2, text2_2)}")  # Expected: 3
    
    # Test case 3
    text1_3, text2_3 = "abc", "def"
    print(f"\nInput: text1 = '{text1_3}', text2 = '{text2_3}'")
    print(f"Output: {longestCommonSubsequence(text1_3, text2_3)}")  # Expected: 0
    
    # Test case 4
    text1_4, text2_4 = "pmjghexybyrgzczy", "hafcdqbgncrcbihkd"
    print(f"\nInput: text1 = '{text1_4}', text2 = '{text2_4}'")
    print(f"Output: {longestCommonSubsequence(text1_4, text2_4)}")  # Expected: 4 