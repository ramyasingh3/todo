# Find Peak Element

## Problem Description
Given an integer array `nums`, find a peak element and return its index. A peak element is an element that is strictly greater than its neighbors.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

## Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: 6 is a peak element and your function should return the index number 5.
```

## Solution Approach
The solution uses binary search to find a peak element in logarithmic time:

1. Initialize two pointers, left and right, pointing to the start and end of the array
2. While left < right:
   - Find the middle element
   - If the middle element is greater than the next element, search in the left half
   - Otherwise, search in the right half
3. Return the left pointer which will point to a peak element

## Complexity Analysis
- Time Complexity: O(log n)
- Space Complexity: O(1)

## How to Run
```bash
python peak_element.py
```
