def rob(nums: list[int]) -> int:
    """
    Find the maximum amount of money you can rob tonight without alerting the police.
    Adjacent houses have security systems connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.
    
    Args:
        nums: List of integers representing the amount of money in each house
        
    Returns:
        Maximum amount of money that can be robbed
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
        
    # dp[i] represents the maximum amount that can be robbed up to house i
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        # At each house, we can either:
        # 1. Rob current house + max amount from i-2 houses
        # 2. Skip current house and take max amount from i-1 houses
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    return dp[-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {rob(nums1)}")  # Expected: 4 (rob house 1 and 3)
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"\nInput: {nums2}")
    print(f"Output: {rob(nums2)}")  # Expected: 12 (rob house 1, 3, and 5)
    
    # Test case 3
    nums3 = [2, 1, 1, 2]
    print(f"\nInput: {nums3}")
    print(f"Output: {rob(nums3)}")  # Expected: 4 (rob house 1 and 4)
    
    # Test case 4
    nums4 = [1]
    print(f"\nInput: {nums4}")
    print(f"Output: {rob(nums4)}")  # Expected: 1 