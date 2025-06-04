class Solution:
    def int_to_roman_naive(self, num: int) -> str:
        """
        Naive solution with O(1) time complexity.
        """
        roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        result = ''
        for value, symbol in roman_map.items():
            while num >= value:
                result += symbol
                num -= value
        return result

    def int_to_roman_optimized(self, num: int) -> str:
        """
        Optimized solution with O(1) time complexity.
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result = []
        i = 0
        while num > 0:
            if num >= values[i]:
                result.append(symbols[i])
                num -= values[i]
            else:
                i += 1
        return ''.join(result)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic conversion
    num1 = 3
    print("Test Case 1:")
    print(f"Input: {num1}")
    print(f"Naive Solution: {solution.int_to_roman_naive(num1)}")
    print(f"Optimized Solution: {solution.int_to_roman_optimized(num1)}")
    print()
    
    # Test Case 2: Subtraction case
    num2 = 4
    print("Test Case 2:")
    print(f"Input: {num2}")
    print(f"Naive Solution: {solution.int_to_roman_naive(num2)}")
    print(f"Optimized Solution: {solution.int_to_roman_optimized(num2)}")
    print()
    
    # Test Case 3: Complex number
    num3 = 1994
    print("Test Case 3:")
    print(f"Input: {num3}")
    print(f"Naive Solution: {solution.int_to_roman_naive(num3)}")
    print(f"Optimized Solution: {solution.int_to_roman_optimized(num3)}")
    print()
    
    # Test Case 4: Large number
    num4 = 3999
    print("Test Case 4:")
    print(f"Input: {num4}")
    print(f"Naive Solution: {solution.int_to_roman_naive(num4)}")
    print(f"Optimized Solution: {solution.int_to_roman_optimized(num4)}")
    print()
    
    # Test Case 5: Single digit
    num5 = 9
    print("Test Case 5:")
    print(f"Input: {num5}")
    print(f"Naive Solution: {solution.int_to_roman_naive(num5)}")
    print(f"Optimized Solution: {solution.int_to_roman_optimized(num5)}")

if __name__ == "__main__":
    test_solution() 