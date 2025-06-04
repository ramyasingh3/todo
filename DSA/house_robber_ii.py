def rob(nums: list[int]) -> int:
    """
    Find the maximum amount of money you can rob without robbing two adjacent houses.
    Uses dynamic programming.
    
    Args:
        nums: List of non-negative integers representing the amount of money at each house
        
    Returns:
        Maximum amount of money you can rob
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {rob(nums1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"\nInput: {nums2}")
    print(f"Output: {rob(nums2)}")  # Expected: 12 