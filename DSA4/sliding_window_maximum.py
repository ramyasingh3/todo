from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Find the maximum value in each sliding window of size k.
    
    Args:
        nums: List of integers
        k: Size of the sliding window
        
    Returns:
        List of maximum values for each sliding window
    """
    if not nums or k <= 0:
        return []
        
    if k == 1:
        return nums
        
    n = len(nums)
    result = []
    dq = deque()  # Store indices of potential maximum values
    
    # Process first window
    for i in range(k):
        # Remove elements smaller than current element
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    # Process rest of the array
    for i in range(k, n):
        # Add maximum of previous window to result
        result.append(nums[dq[0]])
        
        # Remove elements outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
            
        # Remove elements smaller than current element
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
            
        dq.append(i)
    
    # Add maximum of last window
    result.append(nums[dq[0]])
    
    return result

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {maxSlidingWindow(nums1, k1)}")  # Expected: [3, 3, 5, 5, 6, 7]
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"\nInput: nums = {nums2}, k = {k2}")
    print(f"Output: {maxSlidingWindow(nums2, k2)}")  # Expected: [1]
    
    # Test case 3
    nums3 = [1, -1]
    k3 = 1
    print(f"\nInput: nums = {nums3}, k = {k3}")
    print(f"Output: {maxSlidingWindow(nums3, k3)}")  # Expected: [1, -1]
    
    # Test case 4
    nums4 = [9, 11]
    k4 = 2
    print(f"\nInput: nums = {nums4}, k = {k4}")
    print(f"Output: {maxSlidingWindow(nums4, k4)}")  # Expected: [11] 