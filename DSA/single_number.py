from typing import List

class Solution:
    def single_number_xor(self, nums: List[int]) -> int:
        """
        Using XOR operation.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        for num in nums:
            result ^= num
        return result

    def single_number_hash(self, nums: List[int]) -> int:
        """
        Using hash set.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()

    def single_number_math(self, nums: List[int]) -> int:
        """
        Using mathematical formula.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return 2 * sum(set(nums)) - sum(nums)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Single number in middle
    nums = [2, 2, 1]
    print("Test Case 1:")
    print(f"Input: {nums}")
    print(f"XOR Method: {solution.single_number_xor(nums)}")
    print(f"Hash Method: {solution.single_number_hash(nums)}")
    print(f"Math Method: {solution.single_number_math(nums)}")
    print()
    
    # Test Case 2: Single number at end
    nums = [4, 1, 2, 1, 2]
    print("Test Case 2:")
    print(f"Input: {nums}")
    print(f"XOR Method: {solution.single_number_xor(nums)}")
    print(f"Hash Method: {solution.single_number_hash(nums)}")
    print(f"Math Method: {solution.single_number_math(nums)}")
    print()
    
    # Test Case 3: Single number at start
    nums = [1, 2, 2, 3, 3]
    print("Test Case 3:")
    print(f"Input: {nums}")
    print(f"XOR Method: {solution.single_number_xor(nums)}")
    print(f"Hash Method: {solution.single_number_hash(nums)}")
    print(f"Math Method: {solution.single_number_math(nums)}")
    print()
    
    # Test Case 4: Single negative number
    nums = [-1, -1, -2]
    print("Test Case 4:")
    print(f"Input: {nums}")
    print(f"XOR Method: {solution.single_number_xor(nums)}")
    print(f"Hash Method: {solution.single_number_hash(nums)}")
    print(f"Math Method: {solution.single_number_math(nums)}")
    print()
    
    # Test Case 5: Large array
    nums = [i for i in range(1000)] * 2 + [1000]
    print("Test Case 5:")
    print(f"Input: [0,0,1,1,...,999,999,1000]")
    print(f"XOR Method: {solution.single_number_xor(nums)}")
    print(f"Hash Method: {solution.single_number_hash(nums)}")
    print(f"Math Method: {solution.single_number_math(nums)}")

if __name__ == "__main__":
    test_solution() 