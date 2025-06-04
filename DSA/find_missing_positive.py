def find_missing_positive(nums):
    """
    Find the smallest missing positive integer in an unsorted array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    # Step 1: Replace negative numbers and numbers > n with n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark numbers as negative if they exist in array
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1

def main():
    # Test cases
    test_cases = [
        [1, 2, 0],           # Expected: 3
        [3, 4, -1, 1],       # Expected: 2
        [7, 8, 9, 11, 12],   # Expected: 1
        [1, 2, 3, 4],        # Expected: 5
        []                    # Expected: 1
    ]
    
    for nums in test_cases:
        result = find_missing_positive(nums)
        print(f"Input: {nums}")
        print(f"Smallest missing positive: {result}\n")

if __name__ == "__main__":
    main() 