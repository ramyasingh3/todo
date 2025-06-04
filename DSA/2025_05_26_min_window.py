# 18_min_window.py

def min_window(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ""
    
    # Count characters in target string
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1
    
    # Initialize variables
    window_count = {}
    required = len(target_count)
    formed = 0
    left = 0
    min_len = float('inf')
    result = ""
    
    # Sliding window
    for right, char in enumerate(s):
        # Add character to window
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if we've formed a required character
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        
        # Try to minimize window
        while left <= right and formed == required:
            # Update result if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Remove leftmost character
            window_count[s[left]] -= 1
            if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                formed -= 1
            left += 1
    
    return result

# Example usage
if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
    print(min_window("a", "a"))  # Output: "a"
    print(min_window("a", "aa"))  # Output: ""
    print(min_window("aa", "aa"))  # Output: "aa"
    print(min_window("abc", "b"))  # Output: "b"
    print(min_window("abc", "ac"))  # Output: "abc"
    print(min_window("aab", "aab"))  # Output: "aab"
    print(min_window("cabwefgewcwaefgcf", "cae"))  # Output: "cwae" 