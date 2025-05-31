from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find the intersection of two arrays.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        
    Returns:
        List of integers representing the intersection
        
    Example:
        >>> intersection([1, 2, 2, 1], [2, 2])
        [2]
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("Test case 1:")
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {intersection(nums1, nums2)}")
    
    # Test case 2: No intersection
    nums3 = [1, 2, 3]
    nums4 = [4, 5, 6]
    print("\nTest case 2:")
    print(f"Input: nums1 = {nums3}, nums2 = {nums4}")
    print(f"Output: {intersection(nums3, nums4)}")
    
    # Test case 3: Empty arrays
    nums5 = []
    nums6 = []
    print("\nTest case 3:")
    print(f"Input: nums1 = {nums5}, nums2 = {nums6}")
    print(f"Output: {intersection(nums5, nums6)}")
    
    # Test case 4: One empty array
    nums7 = [1, 2, 3]
    nums8 = []
    print("\nTest case 4:")
    print(f"Input: nums1 = {nums7}, nums2 = {nums8}")
    print(f"Output: {intersection(nums7, nums8)}")
    
    # Test case 5: Duplicates in both arrays
    nums9 = [1, 1, 2, 2, 3]
    nums10 = [2, 2, 3, 3, 4]
    print("\nTest case 5:")
    print(f"Input: nums1 = {nums9}, nums2 = {nums10}")
    print(f"Output: {intersection(nums9, nums10)}") 