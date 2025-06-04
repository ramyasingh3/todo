def find_anagrams(s: str, p: str) -> list[int]:
    """
    Find all starting indices of p's anagrams in s.
    
    Args:
        s: The main string to search in
        p: The string whose anagrams we need to find
        
    Returns:
        List of starting indices where anagrams of p are found in s
    """
    if len(p) > len(s):
        return []
        
    p_count = [0] * 26
    s_count = [0] * 26
    
    # Initialize the frequency counts for the first window
    for i in range(len(p)):
        p_count[ord(p[i]) - ord('a')] += 1
        s_count[ord(s[i]) - ord('a')] += 1
        
    result = []
    if p_count == s_count:
        result.append(0)
        
    # Slide the window and update the frequency counts
    for i in range(len(p), len(s)):
        # Remove the leftmost character from the window
        s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        # Add the new character to the window
        s_count[ord(s[i]) - ord('a')] += 1
        
        if p_count == s_count:
            result.append(i - len(p) + 1)
            
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    s1 = "cbaebabacd"
    p1 = "abc"
    print(f"Input: s = '{s1}', p = '{p1}'")
    print(f"Output: {find_anagrams(s1, p1)}")  # Expected: [0, 6]
    
    # Test case 2
    s2 = "abab"
    p2 = "ab"
    print(f"\nInput: s = '{s2}', p = '{p2}'")
    print(f"Output: {find_anagrams(s2, p2)}")  # Expected: [0, 1, 2] 