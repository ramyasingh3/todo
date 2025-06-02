from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two arrays.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        
    Returns:
        List of common elements
        
    Example:
        >>> intersection([1, 2, 2, 1], [2, 2])
        [2]
    """
    # Convert arrays to sets and find intersection
    return list(set(nums1) & set(nums2))

def intersection_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find intersection of two sorted arrays.
    
    Args:
        nums1: First sorted array of integers
        nums2: Second sorted array of integers
        
    Returns:
        List of common elements
    """
    nums1.sort()
    nums2.sort()
    
    result = []
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            # Avoid duplicates
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
    
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    print("Test case 1:")
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Using sets: {intersection(nums1_1, nums2_1)}")
    print(f"Using sorting: {intersection_sorted(nums1_1, nums2_1)}")
    
    # Test case 2: No intersection
    nums1_2 = [1, 2, 3]
    nums2_2 = [4, 5, 6]
    print("\nTest case 2:")
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Using sets: {intersection(nums1_2, nums2_2)}")
    print(f"Using sorting: {intersection_sorted(nums1_2, nums2_2)}")
    
    # Test case 3: Multiple intersections
    nums1_3 = [4, 9, 5]
    nums2_3 = [9, 4, 9, 8, 4]
    print("\nTest case 3:")
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Using sets: {intersection(nums1_3, nums2_3)}")
    print(f"Using sorting: {intersection_sorted(nums1_3, nums2_3)}")
    
    # Test case 4: Empty arrays
    nums1_4 = []
    nums2_4 = []
    print("\nTest case 4:")
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Using sets: {intersection(nums1_4, nums2_4)}")
    print(f"Using sorting: {intersection_sorted(nums1_4, nums2_4)}")
    
    # Test case 5: One empty array
    nums1_5 = [1, 2, 3]
    nums2_5 = []
    print("\nTest case 5:")
    print(f"Input: nums1 = {nums1_5}, nums2 = {nums2_5}")
    print(f"Using sets: {intersection(nums1_5, nums2_5)}")
    print(f"Using sorting: {intersection_sorted(nums1_5, nums2_5)}") 