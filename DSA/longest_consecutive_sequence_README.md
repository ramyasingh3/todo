# Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers `nums`, find the length of the longest consecutive sequence of numbers.

### Example
```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4], which has length 4.
```

## Solution Approach
1. Convert the array into a set for O(1) lookups
2. For each number in the array:
   - Check if it's the start of a sequence (by checking if num-1 exists)
   - If it is, count consecutive numbers until the sequence breaks
3. Keep track of the maximum sequence length found

### Time Complexity
- O(n) where n is the length of the input array
- Each number is only visited once due to the set lookup

### Space Complexity
- O(n) to store the set of numbers
