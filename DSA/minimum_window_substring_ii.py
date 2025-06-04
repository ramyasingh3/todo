def min_window(s: str, t: str) -> str:
    """
    Find the minimum window in string s that contains all characters in string t.
    Uses sliding window technique with two pointers.
    
    Args:
        s: Source string
        t: Target string containing characters to find
        
    Returns:
        Minimum window substring containing all characters from t
    """
    if not s or not t or len(s) < len(t):
        return ""
        
    # Create frequency map for target string
    target_freq = {}
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1
        
    # Initialize variables for sliding window
    left = 0
    min_len = float('inf')
    min_start = 0
    matched = 0
    window_freq = {}
    
    # Expand window to the right
    for right in range(len(s)):
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # If current character matches target frequency
        if char in target_freq and window_freq[char] == target_freq[char]:
            matched += 1
            
        # Try to minimize window from left
        while matched == len(target_freq):
            # Update minimum window if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
                
            # Remove leftmost character
            left_char = s[left]
            window_freq[left_char] -= 1
            
            # If removing character affects matching
            if left_char in target_freq and window_freq[left_char] < target_freq[left_char]:
                matched -= 1
                
            left += 1
            
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(f"Input: s = {s1}, t = {t1}")
    print(f"Output: {min_window(s1, t1)}")  # Expected: "BANC"
    
    # Test case 2
    s2 = "a"
    t2 = "a"
    print(f"\nInput: s = {s2}, t = {t2}")
    print(f"Output: {min_window(s2, t2)}")  # Expected: "a" 