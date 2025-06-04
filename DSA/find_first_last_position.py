def find_first_last_position(nums, target):
    """
    Find the first and last position of target in sorted array.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1  # Continue searching in left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_pos
    
    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last_pos = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1  # Continue searching in right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_pos
    
    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]

def main():
    # Test cases
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),     # Expected: [3, 4]
        ([5, 7, 7, 8, 8, 10], 6),     # Expected: [-1, -1]
        ([], 0),                      # Expected: [-1, -1]
        ([1], 1),                     # Expected: [0, 0]
        ([2, 2], 2),                  # Expected: [0, 1]
        ([1, 2, 3, 3, 3, 4, 5], 3),   # Expected: [2, 4]
    ]
    
    for nums, target in test_cases:
        result = find_first_last_position(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        if result[0] != -1:
            print(f"First occurrence at index {result[0]}")
            print(f"Last occurrence at index {result[1]}\n")
        else:
            print(f"Target {target} not found\n")

if __name__ == "__main__":
    main() 