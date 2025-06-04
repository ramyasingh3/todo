# Remove Element

## Problem Description
Given an array `nums` and a value `val`, remove all instances of that value in-place and return the new length of the array.

## Examples
1. Basic case:
   ```
   Input: nums = [3, 2, 2, 3], val = 3
   Output: 2, nums = [2, 2]
   ```

2. All elements to remove:
   ```
   Input: nums = [1, 1, 1, 1], val = 1
   Output: 0, nums = []
   ```

3. No elements to remove:
   ```
   Input: nums = [4, 5, 6, 7], val = 1
   Output: 4, nums = [4, 5, 6, 7]
   ```

## Solution Approaches

### 1. Two Pointers (O(n))
- Uses two pointers to track positions
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for most cases

### 2. While Loop (O(n))
- Uses a while loop with swapping
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for minimizing writes

### 3. List Comprehension (O(n))
- Uses Python list comprehension
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for readability

## Time Complexity
- All approaches: O(n)
- n is the length of the array

## Space Complexity
- Two Pointers: O(1)
- While Loop: O(1)
- List Comprehension: O(n)

## Usage
```python
from remove_element import Solution

solution = Solution()
nums = [3, 2, 2, 3]
val = 3

# Using two pointers
length = solution.remove_element_two_pointers(nums, val)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")

# Using while loop
length = solution.remove_element_while_loop(nums, val)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")

# Using list comprehension
length = solution.remove_element_list_comprehension(nums, val)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")
```

## Common Applications
- Array manipulation
- Data cleaning
- Memory optimization
- In-place algorithms
- Interview preparation
- System design 