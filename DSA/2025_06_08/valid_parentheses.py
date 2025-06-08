# Valid Parentheses Implementation
def is_valid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    s = "()[]{}"
    print(is_valid(s)) 