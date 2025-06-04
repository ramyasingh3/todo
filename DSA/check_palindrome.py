# 02_check_palindrome.py

def is_palindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(is_palindrome("race a car"))  # Output: False
    print(is_palindrome("Was it a car or a cat I saw?"))  # Output: True
    print(is_palindrome("hello"))  # Output: False
    print(is_palindrome("Madam, I'm Adam"))  # Output: True 