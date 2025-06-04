# Longest Increasing Subsequence

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples

### Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

### Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

### Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Approach
The solution uses dynamic programming with binary search to achieve O(n log n) time complexity. Here's how it works:

1. We maintain a list `tails` where `tails[i]` represents the smallest possible tail value for all increasing subsequences of length `i+1`
2. For each number in the input array:
   - If the number is larger than all elements in `tails`, append it to `tails`
   - Otherwise, find the first element in `tails` that is larger than or equal to the number and replace it with the number
3. The length of `tails` at the end is the length of the longest increasing subsequence

## Time Complexity
- O(n log n), where n is the length of the input array
- For each element, we perform a binary search operation which takes O(log n) time

## Space Complexity
- O(n)
- We maintain a `tails` array that can grow up to the size of the input array

## Solution Code
The solution is implemented in `longest_increasing_subsequence.py`. 