from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        Tuple of indices of the two numbers that add up to target
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
    """
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    
    return (-1, -1)  # No solution found

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Explanation: Because nums[{result1[0]}] + nums[{result1[1]}] == {target1}")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Explanation: Because nums[{result2[0]}] + nums[{result2[1]}] == {target2}")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Explanation: Because nums[{result3[0]}] + nums[{result3[1]}] == {target3}") 