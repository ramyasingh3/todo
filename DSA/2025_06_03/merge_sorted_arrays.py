from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted arrays in-place.
    
    Args:
        nums1: First sorted array with extra space at the end
        m: Number of elements in nums1
        nums2: Second sorted array
        n: Number of elements in nums2
        
    Example:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> nums2 = [2, 5, 6]
        >>> merge(nums1, 3, nums2, 3)
        >>> print(nums1)
        [1, 2, 2, 3, 5, 6]
    """
    # Start from the end of both arrays
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the merged array
    
    # While there are elements in both arrays
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1_1 = [1, 2, 3, 0, 0, 0]
    m1 = 3
    nums2_1 = [2, 5, 6]
    n1 = 3
    print("Test case 1:")
    print(f"Input: nums1 = {nums1_1}, m = {m1}, nums2 = {nums2_1}, n = {n1}")
    merge(nums1_1, m1, nums2_1, n1)
    print(f"Output: {nums1_1}")
    
    # Test case 2: nums1 is empty
    nums1_2 = [0]
    m2 = 0
    nums2_2 = [1]
    n2 = 1
    print("\nTest case 2:")
    print(f"Input: nums1 = {nums1_2}, m = {m2}, nums2 = {nums2_2}, n = {n2}")
    merge(nums1_2, m2, nums2_2, n2)
    print(f"Output: {nums1_2}")
    
    # Test case 3: nums2 is empty
    nums1_3 = [1]
    m3 = 1
    nums2_3 = []
    n3 = 0
    print("\nTest case 3:")
    print(f"Input: nums1 = {nums1_3}, m = {m3}, nums2 = {nums2_3}, n = {n3}")
    merge(nums1_3, m3, nums2_3, n3)
    print(f"Output: {nums1_3}")
    
    # Test case 4: All elements in nums1 are greater
    nums1_4 = [4, 5, 6, 0, 0, 0]
    m4 = 3
    nums2_4 = [1, 2, 3]
    n4 = 3
    print("\nTest case 4:")
    print(f"Input: nums1 = {nums1_4}, m = {m4}, nums2 = {nums2_4}, n = {n4}")
    merge(nums1_4, m4, nums2_4, n4)
    print(f"Output: {nums1_4}")
    
    # Test case 5: All elements in nums2 are greater
    nums1_5 = [1, 2, 3, 0, 0, 0]
    m5 = 3
    nums2_5 = [4, 5, 6]
    n5 = 3
    print("\nTest case 5:")
    print(f"Input: nums1 = {nums1_5}, m = {m5}, nums2 = {nums2_5}, n = {n5}")
    merge(nums1_5, m5, nums2_5, n5)
    print(f"Output: {nums1_5}") 