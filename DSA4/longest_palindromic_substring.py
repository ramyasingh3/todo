def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring using dynamic programming.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
            
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
                    
    return s[start:start + max_len]

def longestPalindromeExpand(s: str) -> str:
    """
    Find the longest palindromic substring using expand around center approach.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
        
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # Odd length palindromes
        left, right = expandAroundCenter(i, i)
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1
            
        # Even length palindromes
        left, right = expandAroundCenter(i, i + 1)
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1
            
    return s[start:start + max_len]

def getAllPalindromicSubstrings(s: str) -> list[str]:
    """
    Get all palindromic substrings.
    
    Args:
        s: Input string
        
    Returns:
        List of all palindromic substrings
    """
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
        
    n = len(s)
    palindromes = []
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if isPalindrome(substring):
                palindromes.append(substring)
                
    return sorted(palindromes, key=len, reverse=True)

def getPalindromicSubstringsByLength(s: str) -> dict[int, list[str]]:
    """
    Get palindromic substrings grouped by their lengths.
    
    Args:
        s: Input string
        
    Returns:
        Dictionary mapping lengths to lists of palindromic substrings
    """
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]
        
    n = len(s)
    palindromes_by_length = {}
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if isPalindrome(substring):
                length = len(substring)
                if length not in palindromes_by_length:
                    palindromes_by_length[length] = []
                palindromes_by_length[length].append(substring)
                
    return palindromes_by_length

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    print(f"Input: '{s1}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s1)}'")  # Expected: "bab" or "aba"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s1)}'")  # Expected: "bab" or "aba"
    print("\nAll palindromic substrings:")
    for pal in getAllPalindromicSubstrings(s1):
        print(f"- '{pal}'")
    print("\nPalindromic substrings by length:")
    for length, pals in getPalindromicSubstringsByLength(s1).items():
        print(f"Length {length}: {pals}")
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: '{s2}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s2)}'")  # Expected: "bb"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s2)}'")  # Expected: "bb"
    print("\nAll palindromic substrings:")
    for pal in getAllPalindromicSubstrings(s2):
        print(f"- '{pal}'")
    print("\nPalindromic substrings by length:")
    for length, pals in getPalindromicSubstringsByLength(s2).items():
        print(f"Length {length}: {pals}")
    
    # Test case 3
    s3 = "a"
    print(f"\nInput: '{s3}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s3)}'")  # Expected: "a"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s3)}'")  # Expected: "a"
    print("\nAll palindromic substrings:")
    for pal in getAllPalindromicSubstrings(s3):
        print(f"- '{pal}'")
    print("\nPalindromic substrings by length:")
    for length, pals in getPalindromicSubstringsByLength(s3).items():
        print(f"Length {length}: {pals}")
    
    # Test case 4
    s4 = "racecar"
    print(f"\nInput: '{s4}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s4)}'")  # Expected: "racecar"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s4)}'")  # Expected: "racecar"
    print("\nAll palindromic substrings:")
    for pal in getAllPalindromicSubstrings(s4):
        print(f"- '{pal}'")
    print("\nPalindromic substrings by length:")
    for length, pals in getPalindromicSubstringsByLength(s4).items():
        print(f"Length {length}: {pals}") 