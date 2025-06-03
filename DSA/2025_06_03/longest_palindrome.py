def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring in s.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
        
    Example:
        >>> longest_palindrome("babad")
        'bab'
    """
    if not s:
        return ""
        
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Check for odd length palindromes
        left, right = expand_around_center(i, i)
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
            
        # Check for even length palindromes
        left, right = expand_around_center(i, i + 1)
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
    
    return s[start:start + max_length]

def longest_palindrome_dp(s: str) -> str:
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
    max_length = 1
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    s1 = "babad"
    print("Test case 1:")
    print(f"Input: s = {s1}")
    print(f"Using expand around center: {longest_palindrome(s1)}")
    print(f"Using dynamic programming: {longest_palindrome_dp(s1)}")
    
    # Test case 2: Single character
    s2 = "a"
    print("\nTest case 2:")
    print(f"Input: s = {s2}")
    print(f"Using expand around center: {longest_palindrome(s2)}")
    print(f"Using dynamic programming: {longest_palindrome_dp(s2)}")
    
    # Test case 3: Empty string
    s3 = ""
    print("\nTest case 3:")
    print(f"Input: s = {s3}")
    print(f"Using expand around center: {longest_palindrome(s3)}")
    print(f"Using dynamic programming: {longest_palindrome_dp(s3)}")
    
    # Test case 4: All same characters
    s4 = "aaaa"
    print("\nTest case 4:")
    print(f"Input: s = {s4}")
    print(f"Using expand around center: {longest_palindrome(s4)}")
    print(f"Using dynamic programming: {longest_palindrome_dp(s4)}")
    
    # Test case 5: No palindrome
    s5 = "abc"
    print("\nTest case 5:")
    print(f"Input: s = {s5}")
    print(f"Using expand around center: {longest_palindrome(s5)}")
    print(f"Using dynamic programming: {longest_palindrome_dp(s5)}") 