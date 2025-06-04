# Search in Rotated Sorted Array

## Problem Description
There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`. Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

## Examples
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Explanation: Target 0 is found at index 4.

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
Explanation: 3 is not in nums so return -1.

Input: nums = [1], target = 0
Output: -1
Explanation: 0 is not in nums so return -1.
```

## Constraints
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

## Approach
1. Use binary search to find the target
2. At each step, determine which half of the array is sorted
3. If the left half is sorted:
   - Check if target is in the left half
   - If yes, search in left half
   - If no, search in right half
4. If the right half is sorted:
   - Check if target is in the right half
   - If yes, search in right half
   - If no, search in left half

## Time and Space Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution
The solution uses a modified binary search approach. The key insight is that in a rotated sorted array, at least one half (either left or right of the middle element) must be sorted. We can use this property to determine which half to search in.

## Key Points
- The array is guaranteed to be sorted before rotation
- All elements in the array are unique
- We need to handle the case where the array is rotated at any point
- The solution must be efficient (O(log n) time complexity)
- The array can be rotated any number of times 