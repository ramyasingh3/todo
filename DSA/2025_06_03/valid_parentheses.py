from typing import Dict

def is_valid(s: str) -> bool:
    """
    Check if the input string has valid parentheses.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[' and ']'
        
    Returns:
        True if the input string is valid, False otherwise
        
    Example:
        >>> is_valid("()")
        True
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
    """
    # Map of closing brackets to their corresponding opening brackets
    brackets: Dict[str, str] = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening brackets
    stack = []
    
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top of stack doesn't match
            if not stack or stack[-1] != brackets[char]:
                return False
            # Pop the matching opening bracket
            stack.pop()
    
    # Stack should be empty for valid string
    return len(stack) == 0

# Example usage
if __name__ == "__main__":
    # Test case 1: Simple valid case
    s1 = "()"
    print(f"Input: {s1}")
    print(f"Output: {is_valid(s1)}")
    print(f"Explanation: Valid because each opening bracket has a matching closing bracket")
    
    # Test case 2: Multiple types of brackets
    s2 = "()[]{}"
    print(f"\nInput: {s2}")
    print(f"Output: {is_valid(s2)}")
    print(f"Explanation: Valid because each opening bracket has a matching closing bracket")
    
    # Test case 3: Invalid case
    s3 = "(]"
    print(f"\nInput: {s3}")
    print(f"Output: {is_valid(s3)}")
    print(f"Explanation: Invalid because the closing bracket ']' doesn't match the opening bracket '('")
    
    # Test case 4: Nested brackets
    s4 = "([{}])"
    print(f"\nInput: {s4}")
    print(f"Output: {is_valid(s4)}")
    print(f"Explanation: Valid because the brackets are properly nested")
    
    # Test case 5: Unmatched opening bracket
    s5 = "("
    print(f"\nInput: {s5}")
    print(f"Output: {is_valid(s5)}")
    print(f"Explanation: Invalid because there is an unmatched opening bracket") 