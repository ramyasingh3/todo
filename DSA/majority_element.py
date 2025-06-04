"""
Find the majority element in an array.
The majority element is the element that appears more than ⌊n/2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Time Complexity:
- Hash map solution: O(n)
- Boyer-Moore Voting Algorithm: O(n)
Space Complexity:
- Hash map solution: O(n)
- Boyer-Moore Voting Algorithm: O(1)
"""

from typing import List
from collections import Counter

def find_majority_element_hash(nums: List[int]) -> int:
    """
    Solution using a hash map to count occurrences.
    """
    counts = Counter(nums)
    return max(counts.items(), key=lambda x: x[1])[0]

def find_majority_element_boyer_moore(nums: List[int]) -> int:
    """
    Solution using Boyer-Moore Voting Algorithm.
    This algorithm works because the majority element appears more than n/2 times,
    so it will always have a positive count at the end.
    """
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Test cases
def test_majority_element():
    test_cases = [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2),
        ([1], 1),
        ([1,1,2,2,2], 2),
        ([3,3,4], 3),
    ]
    
    for nums, expected in test_cases:
        # Test hash map solution
        result_hash = find_majority_element_hash(nums)
        assert result_hash == expected, f"Hash solution failed for {nums}. Expected {expected}, got {result_hash}"
        
        # Test Boyer-Moore solution
        result_boyer = find_majority_element_boyer_moore(nums)
        assert result_boyer == expected, f"Boyer-Moore solution failed for {nums}. Expected {expected}, got {result_boyer}"
        
        print(f"Test passed for nums={nums}")

if __name__ == "__main__":
    test_majority_element() 