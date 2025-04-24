# Longest Substring Without Repeating Characters

## Problem Statement
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
The solution uses a sliding window approach with two pointers (left and right) to track the current window of characters. We maintain a set to keep track of unique characters in the current window. If we encounter a duplicate character, we move the left pointer forward until we remove the duplicate character from our window.

## Time Complexity
- O(n), where n is the length of the string
- Each character is visited at most twice (once by the right pointer and once by the left pointer)

## Space Complexity
- O(min(m, n)), where m is the size of the character set
- In the worst case, we need to store all unique characters in the set 