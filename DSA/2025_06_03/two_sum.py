from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test case 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    
    # Test case 2: Multiple solutions (returns first found)
    nums2 = [3, 2, 4]
    target2 = 6
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    
    # Test case 3: Same number used twice
    nums3 = [3, 3]
    target3 = 6
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    
    # Test case 4: No solution
    nums4 = [1, 2, 3, 4]
    target4 = 10
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {two_sum(nums4, target4)}")
    
    # Test case 5: Negative numbers
    nums5 = [-1, -2, -3, -4]
    target5 = -7
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {two_sum(nums5, target5)}") 