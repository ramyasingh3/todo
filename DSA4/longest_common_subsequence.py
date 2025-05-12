def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # dp[i][j] represents the length of LCS of text1[0:i] and text2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

def getLCS(text1: str, text2: str) -> str:
    """
    Get the actual longest common subsequence string.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        The longest common subsequence string
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return ''.join(reversed(lcs))

# Example usage
if __name__ == "__main__":
    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length of LCS: {longestCommonSubsequence(text1, text2)}")  # Expected: 3
    print(f"LCS string: {getLCS(text1, text2)}")  # Expected: "ace"
    
    # Test case 2
    text1 = "abc"
    text2 = "abc"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length of LCS: {longestCommonSubsequence(text1, text2)}")  # Expected: 3
    print(f"LCS string: {getLCS(text1, text2)}")  # Expected: "abc"
    
    # Test case 3
    text1 = "abc"
    text2 = "def"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length of LCS: {longestCommonSubsequence(text1, text2)}")  # Expected: 0
    print(f"LCS string: {getLCS(text1, text2)}")  # Expected: ""
    
    # Test case 4
    text1 = "AGGTAB"
    text2 = "GXTXAYB"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length of LCS: {longestCommonSubsequence(text1, text2)}")  # Expected: 4
    print(f"LCS string: {getLCS(text1, text2)}")  # Expected: "GTAB" 