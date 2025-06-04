# Trapping Rain Water

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Approach
The solution uses dynamic programming with two arrays to store maximum heights:

1. Create two arrays `left_max` and `right_max` to store the maximum height to the left and right of each position
2. Calculate `left_max` array:
   - For each position i, store the maximum height from the start up to i
3. Calculate `right_max` array:
   - For each position i, store the maximum height from i to the end
4. Calculate trapped water:
   - For each position i, the water trapped is the minimum of left_max[i] and right_max[i] minus height[i]
   - Sum up the trapped water for all positions

## Time Complexity
- O(n), where n is the length of the array
- We traverse the array three times:
  - Once to calculate left_max
  - Once to calculate right_max
  - Once to calculate the trapped water

## Space Complexity
- O(n)
- We use two additional arrays of size n to store left_max and right_max

## Solution Code
The solution is implemented in `trapping_rain_water.py` with detailed comments and example usage. 