def is_palindrome(s):
    """
    Check if a string is a palindrome after removing non-alphanumeric chars.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Test
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
