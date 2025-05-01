def length_of_longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of the longest substring without repeating characters
    """
    # Dictionary to store the last position of each character
    char_position = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If we find a repeating character, update the start pointer
        if char in char_position and char_position[char] >= start:
            start = char_position[char] + 1
        else:
            # Update max_length if current window is larger
            max_length = max(max_length, end - start + 1)
        
        # Update the last position of current character
        char_position[char] = end
    
    return max_length

# Test cases
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",    # Expected: 3 ("abc")
        "bbbbb",       # Expected: 1 ("b")
        "pwwkew",      # Expected: 3 ("wke")
        "",           # Expected: 0
        " ",          # Expected: 1
        "dvdf",       # Expected: 3 ("vdf")
        "abba",       # Expected: 2 ("ab" or "ba")
    ]
    
    for test in test_cases:
        result = length_of_longest_substring(test)
        print(f"Input: {test}")
        print(f"Output: {result}\n") 