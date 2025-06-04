"""
Problem: Find Peak Element

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: 6 is a peak element and your function should return the index number 5.
"""

from typing import List

def find_peak_element(nums: List[int]) -> int:
    """
    Find a peak element in the array using binary search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
            
    return left

def test_peak_element():
    # Test case 1
    nums1 = [1, 2, 3, 1]
    result1 = find_peak_element(nums1)
    print(f"Test case 1: nums = {nums1}")
    print(f"Peak element index: {result1}")
    print(f"Peak element value: {nums1[result1]}")
    print()

    # Test case 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    result2 = find_peak_element(nums2)
    print(f"Test case 2: nums = {nums2}")
    print(f"Peak element index: {result2}")
    print(f"Peak element value: {nums2[result2]}")
    print()

    # Test case 3 (Edge case - single element)
    nums3 = [1]
    result3 = find_peak_element(nums3)
    print(f"Test case 3: nums = {nums3}")
    print(f"Peak element index: {result3}")
    print(f"Peak element value: {nums3[result3]}")

if __name__ == "__main__":
    test_peak_element()
