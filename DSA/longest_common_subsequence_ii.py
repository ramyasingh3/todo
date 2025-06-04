def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    A subsequence is a sequence that appears in both strings in the same order,
    but not necessarily consecutively.
    
    Args:
        text1: First string
        text2: Second string
        
    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # Create a DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
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
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {longest_common_subsequence(text1, text2)}")  # Expected: 3
    
    # Test case 2
    text1 = "abc"
    text2 = "def"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {longest_common_subsequence(text1, text2)}")  # Expected: 0
    
    # Test case 3
    text1 = "abc"
    text2 = "abc"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {longest_common_subsequence(text1, text2)}")  # Expected: 3 