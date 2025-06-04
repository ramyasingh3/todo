from typing import List

class Solution:
    def remove_element_two_pointers(self, nums: List[int], val: int) -> int:
        """
        Two pointers approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
        
    def remove_element_while_loop(self, nums: List[int], val: int) -> int:
        """
        While loop approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
                
        return n
        
    def remove_element_list_comprehension(self, nums: List[int], val: int) -> int:
        """
        List comprehension approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    nums = [3, 2, 2, 3]
    val = 3
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Input: {nums}, val = {val}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 2: All elements to remove
    print("Test Case 2: All elements to remove")
    nums = [1, 1, 1, 1]
    val = 1
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Input: {nums}, val = {val}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 3: No elements to remove
    print("Test Case 3: No elements to remove")
    nums = [4, 5, 6, 7]
    val = 1
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Input: {nums}, val = {val}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 4: Empty array
    print("Test Case 4: Empty array")
    nums = []
    val = 0
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Input: {nums}, val = {val}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 5: Mixed elements
    print("Test Case 5: Mixed elements")
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Input: {nums}, val = {val}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    nums = [3, 2, 2, 3]
    val = 3
    
    print("Two Pointers:")
    result = solution.remove_element_two_pointers(nums.copy(), val)
    print(f"Result: {result}, nums = {nums[:result]}")
    
    print("While Loop:")
    result = solution.remove_element_while_loop(nums.copy(), val)
    print(f"Result: {result}, nums = {nums[:result]}")
    
    print("List Comprehension:")
    result = solution.remove_element_list_comprehension(nums.copy(), val)
    print(f"Result: {result}, nums = {nums[:result]}")

if __name__ == "__main__":
    test_solution() 