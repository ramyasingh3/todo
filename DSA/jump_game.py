def can_jump(nums: list[int]) -> bool:
    """
    Determine if you can reach the last index of the array.
    At each position, you can jump at most the number of steps specified by the value at that position.
    
    Args:
        nums: List of non-negative integers representing maximum jump length at each position
        
    Returns:
        True if you can reach the last index, False otherwise
    """
    if not nums:
        return False
        
    max_reach = 0  # Maximum index we can reach so far
    
    for i in range(len(nums)):
        # If current position is beyond our maximum reach, we can't proceed
        if i > max_reach:
            return False
            
        # Update maximum reach
        max_reach = max(max_reach, i + nums[i])
        
        # If we can reach or exceed the last index, return True
        if max_reach >= len(nums) - 1:
            return True
    
    return False

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {can_jump(nums1)}")  # Expected: True
    
    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    print(f"\nInput: nums = {nums2}")
    print(f"Output: {can_jump(nums2)}")  # Expected: False
    
    # Test case 3
    nums3 = [0]
    print(f"\nInput: nums = {nums3}")
    print(f"Output: {can_jump(nums3)}")  # Expected: True 