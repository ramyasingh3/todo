from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: Sorted array of integers
        
    Returns:
        Length of array after removing duplicates
        
    Example:
        >>> nums = [1, 1, 2]
        >>> remove_duplicates(nums)
        2
        >>> print(nums[:2])
        [1, 2]
    """
    if not nums:
        return 0
    
    # Pointer for the position to place next unique element
    k = 1
    
    # Compare each element with the previous one
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    
    return k

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [1, 1, 2]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    k1 = remove_duplicates(nums1)
    print(f"Output: {k1}")
    print(f"Modified nums: {nums1[:k1]}")
    
    # Test case 2: Multiple duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    k2 = remove_duplicates(nums2)
    print(f"Output: {k2}")
    print(f"Modified nums: {nums2[:k2]}")
    
    # Test case 3: No duplicates
    nums3 = [1, 2, 3, 4, 5]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    k3 = remove_duplicates(nums3)
    print(f"Output: {k3}")
    print(f"Modified nums: {nums3[:k3]}")
    
    # Test case 4: Empty array
    nums4 = []
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    k4 = remove_duplicates(nums4)
    print(f"Output: {k4}")
    print(f"Modified nums: {nums4[:k4]}")
    
    # Test case 5: Single element
    nums5 = [1]
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    k5 = remove_duplicates(nums5)
    print(f"Output: {k5}")
    print(f"Modified nums: {nums5[:k5]}") 