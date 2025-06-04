# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

### Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Approach
The solution uses a combination of sorting and two-pointer technique:
1. Sort the array to handle duplicates and make the two-pointer approach possible
2. For each element at index i:
   - Use two pointers (left and right) to find pairs that sum to -nums[i]
   - Skip duplicates to avoid duplicate triplets
   - Move pointers based on the sum comparison

## Time Complexity
- O(n²), where n is the length of the array
- Sorting takes O(n log n)
- For each element, we perform a two-pointer scan which takes O(n)
- Overall complexity is dominated by the two-pointer scans: O(n²)

## Space Complexity
- O(1) or O(n) depending on the sorting implementation
- We only use constant extra space for the pointers and result list
- The space required for the output is not counted in the space complexity 