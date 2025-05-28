def minWindow(s: str, t: str) -> str:
    """
    Find the minimum window in string s that contains all characters in string t.
    If there is no such window, return an empty string.
    
    Args:
        s: The source string
        t: The target string containing characters to find
        
    Returns:
        The minimum window substring containing all characters from t
    """
    if not s or not t or len(s) < len(t):
        return ""
        
    # Create frequency maps
    target_freq = {}
    window_freq = {}
    
    # Initialize target frequency map
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1
        
    required = len(target_freq)  # Number of unique characters needed
    formed = 0  # Number of unique characters formed in current window
    
    # Sliding window variables
    left = right = 0
    min_len = float('inf')
    result = ""
    
    while right < len(s):
        # Add character to window
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # If current character frequency matches target frequency
        if char in target_freq and window_freq[char] == target_freq[char]:
            formed += 1
            
        # Try to minimize window while maintaining all required characters
        while left <= right and formed == required:
            # Update result if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
                
            # Remove leftmost character
            char = s[left]
            window_freq[char] -= 1
            
            # If removed character was required and frequency is now less than target
            if char in target_freq and window_freq[char] < target_freq[char]:
                formed -= 1
                
            left += 1
            
        right += 1
        
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Output: '{minWindow(s1, t1)}'")  # Expected: "BANC"
    
    # Test case 2
    s2 = "a"
    t2 = "a"
    print(f"\nInput: s = '{s2}', t = '{t2}'")
    print(f"Output: '{minWindow(s2, t2)}'")  # Expected: "a"
    
    # Test case 3
    s3 = "a"
    t3 = "aa"
    print(f"\nInput: s = '{s3}', t = '{t3}'")
    print(f"Output: '{minWindow(s3, t3)}'")  # Expected: ""
    
    # Test case 4
    s4 = "cabwefgewcwaefgcf"
    t4 = "cae"
    print(f"\nInput: s = '{s4}', t = '{t4}'")
    print(f"Output: '{minWindow(s4, t4)}'")  # Expected: "cwae" 