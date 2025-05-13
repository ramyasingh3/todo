"""
Longest Increasing Subsequence

Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.

Time Complexity: O(n²) for the dynamic programming solution
Space Complexity: O(n) for the dp array
"""

def lengthOfLIS(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

def lengthOfLISBinarySearch(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence using binary search.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
            
    return len(sub)

def getLIS(nums: list[int]) -> list[int]:
    """
    Get the actual longest increasing subsequence.
    
    Args:
        nums: List of integers
        
    Returns:
        The longest increasing subsequence
    """
    if not nums:
        return []
        
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
                
    # Find the index of the maximum value in dp
    max_len = max(dp)
    max_idx = dp.index(max_len)
    
    # Reconstruct the subsequence
    lis = []
    while max_idx != -1:
        lis.append(nums[max_idx])
        max_idx = prev[max_idx]
        
    return list(reversed(lis))

def getAllIncreasingSubsequences(nums: list[int]) -> list[list[int]]:
    """
    Get all increasing subsequences.
    
    Args:
        nums: List of integers
        
    Returns:
        List of all increasing subsequences
    """
    def isIncreasing(sub: list[int]) -> bool:
        return all(sub[i] < sub[i+1] for i in range(len(sub)-1))
        
    def generateSubsequences(nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsequences = []
        
        for i in range(1, 1 << n):
            sub = []
            for j in range(n):
                if i & (1 << j):
                    sub.append(nums[j])
            subsequences.append(sub)
            
        return subsequences
        
    # Generate all subsequences
    subs = generateSubsequences(nums)
    
    # Filter increasing subsequences
    increasing_subs = [sub for sub in subs if isIncreasing(sub)]
    
    return sorted(increasing_subs, key=len, reverse=True)

# Example usage
if __name__ == "__main__":
    import bisect
    
    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Input: {nums1}")
    print(f"Length (DP): {lengthOfLIS(nums1)}")  # Expected: 4
    print(f"Length (Binary Search): {lengthOfLISBinarySearch(nums1)}")  # Expected: 4
    print(f"LIS: {getLIS(nums1)}")  # Expected: [2, 5, 7, 101]
    print("All increasing subsequences:")
    for sub in getAllIncreasingSubsequences(nums1):
        print(f"- {sub}")
    
    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    print(f"\nInput: {nums2}")
    print(f"Length (DP): {lengthOfLIS(nums2)}")  # Expected: 4
    print(f"Length (Binary Search): {lengthOfLISBinarySearch(nums2)}")  # Expected: 4
    print(f"LIS: {getLIS(nums2)}")  # Expected: [0, 1, 2, 3]
    print("All increasing subsequences:")
    for sub in getAllIncreasingSubsequences(nums2):
        print(f"- {sub}")
    
    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"\nInput: {nums3}")
    print(f"Length (DP): {lengthOfLIS(nums3)}")  # Expected: 1
    print(f"Length (Binary Search): {lengthOfLISBinarySearch(nums3)}")  # Expected: 1
    print(f"LIS: {getLIS(nums3)}")  # Expected: [7]
    print("All increasing subsequences:")
    for sub in getAllIncreasingSubsequences(nums3):
        print(f"- {sub}")
    
    # Test case 4
    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(f"\nInput: {nums4}")
    print(f"Length (DP): {lengthOfLIS(nums4)}")  # Expected: 6
    print(f"Length (Binary Search): {lengthOfLISBinarySearch(nums4)}")  # Expected: 6
    print(f"LIS: {getLIS(nums4)}")  # Expected: [1, 3, 6, 7, 9, 10]
    print("All increasing subsequences:")
    for sub in getAllIncreasingSubsequences(nums4):
        print(f"- {sub}") 