def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
        
    n = len(s)
    # dp[i][j] represents whether s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        
    start = 0
    max_len = 1
    
    # Check for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
            
    # Check for lengths greater than 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
                    
    return s[start:start+max_len]

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
    end = 0
    
    for i in range(len(s)):
        # Odd length palindromes
        left1, right1 = expandAroundCenter(i, i)
        # Even length palindromes
        left2, right2 = expandAroundCenter(i, i+1)
        
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
            
    return s[start:end+1]

def getAllPalindromes(s: str) -> list[str]:
    """
    Get all palindromic substrings in the given string.
    
    Args:
        s: Input string
        
    Returns:
        List of all palindromic substrings
    """
    def isPalindrome(sub: str) -> bool:
        return sub == sub[::-1]
        
    n = len(s)
    palindromes = []
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if isPalindrome(substring):
                palindromes.append(substring)
                
    return palindromes

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "babad"
    print(f"Input: '{s1}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s1)}'")  # Expected: "bab" or "aba"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s1)}'")  # Expected: "bab" or "aba"
    print("All palindromes:")
    for p in getAllPalindromes(s1):
        print(f"- '{p}'")
    
    # Test case 2
    s2 = "cbbd"
    print(f"\nInput: '{s2}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s2)}'")  # Expected: "bb"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s2)}'")  # Expected: "bb"
    print("All palindromes:")
    for p in getAllPalindromes(s2):
        print(f"- '{p}'")
    
    # Test case 3
    s3 = "a"
    print(f"\nInput: '{s3}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s3)}'")  # Expected: "a"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s3)}'")  # Expected: "a"
    print("All palindromes:")
    for p in getAllPalindromes(s3):
        print(f"- '{p}'")
    
    # Test case 4
    s4 = "racecar"
    print(f"\nInput: '{s4}'")
    print(f"Longest palindrome (DP): '{longestPalindrome(s4)}'")  # Expected: "racecar"
    print(f"Longest palindrome (Expand): '{longestPalindromeExpand(s4)}'")  # Expected: "racecar"
    print("All palindromes:")
    for p in getAllPalindromes(s4):
        print(f"- '{p}'") 