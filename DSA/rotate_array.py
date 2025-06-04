"""
Problem: Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Rotate array in-place using O(1) extra space
    """
    if not nums:
        return
    
    n = len(nums)
    k = k % n  # Handle case where k > n
    
    def reverse(start: int, end: int) -> None:
        """Helper function to reverse a portion of the array"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

def rotate_with_extra_space(nums: List[int], k: int) -> List[int]:
    """
    Alternative solution using extra space
    """
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]

# Test cases
def test_rotate():
    # Test case 1: Regular rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]
    
    # Test case 2: Rotation with k > array length
    nums2 = [1, 2, 3]
    rotate(nums2, 4)
    assert nums2 == [3, 1, 2]
    
    # Test case 3: Empty array
    nums3 = []
    rotate(nums3, 1)
    assert nums3 == []
    
    # Test case 4: Single element
    nums4 = [1]
    rotate(nums4, 1)
    assert nums4 == [1]
    
    # Test case 5: k = 0
    nums5 = [1, 2, 3]
    rotate(nums5, 0)
    assert nums5 == [1, 2, 3]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_rotate() 