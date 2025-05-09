# Longest Increasing Subsequence

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples

### Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.
```

### Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

### Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Solution Approach

The solution uses dynamic programming with the following steps:

1. Create a dp array where dp[i] represents the length of LIS ending at index i
2. Initialize all dp values to 1 (each element is a subsequence of length 1)
3. For each position i:
   - Check all previous positions j
   - If nums[i] > nums[j], update dp[i] = max(dp[i], dp[j] + 1)
4. Return the maximum value in dp array

The key insight is that we can build the solution by considering:
- For each element, we can extend any previous increasing subsequence
- We only extend if the current element is greater than the last element of the subsequence
- We keep track of the maximum length found so far

## Time and Space Complexity

- **Time Complexity**: O(n²)
  - We process each element once
  - For each element, we check all previous elements
  - n is the length of the input array

- **Space Complexity**: O(n)
  - We use a dp array of size n
  - This is the space needed to store all intermediate results

## Edge Cases

1. Empty array
2. Single element
3. All same numbers
4. Strictly increasing array
5. Strictly decreasing array
6. Multiple increasing sequences
7. Negative numbers

## Implementation Notes

- The solution uses a 1D array for dynamic programming
- The solution handles empty arrays correctly
- The solution works with any integer values
- The solution efficiently computes the LIS length
- The solution can be modified to return the actual subsequence

## Alternative Approaches

1. **Binary Search with Patience Sorting**:
   - Use binary search to find insertion points
   - Maintain a sorted array of potential subsequences
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - More efficient but more complex

2. **Segment Tree Approach**:
   - Use a segment tree to track maximum values
   - Process elements in sorted order
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - Good for range queries

3. **Fenwick Tree (Binary Indexed Tree)**:
   - Use a Fenwick tree for efficient updates
   - Process elements in sorted order
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)
   - Efficient for dynamic updates

## Common Applications
- Stock price analysis
- DNA sequence analysis
- Network routing
- Game theory
- Pattern recognition
- Machine learning
- Data compression
- Bioinformatics 