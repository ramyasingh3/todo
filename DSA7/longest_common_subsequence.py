def longest_common_subsequence(text1: str, text2: str) -> tuple[int, str]:
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    Args:
        text1 (str): First input string
        text2 (str): Second input string
        
    Returns:
        tuple: (length of LCS, the LCS string)
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
            
    return dp[m][n], ''.join(reversed(lcs))

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("ABCDGH", "AEDFHR"),           # LCS: "ADH", Length: 3
        ("AGGTAB", "GXTXAYB"),          # LCS: "GTAB", Length: 4
        ("HELLO", "WORLD"),             # LCS: "LO", Length: 2
        ("ABCDEF", "ABCDEF"),           # LCS: "ABCDEF", Length: 6
        ("", "ABCD"),                   # LCS: "", Length: 0
        ("ABCD", ""),                   # LCS: "", Length: 0
        ("ABCD", "EFGH"),               # LCS: "", Length: 0
        ("ABCDEF", "DEFGHI"),           # LCS: "DEF", Length: 3
        ("ABCDEF", "FEDCBA"),           # LCS: "A", Length: 1
        ("ABCDEF", "ABCDEFGHI")         # LCS: "ABCDEF", Length: 6
    ]
    
    for text1, text2 in test_cases:
        length, lcs = longest_common_subsequence(text1, text2)
        print(f"String 1: {text1}")
        print(f"String 2: {text2}")
        print(f"LCS Length: {length}")
        print(f"LCS: {lcs}")
        print("-" * 50) 