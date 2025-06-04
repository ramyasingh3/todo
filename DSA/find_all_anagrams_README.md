# Find All Anagrams in a String

## Problem Description
Given two strings `s` and `p`, find all the start indices of `p`'s anagrams in `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
```
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

### Example 2:
```
Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Approach
The solution uses a sliding window technique with frequency counting:

1. Create frequency counts for both strings using arrays of size 26 (for lowercase English letters)
2. Initialize the frequency counts for the first window of size `len(p)` in `s`
3. Compare the frequency counts of the first window with `p`'s frequency count
4. Slide the window one character at a time, updating the frequency counts:
   - Remove the leftmost character from the window
   - Add the new character to the window
5. If the frequency counts match at any point, add the starting index to the result

## Time Complexity
- O(n), where n is the length of string `s`
- We traverse the string `s` once while maintaining the frequency counts

## Space Complexity
- O(1)
- We use fixed-size arrays (size 26) for frequency counting, regardless of input size

## Solution Code
The solution is implemented in `find_all_anagrams.py` with detailed comments and example usage. 