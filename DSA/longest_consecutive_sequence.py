"""
Find the length of the longest consecutive sequence in an unsorted array of integers.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

Example 2:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Its length is 9.

Time Complexity:
- Hash Set Solution: O(n)
- Sorting Solution: O(n log n)
Space Complexity:
- Hash Set Solution: O(n)
- Sorting Solution: O(1) if we can modify input array, O(n) if we need to keep input array unchanged
"""

from typing import List, Set

def longest_consecutive_hash_set(nums: List[int]) -> int:
    """
    Solution using hash set.
    For each number, we check if it's the start of a sequence by checking if num-1 exists.
    If it is, we keep checking consecutive numbers until we can't find the next number.
    """
    if not nums:
        return 0
    
    num_set: Set[int] = set(nums)
    max_length = 0
    
    for num in num_set:
        # Check if this number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sorting(nums: List[int]) -> int:
    """
    Solution using sorting.
    Sort the array and count consecutive sequences.
    """
    if not nums:
        return 0
    
    # Create a copy to avoid modifying input array
    sorted_nums = sorted(nums)
    max_length = 1
    current_length = 1
    
    for i in range(1, len(sorted_nums)):
        # Skip duplicates
        if sorted_nums[i] == sorted_nums[i - 1]:
            continue
        
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    return max(max_length, current_length)

def get_longest_consecutive_sequence(nums: List[int]) -> List[int]:
    """
    Helper function to get the actual longest consecutive sequence.
    Uses the hash set approach to find the sequence.
    """
    if not nums:
        return []
    
    num_set: Set[int] = set(nums)
    max_length = 0
    start_num = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            if current_length > max_length:
                max_length = current_length
                start_num = num
    
    return list(range(start_num, start_num + max_length))

# Test cases
def test_longest_consecutive_sequence():
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4, [1, 2, 3, 4]),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, [0, 1, 2, 3, 4, 5, 6, 7, 8]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 1, 1], 1, [1]),
        ([1, 3, 5, 7], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 5, 6, 7], 3, [1, 2, 3]),
        ([1, 2, 3, 5, 6, 7, 8, 9], 5, [5, 6, 7, 8, 9]),
    ]
    
    for nums, expected_length, expected_sequence in test_cases:
        # Test hash set solution
        result_hash = longest_consecutive_hash_set(nums)
        assert result_hash == expected_length, \
            f"Hash set solution failed for {nums}. Expected length {expected_length}, got {result_hash}"
        
        # Test sorting solution
        result_sort = longest_consecutive_sorting(nums)
        assert result_sort == expected_length, \
            f"Sorting solution failed for {nums}. Expected length {expected_length}, got {result_sort}"
        
        # Test sequence reconstruction
        result_sequence = get_longest_consecutive_sequence(nums)
        assert len(result_sequence) == expected_length, \
            f"Sequence reconstruction failed for {nums}. Expected length {expected_length}, got {len(result_sequence)}"
        assert result_sequence == expected_sequence, \
            f"Sequence reconstruction failed for {nums}. Expected {expected_sequence}, got {result_sequence}"
        
        print(f"Test passed for nums={nums}")

if __name__ == "__main__":
    test_longest_consecutive_sequence()
