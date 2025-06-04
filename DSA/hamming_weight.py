class Solution:
    def hamming_weight_loop(self, n: int) -> int:
        """
        Simple loop solution checking each bit.
        Time Complexity: O(32) = O(1)
        Space Complexity: O(1)
        """
        count = 0
        while n:
            count += n & 1  # Check rightmost bit
            n >>= 1        # Right shift
        return count

    def hamming_weight_trick(self, n: int) -> int:
        """
        Brian Kernighan's algorithm.
        Uses n & (n-1) to clear the rightmost 1 bit.
        Time Complexity: O(number of 1 bits)
        Space Complexity: O(1)
        """
        count = 0
        while n:
            n &= (n - 1)  # Clear rightmost 1 bit
            count += 1
        return count

    def hamming_weight_builtin(self, n: int) -> int:
        """
        Using Python's built-in bin() function.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return bin(n).count('1')

def test_solution():
    solution = Solution()
    
    # Test Case 1: Single 1 bit
    n = 16  # 10000 in binary
    print("Test Case 1:")
    print(f"Input: {bin(n)[2:]} ({n})")
    print(f"Loop Method: {solution.hamming_weight_loop(n)}")
    print(f"Trick Method: {solution.hamming_weight_trick(n)}")
    print(f"Builtin Method: {solution.hamming_weight_builtin(n)}")
    print()
    
    # Test Case 2: Multiple 1 bits
    n = 11  # 1011 in binary
    print("Test Case 2:")
    print(f"Input: {bin(n)[2:]} ({n})")
    print(f"Loop Method: {solution.hamming_weight_loop(n)}")
    print(f"Trick Method: {solution.hamming_weight_trick(n)}")
    print(f"Builtin Method: {solution.hamming_weight_builtin(n)}")
    print()
    
    # Test Case 3: All 1 bits
    n = 15  # 1111 in binary
    print("Test Case 3:")
    print(f"Input: {bin(n)[2:]} ({n})")
    print(f"Loop Method: {solution.hamming_weight_loop(n)}")
    print(f"Trick Method: {solution.hamming_weight_trick(n)}")
    print(f"Builtin Method: {solution.hamming_weight_builtin(n)}")
    print()
    
    # Test Case 4: Zero
    n = 0
    print("Test Case 4:")
    print(f"Input: {bin(n)[2:]} ({n})")
    print(f"Loop Method: {solution.hamming_weight_loop(n)}")
    print(f"Trick Method: {solution.hamming_weight_trick(n)}")
    print(f"Builtin Method: {solution.hamming_weight_builtin(n)}")
    print()
    
    # Test Case 5: Large number
    n = 4294967293  # 11111111111111111111111111111101 in binary
    print("Test Case 5:")
    print(f"Input: {bin(n)[2:]} ({n})")
    print(f"Loop Method: {solution.hamming_weight_loop(n)}")
    print(f"Trick Method: {solution.hamming_weight_trick(n)}")
    print(f"Builtin Method: {solution.hamming_weight_builtin(n)}")

if __name__ == "__main__":
    test_solution() 