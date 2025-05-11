def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    A palindrome reads the same backward as forward.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    start = 0
    max_length = 1
    n = len(s)
    
    # dp[i][j] represents if substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
    
    # Check for substrings of length > 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1  # End index of current substring
            
            # Check if characters at i and j are same and
            # substring between them is also a palindrome
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start+max_length]

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    print(f"Input: s = '{s1}'")
    print(f"Output: '{longestPalindrome(s1)}'")  # Expected: "bab" or "aba"
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: s = '{s2}'")
    print(f"Output: '{longestPalindrome(s2)}'")  # Expected: "bb"
    
    # Test case 3
    s3 = "a"
    print(f"\nInput: s = '{s3}'")
    print(f"Output: '{longestPalindrome(s3)}'")  # Expected: "a"
    
    # Test case 4
    s4 = "racecar"
    print(f"\nInput: s = '{s4}'")
    print(f"Output: '{longestPalindrome(s4)}'")  # Expected: "racecar" 