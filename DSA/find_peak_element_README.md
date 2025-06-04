# Find Peak Element

## Problem Description
A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

## Examples
```
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

## Constraints
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

## Approach
1. Use binary search to find a peak element
2. Compare the middle element with its right neighbor
3. If the middle element is greater than its right neighbor, the peak must be in the left half
4. If the middle element is less than its right neighbor, the peak must be in the right half
5. Continue until we find a peak element

## Time and Space Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution
The solution uses binary search to efficiently find a peak element. The key insight is that if an element is greater than its right neighbor, there must be a peak in the left half (including the current element). Similarly, if an element is less than its right neighbor, there must be a peak in the right half.

## Key Points
- The array is guaranteed to have at least one peak element
- We can use binary search because the array is not necessarily sorted
- The solution works for any array that satisfies the constraints
- We only need to compare with the right neighbor due to the nature of the problem 