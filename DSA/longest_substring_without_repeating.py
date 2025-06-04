"""
Find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", with length 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", with length 1.

Time Complexity:
- Sliding Window Solution: O(n)
- Hash Map Solution: O(n)
Space Complexity:
- Sliding Window Solution: O(min(m, n)) where m is the size of the character set
- Hash Map Solution: O(min(m, n)) where m is the size of the character set
"""

from typing import Dict

def length_of_longest_substring_sliding_window(s: str) -> int:
    """
    Solution using sliding window technique.
    We maintain a window of characters that haven't been repeated.
    """
    if not s:
        return 0
    
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def length_of_longest_substring_hash_map(s: str) -> int:
    """
    Solution using hash map to store the last position of each character.
    This allows us to jump the left pointer directly to the position after the last occurrence.
    """
    if not s:
        return 0
    
    char_map: Dict[str, int] = {}
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

def get_longest_substring(s: str) -> str:
    """
    Helper function to get the actual longest substring without repeating characters.
    Uses the hash map solution to find the indices.
    """
    if not s:
        return ""
    
    char_map: Dict[str, int] = {}
    max_length = 0
    start_idx = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            start_idx = left
    
    return s[start_idx:start_idx + max_length]

# Test cases
def test_longest_substring():
    test_cases = [
        ("abcabcbb", 3, "abc"),
        ("bbbbb", 1, "b"),
        ("pwwkew", 3, "wke"),
        ("", 0, ""),
        ("a", 1, "a"),
        ("ab", 2, "ab"),
        ("aab", 2, "ab"),
        ("dvdf", 3, "vdf"),
        ("tmmzuxt", 5, "mzuxt"),
        ("abcabcbb", 3, "abc"),
    ]
    
    for s, expected_length, expected_substring in test_cases:
        # Test sliding window solution
        result_sliding = length_of_longest_substring_sliding_window(s)
        assert result_sliding == expected_length, \
            f"Sliding window solution failed for '{s}'. Expected length {expected_length}, got {result_sliding}"
        
        # Test hash map solution
        result_hash = length_of_longest_substring_hash_map(s)
        assert result_hash == expected_length, \
            f"Hash map solution failed for '{s}'. Expected length {expected_length}, got {result_hash}"
        
        # Test substring reconstruction
        result_substring = get_longest_substring(s)
        assert len(result_substring) == expected_length, \
            f"Substring reconstruction failed for '{s}'. Expected length {expected_length}, got {len(result_substring)}"
        assert result_substring == expected_substring, \
            f"Substring reconstruction failed for '{s}'. Expected '{expected_substring}', got '{result_substring}'"
        
        print(f"Test passed for s='{s}'")

if __name__ == "__main__":
    test_longest_substring() 