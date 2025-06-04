# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## Approach
The solution uses a sliding window technique with a set to track unique characters:

1. Initialize a set to keep track of unique characters in the current window
2. Use two pointers (left and right) to represent the current window
3. Move the right pointer forward:
   - If the current character is not in the set, add it and update the maximum length
   - If the current character is in the set, move the left pointer forward and remove characters from the set until the current character is not in the set
4. Keep track of the maximum window size encountered

## Time Complexity
- O(n), where n is the length of the string
- Each character is visited at most twice (once by the right pointer and once by the left pointer)

## Space Complexity
- O(min(m, n)), where m is the size of the character set (ASCII has 128 characters)
- The space used by the set is bounded by the size of the character set

## Solution Code
The solution is implemented in `longest_substring_without_repeating.py` with detailed comments and example usage. 