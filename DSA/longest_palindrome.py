def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    max_length = 1
    
    # Helper function to expand around center
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

# Example usage
if __name__ == "__main__":
    test_cases = [
        "babad",  # Output: "bab" or "aba"
        "cbbd",   # Output: "bb"
        "a",      # Output: "a"
        "racecar", # Output: "racecar"
        "abba",   # Output: "abba"
        "abcde",  # Output: "a"
        "aaaa",   # Output: "aaaa"
    ]
    
    for test in test_cases:
        result = longest_palindrome(test)
        print(f"Input: {test}")
        print(f"Longest palindrome: {result}\n") 