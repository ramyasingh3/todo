# Longest Common Prefix

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

## Examples
```
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Approach
1. If the input array is empty, return an empty string
2. Find the shortest string in the array (since the common prefix cannot be longer than the shortest string)
3. For each character position in the shortest string:
   - Compare the character with the same position in all other strings
   - If any character doesn't match, return the prefix up to that position
4. If all characters match, return the entire shortest string

## Time Complexity
- O(S), where S is the sum of all characters in all strings
- In the worst case, we need to compare all characters in all strings

## Space Complexity
- O(1), as we only use a constant amount of extra space

## Solution
The solution is implemented in `longest_common_prefix.py` with detailed comments and test cases.

## Solution Approaches

### 1. Vertical Scanning (O(S))
- Compares characters vertically (column by column)
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(1)
- Most efficient for most cases
- Stops early when mismatch found

### 2. Horizontal Scanning (O(S))
- Compares strings horizontally (pair by pair)
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(1)
- Simple to understand
- Good for learning the concept

### 3. Divide and Conquer (O(S))
- Divides the problem into smaller subproblems
- Time Complexity: O(S), where S is the sum of all characters
- Space Complexity: O(m log n), where m is the length of the longest string
- More complex but educational
- Good for understanding divide and conquer

## Time Complexity
- Vertical Scanning: O(S)
- Horizontal Scanning: O(S)
- Divide and Conquer: O(S)

## Space Complexity
- Vertical Scanning: O(1)
- Horizontal Scanning: O(1)
- Divide and Conquer: O(m log n)

## Usage
```python
from longest_common_prefix import Solution

solution = Solution()
strs = ["flower", "flow", "flight"]

# Using vertical scanning
result = solution.longest_common_prefix_vertical(strs)
print(f"Longest common prefix: {result}")

# Using horizontal scanning
result = solution.longest_common_prefix_horizontal(strs)
print(f"Longest common prefix: {result}")

# Using divide and conquer
result = solution.longest_common_prefix_divide(strs)
print(f"Longest common prefix: {result}")
```

## Common Applications
- String matching
- Text processing
- DNA sequence analysis
- File path resolution
- URL routing 