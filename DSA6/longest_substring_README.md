# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples
```
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", with length 3.

Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", with length 1.

Input: s = "pwwkew"
Output: 3
Explanation: The longest substring without repeating characters is "wke", with length 3.
```

## Solution Approach
The solution uses the sliding window technique with a hash map. Here's how it works:

1. Use a dictionary to store the last position of each character we've seen.
2. Maintain two pointers: start and end of the current window.
3. For each character:
   - If we find a repeating character within our current window:
     - Update the start pointer to the position after the last occurrence of the repeating character
   - Otherwise:
     - Update the maximum length if the current window is larger
   - Update the last position of the current character

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input string
  - We process each character exactly once
- Space Complexity: O(min(m, n)), where:
  - n is the length of the input string
  - m is the size of the character set (e.g., ASCII, Unicode)
  - In the worst case, we store all unique characters in the hash map

## Implementation
The solution is implemented in `longest_substring.py` with detailed comments and test cases. The implementation handles various edge cases including:
- Empty strings
- Single character strings
- Strings with all repeating characters
- Strings with no repeating characters 