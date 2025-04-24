def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of the longest substring without repeating characters
    """
    # Initialize variables
    char_set = set()
    left = 0
    max_length = 0
    
    # Iterate through the string with right pointer
    for right in range(len(s)):
        # If current character is in the set, move left pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length if current window is larger
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: {s1}")
    print(f"Output: {lengthOfLongestSubstring(s1)}")  # Expected: 3
    
    # Test case 2
    s2 = "bbbbb"
    print(f"\nInput: {s2}")
    print(f"Output: {lengthOfLongestSubstring(s2)}")  # Expected: 1
    
    # Test case 3
    s3 = "pwwkew"
    print(f"\nInput: {s3}")
    print(f"Output: {lengthOfLongestSubstring(s3)}")  # Expected: 3 