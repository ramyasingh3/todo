# Valid Parentheses - DSA Solution

def is_valid_parentheses(s: str) -> bool:
    """
    Check if the given string of parentheses is valid.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[' and ']'
    
    Returns:
        bool: True if parentheses are valid, False otherwise
    """
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets_map[char]:
                return False
    
    return len(stack) == 0

# Example usage
if __name__ == "__main__":
    test_cases = [
        "()",           # True
        "()[]{}",       # True
        "(]",           # False
        "([)]",         # False
        "{[]}",         # True
        "(((",          # False
        ")))",          # False
        "",             # True
        "({[]})",       # True
        "([{}])",       # True
    ]
    
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"'{test}' -> {result}")