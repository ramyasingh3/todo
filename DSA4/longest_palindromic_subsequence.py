def longestPalindromeSubseq(s: str) -> int:
    """
    Find the length of the longest palindromic subsequence in a string.
    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest palindromic subsequence
    """
    n = len(s)
    # dp[i][j] represents the length of longest palindromic subsequence
    # in substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Check for subsequences of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "bbbab"
    print(f"Input: {s1}")
    print(f"Output: {longestPalindromeSubseq(s1)}")  # Expected: 4 (bbbb)
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: {s2}")
    print(f"Output: {longestPalindromeSubseq(s2)}")  # Expected: 2 (bb)
    
    # Test case 3
    s3 = "a"
    print(f"\nInput: {s3}")
    print(f"Output: {longestPalindromeSubseq(s3)}")  # Expected: 1 (a)
    
    # Test case 4
    s4 = "racecar"
    print(f"\nInput: {s4}")
    print(f"Output: {longestPalindromeSubseq(s4)}")  # Expected: 7 (racecar) 