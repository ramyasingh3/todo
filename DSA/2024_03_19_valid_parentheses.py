# 10_valid_parentheses.py

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # If stack is empty or top element doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Push opening bracket to stack
            stack.append(char)
    
    # Stack should be empty if all brackets are matched
    return len(stack) == 0

# Example usage
if __name__ == "__main__":
    print(is_valid_parentheses("()"))  # Output: True
    print(is_valid_parentheses("()[]{}"))  # Output: True
    print(is_valid_parentheses("(]"))  # Output: False
    print(is_valid_parentheses("([)]"))  # Output: False
    print(is_valid_parentheses("{[]}"))  # Output: True
    print(is_valid_parentheses(""))  # Output: True
    print(is_valid_parentheses("((("))  # Output: False
    print(is_valid_parentheses(")))"))  # Output: False
    print(is_valid_parentheses("({[]})"))  # Output: True 