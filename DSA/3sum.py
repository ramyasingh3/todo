def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array which gives the sum of zero.
    
    Args:
        nums (list[int]): Input array of integers
        
    Returns:
        list[list[int]]: List of unique triplets that sum to zero
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1,0,1,2,-1,-4]
    print(f"Input: {nums1}")
    print(f"Output: {threeSum(nums1)}")  # Expected: [[-1,-1,2],[-1,0,1]]
    
    # Test case 2
    nums2 = [0,1,1]
    print(f"\nInput: {nums2}")
    print(f"Output: {threeSum(nums2)}")  # Expected: []
    
    # Test case 3
    nums3 = [0,0,0]
    print(f"\nInput: {nums3}")
    print(f"Output: {threeSum(nums3)}")  # Expected: [[0,0,0]] 