def longest_palindromic_substring(s: str) -> tuple[str, int]:
    """
    Find the longest palindromic substring in a given string using dynamic programming.
    
    Args:
        s (str): Input string
        
    Returns:
        tuple: (longest palindromic substring, its length)
    """
    if not s:
        return "", 0
        
    n = len(s)
    # dp[i][j] will be True if substring s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        
    # Check for substrings of length 2
    start = 0
    max_length = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
            
    # Check for lengths greater than 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1  # Ending index
            
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
                    
    return s[start:start+max_length], max_length

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "babad",           # Output: "bab" or "aba", Length: 3
        "cbbd",           # Output: "bb", Length: 2
        "a",              # Output: "a", Length: 1
        "ac",             # Output: "a", Length: 1
        "racecar",        # Output: "racecar", Length: 7
        "abba",           # Output: "abba", Length: 4
        "abcba",          # Output: "abcba", Length: 5
        "abcdcba",        # Output: "abcdcba", Length: 7
        "aacabdkacaa",    # Output: "aca", Length: 3
        "forgeeksskeegfor" # Output: "geeksskeeg", Length: 10
    ]
    
    for test in test_cases:
        substring, length = longest_palindromic_substring(test)
        print(f"Input String: {test}")
        print(f"Longest Palindromic Substring: {substring}")
        print(f"Length: {length}")
        print("-" * 50) 