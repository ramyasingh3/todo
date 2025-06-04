# Longest Palindromic Substring

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

### Example 3:
```
Input: s = "a"
Output: "a"
```

## Constraints:
- 1 <= s.length <= 1000
- s consist only of lowercase English letters.

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a 2D DP table where dp[i][j] represents whether the substring s[i:j+1] is a palindrome.

2. Base cases:
   - Every single character is a palindrome (dp[i][i] = True)
   - For substrings of length 2, check if both characters are the same

3. For substrings of length > 2:
   - If s[i] == s[j] and dp[i+1][j-1] is True, then dp[i][j] is True
   - Keep track of the longest palindrome found so far

4. Return the longest palindromic substring

## Time and Space Complexity
- Time Complexity: O(n²), where n is the length of the input string
- Space Complexity: O(n²) for the DP table

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation. 