from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Move all zeros to the end of the array while maintaining the relative order of the non-zero elements.
    
    Args:
        nums: List of integers
        
    Example:
        >>> nums = [0, 1, 0, 3, 12]
        >>> move_zeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
    """
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [0, 1, 0, 3, 12]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    move_zeroes(nums1)
    print(f"Output: {nums1}")
    
    # Test case 2: No zeros
    nums2 = [1, 2, 3, 4, 5]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    move_zeroes(nums2)
    print(f"Output: {nums2}")
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0, 0, 0]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    move_zeroes(nums3)
    print(f"Output: {nums3}")
    
    # Test case 4: Single element
    nums4 = [0]
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    move_zeroes(nums4)
    print(f"Output: {nums4}")
    
    # Test case 5: Mixed zeros and non-zeros
    nums5 = [0, 0, 1, 0, 2, 0, 3]
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    move_zeroes(nums5)
    print(f"Output: {nums5}") 