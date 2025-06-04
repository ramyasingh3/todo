"""
Problem: Valid Palindrome

Write a function that checks if a given string is a palindrome.
A string is a palindrome if it reads the same forwards and backwards.
The function should:
1. Convert all characters to lowercase
2. Remove all non-alphanumeric characters
3. Return True if the string is a palindrome, False otherwise

Example:
Input: "A man, a plan, a canal: Panama"
Output: True  # Because "amanaplanacanalpanama" is a palindrome

Input: "race a car"
Output: False  # Because "raceacar" is not a palindrome
"""

def is_palindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the string is a palindrome
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "Madam, I'm Adam",
        "Never odd or even",
        "12321",
        "python",
        "Do geese see God?",
        "Able was I ere I saw Elba"
    ]
    
    for test in test_cases:
        result = is_palindrome(test)
        print(f"String: {test}")
        print(f"Is Palindrome: {result}")
        print("-" * 50)
