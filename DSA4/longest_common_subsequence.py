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
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

def longestCommonSubsequenceMemo(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence using memoization.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    memo = {}
    
    def lcs(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0
            
        if (i, j) in memo:
            return memo[(i, j)]
            
        if text1[i-1] == text2[j-1]:
            memo[(i, j)] = lcs(i-1, j-1) + 1
        else:
            memo[(i, j)] = max(lcs(i-1, j), lcs(i, j-1))
            
        return memo[(i, j)]
        
    return lcs(m, n)

def getLongestCommonSubsequence(text1: str, text2: str) -> str:
    """
    Get the actual longest common subsequence between two strings.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        The longest common subsequence
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
    
    # Reconstruct the subsequence
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

def getAllCommonSubsequences(text1: str, text2: str) -> list[str]:
    """
    Get all common subsequences between two strings.
    
    Args:
        text1: First input string
        text2: Second input string
        
    Returns:
        List of all common subsequences
    """
    def isSubsequence(sub: str, text: str) -> bool:
        it = iter(text)
        return all(c in it for c in sub)
        
    def generateSubsequences(text: str) -> list[str]:
        n = len(text)
        subsequences = []
        
        for i in range(1, 1 << n):
            sub = ''
            for j in range(n):
                if i & (1 << j):
                    sub += text[j]
            subsequences.append(sub)
            
        return subsequences
        
    # Generate all subsequences of text1
    subs1 = generateSubsequences(text1)
    
    # Filter subsequences that are also subsequences of text2
    common_subs = [sub for sub in subs1 if isSubsequence(sub, text2)]
    
    return sorted(common_subs, key=len, reverse=True)

# Example usage
if __name__ == "__main__":
    # Test case 1
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length (DP): {longestCommonSubsequence(text1, text2)}")  # Expected: 3
    print(f"Length (Memo): {longestCommonSubsequenceMemo(text1, text2)}")  # Expected: 3
    print(f"LCS: '{getLongestCommonSubsequence(text1, text2)}'")  # Expected: "ace"
    print("All common subsequences:")
    for sub in getAllCommonSubsequences(text1, text2):
        print(f"- '{sub}'")
    
    # Test case 2
    text1 = "abc"
    text2 = "abc"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length (DP): {longestCommonSubsequence(text1, text2)}")  # Expected: 3
    print(f"Length (Memo): {longestCommonSubsequenceMemo(text1, text2)}")  # Expected: 3
    print(f"LCS: '{getLongestCommonSubsequence(text1, text2)}'")  # Expected: "abc"
    print("All common subsequences:")
    for sub in getAllCommonSubsequences(text1, text2):
        print(f"- '{sub}'")
    
    # Test case 3
    text1 = "abc"
    text2 = "def"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length (DP): {longestCommonSubsequence(text1, text2)}")  # Expected: 0
    print(f"Length (Memo): {longestCommonSubsequenceMemo(text1, text2)}")  # Expected: 0
    print(f"LCS: '{getLongestCommonSubsequence(text1, text2)}'")  # Expected: ""
    print("All common subsequences:")
    for sub in getAllCommonSubsequences(text1, text2):
        print(f"- '{sub}'")
    
    # Test case 4
    text1 = "AGGTAB"
    text2 = "GXTXAYB"
    print(f"\nInput: text1 = '{text1}', text2 = '{text2}'")
    print(f"Length (DP): {longestCommonSubsequence(text1, text2)}")  # Expected: 4
    print(f"Length (Memo): {longestCommonSubsequenceMemo(text1, text2)}")  # Expected: 4
    print(f"LCS: '{getLongestCommonSubsequence(text1, text2)}'")  # Expected: "GTAB"
    print("All common subsequences:")
    for sub in getAllCommonSubsequences(text1, text2):
        print(f"- '{sub}'") 