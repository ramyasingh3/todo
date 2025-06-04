# Minimum Window Substring

## Problem Description
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

### Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

## Approach
The solution uses a sliding window technique with frequency counting:

1. Create frequency maps for both strings:
   - `t_freq`: Count of each character in t
   - `window_freq`: Count of each character in the current window
2. Use two pointers (left and right) to represent the current window
3. Expand the window by moving the right pointer:
   - Add the current character to window_freq
   - If the character completes a required character count, increment formed
4. Contract the window from the left when all required characters are present:
   - Update the result if the current window is smaller
   - Remove the leftmost character from window_freq
   - If the removed character was required, decrement formed
5. Keep track of the minimum window that contains all characters from t

## Time Complexity
- O(|S| + |T|), where |S| and |T| are the lengths of strings s and t
- We traverse string s twice (once with each pointer)
- We traverse string t once to create the frequency map

## Space Complexity
- O(|S| + |T|)
- We use two frequency maps that can store up to all unique characters in s and t

## Solution Code
The solution is implemented in `minimum_window_substring.py` with detailed comments and example usage. 