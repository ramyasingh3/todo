# Palindrome Number - DSA Solution

def is_palindrome(x: int) -> bool:
    """
    Check if a given integer is a palindrome.
    
    Args:
        x: Integer to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert to string for easier comparison
    num_str = str(x)
    return num_str == num_str[::-1]

def is_palindrome_math(x: int) -> bool:
    """
    Check if a given integer is a palindrome using mathematical approach.
    
    Args:
        x: Integer to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Single digit numbers are palindromes
    if x < 10:
        return True
    
    # Find the number of digits
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    return original == reversed_num

# Example usage
if __name__ == "__main__":
    test_cases = [
        121,    # True
        -121,   # False
        10,     # False
        12321,  # True
        12345,  # False
        0,      # True
        1,      # True
        123,    # False
        1221,   # True
        1234,   # False
    ]
    
    print("Using string method:")
    for num in test_cases:
        result = is_palindrome(num)
        print(f"{num} -> {result}")
    
    print("\nUsing mathematical method:")
    for num in test_cases:
        result = is_palindrome_math(num)
        print(f"{num} -> {result}") 