# Container With Most Water

## Problem Description
Given an integer array `height` of length `n`, find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

### Example 1:
```
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The above vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:
```
Input: height = [1, 1]
Output: 1
```

## Approach
The solution uses a two-pointer technique:

1. Initialize two pointers, one at the start (left) and one at the end (right) of the array
2. Calculate the area between the two lines:
   - The height is the minimum of the two lines
   - The width is the distance between the two lines
3. Move the pointer pointing to the shorter line inward:
   - If height[left] < height[right], move left pointer right
   - Otherwise, move right pointer left
4. Keep track of the maximum area encountered

## Time Complexity
- O(n), where n is the length of the array
- We traverse the array once with two pointers

## Space Complexity
- O(1)
- We use constant extra space

## Solution Code
The solution is implemented in `container_with_most_water.py` with detailed comments and example usage. 