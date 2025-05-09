"""
Longest Increasing Subsequence

Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.

Time Complexity: O(n²) for the dynamic programming solution
Space Complexity: O(n) for the dp array
"""

def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    # For each position, check all previous positions
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Test cases
def test_length_of_lis():
    # Test case 1: Basic case
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    # Test case 2: Multiple increasing sequences
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    
    # Test case 3: All same numbers
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1
    
    # Test case 4: Empty array
    assert length_of_lis([]) == 0
    
    # Test case 5: Single element
    assert length_of_lis([1]) == 1
    
    # Test case 6: Strictly increasing
    assert length_of_lis([1, 2, 3, 4, 5]) == 5
    
    # Test case 7: Strictly decreasing
    assert length_of_lis([5, 4, 3, 2, 1]) == 1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_lis() 