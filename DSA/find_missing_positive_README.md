# Find the Smallest Missing Positive Integer

## Problem Description
Given an unsorted integer array `nums`, find the smallest missing positive integer. The solution should run in O(n) time and use O(1) extra space.

## Examples
```
Input: nums = [1, 2, 0]
Output: 3
Explanation: The smallest missing positive integer is 3.

Input: nums = [3, 4, -1, 1]
Output: 2
Explanation: The smallest missing positive integer is 2.

Input: nums = [7, 8, 9, 11, 12]
Output: 1
Explanation: The smallest missing positive integer is 1.
```

## Constraints
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

## Approach
1. First, we replace all negative numbers and numbers greater than n with n+1
2. Then, we use the array indices as a hash table to mark which numbers exist
3. Finally, we scan the array to find the first positive number, which indicates the missing number

## Time and Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution
The solution uses the array itself as a hash table to mark which numbers exist. We use negative numbers to mark the presence of a number at its corresponding index.

## Key Points
- The smallest missing positive integer must be in the range [1, n+1]
- We can use the array indices to mark which numbers exist
- The solution requires careful handling of negative numbers and numbers greater than n 