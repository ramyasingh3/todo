# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
1. Valid anagram:
   ```
   Input: s = "anagram", t = "nagaram"
   Output: true
   Explanation: Both strings contain the same letters in different order.
   ```

2. Not an anagram:
   ```
   Input: s = "rat", t = "car"
   Output: false
   Explanation: The strings contain different letters.
   ```

3. Different lengths:
   ```
   Input: s = "a", t = "ab"
   Output: false
   Explanation: The strings have different lengths.
   ```

## Solution Approaches

### 1. Sorting Solution (O(n log n))
- Sorts both strings and compares them
- Time Complexity: O(n log n)
- Space Complexity: O(1) or O(n)
- Simple but less efficient
- Good for understanding the concept

### 2. Counter Solution (O(n))
- Uses a counter to track character frequencies
- Time Complexity: O(n)
- Space Complexity: O(1)
- More efficient
- Uses built-in Counter class

### 3. Array-based Solution (O(n))
- Uses a fixed-size array to count characters
- Time Complexity: O(n)
- Space Complexity: O(1)
- Most efficient
- Good for learning character counting

## Time Complexity
- Sorting: O(n log n)
- Counter: O(n)
- Array-based: O(n)

## Space Complexity
- Sorting: O(1) or O(n)
- Counter: O(1)
- Array-based: O(1)

## Usage
```python
from valid_anagram import Solution

solution = Solution()
s = "anagram"
t = "nagaram"

# Using sorting solution
result = solution.is_anagram_sort(s, t)
print(f"Is anagram: {result}")

# Using counter solution
result = solution.is_anagram_counter(s, t)
print(f"Is anagram: {result}")

# Using array-based solution
result = solution.is_anagram_array(s, t)
print(f"Is anagram: {result}")
```

## Common Applications
- Word games
- Text analysis
- Cryptography
- Data validation
- Pattern matching 