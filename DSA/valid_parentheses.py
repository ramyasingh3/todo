"""
Valid Parentheses Implementation

This file contains an implementation of the Valid Parentheses problem using a stack approach.

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s: str) -> bool:
    """
    Determine if the input string has valid parentheses.
    Valid parentheses means every opening bracket has a corresponding closing bracket
    of the same type and in the correct order.
    
    Args:
        s: Input string containing only '(', ')', '{', '}', '[' and ']'
        
    Returns:
        bool: True if the string has valid parentheses, False otherwise
        
    Example:
        >>> is_valid("()")
        True
        >>> is_valid("()[]{}")
        True
        >>> is_valid("(]")
        False
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or top of stack doesn't match
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # Stack should be empty if all brackets are properly matched
    return len(stack) == 0

def test_solution():
    # Test cases
    test_cases = [
        ("()", True),           # Simple valid case
        ("()[]{}", True),       # Multiple valid pairs
        ("(]", False),          # Invalid pair
        ("([)]", False),        # Invalid order
        ("{[]}", True),         # Nested valid pairs
        ("", True),             # Empty string
        ("(", False),           # Unclosed bracket
        (")", False),           # Unopened bracket
        ("(((", False),         # Multiple unclosed brackets
        (")))", False),         # Multiple unopened brackets
        ("({[]})", True),       # Complex nested valid case
        ("(hello[world]{!})", True),  # Valid with other characters
    ]
    
    print("Running test cases for Valid Parentheses problem:")
    print("-" * 50)
    
    for input_str, expected in test_cases:
        result = is_valid(input_str)
        print(f"Input: {input_str}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'PASSED' if result == expected else 'FAILED'}")
        print("-" * 50)

if __name__ == "__main__":
    test_solution() 