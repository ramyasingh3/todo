def maxSubArray(nums: list[int]) -> int:
    """
    Find the sum of the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
        
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far

def maxSubArrayWithIndices(nums: list[int]) -> tuple[int, int, int]:
    """
    Find the maximum subarray and return its sum, start index, and end index.
    
    Args:
        nums: List of integers
        
    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not nums:
        return (0, -1, -1)
        
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    temp_start = 0
    
    for i, num in enumerate(nums):
        if max_ending_here + num < num:
            max_ending_here = num
            temp_start = i
        else:
            max_ending_here += num
            
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = temp_start
            end = i
            
    return (max_so_far, start, end)

def maxSubArrayDivideAndConquer(nums: list[int]) -> int:
    """
    Find the maximum subarray sum using divide and conquer approach.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    def maxCrossingSum(nums: list[int], left: int, mid: int, right: int) -> int:
        # Find maximum sum of subarray crossing mid
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(left_sum, curr_sum)
            
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(right_sum, curr_sum)
            
        return left_sum + right_sum
        
    def maxSubArrayHelper(nums: list[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
            
        mid = (left + right) // 2
        
        return max(
            maxSubArrayHelper(nums, left, mid),
            maxSubArrayHelper(nums, mid + 1, right),
            maxCrossingSum(nums, left, mid, right)
        )
        
    if not nums:
        return 0
    return maxSubArrayHelper(nums, 0, len(nums) - 1)

def getAllSubarrays(nums: list[int]) -> list[list[int]]:
    """
    Get all possible contiguous subarrays.
    
    Args:
        nums: List of integers
        
    Returns:
        List of all contiguous subarrays
    """
    n = len(nums)
    subarrays = []
    
    for i in range(n):
        for j in range(i, n):
            subarrays.append(nums[i:j+1])
            
    return subarrays

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums1}")
    print(f"Maximum sum (Kadane): {maxSubArray(nums1)}")  # Expected: 6
    max_sum, start, end = maxSubArrayWithIndices(nums1)
    print(f"Maximum subarray: {nums1[start:end+1]}")  # Expected: [4, -1, 2, 1]
    print(f"Maximum sum (Divide & Conquer): {maxSubArrayDivideAndConquer(nums1)}")  # Expected: 6
    
    # Test case 2
    nums2 = [1]
    print(f"\nInput: {nums2}")
    print(f"Maximum sum (Kadane): {maxSubArray(nums2)}")  # Expected: 1
    max_sum, start, end = maxSubArrayWithIndices(nums2)
    print(f"Maximum subarray: {nums2[start:end+1]}")  # Expected: [1]
    print(f"Maximum sum (Divide & Conquer): {maxSubArrayDivideAndConquer(nums2)}")  # Expected: 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"\nInput: {nums3}")
    print(f"Maximum sum (Kadane): {maxSubArray(nums3)}")  # Expected: 23
    max_sum, start, end = maxSubArrayWithIndices(nums3)
    print(f"Maximum subarray: {nums3[start:end+1]}")  # Expected: [5, 4, -1, 7, 8]
    print(f"Maximum sum (Divide & Conquer): {maxSubArrayDivideAndConquer(nums3)}")  # Expected: 23
    
    # Test case 4
    nums4 = [-1, -2, -3, -4]
    print(f"\nInput: {nums4}")
    print(f"Maximum sum (Kadane): {maxSubArray(nums4)}")  # Expected: -1
    max_sum, start, end = maxSubArrayWithIndices(nums4)
    print(f"Maximum subarray: {nums4[start:end+1]}")  # Expected: [-1]
    print(f"Maximum sum (Divide & Conquer): {maxSubArrayDivideAndConquer(nums4)}")  # Expected: -1 