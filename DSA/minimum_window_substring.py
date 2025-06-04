"""
Find the minimum window substring in s that contains all the characters of t.
If there is no such window, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Time Complexity: O(n)
Space Complexity: O(m + n), where n = len(s), m = len(t)
"""

from collections import Counter, defaultdict

def min_window(s: str, t: str) -> str:
    """
    Sliding window solution to find the minimum window substring.
    """
    if not t or not s:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = defaultdict(int)
    ans = float('inf'), None, None  # window length, left, right
    
    while r < len(s):
        character = s[r]
        window_counts[character] += 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[s[l]] -= 1
            if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

# Test cases
def test_min_window():
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "A", ""),
        ("bba", "ab", "ba"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("", "a", ""),
        ("a", "", ""),
        ("abc", "d", ""),
        ("aa", "aa", "aa"),
    ]
    for s, t, expected in test_cases:
        result = min_window(s, t)
        assert result == expected, f"Failed for s='{s}', t='{t}'. Expected '{expected}', got '{result}'"
        print(f"Test passed for s='{s}', t='{t}'")

if __name__ == "__main__":
    test_min_window() 