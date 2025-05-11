def canPartition(nums: list[int]) -> bool:
    """
    Determine if the array can be partitioned into two subsets such that
    the sum of elements in both subsets is equal.
    
    Args:
        nums: List of integers
        
    Returns:
        True if the array can be partitioned into two equal sum subsets
    """
    total_sum = sum(nums)
    
    # If total sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
        
    target = total_sum // 2
    n = len(nums)
    
    # dp[i][j] represents if we can form sum j using first i elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Empty subset can form sum 0
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                # Either include current number or exclude it
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                # Can't include current number
                dp[i][j] = dp[i-1][j]
    
    return dp[n][target]

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 5, 11, 5]
    print(f"Input: {nums1}")
    print(f"Output: {canPartition(nums1)}")  # Expected: True (11 = 11)
    
    # Test case 2
    nums2 = [1, 2, 3, 5]
    print(f"\nInput: {nums2}")
    print(f"Output: {canPartition(nums2)}")  # Expected: False
    
    # Test case 3
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    print(f"\nInput: {nums3}")
    print(f"Output: {canPartition(nums3)}")  # Expected: True (14 = 14)
    
    # Test case 4
    nums4 = [1, 1]
    print(f"\nInput: {nums4}")
    print(f"Output: {canPartition(nums4)}")  # Expected: True (1 = 1) 