from typing import List

def rotate_array(nums: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps in-place.
    
    Args:
        nums: Array of integers
        k: Number of steps to rotate
        
    Example:
        >>> nums = [1, 2, 3, 4, 5, 6, 7]
        >>> rotate_array(nums, 3)
        >>> print(nums)
        [5, 6, 7, 1, 2, 3, 4]
    """
    n = len(nums)
    k = k % n  # Handle cases where k > n
    
    # Reverse the entire array
    reverse(nums, 0, n - 1)
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Reverse the remaining elements
    reverse(nums, k, n - 1)

def reverse(nums: List[int], start: int, end: int) -> None:
    """Reverse array elements from start to end index"""
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print("Test case 1:")
    print(f"Input: nums = {nums1}, k = {k1}")
    rotate_array(nums1, k1)
    print(f"Output: {nums1}")
    
    # Test case 2: k > array length
    nums2 = [-1, -100, 3, 99]
    k2 = 6
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}, k = {k2}")
    rotate_array(nums2, k2)
    print(f"Output: {nums2}")
    
    # Test case 3: k = 0
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}, k = {k3}")
    rotate_array(nums3, k3)
    print(f"Output: {nums3}")
    
    # Test case 4: Single element
    nums4 = [1]
    k4 = 1
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}, k = {k4}")
    rotate_array(nums4, k4)
    print(f"Output: {nums4}")
    
    # Test case 5: k = array length
    nums5 = [1, 2, 3]
    k5 = 3
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}, k = {k5}")
    rotate_array(nums5, k5)
    print(f"Output: {nums5}") 