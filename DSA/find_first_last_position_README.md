# Find First and Last Position of Element in Sorted Array

## Problem Description
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If `target` is not found in the array, return `[-1, -1]`. You must write an algorithm with O(log n) runtime complexity.

## Examples
```
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: The target value 8 appears at positions 3 and 4.

Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: The target value 6 does not appear in the array.

Input: nums = [], target = 0
Output: [-1, -1]
Explanation: The array is empty, so the target is not found.
```

## Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

## Approach
1. Use binary search to find the first occurrence of the target
   - When we find the target, continue searching in the left half
   - This ensures we find the leftmost occurrence
2. Use binary search to find the last occurrence of the target
   - When we find the target, continue searching in the right half
   - This ensures we find the rightmost occurrence
3. Return the positions as [first, last]

## Time and Space Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution
The solution uses two binary searches:
1. First binary search to find the leftmost occurrence
2. Second binary search to find the rightmost occurrence
The key insight is that when we find the target, we need to continue searching in the appropriate half to find the boundary positions.

## Key Points
- The array is guaranteed to be sorted
- We need to find both the first and last occurrence
- The solution must be efficient (O(log n) time complexity)
- We need to handle edge cases (empty array, target not found)
- The array can contain duplicate elements 