def search_rotated_array(nums, target):
    """
    Search for a target value in a rotated sorted array.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # If target is in left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half must be sorted
        else:
            # If target is in right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def main():
    # Test cases
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),    # Expected: 4
        ([4, 5, 6, 7, 0, 1, 2], 3),    # Expected: -1
        ([1], 0),                      # Expected: -1
        ([1, 3], 3),                   # Expected: 1
        ([3, 1], 1),                   # Expected: 1
        ([5, 1, 3], 5),               # Expected: 0
    ]
    
    for nums, target in test_cases:
        result = search_rotated_array(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        if result != -1:
            print(f"Found {target} at index {result}\n")
        else:
            print(f"Target {target} not found\n")

if __name__ == "__main__":
    main() 