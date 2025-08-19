def reverse_string(s):
    """
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test cases
if __name__ == "__main__":
    # Test 1
    s1 = ["h", "e", "l", "l", "o"]
    print(f"Input: {s1}")
    reverse_string(s1)
    print(f"Output: {s1}")  # Expected: ['o', 'l', 'l', 'e', 'h']
    
    # Test 2
    s2 = ["H", "a", "n", "n", "a", "h"]
    print(f"\nInput: {s2}")
    reverse_string(s2)
    print(f"Output: {s2}")  # Expected: ['h', 'a', 'n', 'n', 'a', 'H']
    
    # Test 3
    s3 = ["a"]
    print(f"\nInput: {s3}")
    reverse_string(s3)
    print(f"Output: {s3}")  # Expected: ['a'] 