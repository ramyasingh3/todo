# 07_valid_palindrome.py

def is_valid_palindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two pointer approach
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
if __name__ == "__main__":
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(is_valid_palindrome("race a car"))  # Output: False
    print(is_valid_palindrome("Was it a car or a cat I saw?"))  # Output: True
    print(is_valid_palindrome("hello"))  # Output: False
    print(is_valid_palindrome("Madam, I'm Adam"))  # Output: True
    print(is_valid_palindrome(""))  # Output: True
    print(is_valid_palindrome("a"))  # Output: True
    print(is_valid_palindrome(".,"))  # Output: True
    print(is_valid_palindrome("0P"))  # Output: False 