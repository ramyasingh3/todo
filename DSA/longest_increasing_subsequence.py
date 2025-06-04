"""
Find the length of the longest strictly increasing subsequence in an array.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Time Complexity:
- Dynamic Programming: O(n²)
- Binary Search: O(n log n)
Space Complexity:
- Dynamic Programming: O(n)
- Binary Search: O(n)
"""

from typing import List
import bisect

def length_of_lis_dp(nums: List[int]) -> int:
    """
    Dynamic programming solution.
    dp[i] represents the length of the longest increasing subsequence ending at index i.
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def length_of_lis_binary_search(nums: List[int]) -> int:
    """
    Solution using binary search.
    We maintain a list where each element represents the smallest possible tail value
    for all increasing subsequences of a given length.
    """
    if not nums:
        return 0
    
    tails = []
    
    for num in nums:
        # Find the first element in tails that is greater than or equal to num
        idx = bisect.bisect_left(tails, num)
        
        if idx == len(tails):
            # If num is greater than all elements in tails, append it
            tails.append(num)
        else:
            # Otherwise, replace the first element that is greater than or equal to num
            tails[idx] = num
    
    return len(tails)

def get_lis_sequence(nums: List[int]) -> List[int]:
    """
    Helper function to get the actual longest increasing subsequence.
    Uses dynamic programming with parent pointers to reconstruct the sequence.
    """
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    
    # Fill dp and parent arrays
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    # Find the index of the maximum value in dp
    max_len = max(dp)
    max_idx = dp.index(max_len)
    
    # Reconstruct the sequence
    sequence = []
    while max_idx != -1:
        sequence.append(nums[max_idx])
        max_idx = parent[max_idx]
    
    return list(reversed(sequence))

# Test cases
def test_longest_increasing_subsequence():
    test_cases = [
        ([10,9,2,5,3,7,101,18], 4, [2,5,7,101]),
        ([0,1,0,3,2,3], 4, [0,1,2,3]),
        ([], 0, []),
        ([1], 1, [1]),
        ([7,7,7,7,7,7,7], 1, [7]),
        ([1,3,6,7,9,4,10,5,6], 6, [1,3,6,7,9,10]),
        ([3,5,6,2,5,4,19,5,6,7,12], 6, [3,5,6,7,12]),
    ]
    
    for nums, expected_length, expected_sequence in test_cases:
        # Test DP solution
        result_dp = length_of_lis_dp(nums)
        assert result_dp == expected_length, \
            f"DP solution failed for {nums}. Expected length {expected_length}, got {result_dp}"
        
        # Test binary search solution
        result_binary = length_of_lis_binary_search(nums)
        assert result_binary == expected_length, \
            f"Binary search solution failed for {nums}. Expected length {expected_length}, got {result_binary}"
        
        # Test sequence reconstruction
        result_sequence = get_lis_sequence(nums)
        assert result_sequence == expected_sequence, \
            f"Sequence reconstruction failed for {nums}. Expected {expected_sequence}, got {result_sequence}"
        
        print(f"Test passed for nums={nums}")

if __name__ == "__main__":
    test_longest_increasing_subsequence() 