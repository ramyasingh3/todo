from typing import List

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted arrays in-place.
    
    Args:
        nums1: First sorted array with extra space at the end
        m: Number of elements in nums1
        nums2: Second sorted array
        n: Number of elements in nums2
        
    Example:
        >>> nums1 = [1,2,3,0,0,0]
        >>> m = 3
        >>> nums2 = [2,5,6]
        >>> n = 3
        >>> merge_sorted_arrays(nums1, m, nums2, n)
        >>> print(nums1)
        [1,2,2,3,5,6]
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
    # Test case 1: Basic merge
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print("Test case 1:")
    print(f"nums1 = {nums1}")
    print(f"m = {m}")
    print(f"nums2 = {nums2}")
    print(f"n = {n}")
    
    merge_sorted_arrays(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    
    # Test case 2: nums2 is empty
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print("\nTest case 2:")
    print(f"nums1 = {nums1}")
    print(f"m = {m}")
    print(f"nums2 = {nums2}")
    print(f"n = {n}")
    
    merge_sorted_arrays(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    
    # Test case 3: nums1 is empty
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print("\nTest case 3:")
    print(f"nums1 = {nums1}")
    print(f"m = {m}")
    print(f"nums2 = {nums2}")
    print(f"n = {n}")
    
    merge_sorted_arrays(nums1, m, nums2, n)
    print(f"Output: {nums1}")
    
    # Test case 4: Larger arrays
    nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
    m = 4
    nums2 = [2, 4, 6, 8]
    n = 4
    print("\nTest case 4:")
    print(f"nums1 = {nums1}")
    print(f"m = {m}")
    print(f"nums2 = {nums2}")
    print(f"n = {n}")
    
    merge_sorted_arrays(nums1, m, nums2, n)
    print(f"Output: {nums1}") 