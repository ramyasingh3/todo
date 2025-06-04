"""
Problem: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

from typing import List

def missing_number(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test cases
def test_missing_number():
    assert missing_number([3,0,1]) == 2
    assert missing_number([0,1]) == 2
    assert missing_number([9,6,4,2,3,5,7,0,1]) == 8
    assert missing_number([0]) == 1
    assert missing_number([1]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_missing_number() 