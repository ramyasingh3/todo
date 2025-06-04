def can_jump(nums: list[int]) -> bool:
    """
    Determine if you can reach the last index starting from the first index.
    Each element in the array represents your maximum jump length at that position.
    
    Args:
        nums: List of non-negative integers
        
    Returns:
        True if you can reach the last index, False otherwise
    """
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    print(f"Input: {nums1}")
    print(f"Output: {can_jump(nums1)}")  # Expected: True
    
    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    print(f"\nInput: {nums2}")
    print(f"Output: {can_jump(nums2)}")  # Expected: False 