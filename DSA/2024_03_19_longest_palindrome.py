# 12_longest_palindrome.py

def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Check odd length palindromes
        odd = expand_around_center(i, i)
        if len(odd) > len(longest):
            longest = odd
            
        # Check even length palindromes
        even = expand_around_center(i, i + 1)
        if len(even) > len(longest):
            longest = even
    
    return longest

# Example usage
if __name__ == "__main__":
    print(longest_palindrome("babad"))  # Output: "bab" or "aba"
    print(longest_palindrome("cbbd"))  # Output: "bb"
    print(longest_palindrome("a"))  # Output: "a"
    print(longest_palindrome(""))  # Output: ""
    print(longest_palindrome("racecar"))  # Output: "racecar"
    print(longest_palindrome("python"))  # Output: "p"
    print(longest_palindrome("madam"))  # Output: "madam"
    print(longest_palindrome("noon"))  # Output: "noon"
    print(longest_palindrome("level"))  # Output: "level" 