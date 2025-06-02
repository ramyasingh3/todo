from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicates.
    
    Args:
        nums: Array of integers
        
    Returns:
        True if array contains duplicates, False otherwise
        
    Example:
        >>> contains_duplicate([1, 2, 3, 1])
        True
        >>> contains_duplicate([1, 2, 3, 4])
        False
    """
    # Using set to track seen numbers
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

def contains_duplicate_sorted(nums: List[int]) -> bool:
    """
    Check if array contains any duplicates using sorting.
    
    Args:
        nums: Array of integers
        
    Returns:
        True if array contains duplicates, False otherwise
    """
    nums.sort()
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    return False

# Example usage
if __name__ == "__main__":
    # Test case 1: Contains duplicates
    nums1 = [1, 2, 3, 1]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    print(f"Using set: {contains_duplicate(nums1)}")
    print(f"Using sorting: {contains_duplicate_sorted(nums1)}")
    
    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    print(f"Using set: {contains_duplicate(nums2)}")
    print(f"Using sorting: {contains_duplicate_sorted(nums2)}")
    
    # Test case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    print(f"Using set: {contains_duplicate(nums3)}")
    print(f"Using sorting: {contains_duplicate_sorted(nums3)}")
    
    # Test case 4: Empty array
    nums4 = []
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    print(f"Using set: {contains_duplicate(nums4)}")
    print(f"Using sorting: {contains_duplicate_sorted(nums4)}")
    
    # Test case 5: Single element
    nums5 = [1]
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    print(f"Using set: {contains_duplicate(nums5)}")
    print(f"Using sorting: {contains_duplicate_sorted(nums5)}") 