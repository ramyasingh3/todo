def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
    
    Args:
        s: Input string
        
    Returns:
        True if s is a palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
    """
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic palindrome
    s1 = "A man, a plan, a canal: Panama"
    print("Test case 1:")
    print(f"Input: s = '{s1}'")
    print(f"Is palindrome: {is_palindrome(s1)}")
    
    # Test case 2: Not a palindrome
    s2 = "race a car"
    print("\nTest case 2:")
    print(f"Input: s = '{s2}'")
    print(f"Is palindrome: {is_palindrome(s2)}")
    
    # Test case 3: Empty string
    s3 = ""
    print("\nTest case 3:")
    print(f"Input: s = '{s3}'")
    print(f"Is palindrome: {is_palindrome(s3)}")
    
    # Test case 4: Single character
    s4 = "a"
    print("\nTest case 4:")
    print(f"Input: s = '{s4}'")
    print(f"Is palindrome: {is_palindrome(s4)}")
    
    # Test case 5: Palindrome with numbers
    s5 = "12321"
    print("\nTest case 5:")
    print(f"Input: s = '{s5}'")
    print(f"Is palindrome: {is_palindrome(s5)}") 