# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers in the array such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Examples
1. Basic case:
   ```
   Input: nums = [2, 7, 11, 15], target = 9
   Output: [0, 1]
   Explanation: nums[0] + nums[1] = 2 + 7 = 9
   ```

2. Multiple valid pairs:
   ```
   Input: nums = [3, 2, 4], target = 6
   Output: [1, 2]
   Explanation: nums[1] + nums[2] = 2 + 4 = 6
   ```

3. Same number used twice:
   ```
   Input: nums = [3, 3], target = 6
   Output: [0, 1]
   Explanation: nums[0] + nums[1] = 3 + 3 = 6
   ```

## Solution Approaches

### 1. Brute Force (O(n²))
- Check every possible pair of numbers
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best for small arrays or when space is limited

### 2. Hash Map (O(n))
- Use a hash map to store complements
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best overall solution for most cases

### 3. Two Pointers (O(n log n))
- Sort array and use two pointers
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Best when array is already sorted

## Time Complexity
- Brute Force: O(n²)
- Hash Map: O(n)
- Two Pointers: O(n log n)

## Space Complexity
- Brute Force: O(1)
- Hash Map: O(n)
- Two Pointers: O(n)

## Usage
```python
from two_sum import Solution

solution = Solution()
nums = [2, 7, 11, 15]
target = 9

# Using brute force
result = solution.two_sum_brute_force(nums, target)
print(result)  # Output: [0, 1]

# Using hash map
result = solution.two_sum_hash_map(nums, target)
print(result)  # Output: [0, 1]

# Using two pointers
result = solution.two_sum_sorted(nums, target)
print(result)  # Output: [0, 1]
```

## Common Applications
- Finding pairs in financial transactions
- Matching items in inventory
- Game development (matching scores)
- Data analysis
- Algorithm interviews 