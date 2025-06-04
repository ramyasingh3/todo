class Solution:
    def is_power_of_two_loop(self, n: int) -> bool:
        """
        Iterative solution using division.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if n <= 0:
            return False
            
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
            
        return True

    def is_power_of_two_bit(self, n: int) -> bool:
        """
        Bit manipulation solution.
        Uses the fact that powers of 2 have exactly one '1' bit.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if n <= 0:
            return False
            
        return n & (n - 1) == 0

    def is_power_of_two_math(self, n: int) -> bool:
        """
        Mathematical solution using logarithms.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if n <= 0:
            return False
            
        import math
        # Check if log2(n) is an integer
        return math.log2(n).is_integer()

def test_solution():
    solution = Solution()
    
    # Test Case 1: Power of 2
    n = 16
    print("Test Case 1:")
    print(f"Input: {n}")
    print(f"Loop Method: {solution.is_power_of_two_loop(n)}")
    print(f"Bit Method: {solution.is_power_of_two_bit(n)}")
    print(f"Math Method: {solution.is_power_of_two_math(n)}")
    print()
    
    # Test Case 2: Not power of 2
    n = 6
    print("Test Case 2:")
    print(f"Input: {n}")
    print(f"Loop Method: {solution.is_power_of_two_loop(n)}")
    print(f"Bit Method: {solution.is_power_of_two_bit(n)}")
    print(f"Math Method: {solution.is_power_of_two_math(n)}")
    print()
    
    # Test Case 3: Negative number
    n = -16
    print("Test Case 3:")
    print(f"Input: {n}")
    print(f"Loop Method: {solution.is_power_of_two_loop(n)}")
    print(f"Bit Method: {solution.is_power_of_two_bit(n)}")
    print(f"Math Method: {solution.is_power_of_two_math(n)}")
    print()
    
    # Test Case 4: Zero
    n = 0
    print("Test Case 4:")
    print(f"Input: {n}")
    print(f"Loop Method: {solution.is_power_of_two_loop(n)}")
    print(f"Bit Method: {solution.is_power_of_two_bit(n)}")
    print(f"Math Method: {solution.is_power_of_two_math(n)}")
    print()
    
    # Test Case 5: Large power of 2
    n = 1024
    print("Test Case 5:")
    print(f"Input: {n}")
    print(f"Loop Method: {solution.is_power_of_two_loop(n)}")
    print(f"Bit Method: {solution.is_power_of_two_bit(n)}")
    print(f"Math Method: {solution.is_power_of_two_math(n)}")

if __name__ == "__main__":
    test_solution() 