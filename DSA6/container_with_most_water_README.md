# Container With Most Water

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

### Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:
```
Input: height = [1,1]
Output: 1
```

## Approach
The solution uses a two-pointer approach:
1. Start with two pointers at the beginning and end of the array
2. Calculate the area between the two pointers
3. Move the pointer pointing to the shorter line inward
4. Keep track of the maximum area found
5. Continue until the pointers meet

## Time Complexity
- O(n), where n is the length of the height array
- We only traverse the array once with two pointers

## Space Complexity
- O(1)
- We only use constant extra space for the pointers and max_area variable 