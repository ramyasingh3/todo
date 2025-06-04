def find_peak_element(nums):
    """
    Find a peak element in an array. A peak element is an element that is strictly greater than its neighbors.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than its right neighbor, peak must be in left half
        if nums[mid] > nums[mid + 1]:
            right = mid
        # If mid element is less than its right neighbor, peak must be in right half
        else:
            left = mid + 1
    
    return left

def main():
    # Test cases
    test_cases = [
        [1, 2, 3, 1],           # Expected: 2 (index of 3)
        [1, 2, 1, 3, 5, 6, 4],  # Expected: 5 (index of 6)
        [1],                     # Expected: 0 (single element)
        [1, 2],                 # Expected: 1 (last element)
        [2, 1],                 # Expected: 0 (first element)
    ]
    
    for nums in test_cases:
        peak_index = find_peak_element(nums)
        print(f"Input: {nums}")
        print(f"Peak element index: {peak_index}")
        print(f"Peak element value: {nums[peak_index]}\n")

if __name__ == "__main__":
    main() 