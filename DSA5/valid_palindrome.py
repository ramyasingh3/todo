def is_palindrome(s):
    """
    Given a string s, return true if it is a palindrome, or false otherwise.
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if palindrome
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
if __name__ == "__main__":
    # Test 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: '{s1}'")
    print(f"Output: {is_palindrome(s1)}")  # Expected: True
    
    # Test 2
    s2 = "race a car"
    print(f"\nInput: '{s2}'")
    print(f"Output: {is_palindrome(s2)}")  # Expected: False
    
    # Test 3
    s3 = " "
    print(f"\nInput: '{s3}'")
    print(f"Output: {is_palindrome(s3)}")  # Expected: True 