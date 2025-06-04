# 3Sum

## Problem Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

### Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

## Approach
The solution uses a two-pointer technique with sorting:

1. Sort the input array to make it easier to handle duplicates and use two-pointer technique
2. Iterate through the array with a fixed first element (i)
3. Use two pointers (left and right) to find the remaining two elements:
   - left starts at i + 1
   - right starts at the end of the array
4. Calculate the sum of the three elements:
   - If sum == 0, add the triplet to the result
   - If sum < 0, move left pointer right
   - If sum > 0, move right pointer left
5. Skip duplicates to avoid duplicate triplets in the result

## Time Complexity
- O(n²), where n is the length of the array
- Sorting takes O(n log n)
- The nested loop with two pointers takes O(n²)

## Space Complexity
- O(1) or O(n) depending on the sorting implementation
- We use constant extra space for variables
- The result list is not counted in space complexity as it's part of the output

## Solution Code
The solution is implemented in `three_sum.py` with detailed comments and example usage. 