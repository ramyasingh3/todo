# Group Anagrams

## Problem Description
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
1. Basic case:
   ```
   Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
   Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
   Explanation: Words with same letters are grouped together
   ```

2. Empty strings:
   ```
   Input: [""]
   Output: [[""]]
   Explanation: Empty string forms its own group
   ```

3. Single character strings:
   ```
   Input: ["a", "b", "a"]
   Output: [["a", "a"], ["b"]]
   Explanation: Same characters are grouped together
   ```

## Solution Approaches

### 1. Sorting Solution (O(n * k log k))
- Sort characters of each string to create key
- Group strings by sorted key
- Time Complexity: O(n * k log k)
- Space Complexity: O(n * k)
- Best for readability and simplicity

### 2. Character Counting Solution (O(n * k))
- Create character frequency array for each string
- Use frequency array as key
- Time Complexity: O(n * k)
- Space Complexity: O(n * k)
- Best for performance

### 3. Prime Number Solution (O(n * k))
- Assign prime number to each character
- Use product as key
- Time Complexity: O(n * k)
- Space Complexity: O(n * k)
- Best for understanding hash functions

Where:
- n is the number of strings
- k is the maximum length of a string

## Time Complexity
- Sorting: O(n * k log k)
- Character Counting: O(n * k)
- Prime Number: O(n * k)

## Space Complexity
All solutions: O(n * k)

## Usage
```python
from group_anagrams import Solution

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Using sorting
result = solution.group_anagrams_sort(strs)
print(result)  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# Using character counting
result = solution.group_anagrams_count(strs)
print(result)  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# Using prime numbers
result = solution.group_anagrams_prime(strs)
print(result)  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

## Common Applications
- Word grouping in dictionaries
- Spell checking
- Word games and puzzles
- Text analysis
- Natural language processing
- Cryptography 