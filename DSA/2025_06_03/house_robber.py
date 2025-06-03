from typing import List

def rob(nums: List[int]) -> int:
    """
    Find the maximum amount of money you can rob tonight without alerting the police.
    Adjacent houses have security systems connected and will automatically contact the police.
    
    Args:
        nums: List of money in each house
        
    Returns:
        Maximum amount of money that can be robbed
        
    Example:
        >>> rob([1, 2, 3, 1])
        4
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
        
    # Initialize dp array
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill dp array
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

def rob_optimized(nums: List[int]) -> int:
    """
    Find the maximum amount of money you can rob using constant space.
    
    Args:
        nums: List of money in each house
        
    Returns:
        Maximum amount of money that can be robbed
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
        
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [1, 2, 3, 1]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    print(f"Using DP: {rob(nums1)}")
    print(f"Using optimized: {rob_optimized(nums1)}")
    
    # Test case 2: Two houses
    nums2 = [2, 7, 9, 3, 1]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    print(f"Using DP: {rob(nums2)}")
    print(f"Using optimized: {rob_optimized(nums2)}")
    
    # Test case 3: Single house
    nums3 = [1]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    print(f"Using DP: {rob(nums3)}")
    print(f"Using optimized: {rob_optimized(nums3)}")
    
    # Test case 4: Empty list
    nums4 = []
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    print(f"Using DP: {rob(nums4)}")
    print(f"Using optimized: {rob_optimized(nums4)}")
    
    # Test case 5: All same values
    nums5 = [2, 2, 2, 2, 2]
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    print(f"Using DP: {rob(nums5)}")
    print(f"Using optimized: {rob_optimized(nums5)}") 