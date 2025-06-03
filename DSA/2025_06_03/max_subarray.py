from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Find the sum of the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
        
    Example:
        >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
    """
    if not nums:
        return 0
        
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Either extend the current subarray or start a new one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_with_indices(nums: List[int]) -> tuple:
    """
    Find the contiguous subarray with the largest sum and return its indices.
    
    Args:
        nums: List of integers
        
    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not nums:
        return (0, -1, -1)
        
    max_sum = current_sum = nums[0]
    start = end = 0
    current_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i
        else:
            current_sum += nums[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
    
    return (max_sum, start, end)

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    print(f"Maximum sum: {max_subarray(nums1)}")
    max_sum1, start1, end1 = max_subarray_with_indices(nums1)
    print(f"Maximum subarray: {nums1[start1:end1+1]}")
    
    # Test case 2: All positive numbers
    nums2 = [1, 2, 3, 4, 5]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    print(f"Maximum sum: {max_subarray(nums2)}")
    max_sum2, start2, end2 = max_subarray_with_indices(nums2)
    print(f"Maximum subarray: {nums2[start2:end2+1]}")
    
    # Test case 3: All negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    print(f"Maximum sum: {max_subarray(nums3)}")
    max_sum3, start3, end3 = max_subarray_with_indices(nums3)
    print(f"Maximum subarray: {nums3[start3:end3+1]}")
    
    # Test case 4: Single element
    nums4 = [5]
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    print(f"Maximum sum: {max_subarray(nums4)}")
    max_sum4, start4, end4 = max_subarray_with_indices(nums4)
    print(f"Maximum subarray: {nums4[start4:end4+1]}")
    
    # Test case 5: Empty array
    nums5 = []
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    print(f"Maximum sum: {max_subarray(nums5)}")
    max_sum5, start5, end5 = max_subarray_with_indices(nums5)
    print(f"Maximum subarray: {nums5[start5:end5+1] if start5 != -1 else []}") 