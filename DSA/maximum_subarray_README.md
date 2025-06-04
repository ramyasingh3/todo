# Maximum Subarray

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## Examples

### Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### Example 2:
```
Input: nums = [1]
Output: 1
```

### Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Approach
The solution uses Kadane's Algorithm, which is an efficient way to solve this problem in O(n) time complexity and O(1) space complexity. The algorithm works by maintaining two variables:
1. `current_sum`: Tracks the maximum sum of the subarray ending at the current position
2. `max_sum`: Tracks the overall maximum sum found so far

For each element in the array:
- Update `current_sum` to be the maximum of either the current element alone or the current element plus the previous `current_sum`
- Update `max_sum` if the new `current_sum` is greater

## Time Complexity
- O(n), where n is the length of the input array
- We traverse the array only once

## Space Complexity
- O(1)
- We use only a constant amount of extra space

## Solution Code
The solution is implemented in `maximum_subarray.py`. 