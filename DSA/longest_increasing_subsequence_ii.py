def length_of_lis(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    # dp[i] represents the smallest tail value of all increasing subsequences of length i+1
    dp = []
    
    for num in nums:
        # Binary search to find the first element in dp that is greater than or equal to num
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
                
        # If num is greater than all elements in dp, append it
        if left == len(dp):
            dp.append(num)
        # Otherwise, replace the first element that is greater than or equal to num
        else:
            dp[left] = num
            
    return len(dp)

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Input: nums = {nums1}")
    print(f"Output: {length_of_lis(nums1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"\nInput: nums = {nums2}")
    print(f"Output: {length_of_lis(nums2)}")  # Expected: 4
    
    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"\nInput: nums = {nums3}")
    print(f"Output: {length_of_lis(nums3)}")  # Expected: 1 