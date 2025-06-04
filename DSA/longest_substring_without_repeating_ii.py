def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    Uses sliding window technique.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    char_index = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: {s1}")
    print(f"Output: {length_of_longest_substring(s1)}")  # Expected: 3 (abc)
    
    # Test case 2
    s2 = "bbbbb"
    print(f"\nInput: {s2}")
    print(f"Output: {length_of_longest_substring(s2)}")  # Expected: 1 (b) 