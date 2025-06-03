from typing import Dict

def is_valid(s: str) -> bool:
    """
    Check if the input string has valid parentheses.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[' and ']'
        
    Returns:
        True if the string has valid parentheses, False otherwise
        
    Example:
        >>> is_valid("()")
        True
        >>> is_valid("([)]")
        False
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':  # Opening bracket
            stack.append(char)
        elif char in ')}]':  # Closing bracket
            if not stack or stack.pop() != brackets[char]:
                return False
    
    # Stack should be empty if all brackets are matched
    return len(stack) == 0

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple valid case
    s1 = "()"
    print("Test case 1:")
    print(f"Input: s = {s1}")
    print(f"Output: {is_valid(s1)}")
    
    # Test case 2: Nested valid case
    s2 = "({[]})"
    print("\nTest case 2:")
    print(f"Input: s = {s2}")
    print(f"Output: {is_valid(s2)}")
    
    # Test case 3: Invalid case
    s3 = "([)]"
    print("\nTest case 3:")
    print(f"Input: s = {s3}")
    print(f"Output: {is_valid(s3)}")
    
    # Test case 4: Empty string
    s4 = ""
    print("\nTest case 4:")
    print(f"Input: s = {s4}")
    print(f"Output: {is_valid(s4)}")
    
    # Test case 5: Unmatched opening bracket
    s5 = "({["
    print("\nTest case 5:")
    print(f"Input: s = {s5}")
    print(f"Output: {is_valid(s5)}")
    
    # Test case 6: Unmatched closing bracket
    s6 = ")}]"
    print("\nTest case 6:")
    print(f"Input: s = {s6}")
    print(f"Output: {is_valid(s6)}") 