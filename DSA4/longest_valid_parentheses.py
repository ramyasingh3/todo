"""
Longest Valid Parentheses

Problem:
Given a string containing just the characters '(' and ')', find the length of the longest valid
(well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
Explanation: There are no valid parentheses.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""

def longest_valid_parentheses(s: str) -> int:
    if not s:
        return 0
    
    # Initialize stack with -1 to handle edge cases
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            # Push index of opening bracket
            stack.append(i)
        else:
            # Pop the last opening bracket's index
            stack.pop()
            
            if not stack:
                # If stack is empty, push current index
                stack.append(i)
            else:
                # Calculate length of valid parentheses
                max_length = max(max_length, i - stack[-1])
    
    return max_length

# Test cases
def test_longest_valid_parentheses():
    # Test case 1: Basic case
    assert longest_valid_parentheses("(()") == 2
    
    # Test case 2: Multiple valid pairs
    assert longest_valid_parentheses(")()())") == 4
    
    # Test case 3: Empty string
    assert longest_valid_parentheses("") == 0
    
    # Test case 4: All valid
    assert longest_valid_parentheses("()()()") == 6
    
    # Test case 5: All invalid
    assert longest_valid_parentheses("(((") == 0
    
    # Test case 6: Nested valid
    assert longest_valid_parentheses("(()())") == 6
    
    # Test case 7: Single pair
    assert longest_valid_parentheses("()") == 2
    
    # Test case 8: Alternating valid and invalid
    assert longest_valid_parentheses("()(()") == 2
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_valid_parentheses() 