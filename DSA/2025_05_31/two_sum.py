from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find indices of the two numbers such that they add up to a specific target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        Indices of the two numbers, or None if no solution exists
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return None

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    
    # Test case 2: No solution
    nums2 = [1, 2, 3]
    target2 = 7
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    
    # Test case 3: Negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    target3 = -8
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    
    # Test case 4: Duplicates
    nums4 = [3, 3]
    target4 = 6
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {two_sum(nums4, target4)}")
    
    # Test case 5: Single element
    nums5 = [1]
    target5 = 2
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {two_sum(nums5, target5)}") 