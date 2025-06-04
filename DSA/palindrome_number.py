class Solution:
    def is_palindrome_string(self, x: int) -> bool:
        """
        String conversion solution
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        s = str(x)
        return s == s[::-1]

    def is_palindrome_reverse(self, x: int) -> bool:
        """
        Number reversal solution
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x < 0:
            return False
            
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
            
        return original == reversed_num

    def is_palindrome_half(self, x: int) -> bool:
        """
        Half number comparison solution
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
            
        return x == reversed_half or x == reversed_half // 10

def test_solution():
    solution = Solution()
    
    # Test Case 1: Positive palindrome
    print("Test Case 1: Positive palindrome")
    x = 121
    result = solution.is_palindrome_string(x)
    print(f"Input: {x}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Negative number
    print("Test Case 2: Negative number")
    x = -121
    result = solution.is_palindrome_string(x)
    print(f"Input: {x}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Non-palindrome
    print("Test Case 3: Non-palindrome")
    x = 10
    result = solution.is_palindrome_string(x)
    print(f"Input: {x}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Single digit
    print("Test Case 4: Single digit")
    x = 5
    result = solution.is_palindrome_string(x)
    print(f"Input: {x}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Large palindrome
    print("Test Case 5: Large palindrome")
    x = 123454321
    result = solution.is_palindrome_string(x)
    print(f"Input: {x}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    x = 12321
    print(f"Input: {x}")
    print(f"String method: {solution.is_palindrome_string(x)}")
    print(f"Reverse method: {solution.is_palindrome_reverse(x)}")
    print(f"Half method: {solution.is_palindrome_half(x)}")

if __name__ == "__main__":
    test_solution() 