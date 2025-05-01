def is_valid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    Args:
        s (str): Input string containing brackets
        
    Returns:
        bool: True if the string is valid, False otherwise
    """
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
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

# Test cases
if __name__ == "__main__":
    test_cases = [
        "()",           # True
        "()[]{}",      # True
        "(]",          # False
        "([)]",        # False
        "{[]}",        # True
        "",            # True
        "(((",         # False
        ")))",         # False
    ]
    
    for test in test_cases:
        result = is_valid(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n") 