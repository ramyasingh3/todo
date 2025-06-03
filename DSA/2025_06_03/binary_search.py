from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Find target in sorted array using binary search.
    
    Args:
        nums: Sorted array of integers
        target: Value to find
        
    Returns:
        Index of target if found, -1 otherwise
        
    Example:
        >>> binary_search([-1, 0, 3, 5, 9, 12], 9)
        4
        >>> binary_search([-1, 0, 3, 5, 9, 12], 2)
        -1
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(nums: List[int], target: int) -> int:
    """
    Find target in sorted array using recursive binary search.
    
    Args:
        nums: Sorted array of integers
        target: Value to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    def search(left: int, right: int) -> int:
        if left > right:
            return -1
            
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)
    
    return search(0, len(nums) - 1)

# Example usage
if __name__ == "__main__":
    # Test case 1: Target exists
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print("Test case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Iterative: {binary_search(nums1, target1)}")
    print(f"Recursive: {binary_search_recursive(nums1, target1)}")
    
    # Test case 2: Target doesn't exist
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Iterative: {binary_search(nums2, target2)}")
    print(f"Recursive: {binary_search_recursive(nums2, target2)}")
    
    # Test case 3: Target at start
    nums3 = [1, 2, 3, 4, 5]
    target3 = 1
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Iterative: {binary_search(nums3, target3)}")
    print(f"Recursive: {binary_search_recursive(nums3, target3)}")
    
    # Test case 4: Target at end
    nums4 = [1, 2, 3, 4, 5]
    target4 = 5
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Iterative: {binary_search(nums4, target4)}")
    print(f"Recursive: {binary_search_recursive(nums4, target4)}")
    
    # Test case 5: Single element
    nums5 = [1]
    target5 = 1
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Iterative: {binary_search(nums5, target5)}")
    print(f"Recursive: {binary_search_recursive(nums5, target5)}") 